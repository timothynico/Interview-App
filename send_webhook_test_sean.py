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
    "nama": "Sean Christophe Hartanto",
    "email": "c14220046@john.petra.ac.id",
    "posisi_dilamar": "Backend Developer",

    # CV Text
    "cv_text": """SEAN CHRISTOPHE HARTANTO
08819431535 | sean.christophe123@gmail.com | https://www.linkedin.com/in/sean-christophe-hartanto |
https://847980.itch.io
Surabaya
Christophe is an informatics student at Petra Christian University, class of 2022, focusing on game development
as both his academic concentration and future career path. He has strong technical skills in Unreal Engine and
Unity, along with solid public speaking and project management abilities.

Education Level
Petra Christian University  - Surabaya, Indonesia Jul 2022 - Jun 2026 (Expected)
Bachelor of Informatics, Game Developer, 3.92/4.00
Student Leadership and Basic Management Training
Top 10% Academic Achievement in Class of 2022
Participated in 7 Committee Events at the HIMA and Student Executive Board (BEM) levels
Volunteered in 7 Community Service Activities
Current Game Developer Projects
Aim to Mite Studio - Unity Jan 2025 - Present
Internship
Game development studio founded in 2022, with 20+ titles published on Play Store and Steam. Its best-selling game, Berandal Sekolah,
reached over 2 million downloads. The team is now developing the sequel, Berandal City, along with several new mobile games.
I contributed to the released android titles Waifuku Menjadi Nyata and Brainrot Battle Tung Tung Sahur, and I’m currently involved in
Squiddy Squad: Party Game, which is still in development. I am also working on confidential projects in collaboration with other studios and
B2B clients.
Collaborating closely with teammates to create games with engaging player experiences
Responsible for developing game UI, gameplay mechanics, and backend systems
Conducting research and integrating various services provided by Unity and Google, including Google Login, Play Asset Delivery,
Firebase, and Unity Services, to achieve faster game development and deliver a better player experience
Board Game - Card Game Oct 2024 - Dec 2024
Promotional Game
Collaborating in a team of four to create a game promoting the Strategic Communication Bachelor Program to high school students
Responsible for developing the story, mechanics, and incremental prototypes
Project fulfills requirements for the Game Content concentration course
Planned testing with PCU's Strategic Communication faculty, the head of the study program, and high school students
Ngeluber! - Unreal Engine Aug 2024 - Jan 2025
Educational Game
Collaborating in a team of four as project manager
Developing the Game Design Document (GDD) and programming the game in Unreal Engine 5.5
Fulfilling requirements for concentration courses in Game Design, Game Programming, and Project Management
Co-curricular Activites & Leadership
Laboratory Assistant - Informatics PCU Jul 2024 - Jan 2025
VR Laboratory
Virtual Reality Lab Manager
Promoted the Informatics Program at PCU through the Visit PCU initiative
Teaching Assistant - Informatics PCU Jun 2023 - Jan 2025
Part Time
Teaching Assistant for Programming Algorithms, Data Structures, and Algorithm Design and Analysis
Student Executive Board Officer 2023/2024 - PCU Jul 2023 - Jun 2024
Patriotic Social Creative
Served as an officer in the PSC Department, where we focused on discussing social, political, and nationalism issues.
Managed the @bisikbybempetra instagram account
Responsible for content creation and engagement from September 2023 to June 2024

Served as monthly PIC in rotation
Produced 55 Stories, 56 Feed posts, and 11 Reels
Skills, Achievements & Other Experience
Global Game Jam Surabaya  (2025): Participated in a 48-Hours Game Jam with a team of four
3rd Winner LO Kreatif International  (2024): Created a Maggot Farming game for SDGs in collaboration with IPDM PCU
Kenney Jam  (2024): Joined a 2-day Game Jam with a senior developer (Alumni)
Gemastik Competition  (2024): Developed an Android Mobile Game Supporting SDGs
GameDev.TV Game Jam  (2024): Contributed as a junior developer in a 10-day Game Jam with a team of six
National Research Paper Competition  (2023): 3rd runner up winner at Dies Natalis AMN Surabaya
Compfest Game Jam & Competition  (2024): Participated in a 3-Day Game Jam with a team of three""",

    # Transkrip Jawaban Interview
    "transkrip_pertanyaan_1": """Halo, perkenalkan saya Sean Christophe Hartanto.
Saya merupakan seorang Backend Developer dengan pengalaman mengembangkan API, mengelola database, serta membangun sistem backend yang scalable dan reliable.

Selama beberapa tahun terakhir, saya fokus pada pengembangan backend menggunakan Node.js, Express, Laravel, dan PostgreSQL, serta memiliki pengalaman dalam REST API, authentication, sistem pembayaran, logging, dan deployment.

Saya adalah pribadi yang senang belajar, detail-oriented, dan terbiasa bekerja kolaboratif dalam tim pengembang.""",


    "transkrip_pertanyaan_2": """Saya tertarik melamar di PT XYZ karena perusahaan ini memiliki lingkungan kerja yang modern dan berorientasi pada teknologi, inovasi, serta kualitas produk digital.

Saya melihat PT XYZ mengembangkan sistem dengan skala pengguna yang cukup besar, sehingga menjadi kesempatan yang sangat baik bagi saya untuk berkontribusi dalam membangun backend yang stabil, aman, dan efisien sekaligus memperdalam kemampuan teknis saya.

Selain itu, saya merasa nilai perusahaan yang mengutamakan kolaborasi dan continuous improvement sangat selaras dengan prinsip kerja saya.""",
    
    
    "transkrip_pertanyaan_3": """Dalam proyek yang saya kerjakan sebelumnya, saya bertanggung jawab untuk:
Mendesain dan mengembangkan RESTful API untuk aplikasi web dan mobile
Mengelola database menggunakan MySQL / PostgreSQL
Menerapkan JWT Authentication & Role-Based Access
Mengoptimalkan query dan struktur data agar lebih efisien
Mengembangkan fitur transactional process & background jobs
Melakukan debugging, error handling, logging, dan unit testing
Deployment ke VPS / Cloud environment
Saya juga terbiasa menggunakan Git, Postman, Docker, serta mengikuti konsep clean architecture dan best-practice backend development.""",

    "transkrip_pertanyaan_4": """Saya percaya bisa memberikan kontribusi nyata karena:
Saya memiliki kompetensi teknis yang relevan dengan kebutuhan backend
Terbiasa bekerja terstruktur, rapi, dan fokus pada reliability sistem
Cepat beradaptasi dengan teknologi baru dan lingkungan tim
Memiliki mindset problem-solving, ownership, dan continuous improvement
Siap memberikan dedikasi penuh serta tumbuh bersama perusahaan
Dengan kombinasi kemampuan teknis dan attitude kerja yang profesional, saya yakin dapat membantu perusahaan dalam mengembangkan sistem backend yang stabil, aman, dan scalable.""",

    # Data Transkrip Akademik
    "transkrip_nrp": "c14220019",
    "transkrip_prodi": "INFORMATIKA",
    "transkrip_ipk": 3.92,
    "transkrip_total_sks": 132,
    "transkrip_total_mk": 45,
    "transkrip_courses": [
       {
      "Kode": "DU4197",
      "Mata_Kuliah": "AGAMA DAN HIDUP BERMAKNA",
      "Semester": "1-22/23",
      "SKS": 4,
      "Nilai": "A"
    },
    {
      "Kode": "DU4122",
      "Mata_Kuliah": "BAHASA INDONESIA",
      "Semester": "1-22/23",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "TF4205",
      "Mata_Kuliah": "DASAR SISTEM KOMPUTER",
      "Semester": "1-22/23",
      "SKS": 2,
      "Nilai": "B+"
    },
    {
      "Kode": "FD4505",
      "Mata_Kuliah": "KALKULUS I",
      "Semester": "1-22/23",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4537",
      "Mata_Kuliah": "KONSEP ALGORITMA",
      "Semester": "1-22/23",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4220",
      "Mata_Kuliah": "PENGANTAR MANAJEMEN DAN BISNIS",
      "Semester": "1-22/23",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "TF4536",
      "Mata_Kuliah": "DASAR PEMROGRAMAN",
      "Semester": "1-22/23",
      "SKS": 4,
      "Nilai": "A"
    },
    {
      "Kode": "DU4101",
      "Mata_Kuliah": "PANCASILA",
      "Semester": "2-22/23",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "TF4227",
      "Mata_Kuliah": "STATISTIKA DASAR",
      "Semester": "2-22/23",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4253",
      "Mata_Kuliah": "JARINGAN KOMPUTER",
      "Semester": "2-22/23",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4267",
      "Mata_Kuliah": "KOMUNIKASI INTERPERSONAL",
      "Semester": "2-22/23",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4245",
      "Mata_Kuliah": "MATEMATIKA DISKRIT",
      "Semester": "2-22/23",
      "SKS": 3,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4235",
      "Mata_Kuliah": "PEMROGRAMAN BERORIENTASI OBYEK",
      "Semester": "2-22/23",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4229",
      "Mata_Kuliah": "BASIS DATA",
      "Semester": "2-22/23",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "DU4164",
      "Mata_Kuliah": "PENDIDIKAN KEWARGANEGARAAN",
      "Semester": "1-23/24",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "TF4249",
      "Mata_Kuliah": "PENGANTAR AKUNTANSI",
      "Semester": "1-23/24",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "TF4255",
      "Mata_Kuliah": "REKAYASA PERANGKAT LUNAK",
      "Semester": "1-23/24",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4219",
      "Mata_Kuliah": "STRUKTUR DATA",
      "Semester": "1-23/24",
      "SKS": 3,
      "Nilai": "B"
    },
    {
      "Kode": "FD4507",
      "Mata_Kuliah": "ALJABAR LINIER",
      "Semester": "1-23/24",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4270",
      "Mata_Kuliah": "DESAIN DAN ANALISIS ALGORITMA",
      "Semester": "1-23/24",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4372",
      "Mata_Kuliah": "ARSITEKTUR DAN ORGANISASI KOMPUTER",
      "Semester": "1-23/24",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4343",
      "Mata_Kuliah": "TEKNOLOGI WEB",
      "Semester": "1-23/24",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "DU4198",
      "Mata_Kuliah": "DIGITAL LEADERSHIP",
      "Semester": "1-23/24",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "DU4163",
      "Mata_Kuliah": "ETIKA PROFESI",
      "Semester": "2-23/24",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "TF4327",
      "Mata_Kuliah": "ANALISIS DAN DESAIN SISTEM INFORMASI",
      "Semester": "2-23/24",
      "SKS": 3,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4504",
      "Mata_Kuliah": "BAHASA INGGRIS",
      "Semester": "2-23/24",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "TF4409",
      "Mata_Kuliah": "KECERDASAN BUATAN",
      "Semester": "2-23/24",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4237",
      "Mata_Kuliah": "INTERAKSI MANUSIA DAN KOMPUTER",
      "Semester": "2-23/24",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4544",
      "Mata_Kuliah": "CYBER OPERATIONS",
      "Semester": "2-23/24",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4243",
      "Mata_Kuliah": "SISTEM OPERASI",
      "Semester": "2-23/24",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4415",
      "Mata_Kuliah": "GRAFIKA KOMPUTER",
      "Semester": "2-23/24",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4247",
      "Mata_Kuliah": "METODE NUMERIK",
      "Semester": "2-23/24",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "TF4425",
      "Mata_Kuliah": "PEMROGRAMAN GAME",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "FD4508",
      "Mata_Kuliah": "TECHNOPRENEURSHIP",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4579",
      "Mata_Kuliah": "WEB FRAMEWORKS AND DEPLOYMENT",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4507",
      "Mata_Kuliah": "SISTEM TERDISTRIBUSI",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4317",
      "Mata_Kuliah": "MANAJEMEN PROYEK TEKNOLOGI INFORMASI",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4582",
      "Mata_Kuliah": "GAME CONTENT DEVELOPMENT",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4569",
      "Mata_Kuliah": "NETWORK DEFENSE",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4513",
      "Mata_Kuliah": "DESAIN UI / GAME DESIGN",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4516",
      "Mata_Kuliah": "PENGEMBANGAN APLIKASI BERBASIS ANDROID",
      "Semester": "2-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4259",
      "Mata_Kuliah": "METODOLOGI PENELITIAN",
      "Semester": "2-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4540",
      "Mata_Kuliah": "INDUSTRIAL TRAINING",
      "Semester": "2-24/25",
      "SKS": 6,
      "Nilai": "A"
    },
    {
      "Kode": "TF4261",
      "Mata_Kuliah": "KERJA PRAKTEK",
      "Semester": "2-24/25",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "TF4539",
      "Mata_Kuliah": "PROFESSIONAL DEVELOPMENT",
      "Semester": "2-24/25",
      "SKS": 6,
      "Nilai": "A"
    }
  ],
   "transkrip_grade_distribution": {
    "A": 40,
    "B+": 4,
    "B": 1,
    "C+": 0
  },

    # Data SKKK
    
   "skkk_data": [
    {
      "No": 1,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "BANK PANITIA INFORMATICS COMMITTEE CLUB 2022",
      "Nilai_SKKK": 1.5,
      "Periode": "221",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 2,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "KULIAH UMUM - CYBER SECURITY AWARENESS, JUMAT - 25 NOVEMBER 2022",
      "Nilai_SKKK": 1.5,
      "Periode": "221",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 3,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "ACCOUNTING TALK 2023 : BIG DATA, IMPACTS ON ACCOUNTING CAREER",
      "Nilai_SKKK": 7.5,
      "Periode": "222",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 4,
      "Jabatan": "Peserta",
      "Nama_Kegiatan": "BORN TO CARE 2023",
      "Nilai_SKKK": 1,
      "Periode": "222",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 5,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "BUSINESS X CONTENT CREATION WEBINAR",
      "Nilai_SKKK": 7.5,
      "Periode": "222",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 6,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "CHARACTER AND RELATIONSHIP ENHANCEMENT (CARE) 2023",
      "Nilai_SKKK": 6,
      "Periode": "222",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 7,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "INTERIOR DESIGN EXHIBITION (INDEX) 2023 \"INTERLINK\"",
      "Nilai_SKKK": 7.5,
      "Periode": "222",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 8,
      "Jabatan": "Peserta UKM",
      "Nama_Kegiatan": "KEGIATAN RUTIN UKM CATUR 2022",
      "Nilai_SKKK": 10,
      "Periode": "222",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 9,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "MAXIMIZE YOUR TALENT",
      "Nilai_SKKK": 2.3,
      "Periode": "222",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 10,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "PETRA CHESS COMPETITION 2023",
      "Nilai_SKKK": 6,
      "Periode": "222",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 11,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "PRIME TIME 2023 2022",
      "Nilai_SKKK": 4.5,
      "Periode": "222",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 12,
      "Jabatan": "Anggota HIMA - Acara",
      "Nama_Kegiatan": "RARE RAISE OF AWARNESS 2023",
      "Nilai_SKKK": 9.9,
      "Periode": "222",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 13,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "SEMINAR BCA FUTURE TALENT MEI 2023",
      "Nilai_SKKK": 3,
      "Periode": "222",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 14,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "SEMINAR BETTER PERSON BRIGHTER FUTURE 2023",
      "Nilai_SKKK": 1.5,
      "Periode": "222",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 15,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "SEMINAR WAWASAN KEBANGSAAN TANGGAL 30 MEI 2023",
      "Nilai_SKKK": 6,
      "Periode": "222",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 16,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "ACCOUNTING TALK",
      "Nilai_SKKK": 7.5,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 17,
      "Jabatan": "Harapan 1",
      "Nama_Kegiatan": "DIES NATALIS AMN SURABAYA KE-1",
      "Nilai_SKKK": 6,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 18,
      "Jabatan": "Anggota HIMA - Acara",
      "Nama_Kegiatan": "IRGL 2023 - SABTU, 21 OKTOBER 2023",
      "Nilai_SKKK": 9.9,
      "Periode": "231",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 19,
      "Jabatan": "Anggota HIMA - Acara",
      "Nama_Kegiatan": "KAMPUNG BINAAN MAHASISWA VII 2023",
      "Nilai_SKKK": 1,
      "Periode": "231",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 20,
      "Jabatan": "Harapan 1",
      "Nama_Kegiatan": "LOMBA KARYA TULIS ILMIAH NASIONAL",
      "Nilai_SKKK": 6,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 21,
      "Jabatan": "Peserta",
      "Nama_Kegiatan": "NUNI INTERNATIONAL SEMINAR SERIES 6 - FAIR TRADE: A WAY",
      "Nilai_SKKK": 7.5,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 22,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "PEMBELAJARAN KEBERAGAMAN BANGSA INDONESIA DI SD SE-SURABAYA (PENGMAS SL)",
      "Nilai_SKKK": 2,
      "Periode": "231",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 23,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "SL - KOMAL (A,B,C,D) - GENAP 22/23 (6/2/23 - 30/6/23)",
      "Nilai_SKKK": 2,
      "Periode": "231",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 24,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "TECHNICAL PROGRAM MANAGEMENT IN B2B VS B2C WEBINAR",
      "Nilai_SKKK": 7.5,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 25,
      "Jabatan": "Pengisi Acara/Pengmas 5Aspek",
      "Nama_Kegiatan": "VENTURE FESTIVAL-TECHNOLOGY FOR SUSTAINABILITY AND BETTER FUTURE",
      "Nilai_SKKK": 5.3,
      "Periode": "231",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 26,
      "Jabatan": "Anggota HIMA - Anggota PSC",
      "Nama_Kegiatan": "BADAN EKSEKUTIF MAHASISWA 2023-2024",
      "Nilai_SKKK": 22,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 27,
      "Jabatan": "Anggota HIMA - Acara dan Materi",
      "Nama_Kegiatan": "BRAIN BOOST: BEAVER BOOTCAMP",
      "Nilai_SKKK": 1,
      "Periode": "232",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 28,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "CAREER SHAPING IN ENTREPRENEURIAL - CAPITAL 2024",
      "Nilai_SKKK": 3.8,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 29,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "DYNAMIC CAREER CHANGES IN THE AGE OF DIGITAL TRANSFORMATION 2024",
      "Nilai_SKKK": 3.8,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 30,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "OUTSOURCE INTENSIVE LEADERSHIP TRAINING 1 2024",
      "Nilai_SKKK": 3,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 31,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "OUTSOURCE INTENSIVE LEADERSHIP TRAINING 2 2024",
      "Nilai_SKKK": 3,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 32,
      "Jabatan": "Anggota HIMA",
      "Nama_Kegiatan": "PANITIA BEBRAS CHALLENGE 2023",
      "Nilai_SKKK": 1.25,
      "Periode": "232",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 33,
      "Jabatan": "Anggota HIMA",
      "Nama_Kegiatan": "PENGAWAS PELAKSANAAN BEBRAS CHALLENGE 2023",
      "Nilai_SKKK": 1,
      "Periode": "232",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 34,
      "Jabatan": "Penulis",
      "Nama_Kegiatan": "PROGRAM KREATIVITAS MAHASISWA 2024",
      "Nilai_SKKK": 6,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 35,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "RAPAT AKHIR BEM 2024",
      "Nilai_SKKK": 3,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 36,
      "Jabatan": "Koordinator",
      "Nama_Kegiatan": "SERVANT LEADERSHIP TRAINING 2024",
      "Nilai_SKKK": 7.8,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 37,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "SPARK 2024",
      "Nilai_SKKK": 3,
      "Periode": "232",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 38,
      "Jabatan": "Koordinator/Anggota BKU/BPMF - Acara",
      "Nama_Kegiatan": "TALKSHOW MAGANG HIMAINFRA",
      "Nilai_SKKK": 3.9,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 39,
      "Jabatan": "Juara III",
      "Nama_Kegiatan": "LO KREATIF 2024",
      "Nilai_SKKK": 6,
      "Periode": "241",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 40,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "KEJAR MIMPI WEALTH FEST",
      "Nilai_SKKK": 6,
      "Periode": "251",
      "Bidang": "Pembelajaran"
    }
  ],
  "skkk_total_activities": 40,
  "skkk_success": True,


    # Analisis Video +
    "analisis_video": {
      "analisis_pertanyaan_1": "analisis: Subjek memberikan jawaban yang terstruktur dengan baik, dimulai dari definisi kemudian berkembang ke aplikasi. Alur pemikiran sangat jelas. kesimpulan: 88",
      "analisis_pertanyaan_2": "analisis: Bahasa tubuh terbuka dan rileks menunjukkan kenyamanan dengan materi. Volume suara konsisten dan mudah didengar. kesimpulan: 85",
      "analisis_pertanyaan_3": "analisis: Subjek sangat responsif dan mampu mengelaborasi setiap poin yang ditanyakan dengan detail yang relevan dan mendalam. kesimpulan: 91",
      "analisis_pertanyaan_4": "analisis: Jawaban tidak hanya teoritis tetapi diperkaya dengan insight pribadi dan pengalaman. Menunjukkan pemahaman yang autentik. kesimpulan: 86"
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
