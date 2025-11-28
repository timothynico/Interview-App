import requests
import json
from datetime import datetime

# Webhook URL (PRODUCTION)
WEBHOOK_URL = "https://n8n-1.saturn.petra.ac.id/webhook-test/939b69b4-4d28-4531-b451-804809c2399c"

print("="*80)
print("SENDING DUMMY DATA TO WEBHOOK (PRODUCTION)")
print("="*80)
print(f"Webhook URL: {WEBHOOK_URL}\n")

# =============================================================================
# INTERVIEW SELESAI (DATA LENGKAP)
# =============================================================================
print("="*80)
print("KIRIM DATA INTERVIEW LENGKAP + TRANSKRIP + SKKK")
print("="*80)

payload = {
    "session_id": "test_dummy_" + datetime.now().strftime("%Y%m%d_%H%M%S"),
    "timestamp_completed": datetime.now().isoformat(),

    # Data Kandidat
    "nama": "Timothy Nico Test",
    "email": "timothy.test@example.com",
    "posisi_dilamar": "Data Scientist",

    # CV Text
    "cv_text": "TIMOTHY NICO\nSurabaya, Indonesia | +62 812 3456 7890 | timothy.nico@example.com\n\nPROFESSIONAL SUMMARY\nPassionate Data Scientist with strong background in Informatics and AI. Experienced in machine learning and data analytics.\n\nEDUCATION\nPetra Christian University - Bachelor of Informatics (AI Specialization)\nGPA: 3.86/4.00 | 2021-2025\n\nEXPERIENCE\nData Scientist Intern - Tech Innovate Lab (Jun 2024 - Aug 2024)\n- Developed ML models for customer behavior prediction\n- Improved model accuracy by 10%\n\nTECHNICAL SKILLS\nPython, R, SQL, TensorFlow, Scikit-learn, Docker, Git\n\nPROJECTS\n- Customer Churn Prediction (92% accuracy)\n- Sales Forecasting using LSTM",

    # Transkrip Jawaban Interview
    "transkrip_pertanyaan_1": "Saya tertarik dengan posisi Data Scientist ini karena saya memiliki passion dalam mengolah data menjadi insight yang valuable. Selama kuliah saya fokus di AI dan machine learning, dan saya ingin mengaplikasikan skill ini untuk membantu perusahaan membuat keputusan berbasis data.",
    "transkrip_pertanyaan_2": "Kelebihan saya adalah analytical thinking yang kuat, kemampuan programming yang baik terutama di Python dan R, serta kemampuan storytelling dengan data. Saya juga cepat belajar teknologi baru dan bisa bekerja sama dalam tim.",
    "transkrip_pertanyaan_3": "Saya pernah membuat project Customer Churn Prediction menggunakan Random Forest dan XGBoost dengan akurasi 92%. Saya juga deploy model tersebut menggunakan FastAPI dan Docker. Project lainnya adalah Sales Forecasting menggunakan LSTM yang meningkatkan akurasi prediksi 18% dibanding baseline ARIMA.",
    "transkrip_pertanyaan_4": "5 tahun ke depan saya ingin menjadi Senior Data Scientist yang expert dalam deep learning dan bisa lead ML projects end-to-end. Saya juga ingin berkontribusi dalam research dan berbagi knowledge melalui mentoring dan technical writing.",

    # Data Transkrip Akademik
    "transkrip_nrp": "C14220062",
    "transkrip_prodi": "INFORMATIKA",
    "transkrip_ipk": 3.86,
    "transkrip_total_sks": 144,
    "transkrip_total_mk": 48,
    "transkrip_courses": [
        {"Kode": "IF1234", "Mata_Kuliah": "Pemrograman Berorientasi Objek", "Semester": "1-21/22", "SKS": 3, "Nilai": "A"},
        {"Kode": "IF5678", "Mata_Kuliah": "Basis Data", "Semester": "2-21/22", "SKS": 4, "Nilai": "A"},
        {"Kode": "IF9012", "Mata_Kuliah": "Algoritma dan Struktur Data", "Semester": "1-21/22", "SKS": 4, "Nilai": "A"},
        {"Kode": "IF3456", "Mata_Kuliah": "Machine Learning", "Semester": "1-23/24", "SKS": 3, "Nilai": "A"},
        {"Kode": "IF7890", "Mata_Kuliah": "Deep Learning", "Semester": "2-23/24", "SKS": 3, "Nilai": "A"},
        {"Kode": "IF2345", "Mata_Kuliah": "Data Mining", "Semester": "1-23/24", "SKS": 3, "Nilai": "A"},
        {"Kode": "IF6789", "Mata_Kuliah": "Computer Vision", "Semester": "2-23/24", "SKS": 3, "Nilai": "B+"},
        {"Kode": "IF4567", "Mata_Kuliah": "Natural Language Processing", "Semester": "1-24/25", "SKS": 3, "Nilai": "A"}
    ],
    "transkrip_grade_distribution": {
        "A": 38,
        "B+": 8,
        "B": 2
    },

    # Data SKKK
    "skkk_data": [
        {
            "No": "1",
            "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR",
            "Nama \r\n              Kegiatan": "ACTS 2022",
            "Nilai \r\n              SKKK": "3.000",
            "Periode": "221",
            "Bidang": "PEMBELAJARAN"
        },
        {
            "No": "2",
            "Jabatan": "PANITIA : KETUA PANITIA",
            "Nama \r\n              Kegiatan": "BANK PANITIA INFORMATICS COMMITTEE CLUB 2022",
            "Nilai \r\n              SKKK": "6.000",
            "Periode": "221",
            "Bidang": "PEMBELAJARAN"
        },
        {
            "No": "3",
            "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR",
            "Nama \r\n              Kegiatan": "KULIAH UMUM - AI AND MACHINE LEARNING",
            "Nilai \r\n              SKKK": "1.500",
            "Periode": "222",
            "Bidang": "PEMBELAJARAN"
        },
        {
            "No": "4",
            "Jabatan": "PANITIA : ANGGOTA DIVISI",
            "Nama \r\n              Kegiatan": "HACKATHON DATA SCIENCE 2023",
            "Nilai \r\n              SKKK": "4.500",
            "Periode": "231",
            "Bidang": "PEMBELAJARAN"
        },
        {
            "No": "5",
            "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR",
            "Nama \r\n              Kegiatan": "SEMINAR NASIONAL ARTIFICIAL INTELLIGENCE",
            "Nilai \r\n              SKKK": "6.000",
            "Periode": "232",
            "Bidang": "PEMBELAJARAN"
        }
    ],
    "skkk_total_activities": 30,
    "skkk_success": True,

    # Analisis Video
    "analisis_video": {
        "analisis_pertanyaan_1": "Confidence: High\nBody Language: Positive, maintaining good posture\nEye Contact: Good, consistent throughout\nSpeech Clarity: Clear and articulate\nEngagement: High, shows enthusiasm",
        "analisis_pertanyaan_2": "Confidence: High\nBody Language: Engaged, uses appropriate gestures\nEye Contact: Excellent\nSpeech Clarity: Very clear with good pacing\nEngagement: Excellent, passionate about the topic",
        "analisis_pertanyaan_3": "Confidence: Very High\nBody Language: Confident, animated when discussing projects\nEye Contact: Excellent, maintains strong connection\nSpeech Clarity: Clear with technical terminology\nEngagement: Excellent, demonstrates deep knowledge",
        "analisis_pertanyaan_4": "Confidence: High\nBody Language: Professional and forward-looking\nEye Contact: Good\nSpeech Clarity: Clear and thoughtful\nEngagement: High, shows career vision"
    }
}

