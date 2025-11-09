from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import speech_recognition as sr
import os
from datetime import datetime
import requests
import json
import PyPDF2
import mimetypes
from contextlib import ExitStack
from requests_toolbelt.multipart.encoder import MultipartEncoder

app = Flask(__name__)
CORS(app)

OUTPUT_DIR = "recordings"
VIDEO_OUTPUT_DIR = "video_recordings"
CV_DIR = "cv_uploads"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(VIDEO_OUTPUT_DIR, exist_ok=True)
os.makedirs(CV_DIR, exist_ok=True)

MAX_VIDEO_SIZE_BYTES = 20 * 1024 * 1024  # 20 MB per video
MAX_TOTAL_VIDEO_SIZE_BYTES = 80 * 1024 * 1024  # 80 MB untuk semua video
MAX_WEBHOOK_PAYLOAD_BYTES = 80 * 1024 * 1024  # Batas ukuran payload webhook termasuk overhead multipart

WEBHOOK_URL = "https://n8n-1.saturn.petra.ac.id/webhook/939b69b4-4d28-4531-b451-804809c2399c"
DASHBOARD_DATA_URL = "https://n8n-1.saturn.petra.ac.id/webhook/d14704c6-0264-43d4-a978-e17cccf06e45"

# Menyimpan semua hasil transkripsi dan data kandidat
all_transcripts = {}
candidate_info = {}


class WebhookPayloadTooLarge(Exception):
    """Error yang dilempar ketika payload webhook melebihi kapasitas server."""

    def __init__(self, payload_size_bytes, message):
        super().__init__(message)
        self.payload_size_bytes = payload_size_bytes


def _send_multipart_request(fields, attachments=None, log_label=""):
    """Kirim request multipart ke webhook dan validasi ukurannya."""

    attachments = attachments or []

    with ExitStack() as stack:
        encoder_fields = {
            key: "" if value is None else str(value)
            for key, value in fields.items()
        }

        for attachment in attachments:
            file_handle = stack.enter_context(open(attachment["path"], "rb"))
            encoder_fields[attachment["field_name"]] = (
                attachment["filename"],
                file_handle,
                attachment["mime"],
            )

        encoder = MultipartEncoder(fields=encoder_fields)
        payload_size_bytes = encoder.len
        payload_mb = payload_size_bytes / (1024 * 1024)
        print(f"{log_label}ℹ️ Ukuran payload webhook: {payload_mb:.2f} MB")

        if payload_size_bytes > MAX_WEBHOOK_PAYLOAD_BYTES:
            raise WebhookPayloadTooLarge(
                payload_size_bytes,
                "Total data (video + transkrip) yang dikirim ke webhook melebihi 80MB. "
                "Mohon kurangi durasi rekaman agar ukurannya lebih kecil.",
            )

        try:
            response = requests.post(
                WEBHOOK_URL,
                data=encoder,
                headers={"Content-Type": encoder.content_type},
                timeout=20,
            )
        except requests.RequestException as req_err:
            raise ValueError(f"Gagal mengirim data ke webhook: {req_err}") from req_err

    if response.status_code == 413:
        raise WebhookPayloadTooLarge(
            payload_size_bytes,
            "Server webhook menolak data karena ukurannya terlalu besar (HTTP 413).",
        )

    if response.status_code != 200:
        raise ValueError(
            f"Webhook gagal dengan status {response.status_code}: {response.text}"
        )

    return response


def _send_chunked_webhook_upload(form_data, video_attachments, session_id):
    """Kirim metadata lalu tiap video secara terpisah untuk menghindari batas ukuran."""

    if not video_attachments:
        raise ValueError("Tidak ada video yang perlu dikirim secara terpisah.")

    metadata_fields = dict(form_data)
    metadata_fields.update(
        {
            "delivery_mode": "chunked",
            "payload_type": "metadata",
            "video_count": len(video_attachments),
        }
    )

    _send_multipart_request(metadata_fields, [], log_label="[metadata] ")

    transcripts_for_session = all_transcripts.get(session_id, {})

    for index, attachment in enumerate(video_attachments, start=1):
        transcript_text = transcripts_for_session.get(attachment["question_key"], {}).get(
            "transkrip", ""
        )

        video_fields = {
            "session_id": form_data.get("session_id"),
            "timestamp_completed": form_data.get("timestamp_completed"),
            "delivery_mode": "chunked",
            "payload_type": "video",
            "video_index": index,
            "video_count": len(video_attachments),
            "question_key": attachment["question_key"],
            "video_filename": attachment["filename"],
            "transkrip": transcript_text,
        }

        for info_key in ("nama", "email", "posisi_dilamar"):
            if info_key in form_data:
                video_fields[info_key] = form_data[info_key]

        reference_key = f"video_{attachment['question_key']}_filename"
        if reference_key in form_data:
            video_fields[reference_key] = form_data[reference_key]

        _send_multipart_request(
            video_fields,
            [attachment],
            log_label=f"[video {index}/{len(video_attachments)}] ",
        )

    print("✅ Pengiriman video secara bertahap (chunked) berhasil.")
    return "chunked"


