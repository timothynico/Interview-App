from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import speech_recognition as sr
import os
from datetime import datetime
import requests
import json
import base64
import PyPDF2
from process_video import analyze_video_confidence
import re
from typing import List, Dict
import pandas as pd

app = Flask(__name__)
CORS(app)

OUTPUT_DIR = "recordings"
VIDEO_OUTPUT_DIR = "video_recordings"
CV_DIR = "cv_uploads"
TRANSKRIP_DIR = "transkrip_uploads"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(VIDEO_OUTPUT_DIR, exist_ok=True)
os.makedirs(CV_DIR, exist_ok=True)
os.makedirs(TRANSKRIP_DIR, exist_ok=True)

WEBHOOK_URL = "https://n8n-1.saturn.petra.ac.id/webhook/939b69b4-4d28-4531-b451-804809c2399c"
# WEBHOOK_URL = "https://n8n-1.saturn.petra.ac.id/webhook-test/939b69b4-4d28-4531-b451-804809c2399c"
DASHBOARD_DATA_URL = "https://n8n-1.saturn.petra.ac.id/webhook/d14704c6-0264-43d4-a978-e17cccf06e45"

# Menyimpan semua hasil transkripsi dan data kandidat
all_transcripts = {}
candidate_info = {}
session_videos = {}


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


def parse_student_info(text: str) -> Dict[str, str]:
    """Ekstrak informasi mahasiswa dari transkrip"""
    info = {}

    # Ekstrak nama
    nama_match = re.search(r'Nama\s*:([A-Z\s]+?)(?:Fakultas|NRP)', text)
    if nama_match:
        info['Nama'] = nama_match.group(1).strip()

    # Ekstrak NRP
    nrp_match = re.search(r'NRP\s*:([A-Z0-9]+)', text)
    if nrp_match:
        info['NRP'] = nrp_match.group(1).strip()

    # Ekstrak Program Studi
    prodi_match = re.search(r'Program Studi\s*:([A-Z\s]+?)(?:Tempat|Program)', text)
    if prodi_match:
        info['Program_Studi'] = prodi_match.group(1).strip()

    # Ekstrak IPK
    ipk_match = re.search(r'Indeks Prestasi Kumulatif\s*:\s*([0-9.]+)', text)
    if ipk_match:
        info['IPK'] = float(ipk_match.group(1))

    # Ekstrak Total SKS
    sks_match = re.search(r'Jumlah SKS\s*:\s*([0-9]+)\s*SKS', text)
    if sks_match:
        info['Total_SKS'] = int(sks_match.group(1))

    return info


def parse_courses(text: str) -> List[Dict[str, str]]:
    """Ekstrak data mata kuliah dari transkrip"""
    courses = []
    seen_courses = set()

    # Cari semua kemunculan kode mata kuliah dan posisinya
    pattern_kode = r'([A-Z]{2}\d{4})(?=[A-Z\s])'
    matches = list(re.finditer(pattern_kode, text))

    for i, match in enumerate(matches):
        kode = match.group(1)

        # Ambil text mulai dari kode ini sampai kode berikutnya
        start_pos = match.end()
        if i < len(matches) - 1:
            end_pos = matches[i + 1].start()
        else:
            end_pos = len(text)

        fragment = text[start_pos:end_pos]
        fragment_clean = re.sub(r'\s+', ' ', fragment).strip()

        if len(fragment_clean) < 10:
            continue

        # Cari semester, SKS, dan nilai
        pattern_data = r'(\d-\d{2}/\d{2})\s*(\d+)\s*([A-E]\+?)'
        data_match = re.search(pattern_data, fragment_clean)

        if not data_match:
            continue

        semester = data_match.group(1)
        sks = int(data_match.group(2))
        nilai = data_match.group(3)

        # Nama mata kuliah adalah text sebelum semester
        nama_end_pos = data_match.start()
        mata_kuliah = fragment_clean[:nama_end_pos].strip()
        mata_kuliah = re.sub(r'\s+', ' ', mata_kuliah)
        mata_kuliah = re.sub(r'\s*/\s*$', '', mata_kuliah).strip()

        # Filter noise
        if (len(mata_kuliah) < 5 or
            'Kode' in mata_kuliah or
            'Mata Kuliah' in mata_kuliah or
            'SMT' in mata_kuliah):
            continue

        course_id = f"{kode}-{semester}"
        if course_id in seen_courses:
            continue

        courses.append({
            'Kode': kode,
            'Mata_Kuliah': mata_kuliah,
            'Semester': semester,
            'SKS': sks,
            'Nilai': nilai
        })
        seen_courses.add(course_id)

    return courses


def calculate_grade_point(grade: str) -> float:
    """Konversi nilai huruf ke bobot nilai"""
    grade_mapping = {
        'A': 4.00, 'B+': 3.50, 'B': 3.00,
        'C+': 2.50, 'C': 2.00, 'D': 1.00, 'E': 0.00
    }
    return grade_mapping.get(grade, 0.0)


def analyze_transcript(courses: List[Dict[str, str]]) -> Dict:
    """Analisis data transkrip"""
    analysis = {
        'total_courses': len(courses),
        'grade_distribution': {},
        'total_sks': 0,
        'weighted_sum': 0.0
    }

    for course in courses:
        grade = course['Nilai']
        analysis['grade_distribution'][grade] = analysis['grade_distribution'].get(grade, 0) + 1

        sks = course['SKS']
        grade_point = calculate_grade_point(grade)
        analysis['total_sks'] += sks
        analysis['weighted_sum'] += sks * grade_point

    if analysis['total_sks'] > 0:
        analysis['calculated_ipk'] = round(analysis['weighted_sum'] / analysis['total_sks'], 2)

    return analysis


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