print("\nMengirim data ke webhook...")
print("\nPayload Summary:")
print(f"  - Session ID: {payload['session_id']}")
print(f"  - Nama: {payload['nama']}")
print(f"  - Email: {payload['email']}")
print(f"  - Posisi: {payload['posisi_dilamar']}")
print(f"  - NRP: {payload['transkrip_nrp']}")
print(f"  - IPK: {payload['transkrip_ipk']}")
print(f"  - Total Mata Kuliah: {payload['transkrip_total_mk']}")
print(f"  - Total SKKK: {payload['skkk_total_activities']}")
print()

try:
    response = requests.post(
        WEBHOOK_URL,
        json=payload,
        headers={"Content-Type": "application/json"},
        timeout=30
    )

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        print("\n[SUCCESS] Data dummy berhasil dikirim ke webhook!")
        try:
            response_data = response.json()
            print(f"\nResponse dari n8n:")
            print(json.dumps(response_data, indent=2, ensure_ascii=False))
        except:
            print(f"\nResponse Text: {response.text}")
    else:
        print(f"\n[FAILED] Webhook gagal: HTTP {response.status_code}")
        print(f"Response: {response.text}")

except requests.Timeout:
    print("\n[TIMEOUT] Webhook tidak merespons dalam 30 detik")
except requests.RequestException as e:
    print(f"\n[ERROR] Network error: {str(e)}")
except Exception as e:
    print(f"\n[ERROR] {str(e)}")


# =============================================================================
# SUMMARY
# =============================================================================
print("\n\n" + "="*80)
print("SUMMARY")
print("="*80)
print(f"Webhook URL: {WEBHOOK_URL}")

try:
    status = "SUCCESS" if response.status_code == 200 else f"FAILED (HTTP {response.status_code})"
    print(f"\nStatus: {status}")
except:
    print(f"\nStatus: ERROR")

print("\nData yang dikirim:")
print(f"  - CV: {len(payload['cv_text'])} characters")
print(f"  - Interview Answers: 4 pertanyaan")
print(f"  - Transkrip Akademik: {len(payload['transkrip_courses'])} mata kuliah")
print(f"  - SKKK: {len(payload['skkk_data'])} kegiatan")
print(f"  - Video Analysis: 4 pertanyaan")

print("\n>>> Cek n8n workflow untuk melihat data yang diterima! <<<")
print("="*80)
