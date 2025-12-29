import requests
import json
from datetime import datetime

# Webhook URL (PRODUCTION)
WEBHOOK_URL = "https://n8n-1.saturn.petra.ac.id/webhook/939b69b4-4d28-4531-b451-804809c2399c"

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
    "session_id": datetime.now().strftime("%Y%m%d_%H%M%S"),
    "timestamp_completed": datetime.now().isoformat(),

    # Data Kandidat
    "nama": "Willson Clevelan Jioe",
    "email": "c14220046@john.petra.ac.id",
    "posisi_dilamar": "Backend Developer",

    # CV Text
    "cv_text": """WILLSON CLEVELAN JIOE
085859120016 | willsoncj285@gmail.com | https://www.linkedin.com/in/willson-clevelan-jioe-6b5337293?
utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
Puri Surya Jaya B7 no 23, Gedangan, Sidoarjo, Jawa Timur
I am an active undergraduate Informatics student with a strong interest in web development. With hands-on
experience in various organizational and tech competition roles, I have developed skills in team collaboration, IT
project leadership, database design, and web development.

Work Experiences
Petra Christian University - Surabaya, Indonesia Dec 2024 - Present
Laboratory Assistant
Prepared labs and equipment before sessions, setting up for 5–10 practical sessions per week
Ensuring that the lab environment is well-maintained, organized, and ready for both teaching and practical use.
Petra Christian University - Surabaya, Indonesia Jan 2024 - Present
Assistant Lecturer
Assisted students during practicum sessions, supporting 20–25 students per session in understanding core programming concepts.
Evaluated and provided feedback on student assignments, improving coding accuracy and understanding, contributing to a 15%
increase in overall student performance.

Education Level
UK Petra - Surabaya, Indonesia Aug 2023 - Jul 2027 (Expected)
Bachelor of Informatics, 3.97/4.00
Certificate of Appreciation as the freshmen of 2023 with outstanding academic achievement
Organisational Experience
Welcome Grateful Generation 2024 - Surabaya, Indonesia Mar 2024 - Jul 2024
Member of IT Division
Welcome Grateful Generation, also known as Student Orientation, is an annual event dedicated to helping more than 1000 new students
transition smoothly into university life at Petra Christian University.
Designed and developed a user-friendly orientation polyclinic website, streamlining access for over 400 students and staff, and enabling
seamless back-end management for administrators.
Created an interactive game page for new students, increasing orientation engagement metrics by 40% and enhancing educational
outcomes through gamified learning.
Advance Servant Leadership Training 2024 - Surabaya, Indonesia Dec 2024 - Feb 2025
Member of IT Division
Advance Servant Leadership Training is an intensive annual leadership development program designed for individuals preparing to take on
key roles such as department heads, vice heads, and executive board positions (e.g., president, secretary, treasurer) within the
organization.
Implemented an admin dashboard to review, accept, or reject participant registrations, reducing manual processing time by 50%.
Developed functionality for scheduling and assigning interview sessions, improving coordinator efficiency and reducing scheduling errors
by 35%.
Epiclair: The Chosen Warior 2025 - Surabaya, Indonesia Dec 2024 - May 2025
Vice Coordinator of IT Division
Epiclair is an annual event organized by BEM Petra Christian University. It features internal competitions, where all faculties within Petra
Christian University compete to earn points across a variety of events, and external competitions, which are open to participants from all
over Indonesia.
Supported team management, tracking project progress and providing guidance, resulting in on-time delivery of 100% of internal IT
projects.
Designed and implemented a dynamic tournament bracket system using tree data structures, enabling clear visualization and
management of competitions for 50+ participants.
Welcome Grateful Generation 2025 - Surabaya, Indonesia Jan 2025 - Aug 2025
Internal Sub-coordinator of IT Division

Coordinated team members in the development of internal organizational websites and IT solutions, increasing overall team productivity
by 25%.""",

    # Transkrip Jawaban Interview
    "transkrip_pertanyaan_1": """Perkenalkan nama saya Willson Clevelan Jioe""",


    "transkrip_pertanyaan_2": """Karena dengan melamar di perusahaan ini, saya dapat menerapkan skill saya di dunia perusahaan yang asli sehingga tau bagaimana skill saya dapat berguna di kehidupan kerja.""",
    
    
    "transkrip_pertanyaan_3": """Saya memiliki pengalaman di bidang IT melalui organisasi seperti kepanitiaan suatu acara. Saya juga pernah menjadi wakil koordinator untuk divisi IT dalam suatu kepanitiaan.""",

    "transkrip_pertanyaan_4": """Karena saya yakin diri saya bisa berguna untuk kemajuan perusahaan. :)""",

    # Data Transkrip Akademik
    "transkrip_nrp": "c14230033",
    "transkrip_prodi": "INFORMATIKA",
    "transkrip_ipk": 3.97,
    "transkrip_total_sks": 88,
    "transkrip_total_mk": 31,
    "transkrip_courses": [
       {
      "Kode": "TF4249",
      "Mata_Kuliah": "PENGANTAR AKUNTANSI",
      "Semester": "1-23/24",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "FD4505",
      "Mata_Kuliah": "KALKULUS I",
      "Semester": "1-23/24",
      "SKS": 3,
      "Nilai": "B+"
    },
    {
      "Kode": "DU4122",
      "Mata_Kuliah": "BAHASA INDONESIA",
      "Semester": "1-23/24",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "TF4204",
      "Mata_Kuliah": "ALGORITMA DAN PEMROGRAMAN",
      "Semester": "1-23/24",
      "SKS": 5,
      "Nilai": "A"
    },
    {
      "Kode": "TF4205",
      "Mata_Kuliah": "DASAR SISTEM KOMPUTER",
      "Semester": "1-23/24",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "TF4504",
      "Mata_Kuliah": "BAHASA INGGRIS",
      "Semester": "1-23/24",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "DU4197",
      "Mata_Kuliah": "AGAMA DAN HIDUP BERMAKNA",
      "Semester": "1-23/24",
      "SKS": 4,
      "Nilai": "A"
    },
    {
      "Kode": "DU4101",
      "Mata_Kuliah": "PANCASILA",
      "Semester": "2-23/24",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "TF4227",
      "Mata_Kuliah": "STATISTIKA DASAR",
      "Semester": "2-23/24",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4245",
      "Mata_Kuliah": "MATEMATIKA DISKRIT",
      "Semester": "2-23/24",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4253",
      "Mata_Kuliah": "JARINGAN KOMPUTER",
      "Semester": "2-23/24",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4267",
      "Mata_Kuliah": "KOMUNIKASI INTERPERSONAL",
      "Semester": "2-23/24",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4229",
      "Mata_Kuliah": "BASIS DATA",
      "Semester": "2-23/24",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4235",
      "Mata_Kuliah": "PEMROGRAMAN BERORIENTASI OBYEK",
      "Semester": "2-23/24",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4343",
      "Mata_Kuliah": "TEKNOLOGI WEB",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4219",
      "Mata_Kuliah": "STRUKTUR DATA",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4270",
      "Mata_Kuliah": "DESAIN DAN ANALISIS ALGORITMA",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4591",
      "Mata_Kuliah": "SOFTWARE DESIGN AND ARCHITECTURE",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4243",
      "Mata_Kuliah": "SISTEM OPERASI",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4372",
      "Mata_Kuliah": "ARSITEKTUR DAN ORGANISASI KOMPUTER",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "DU4198",
      "Mata_Kuliah": "DIGITAL LEADERSHIP",
      "Semester": "1-24/25",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "DU4210",
      "Mata_Kuliah": "KEWARGANEGARAAN",
      "Semester": "1-24/25",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "DU4163",
      "Mata_Kuliah": "ETIKA PROFESI",
      "Semester": "1-24/25",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "FD4508",
      "Mata_Kuliah": "TECHNOPRENEURSHIP",
      "Semester": "2-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4579",
      "Mata_Kuliah": "WEB FRAMEWORKS AND DEPLOYMENT",
      "Semester": "2-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "FD4507",
      "Mata_Kuliah": "ALJABAR LINIER",
      "Semester": "2-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4255",
      "Mata_Kuliah": "REKAYASA PERANGKAT LUNAK",
      "Semester": "2-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4578",
      "Mata_Kuliah": "ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING (AIML)",
      "Semester": "2-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4544",
      "Mata_Kuliah": "CYBER OPERATIONS",
      "Semester": "2-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4247",
      "Mata_Kuliah": "METODE NUMERIK",
      "Semester": "2-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4592",
      "Mata_Kuliah": "ASSOCIATE DATA SCIENTIST",
      "Semester": "2-24/25",
      "SKS": 3,
      "Nilai": "A"
    }
  ],
    "transkrip_grade_distribution": {
       "A": 29,
      "B+": 2,
      "B": 0,
      "C+": 0
    },

    # Data SKKK
    
   "skkk_data": [
    {
      "No": 1,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "GUEST LECTURE - WORLD CLASS PROFESSOR",
      "Nilai_SKKK": 4.5,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 2,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "TECHNICAL PROGRAM MANAGEMENT IN B2B VS B2C WEBINAR",
      "Nilai_SKKK": 7.5,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 3,
      "Jabatan": "Peserta UKM",
      "Nama_Kegiatan": "KEGIATAN RUTIN UKM VOLI 2024",
      "Nilai_SKKK": 10,
      "Periode": "232",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 4,
      "Jabatan": "Anggota HIMA",
      "Nama_Kegiatan": "PENGAWAS PELAKSANAAN BEBRAS CHALLENGE 2023",
      "Nilai_SKKK": 1,
      "Periode": "232",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 5,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "SEMINAR THE ROLE OF AI IN LOGISTIC",
      "Nilai_SKKK": 3,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 6,
      "Jabatan": "Peserta",
      "Nama_Kegiatan": "SERVANT LEADERSHIP TRAINING 2024",
      "Nilai_SKKK": 3,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 7,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "SL - KOMAL (A,B,C,D) - GENAP 23/24 (5/2/24 - 28/6/24)",
      "Nilai_SKKK": 2,
      "Periode": "232",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 8,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "TUTORIAL UAS SEMESTER GENAP 2024",
      "Nilai_SKKK": 1.5,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 9,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "WORKSHOP PELATIHAN LOMBA GEMASTIK II CYBER SECURITY",
      "Nilai_SKKK": 1.5,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 10,
      "Jabatan": "Anggota HIMA - IT",
      "Nama_Kegiatan": "INDUSTRIAL COMPETITION 2024",
      "Nilai_SKKK": 13.2,
      "Periode": "241",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 11,
      "Jabatan": "Anggota HIMA - Divisi Information Technology",
      "Nama_Kegiatan": "PANITIA WELCOME, GRATEFUL GENERATION 2024",
      "Nilai_SKKK": 9.9,
      "Periode": "241",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 12,
      "Jabatan": "Peserta",
      "Nama_Kegiatan": "SL KOLABORASI SERVICE LEARNING MK. PANCASILA, KEWARGANEGARAAN,-BHS. INDONESIA GASAL 24/25",
      "Nilai_SKKK": 2,
      "Periode": "241",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 13,
      "Jabatan": "Anggota HIMA - IT",
      "Nama_Kegiatan": "ADVANCED SERVANT LEADERSHIP TRAINING 2025",
      "Nilai_SKKK": 6.6,
      "Periode": "242",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 14,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "CAREER SHAPING IN ENTREPRENEURIAL 2025",
      "Nilai_SKKK": 3.8,
      "Periode": "242",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 15,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "DIES NATALIS INFORMATIKA 27",
      "Nilai_SKKK": 1.5,
      "Periode": "242",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 16,
      "Jabatan": "Anggota HIMA - Information Technology",
      "Nama_Kegiatan": "EPICLAIR: THE CHOSEN WARRIOR 2025 (EXTERNUS)",
      "Nilai_SKKK": 13.2,
      "Periode": "242",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 17,
      "Jabatan": "Anggota HIMA",
      "Nama_Kegiatan": "FESTIVAL HUT GENTA 61",
      "Nilai_SKKK": 1,
      "Periode": "242",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 18,
      "Jabatan": "Anggota HIMA",
      "Nama_Kegiatan": "FESTIVAL HUT GENTA 61",
      "Nilai_SKKK": 13.2,
      "Periode": "242",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 19,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "FESTIVE YOUTH INTERSALON 2025",
      "Nilai_SKKK": 6,
      "Periode": "242",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 20,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "NUNI INTERNATIONAL SEMINAR SERIES #9 COMPLEX NETWORKS: TOPOLOGICAL ANALYSIS OF CONNECTIVITY",
      "Nilai_SKKK": 7.5,
      "Periode": "242",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 21,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "NUNI INTERNATIONAL SEMINAR SERIES #9 FINANCIAL LITERACY AND FINTECH",
      "Nilai_SKKK": 7.5,
      "Periode": "242",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 22,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "NUNI INTERNATIONAL SEMINAR SERIES #9 UNDERSTANDING AND ANALYZING WORK MOTIVATION THROUGH DATA",
      "Nilai_SKKK": 7.5,
      "Periode": "242",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 23,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "TRASHURE 2025",
      "Nilai_SKKK": 4.5,
      "Periode": "242",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 24,
      "Jabatan": "Anggota HIMA - Divisi IT",
      "Nama_Kegiatan": "WELCOME, GRATEFUL GENERATION 2025",
      "Nilai_SKKK": 9.9,
      "Periode": "251",
      "Bidang": "Organisasi & Kepemimpinan"
    }
  ],
  "skkk_total_activities": 24,
  "skkk_success": True,


    # Analisis Video +
    "analisis_video": {
    "analisis_pertanyaan_1": "analisis: Subjek kesulitan mempertahankan focus selama menjawab. Sering terdistraksi dan harus dikembalikan ke topik utama oleh pewawancara. kesimpulan: 58",
    "analisis_pertanyaan_2": "analisis: Penjelasan teknis yang diberikan mengandung beberapa kesalahan konsep. Subjek tidak terlihat yakin dengan informasi yang disampaikan. kesimpulan: 60",
    "analisis_pertanyaan_3": "analisis: Bahasa tubuh sangat defensive dengan tangan yang disilangkan. Nada bicara terdengar sedikit defensif saat pertanyaan menantang diajukan. kesimpulan: 57",
    "analisis_pertanyaan_4": "analisis: Subjek memberikan jawaban yang terlalu pendek tanpa elaborasi yang memadai. Terkesan tidak memiliki pengetahuan yang cukup tentang topik. kesimpulan: 54"
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