@app.route('/upload-transkrip', methods=['POST'])
def upload_transkrip():
    try:
        if 'transkrip' not in request.files:
            return jsonify({'error': 'Tidak ada file transkrip'}), 400

        transkrip_file = request.files['transkrip']
        session_id = request.form.get('session_id', 'default')

        # Validasi file PDF
        if not transkrip_file.filename.endswith('.pdf'):
            return jsonify({'error': 'File transkrip harus berformat PDF'}), 400

        # Simpan transkrip
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        transkrip_filename = f"Transkrip_{session_id}_{timestamp}.pdf"
        transkrip_path = os.path.join(TRANSKRIP_DIR, transkrip_filename)
        transkrip_file.save(transkrip_path)

        # Extract dan parse transkrip
        transkrip_text = extract_text_from_pdf(transkrip_path)

        if not transkrip_text:
            return jsonify({'error': 'Gagal membaca file transkrip'}), 400

        # Parse informasi mahasiswa
        student_info = parse_student_info(transkrip_text)

        # Parse mata kuliah
        courses = parse_courses(transkrip_text)

        # Analisis transkrip
        analysis = analyze_transcript(courses)

        # Update candidate_info dengan data transkrip
        if session_id not in candidate_info:
            candidate_info[session_id] = {}

        candidate_info[session_id].update({
            "transkrip_filename": transkrip_filename,
            "transkrip_path": transkrip_path,
            "transkrip_nrp": student_info.get('NRP', ''),
            "transkrip_prodi": student_info.get('Program_Studi', ''),
            "transkrip_ipk": student_info.get('IPK', analysis.get('calculated_ipk', 0)),
            "transkrip_total_sks": student_info.get('Total_SKS', analysis.get('total_sks', 0)),
            "transkrip_total_mk": analysis.get('total_courses', 0),
            "transkrip_courses": courses,  # Simpan list mata kuliah
            "transkrip_analysis": analysis  # Simpan analisis lengkap
        })

        return jsonify({
            'success': True,
            'transkrip_filename': transkrip_filename,
            'student_info': student_info,
            'analysis': {
                'total_courses': analysis.get('total_courses', 0),
                'total_sks': analysis.get('total_sks', 0),
                'ipk': analysis.get('calculated_ipk', 0),
                'grade_distribution': analysis.get('grade_distribution', {})
            }
        })

    except Exception as e:
        print(f"Error upload transkrip: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    try:
        video_file = request.files.get('video')
        audio_file = request.files.get('audio')

        if not video_file and not audio_file:
            return jsonify({'error': 'Tidak ada file media'}), 400

        question_number = str(request.form.get('question_number', '0'))
        session_id = request.form.get('session_id', 'default')

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        extracted_audio_filename = f"answer_q{question_number}_{timestamp}.wav"
        audio_save_path = os.path.join(OUTPUT_DIR, extracted_audio_filename)
        media_filename = extracted_audio_filename
        media_save_path = audio_save_path

        if video_file:
            ext = os.path.splitext(video_file.filename)[1] or '.webm'
            media_filename = f"answer_q{question_number}_{timestamp}{ext}"
            media_save_path = os.path.join(VIDEO_OUTPUT_DIR, media_filename)
            video_file.save(media_save_path)

            if session_id not in session_videos:
                session_videos[session_id] = {}
            session_videos[session_id][f"pertanyaan_{question_number}"] = media_save_path

        if audio_file:
            audio_file.save(audio_save_path)
        elif video_file:
            return jsonify({'error': 'Audio tidak ditemukan, silakan rekam ulang.'}), 400
        else:
            return jsonify({'error': 'File audio diperlukan untuk transkripsi.'}), 400

        # Transkripsi suara
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_save_path) as source:
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
            "filename": media_filename
        }

        webhook_status = "pending"
        video_analysis_payload = {}

        # Kalau sudah pertanyaan terakhir (q4) → kirim semua ke n8n
        if question_number == "4":
            try:
                # Ambil data kandidat
                candidate = candidate_info.get(session_id, {})

                # Analisis seluruh video yang direkam
                session_video_files = session_videos.get(session_id, {})
                for key in sorted(session_video_files.keys()):
                    video_path = session_video_files[key]
                    try:
                        analysis_text = analyze_video_confidence(video_path)
                    except Exception as analysis_error:
                        analysis_text = f"Error analisis video: {str(analysis_error)}"
                    video_analysis_payload[f"analisis_{key}"] = analysis_text

                # 🔹 Struktur payload dengan CV TEXT (bukan file)
                payload = {
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

                    # Data Transkrip Akademik
                    "transkrip_nrp": candidate.get("transkrip_nrp", ""),
                    "transkrip_prodi": candidate.get("transkrip_prodi", ""),
                    "transkrip_ipk": candidate.get("transkrip_ipk", 0),
                    "transkrip_total_sks": candidate.get("transkrip_total_sks", 0),
                    "transkrip_total_mk": candidate.get("transkrip_total_mk", 0),
                    "transkrip_courses": candidate.get("transkrip_courses", []),
                    "transkrip_grade_distribution": candidate.get("transkrip_analysis", {}).get("grade_distribution", {})
                }

                if video_analysis_payload:
                    payload["analisis_video"] = video_analysis_payload

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
                    if session_id in session_videos:
                        del session_videos[session_id]
                else:
                    webhook_status = f"failed (HTTP {resp.status_code})"
                    print(f"❌ Webhook gagal: {resp.status_code} - {resp.text}")

            except Exception as e:
                webhook_status = f"error: {str(e)}"
                print(f"❌ Error kirim webhook: {str(e)}")

        return jsonify({
            'success': True,
            'transcript': text,
            'filename': media_filename,
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