def _deliver_webhook_payload(form_data, video_attachments, session_id):
    """Coba kirim payload gabungan, fallback ke chunked jika ditolak."""

    if not video_attachments:
        metadata_only = dict(form_data)
        metadata_only["delivery_mode"] = "metadata_only"
        _send_multipart_request(metadata_only, [], log_label="[metadata-only] ")
        return "metadata_only"

    single_payload = dict(form_data)
    single_payload["delivery_mode"] = "single_payload"

    try:
        _send_multipart_request(
            single_payload,
            video_attachments,
            log_label="[gabungan] ",
        )
        return "single_payload"
    except WebhookPayloadTooLarge as combined_error:
        print(
            "⚠️ Payload gabungan ditolak webhook (HTTP 413 atau melebihi batas). "
            "Mengirim video secara bertahap."
        )
        return _send_chunked_webhook_upload(form_data, video_attachments, session_id)
def extract_text_from_pdf(pdf_path):
    """Extract semua teks dari PDF"""
    try:
        text = ""
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        print(f"Error extract PDF: {str(e)}")
        return None


def transform_n8n_data_to_candidate(user_data):
    """Transform data dari n8n ke format kandidat untuk dashboard"""
    documents = {doc['type']: doc['content'] for doc in user_data.get('documents', [])}
    
    return {
        'id': user_data.get('user_id'),
        'session_id': f"session_{user_data.get('user_id')}",
        'nama': user_data.get('name', ''),
        'email': user_data.get('email', ''),
        'posisi_dilamar': user_data.get('posisi_dilamar'),  # Tidak ada di data n8n, bisa ditambahkan nanti
        'status': 'complete',
        'registered_at': datetime.now().isoformat(),  # Atau ambil dari timestamp jika ada
        'CV': documents.get('CV', ''),
        'Q1': documents.get('Q1', ''),
        'Q2': documents.get('Q2', ''),
        'Q3': documents.get('Q3', ''),
        'Q4': documents.get('Q4', '')
    }


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/review')
def review_page():
    """Serve halaman review dashboard"""
    return send_from_directory('.', 'review.html')


@app.route('/videos/<path:filename>')
def serve_video(filename):
    return send_from_directory('videos', filename)


@app.route('/recorded_videos/<path:filename>')
def serve_recorded_video(filename):
    return send_from_directory(VIDEO_OUTPUT_DIR, filename)


