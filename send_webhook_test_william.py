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
    "nama": "William Constantine Jioe ",
    "email": "c14220046@john.petra.ac.id",
    "posisi_dilamar": "Backend Developer",

    # CV Text
    "cv_text": """WILLIAM CONSTANTINE JIOE
081252899579 | w1ll14m285@gmail.com | https://www.linkedin.com/in/william-constantine-jioe-90099a368
Puri Surya Jaya B7/23, Gedangan, Sidoarjo
I am a 5th semester Informatics student at Petra Christian University with a strong interest in software
engineering and AI engineering. I enjoy exploring how technology can solve real-world problems and
continuously seek opportunities to grow my skills in programming, system design, and artificial intelligence.

Work Experiences
Petra Christian University - Indonesia, Surabaya Jan 2024 - Present
Assistant Lecturer
Petra Christian University - Indonesia, Surabaya Dec 2024 - Present
Laboratory Assistant
Education Level
UK Petra - Surabaya, Indonesia Aug 2023 - Dec 2026 (Expected)
Bachelor of Informatics, 3.96/4.00
Organisational Experience
Battle of Minds 2025 - Surabaya, Indonesia Sep 2024 - Sep 2025
Sub Coordinator of Information Technology Division
Battle of Minds (BoM) 2025 is a logic and mathematics competition organized by the Faculty of Industrial Technology at Petra Christian
University. The event is designed for high school students to challenge their critical thinking, problem-solving, and analytical skills through a
series of logic and math-based tests. Each team consists of three members, working together to solve complex problems and compete for
the championship title.
Supervised team members and assisted the coordinator to ensure smooth event execution, contributing to the success of an event with
100+ participants.
Developed a web-based game used in the first elimination round, engaging 100+ high school participants.
Built a real-time lobby system that allowed participants to seamlessly select and join the elimination game, reducing waiting time by 50%
and improving user experience.
Innofashion Show 7 - Surabaya, Indonesia Mar 2025 - Aug 2025
Sub Coordinator of Information Technology Division
Innofashion Show 7 is the largest and most prestigious event organized by the Fashion Design and Textile program, a key department
within the Faculty of Design and Visual Communication of Petra Christian University. This annual event brings together aspiring designers
to showcase their creativity and talent in the world of fashion. The event consists of a design competition, where participants are tasked
with creating innovative and original clothing pieces that push the boundaries of fashion. The highlight of the event is a dazzling fashion
show, where the winning designs are presented on the runway, giving the designers a platform to gain recognition for their work.
Innofashion Show 7 not only celebrates the skills of budding designers but also fosters collaboration, creativity, and the spirit of innovation
within the fashion community.
Developed a user-friendly registration form to simplify the sign-up process, resulting in a 30% faster registration flow and ensuring
accurate data collection for participants.
Built an admin dashboard to manage participants, submissions, and event data efficiently, improving event coordination and reducing
manual tracking time by 60%.
Welcome Grateful Generation 2024 - Surabaya, Indonesia Mar 2024 - Jul 2024
Member of Information Technology Division
Welcome Grateful Generation 2024 is an annual orientation event designed to warmly welcome new students and help them begin their
journey with strong spiritual and academic foundations. This year’s theme, “On The Solid Rock I Stand,” emphasizes our commitment to
nurturing a resilient, purpose-driven community rooted in faith, values, and meaningful connection. Through various activities and sessions,
the event aims to inspire, equip, and unite the newest generation as they step into a new chapter of growth and discovery.
Created polyclinic Management Web App, reduced patient registration time by 40% and improve record-keeping accuracy
Epiclair 2024 - Surabaya, Indonesia Dec 2023 - Dec 2024
Member of Information Technology Division
Epiclair 2024 was a dynamic competition-based event featuring two main editions that showcased both athletic and creative talents. The
BOM Edition was an internal sports competition exclusively for Petra students, featuring popular sports such as Badminton, Basketball,
Football, Volleyball, and Table Tennis, fostering camaraderie and school spirit. Meanwhile, the Global Showdown Edition was open to the

public, expanding the excitement with diverse categories including Esports, Chess, Illustration, Decor, and Dance—providing a platform for
broader participation and creative expression.
Developed the login page for individual Decor participants, simplified user onboarding, enabling 50+ participants to securely access the
platform.
Created the submission system for participants in the Decor category to upload their work, facilitated smooth handling of 50+ project
submissions and reducing manual errors by 60%
Assisted in the early stages of tournament bracket creation, contributed to organizing a bracket system that handled 50+ participants
efficiently.
Advance Servant Leadership Training 2025 - Surabaya, Indonesia Dec 2024 - Feb 2025
Member of Information Technology Division
Advance Servant Leadership Training (ASLT) 2025 is a leadership development program that equips university students with strong
leadership character grounded in servant leadership values. The program focuses on mentoring and practical training to shape future
leaders who lead with purpose, empathy, and integrity.
Developed material management system where admins could upload leadership training materials, streamlined content delivery,
reducing manual distribution by 60%
Created a participant portal to access and read the uploaded materials, improved accessibility for participants during training by 40%
Created submission system for assignments, enabling participants to upload tasks and allowing admins to monitor progress and
completion, increased submission tracking efficiency by 45-50%
Skills, Achievements & Other Experience
Projects  (2025): AI Video Summarizer is a React-based web app that transforms YouTube videos into structured, easy-to-read
summaries. Users simply paste a video link, and the app leverages n8n automation and Gemini AI to analyze the content, generating
key insights and actionable tips in clean HTML and downloadable PDF format. By removing the need to watch full videos, it helps users
quickly digest long-form content, making information consumption efficient and shareable, all deployed seamlessly on Vercel.
Projects (2024): Real-Time BISINDO Hand Gesture Recognition (Group Project): We make the implementation of a Long Short-Term
Memory (LSTM) model using TensorFlow/Keras for real-time classification of 5 BISINDO hand gestures. The system utilized MediaPipe
Holistic to extract 126 keypoints from hand sequences. Through optimization techniques like Batch Normalization and Dropout to
manage the limited dataset (5 classes, 60 sequences each), the model achieved a high training accuracy of 96.49%, showcasing
proficiency in sequence modeling and real-time computer vision.""",

    # Transkrip Jawaban Interview
    "transkrip_pertanyaan_1": """Halo Ibu Lesti, terima kasih atas kesempatannya.
Perkenalkan, nama saya William Constantine Jioe. Saya merupakan pribadi yang bertanggung jawab, cepat belajar, dan terbiasa bekerja secara terstruktur maupun kolaboratif. Saya memiliki ketertarikan untuk terus mengembangkan kemampuan profesional, khususnya dalam bidang IT terutama Backend Developer. Dalam setiap pekerjaan, saya selalu berusaha memberikan hasil terbaik dengan tetap menjunjung tinggi etika dan profesionalisme.""",


    "transkrip_pertanyaan_2": """Saya tertarik melamar di PT XYZ karena perusahaan ini memiliki reputasi yang baik, visi yang jelas, serta komitmen terhadap pengembangan karyawan. Saya melihat PT XYZ sebagai perusahaan yang tidak hanya berorientasi pada hasil, tetapi juga pada kualitas SDM dan inovasi. Hal tersebut sejalan dengan nilai dan tujuan karier saya, di mana saya ingin bertumbuh bersama perusahaan yang stabil dan progresif.""",
    
    
    "transkrip_pertanyaan_3": """Saya memiliki pengalaman sebagai Backend Developer dalam mengembangkan dan memelihara sistem backend untuk aplikasi berbasis web. Saya terbiasa membangun RESTful API menggunakan framework backend seperti Node.js/Laravel serta mengelola database MySQL/PostgreSQL mulai dari perancangan skema hingga optimasi query. Selain itu, saya pernah mengimplementasikan fitur autentikasi dan otorisasi pengguna, melakukan integrasi dengan API pihak ketiga, serta memastikan performa dan keamanan sistem berjalan dengan baik. Dalam proses pengembangan, saya terbiasa menggunakan Git untuk version control, melakukan debugging, testing, dan berkolaborasi dengan tim frontend maupun tim terkait lainnya.""",

    "transkrip_pertanyaan_4": """Menurut saya, PT XYZ perlu mempertimbangkan saya karena saya memiliki kombinasi antara sikap kerja yang positif, kemampuan yang relevan, serta komitmen untuk berkembang jangka panjang. Saya bukan hanya ingin bekerja, tetapi juga berkontribusi secara nyata bagi perusahaan. Saya siap belajar, beradaptasi dengan budaya perusahaan, dan memberikan kinerja terbaik agar dapat mendukung pencapaian tujuan PT XYZ.""",

    # Data Transkrip Akademik
    "transkrip_nrp": "c14230036",
    "transkrip_prodi": "INFORMATIKA",
    "transkrip_ipk": 3.96,
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
      "Kode": "DU4122",
      "Mata_Kuliah": "BAHASA INDONESIA",
      "Semester": "1-23/24",
      "SKS": 2,
      "Nilai": "B+"
    },
    {
      "Kode": "FD4505",
      "Mata_Kuliah": "KALKULUS I",
      "Semester": "1-23/24",
      "SKS": 3,
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
      "Nilai": "B+"
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
      "Kode": "DU4210",
      "Mata_Kuliah": "KEWARGANEGARAAN",
      "Semester": "1-24/25",
      "SKS": 2,
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
      "Nilai": "A"
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
      "Kode": "DU4163",
      "Mata_Kuliah": "ETIKA PROFESI",
      "Semester": "1-24/25",
      "SKS": 2,
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
      "Kode": "TF4592",
      "Mata_Kuliah": "ASSOCIATE DATA SCIENTIST",
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
      "Kode": "FD4508",
      "Mata_Kuliah": "TECHNOPRENEURSHIP",
      "Semester": "2-24/25",
      "SKS": 3,
      "Nilai": "B+"
    }
  ],
    "transkrip_grade_distribution": {
      "A": 28,
      "B+": 3,
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
      "Jabatan": "Anggota",
      "Nama_Kegiatan": "EPICLAIR 2024",
      "Nilai_SKKK": 16.5,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 4,
      "Jabatan": "Peserta UKM",
      "Nama_Kegiatan": "KEGIATAN RUTIN UKM VOLI 2024",
      "Nilai_SKKK": 10,
      "Periode": "232",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 5,
      "Jabatan": "Anggota HIMA",
      "Nama_Kegiatan": "PENGAWAS PELAKSANAAN BEBRAS CHALLENGE 2023",
      "Nilai_SKKK": 1,
      "Periode": "232",
      "Bidang": "Pengabdian Masyarakat"
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
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "EPICLAIR: THE CHOSEN WARRIOR 2025 (INTERNUS)",
      "Nilai_SKKK": 3,
      "Periode": "242",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 17,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "FESTIVE YOUTH INTERSALON 2025",
      "Nilai_SKKK": 6,
      "Periode": "242",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 18,
      "Jabatan": "Anggota HIMA - Divisi IT",
      "Nama_Kegiatan": "LIFE ENRICHMENT 13 2024",
      "Nilai_SKKK": 6.6,
      "Periode": "242",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 19,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "NUNI INTERNATIONAL SEMINAR SERIES #9 COMPLEX NETWORKS: TOPOLOGICAL ANALYSIS OF CONNECTIVITY",
      "Nilai_SKKK": 7.5,
      "Periode": "242",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 20,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "NUNI INTERNATIONAL SEMINAR SERIES #9 FINANCIAL LITERACY AND FINTECH",
      "Nilai_SKKK": 7.5,
      "Periode": "242",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 21,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "NUNI INTERNATIONAL SEMINAR SERIES #9 UNDERSTANDING AND ANALYZING WORK MOTIVATION THROUGH DATA",
      "Nilai_SKKK": 7.5,
      "Periode": "242",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 22,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "TRASHURE 2025",
      "Nilai_SKKK": 4.5,
      "Periode": "242",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 23,
      "Jabatan": "Anggota HIMA - IT",
      "Nama_Kegiatan": "BATTLE OF MINDS 2025",
      "Nilai_SKKK": 9.9,
      "Periode": "251",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 24,
      "Jabatan": "Anggota HIMA - IT",
      "Nama_Kegiatan": "INNOFASHION SHOW 7",
      "Nilai_SKKK": 16.5,
      "Periode": "251",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 25,
      "Jabatan": "Juara I",
      "Nama_Kegiatan": "PADJADJARAN STATISTICS OLYMPIAD (RASIO) 2025",
      "Nilai_SKKK": 7.5,
      "Periode": "251",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 26,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "PEMBUATAN APLIKASI DATA JEMAAT UNTUK GEREJA KRISTEN INDONESIA MAJELIS JEMAAT PONDOK TJANDRA",
      "Nilai_SKKK": 1,
      "Periode": "251",
      "Bidang": "Pengabdian Masyarakat"
    }
  ],
  "skkk_total_activities": 26,
  "skkk_success": True,


    # Analisis Video +
    "analisis_video": {
      "analisis_pertanyaan_1": "analisis: Subjek memberikan jawaban yang tidak terorganisir dengan baik. Sulit mengikuti alur pemikiran yang disampaikan karena terlalu loncat-loncat. kesimpulan: 59",
      "analisis_pertanyaan_2": "analisis: Terlihat sangat tegang dengan bahu yang kaku dan postur yang rigid. Suara monoton tanpa variasi intonasi yang membuat penjelasan kurang engaging. kesimpulan: 61",
      "analisis_pertanyaan_3": "analisis: Subjek tidak mampu menjawab pertanyaan follow-up dengan baik. Terlihat kesulitan saat diminta untuk mengelaborasi poin tertentu. kesimpulan: 56",
      "analisis_pertanyaan_4": "analisis: Jawaban sangat generic dan seperti copy-paste dari teori tanpa personalisasi atau insight pribadi. Kurang menunjukkan critical thinking. kesimpulan: 58"
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
