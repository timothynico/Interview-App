from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import speech_recognition as sr
import os
from datetime import datetime
import requests
import json
import base64
import PyPDF2

app = Flask(__name__)
CORS(app)

OUTPUT_DIR = "recordings"
CV_DIR = "cv_uploads"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(CV_DIR, exist_ok=True)

WEBHOOK_URL = "https://n8n-1.saturn.petra.ac.id/webhook-test/939b69b4-4d28-4531-b451-804809c2399c"

# Menyimpan semua hasil transkripsi dan data kandidat
all_transcripts = {}
candidate_info = {}


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


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/videos/<path:filename>')
def serve_video(filename):
    return send_from_directory('videos', filename)


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

        # 🔹 Extract teks dari PDF
        cv_text = extract_text_from_pdf(cv_path)

        # Simpan info kandidat
        candidate_info[session_id] = {
            "nama": name,
            "email": email,
            "posisi_dilamar": position,
            "cv_filename": cv_filename,
            "cv_path": cv_path,
            "cv_text": cv_text,  # Simpan teks CV
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
        question_number = request.form.get('question_number', '0')
        session_id = request.form.get('session_id', 'default')

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"answer_q{question_number}_{timestamp}.wav"
        save_path = os.path.join(OUTPUT_DIR, filename)
        audio_file.save(save_path)

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
            "filename": filename
        }

        webhook_status = "pending"

                        # Kalau sudah pertanyaan terakhir (q4) → kirim semua ke n8n
        if question_number == "4":
            try:
                # Ambil data kandidat
                candidate = candidate_info.get(session_id, {})
                cv_path = candidate.get("cv_path")

                # 🔹 Struktur payload dengan CV TEXT (bukan file)
                payload = {
                    "session_id": session_id,
                    "timestamp_completed": datetime.now().isoformat(),
                    
                    # Data Kandidat
                    "nama": candidate.get("nama", ""),
                    "email": candidate.get("email", ""),
                    "posisi_dilamar": candidate.get("posisi_dilamar", ""),
                    
                    "cv_text": candidate.get("cv_text", ""),
                    
                    # Transkrip Pertanyaan 1-4
                    "transkrip_pertanyaan_1": all_transcripts[session_id].get("pertanyaan_1", {}).get("transkrip", ""),
                    "transkrip_pertanyaan_2": all_transcripts[session_id].get("pertanyaan_2", {}).get("transkrip", ""),
                    "transkrip_pertanyaan_3": all_transcripts[session_id].get("pertanyaan_3", {}).get("transkrip", ""),
                    "transkrip_pertanyaan_4": all_transcripts[session_id].get("pertanyaan_4", {}).get("transkrip", ""),
                }

                # Kirim ke webhook sebagai JSON (SEMUA DATA DALAM 1 REQUEST!)
                resp = requests.post(
                    WEBHOOK_URL,
                    json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=20
                )

                if resp.status_code == 200:
                    webhook_status = "success"
                    print(f"✅ Semua data berhasil dikirim untuk session: {session_id}")
                    
                    # Bersihkan data session
                    if session_id in all_transcripts:
                        del all_transcripts[session_id]
                    if session_id in candidate_info:
                        del candidate_info[session_id]
                else:
                    webhook_status = f"failed (HTTP {resp.status_code})"
                    print(f"❌ Webhook gagal: {resp.status_code} - {resp.text}")

            except Exception as e:
                webhook_status = f"error: {str(e)}"
                print(f"❌ Error kirim webhook: {str(e)}")

        return jsonify({
            'success': True,
            'transcript': text,
            'filename': filename,
            'question_number': question_number,
            'webhook_status': webhook_status,
            'is_last_question': question_number == "4"
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