@app.route('/api/candidates', methods=['GET'])
def get_candidates():
    """API untuk mendapatkan list kandidat dari n8n"""
    try:
        # Fetch data dari n8n webhook
        response = requests.get(DASHBOARD_DATA_URL, timeout=10)
        
        if response.status_code != 200:
            return jsonify({
                'success': False,
                'error': f'Failed to fetch data from n8n: HTTP {response.status_code}'
            }), 500
        
        data = response.json()
        
        # Transform data
        # Jika response berisi single user_data
        if 'user_data' in data:
            candidates = [transform_n8n_data_to_candidate(data['user_data'])]
        # Jika response berisi array of users
        elif isinstance(data, list):
            candidates = [transform_n8n_data_to_candidate(item.get('user_data', item)) for item in data]
        # Jika response berisi users array
        elif 'users' in data:
            candidates = [transform_n8n_data_to_candidate(user) for user in data['users']]
        else:
            # Fallback: coba parse langsung
            candidates = [transform_n8n_data_to_candidate(data)]
        
        return jsonify({
            'success': True,
            'candidates': candidates
        })
        
    except requests.Timeout:
        return jsonify({
            'success': False,
            'error': 'Request timeout - n8n tidak merespons'
        }), 504
    except requests.RequestException as e:
        print(f"Error fetching candidates: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Network error: {str(e)}'
        }), 500
    except Exception as e:
        print(f"Error processing candidates: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/candidate/<session_id>', methods=['GET'])
def get_candidate_detail(session_id):
    """API untuk mendapatkan detail kandidat berdasarkan session_id"""
    try:
        # Fetch semua kandidat
        response = requests.get(DASHBOARD_DATA_URL, timeout=10)
        
        if response.status_code != 200:
            return jsonify({
                'success': False,
                'error': f'Failed to fetch data from n8n: HTTP {response.status_code}'
            }), 500
        
        data = response.json()
        
        # Transform dan cari kandidat yang sesuai
        candidates = []
        if 'user_data' in data:
            candidates = [transform_n8n_data_to_candidate(data['user_data'])]
        elif isinstance(data, list):
            candidates = [transform_n8n_data_to_candidate(item.get('user_data', item)) for item in data]
        elif 'users' in data:
            candidates = [transform_n8n_data_to_candidate(user) for user in data['users']]
        
        # Cari kandidat dengan session_id yang sesuai
        candidate = next((c for c in candidates if c['session_id'] == session_id), None)
        
        if not candidate:
            return jsonify({
                'success': False,
                'error': 'Candidate not found'
            }), 404
        
        return jsonify({
            'success': True,
            'candidate': candidate
        })
        
    except Exception as e:
        print(f"Error fetching candidate detail: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


N8N_CHAT_WEBHOOK = "https://n8n-1.saturn.petra.ac.id/webhook/d14704c6-0264-43d4-a978-e17cccf06e45"  # Ganti dengan webhook n8n Anda

@app.route('/api/chat', methods=['POST'])
def chat_with_ai():
    try:
        data = request.get_json()
        session_id = data.get('session_id')
        message = data.get('message')
        
        if not session_id or not message:
            return jsonify({
                'success': False,
                'error': 'session_id dan message required'
            }), 400
        
        payload = {
            'user_id': session_id, 
            'message': message,
            'timestamp': datetime.now().isoformat()
        }
        
        response = requests.post(
            N8N_CHAT_WEBHOOK,
            json=payload,
            headers={'Content-Type': 'application/json'},
            timeout=30
        )
        
        response.raise_for_status()
        response_data = response.json()
        
        ai_message = response_data.get('output', '')
        
        if isinstance(ai_message, dict):
            ai_message = json.dumps(ai_message, ensure_ascii=False)
        
        return jsonify({
            'success': True,
            'response': ai_message
        })
            
    except requests.Timeout:
        return jsonify({
            'success': False,
            'error': 'Request timeout - AI membutuhkan waktu terlalu lama'
        }), 504
    except requests.RequestException as e:
        print(f"Error calling n8n: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Error connecting to AI: {str(e)}'
        }), 500
    except Exception as e:
        print(f"Error chat with AI: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/upload-cv', methods=['POST'])
def upload_cv():
    try:
        if 'cv' not in request.files:
            return jsonify({'error': 'Tidak ada file CV'}), 400

        cv_file = request.files['cv']
        session_id = request.form.get('session_id', 'default')
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        position = request.form.get('position', '')

        # Validasi file PDF
        if not cv_file.filename.endswith('.pdf'):
            return jsonify({'error': 'File harus berformat PDF'}), 400

        # Simpan CV
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = name.replace(' ', '_').replace('.', '')
        cv_filename = f"CV_{safe_name}_{timestamp}.pdf"
        cv_path = os.path.join(CV_DIR, cv_filename)
        cv_file.save(cv_path)

        # Extract teks dari PDF
        cv_text = extract_text_from_pdf(cv_path)
        print('cv_text', cv_text)

        # Simpan info kandidat dengan struktur yang match database
        candidate_info[session_id] = {
            "nama": name,
            "email": email,
            "posisi_dilamar": position,
            "cv_filename": cv_filename,
            "cv_path": cv_path,
            "CV": cv_text,  # Sesuai dengan kolom di database
            "registered_at": datetime.now().isoformat()
        }

        return jsonify({
            'success': True,
            'cv_filename': cv_filename
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    try:
        if 'audio' not in request.files:
            return jsonify({'error': 'Tidak ada file audio'}), 400

        audio_file = request.files['audio']
        video_file = request.files.get('video')
        question_number = request.form.get('question_number', '0')
        session_id = request.form.get('session_id', 'default')

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"answer_q{question_number}_{timestamp}.wav"
        save_path = os.path.join(OUTPUT_DIR, filename)
        audio_file.save(save_path)

        video_filename = None
        video_url = None
        if video_file:
            video_extension = os.path.splitext(video_file.filename)[1] or '.webm'
            video_filename = f"answer_q{question_number}_{timestamp}{video_extension}"
            video_path = os.path.join(VIDEO_OUTPUT_DIR, video_filename)
            video_file.save(video_path)

            video_size = os.path.getsize(video_path)
            if video_size > MAX_VIDEO_SIZE_BYTES:
                if os.path.exists(video_path):
                    os.remove(video_path)
                if os.path.exists(save_path):
                    os.remove(save_path)
                return jsonify({
                    'success': False,
                    'error': 'Ukuran video melebihi batas 20MB. Mohon rekam ulang dengan durasi yang lebih singkat.'
                }), 400

            video_url = f"/recorded_videos/{video_filename}"

        # Transkripsi suara
        recognizer = sr.Recognizer()
        with sr.AudioFile(save_path) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data, language="id-ID")
            except sr.UnknownValueError:
                text = "Suara tidak dikenali."
            except sr.RequestError as e:
                text = f"Error speech recognition: {e}"

        # Simpan hasil
        if session_id not in all_transcripts:
            all_transcripts[session_id] = {}

        all_transcripts[session_id][f"pertanyaan_{question_number}"] = {
            "transkrip": text,
            "timestamp": timestamp,
            "filename": filename,
            "video_filename": video_filename
        }

        webhook_status = "pending"
        webhook_delivery = None

                        # Kalau sudah pertanyaan terakhir (q4) → kirim semua ke n8n
        if question_number == "4":
            try:
                # Ambil data kandidat
                candidate = candidate_info.get(session_id, {})

                # 🔹 Struktur payload form-data
                form_data = {
                    "session_id": session_id,
                    "timestamp_completed": datetime.now().isoformat(),

                    # Data Kandidat
                    "nama": candidate.get("nama", ""),
                    "email": candidate.get("email", ""),
                    "posisi_dilamar": candidate.get("posisi_dilamar", ""),

                    "cv_text": candidate.get("CV", ""),

                    # Transkrip Pertanyaan 1-4
                    "transkrip_pertanyaan_1": all_transcripts[session_id].get("pertanyaan_1", {}).get("transkrip", ""),
                    "transkrip_pertanyaan_2": all_transcripts[session_id].get("pertanyaan_2", {}).get("transkrip", ""),
                    "transkrip_pertanyaan_3": all_transcripts[session_id].get("pertanyaan_3", {}).get("transkrip", ""),
                    "transkrip_pertanyaan_4": all_transcripts[session_id].get("pertanyaan_4", {}).get("transkrip", ""),
                }

                video_attachments = []
                total_video_size = 0

                for idx in range(1, 5):
                    key = f"pertanyaan_{idx}"
                    video_filename = all_transcripts[session_id].get(key, {}).get("video_filename")

                    if not video_filename:
                        continue

                    video_path = os.path.join(VIDEO_OUTPUT_DIR, video_filename)

                    if not os.path.exists(video_path):
                        continue

                    video_size = os.path.getsize(video_path)
                    if video_size > MAX_VIDEO_SIZE_BYTES:
                        raise ValueError(f"Video untuk {key} melebihi batas 20MB.")

                    total_video_size += video_size
                    if total_video_size > MAX_TOTAL_VIDEO_SIZE_BYTES:
                        raise ValueError("Total ukuran video melebihi batas 80MB.")

                    mime_type = mimetypes.guess_type(video_path)[0] or "application/octet-stream"
                    video_attachments.append(
                        {
                            "field_name": f"video_{key}",
                            "filename": video_filename,
                            "path": video_path,
                            "mime": mime_type,
                            "size": video_size,
                            "question_key": key,
                        }
                    )

                    # Sertakan nama file pada payload teks untuk referensi
                    form_data[f"video_{key}_filename"] = video_filename

                try:
                    webhook_delivery = _deliver_webhook_payload(
                        form_data,
                        video_attachments,
                        session_id,
                    )
                    webhook_status = "success"
                    print(
                        f"✅ Semua data berhasil dikirim untuk session: {session_id} "
                        f"(mode: {webhook_delivery})"
                    )

                    # Bersihkan data session
                    if session_id in all_transcripts:
                        del all_transcripts[session_id]
                    if session_id in candidate_info:
                        del candidate_info[session_id]

                except WebhookPayloadTooLarge as size_error:
                    webhook_status = f"error: {str(size_error)}"
                    return jsonify({
                        'success': False,
                        'error': str(size_error),
                        'question_number': question_number,
                        'webhook_status': webhook_status
                    }), 400
                except ValueError as send_error:
                    webhook_status = f"error: {str(send_error)}"
                    return jsonify({
                        'success': False,
                        'error': str(send_error),
                        'question_number': question_number,
                        'webhook_status': webhook_status
                    }), 400
            except Exception as e:
                webhook_status = f"error: {str(e)}"
                print(f"❌ Error kirim webhook: {str(e)}")

        return jsonify({
            'success': True,
            'transcript': text,
            'filename': filename,
            'question_number': question_number,
            'webhook_status': webhook_status,
            'webhook_delivery': webhook_delivery if question_number == "4" else None,
            'is_last_question': question_number == "4",
            'video_filename': video_filename,
            'video_url': video_url
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/reset-session', methods=['POST'])
def reset_session():
    """Reset session jika user ingin mulai ulang"""
    try:
        data = request.get_json()
        session_id = data.get('session_id', 'default')
        if session_id in all_transcripts:
            del all_transcripts[session_id]
        if session_id in candidate_info:
            del candidate_info[session_id]
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)