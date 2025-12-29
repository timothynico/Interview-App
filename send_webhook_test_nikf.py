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
    "nama": "Nicholas Fransisco",
    "email": "nicholasfransisco09@gmail.com",
    "posisi_dilamar": "Frontend Developer",

    # CV Text
    "cv_text": """Starting as a curious learner, my enthusiasm for programming has grown from a simple curiosity into a
deep commitment to mastering full-stack software engineering. I am deeply invested in both web and
mobile development, understanding the critical balance between front-end and back-end components. By
using the power of AI, cloud computing, and developing user-friendly mobile applications, my aim is to
contribute to technological advancements that make a meaningful impact on society.
Undergraduate of Informatics, Petra Christian University
EXECUTIVE SUMMARY
nicholasfransisco09@gmail.com | +6281216196735 | linkedin.com/in/nicholasf09
| github.com/nicholasf09 | Surabaya, Indonesia
NICHOLAS FRANSISCO
EDUCATION
Current GPA: 3.87 / 4.00
Top 10% Academic Performance Students of the 2022 Batch
2022 - Present
Bangkit Academy by Google, Tokopedia, Gojek, & Traveloka
Cloud Computing Learning Path
Sep 2024 - Dec 2024
Coordinator of Information Technology Division, EPICLAIR 2024
Engineered a seamless front-end and back-end system for competitions participant registration,
enhancing user experience and operational efficiency.
Developed a sophisticated website featuring a bracket system with 93 groups and hundreds of
participants, supporting real-time live input.
Led IT division members, effectively coordinating with other divisions to complete essential tasks.
COMMITTEE EXPERIENCE Oct 2023 - Jul 2024
ORGANIZATION EXPERIENCE
Member of Information System Department, Student Executive Board
Coordinated and developed a dynamic e-commerce website to market and sell apparel for
committee events and merchandise for the Student Executive Board.
Provided a system feature to upload committee member details for events using an extension
to convert Excel files into a MySQL database.
Maintained and redefining the assessment column criteria for the committee performances.
Jul 2023 - Aug 2024
WORK EXPERIENCE
Software Engineer Intern, PT. Avia Avian Tbk.
Coordinated with Quality Assurance Department to developed an internal web-based system for
company products complaint handling and follow up using Laravel 11 and SQLyog
Developed a new website named Avian Logistic to facilitate the recording process and manage the
flow of loading and unloading trucks to and from the warehouse using React & Laravel 12
Developed a new Internal Ticketing Website for Marketing Department purchase order included with
laravel scheduler, whatsapp and email notification capabilities using Laravel 11.
Enhanced internal Human Resource systems with employee leave conversion & payroll calculations
feature included with Excel export, and an RBAC-enabled material request form for HR web ticketing.
Jan 2025 - July 2025
Member of Information Technology Division, Battle Of Minds 2024
Developed a comprehensive program with a front-end interface and a secure back-end system,
that provide the participants to take a 300 mathematical problems.
Apr 2024 - July 2024
Member of IT Division, Bharatika Creative Design Festival
Collaboration with the creative team using Figma to design and develop a user-friendly website.
Develop the categories and types of competitions page, ensuring alignment with participant interest
Dec 2023 - July 2024
Multiculturalism Learning Project at Nurul Huda Elementary School
Arranged a virtual trip to Indonesia as a learning material for the students, including the PPT
Design and activities.
Conducted an interactive quiz and activities about Pancasila and Nationality.
VOLUNTEER ACTIVITIES
Scratch Your Potential at Petra 1 Elementary School
Delivered the materials about the basics of Scratch programming
language for three days.
Born To Care 2023
Collaborated to create an engaging and informative poster on the theme of health awareness.
Presented the poster to elementary school students, emphasizing the importance of healthy living
Matrapenza: Marina 2023
Developed an event agenda, games, and materials for elementary school students.
Presented to the elementary school students, highlighting the dangers of illegal drugs.
ACHIEVEMENTS AND AWARDS
1st Place, Bytesfest National Web Design Competition by UNS
Developed a React JS-powered digital artworks online exhibition website, collaboration with
my partner, which secured us First Place at the national BytesFest competition.
Vice Coordinator of Information Technology Division, CAPITAL 2024
Engineered a seamless front-end for high school competitions registration
Developed a feature to create news rally games with real-time updates.
Implemented a secure Gmail login using Google Cloud Console, including
validation checks to enhance protection against external attacks.
Sep 2023 - Mar 2024
Member of Information Technology Division, WGG 2023
Designed a main page for Rally Games, featuring stunning animations and effects
that immerse participants in a gaming-like experience.
Designed an intuitive event briefing page showcasing videos in a carousel format.
Des 2022 - July 2023
LICENSES & CERTIFICATIONS
Japanese Langguage Proficiency Test (JLPT)
Successfully Passed the JLPT N4 Certified at July 2023
Successfully Passed the JLPT N5 Certified at December 2022
Google (Google Cloud Skill Boost)
Google Cloud Computing Foundations: Cloud Computing Fundamentals
Google Cloud Computing Foundations: Infrastructure in Google Cloud
Google Cloud Computing Foundations: Networking & Security in Google Cloud
Google Cloud Computing Foundations: Data, ML, and AI in Google Cloud
Implement Load Balancing on Compute Engine
Set Up an App Dev Environment on Google Cloud
Build a Secure Google Cloud Network
Prepare Data for ML APIs on Google Cloud
Google Cloud Fundamentals: Core Infrastructure
Essential Google Cloud Infrastructure: Foundation
Essential Google Cloud Infrastructure: Core Services
Elastic Google Cloud Infrastructure: Scaling and Automation
Getting Started with Google Kubernetes Engine
Getting Started with Terraform for Google Cloud
Develop your Google Cloud Network
Red Hat Academy
2024 Red Hat Academy - Program Learner
SKILLS
Language: Bahasa Indonesia (Native), English (Fluent), Japanese (JLPT N4 and N5 Certified)
Software: Microsoft Office, Google Spreadsheet, SQL, Visual Studio Code, XAMPP, Laragon, Postman,
Android Studio, Adobe Photoshop, Adobe Premiere Pro, AWS Cloud, Google Cloud Platform (GCP) Cloud
Programming: Java, Phyton, C++, HTML, Cascading Style Sheet (CSS), Javascript, PHP, Laravel,
React JS, Kotlin, Bootstrap, Tailwind CSS, jQuery, AJAX, Next JS, Structured Query Language (SQL)
Soft-Skill: Communication, teamwork, problem-solving, adaptability, time management, critical thinking,
creativity, emotional intelligence, leadership, conflict resolution, Growth Mindset
Amazon Web Services (AWS) Academy
AWS Academy Cloud Foundations
AWS Academy Cloud Developing
Dicoding Indonesia
Belajar Dasar Pemrograman Web
Memulai Dasar Pemrograman untuk Menjadi Pengembang Software
Pengenalan ke Logika Pemrograman (Programming Logic 101)
Belajar Dasar Git dengan GitHub
Belajar Pemrograman Prosedural dengan Python
Belajar Dasar Google Cloud
Red Hat Academy
2024 Red Hat Academy - Program Learner
Google (Google Cloud Skill Boost)
Google Cloud Computing Foundations: Cloud Computing Fundamentals
Google Cloud Computing Foundations: Infrastructure in Google Cloud
Google Cloud Computing Foundations: Networking & Security in Google Cloud
Google Cloud Computing Foundations: Data, ML, and AI in Google Cloud
Implement Load Balancing on Compute Engine
Set Up an App Dev Environment on Google Cloud
Build a Secure Google Cloud Network
Prepare Data for ML APIs on Google Cloud
Google Cloud Fundamentals: Core Infrastructure
Essential Google Cloud Infrastructure: Foundation
Essential Google Cloud Infrastructure: Core Services
Elastic Google Cloud Infrastructure: Scaling and Automation
Getting Started with Google Kubernetes Engine
Getting Started with Terraform for Google Cloud
Develop your Google Cloud Network
SKILLS
Language: Bahasa Indonesia (Native), English (Fluent), Japanese (JLPT N4 and N5 Certified)
Soft-Skill: Communication, teamwork, problem-solving, adaptability, time management, critical thinking,
creativity, emotional intelligence, leadership, conflict resolution, Growth Mindset
Programming: Java, Phyton, C++, HTML, Cascading Style Sheet (CSS), Javascript, PHP, Laravel,
React JS, Kotlin, Bootstrap, Tailwind CSS, jQuery, AJAX, Next JS, Structured Query Language (SQL)
Software: Microsoft Office, Google Spreadsheet, SQL, Visual Studio Code, XAMPP, Laragon, Postman,
Android Studio, Adobe Photoshop, Adobe Premiere Pro, AWS Cloud, Google Cloud Platform (GCP) Cloud""",

    # Transkrip Jawaban Interview
    "transkrip_pertanyaan_1": """Selamat Siang Ibu Lesti, terima kasih atas waktunya hari ini. perkenalkan saya Nicholas fresh graduate informatika Universitas Kristen Petra yang tertarik di bidang front end.""",


    "transkrip_pertanyaan_2": """Karena perusahaan ini cocok dengan visi saya yaitu selalu ingin maju dan berinovasi melalui perkembangan teknologi jaman sekarang seperti penggunaan AI dan Blockchain""",
    
    
    "transkrip_pertanyaan_3": """Saya mempunyai pengalaman memenangkan lomba web design yang berfokus pada front end bersama teman saya, dan saya ingin mengembangkan bakat minat saya lebih lanjut lagi di perusahaan ini""",

    "transkrip_pertanyaan_4": """Karena dengan pengalaman saya, saya yakin bisa berkontribusi di perusahaan ini dan terus berkembang dan belajar lagi untuk menjadi programmer ynag baik dan dapat diandalkan perusahaan""",

    # Data Transkrip Akademik
    "transkrip_nrp": "C14220007",
    "transkrip_prodi": "INFORMATIKA",
    "transkrip_ipk": 3.87,
    "transkrip_total_sks": 135,
    "transkrip_total_mk": 46,
    "transkrip_courses": [
        {"Kode": "DU4122", "Mata_Kuliah": "BAHASA INDONESIA", "Semester": "1-22/23", "SKS": 2, "Nilai": "A"},
        {"Kode": "TF4205", "Mata_Kuliah": "DASAR SISTEM KOMPUTER", "Semester": "1-22/23", "SKS": 2, "Nilai": "B"},
        {"Kode": "FD4505", "Mata_Kuliah": "KALKULUS I", "Semester": "1-22/23", "SKS": 3, "Nilai": "B"},
        {"Kode": "TF4537", "Mata_Kuliah": "KONSEP ALGORITMA", "Semester": "1-22/23", "SKS": 3, "Nilai": "B+"},
        {"Kode": "TF4220", "Mata_Kuliah": "PENGANTAR MANAJEMEN DAN BISNIS", "Semester": "1-22/23", "SKS": 2, "Nilai": "A"},
        {"Kode": "TF4536", "Mata_Kuliah": "DASAR PEMROGRAMAN", "Semester": "1-22/23", "SKS": 4, "Nilai": "A"},
        {"Kode": "DU4197", "Mata_Kuliah": "AGAMA DAN HIDUP BERMAKNA", "Semester": "1-22/23", "SKS": 4, "Nilai": "A"},
        {"Kode": "DU4101", "Mata_Kuliah": "PANCASILA", "Semester": "2-22/23", "SKS": 2, "Nilai": "A"},
        {"Kode": "TF4267", "Mata_Kuliah": "KOMUNIKASI INTERPERSONAL", "Semester": "2-22/23", "SKS": 3, "Nilai": "B+"},
        {"Kode": "TF4245", "Mata_Kuliah": "MATEMATIKA DISKRIT", "Semester": "2-22/23", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4235", "Mata_Kuliah": "PEMROGRAMAN BERORIENTASI OBYEK", "Semester": "2-22/23", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4253", "Mata_Kuliah": "JARINGAN KOMPUTER", "Semester": "2-22/23", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4229", "Mata_Kuliah": "BASIS DATA", "Semester": "2-22/23", "SKS": 3, "Nilai": "B+"},
        {"Kode": "TF4227", "Mata_Kuliah": "STATISTIKA DASAR", "Semester": "2-22/23", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4255", "Mata_Kuliah": "REKAYASA PERANGKAT LUNAK", "Semester": "2-22/23", "SKS": 3, "Nilai": "B+"},
        {"Kode": "TF4270", "Mata_Kuliah": "DESAIN DAN ANALISIS ALGORITMA", "Semester": "1-23/24", "SKS": 3, "Nilai": "B+"},
        {"Kode": "TF4372", "Mata_Kuliah": "ARSITEKTUR DAN ORGANISASI KOMPUTER", "Semester": "1-23/24", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4219", "Mata_Kuliah": "STRUKTUR DATA", "Semester": "1-23/24", "SKS": 3, "Nilai": "B+"},
        {"Kode": "DU4164", "Mata_Kuliah": "PENDIDIKAN KEWARGANEGARAAN", "Semester": "1-23/24", "SKS": 2, "Nilai": "A"},
        {"Kode": "TF4343", "Mata_Kuliah": "TEKNOLOGI WEB", "Semester": "1-23/24", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4504", "Mata_Kuliah": "BAHASA INGGRIS", "Semester": "1-23/24", "SKS": 2, "Nilai": "A"},
        {"Kode": "TF4249", "Mata_Kuliah": "PENGANTAR AKUNTANSI", "Semester": "1-23/24", "SKS": 2, "Nilai": "B+"},
        {"Kode": "FD4507", "Mata_Kuliah": "ALJABAR LINIER", "Semester": "1-23/24", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4327", "Mata_Kuliah": "ANALISIS DAN DESAIN SISTEM INFORMASI", "Semester": "2-23/24", "SKS": 3, "Nilai": "B+"},
        {"Kode": "TF4237", "Mata_Kuliah": "INTERAKSI MANUSIA DAN KOMPUTER", "Semester": "2-23/24", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4243", "Mata_Kuliah": "SISTEM OPERASI", "Semester": "2-23/24", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4247", "Mata_Kuliah": "METODE NUMERIK", "Semester": "2-23/24", "SKS": 2, "Nilai": "A"},
        {"Kode": "TF4415", "Mata_Kuliah": "GRAFIKA KOMPUTER", "Semester": "2-23/24", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4544", "Mata_Kuliah": "CYBER OPERATIONS", "Semester": "2-23/24", "SKS": 3, "Nilai": "B+"},
        {"Kode": "DU4163", "Mata_Kuliah": "ETIKA PROFESI", "Semester": "2-23/24", "SKS": 2, "Nilai": "A"},
        {"Kode": "DU4198", "Mata_Kuliah": "DIGITAL LEADERSHIP", "Semester": "2-23/24", "SKS": 2, "Nilai": "A"},
        {"Kode": "TF4409", "Mata_Kuliah": "KECERDASAN BUATAN", "Semester": "2-23/24", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4569", "Mata_Kuliah": "NETWORK DEFENSE", "Semester": "1-24/25", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4579", "Mata_Kuliah": "WEB FRAMEWORKS AND DEPLOYMENT", "Semester": "1-24/25", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4509", "Mata_Kuliah": "CLOUD COMPUTING", "Semester": "1-24/25", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4507", "Mata_Kuliah": "SISTEM TERDISTRIBUSI", "Semester": "1-24/25", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4317", "Mata_Kuliah": "MANAJEMEN PROYEK TEKNOLOGI INFORMASI", "Semester": "1-24/25", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4516", "Mata_Kuliah": "PENGEMBANGAN APLIKASI BERBASIS ANDROID", "Semester": "1-24/25", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4587", "Mata_Kuliah": "SOFTWARE TESTING AND QUALITY ASSURANCE", "Semester": "1-24/25", "SKS": 3, "Nilai": "A"},
        {"Kode": "FD4508", "Mata_Kuliah": "TECHNOPRENEURSHIP", "Semester": "1-24/25", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4540", "Mata_Kuliah": "INDUSTRIAL TRAINING", "Semester": "1-24/25", "SKS": 6, "Nilai": "A"},
        {"Kode": "TF4261", "Mata_Kuliah": "KERJA PRAKTEK", "Semester": "2-24/25", "SKS": 2, "Nilai": "A"},
        {"Kode": "TF4539", "Mata_Kuliah": "PROFESSIONAL DEVELOPMENT", "Semester": "2-24/25", "SKS": 6, "Nilai": "A"},
        {"Kode": "TF4259", "Mata_Kuliah": "METODOLOGI PENELITIAN", "Semester": "2-24/25", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4452", "Mata_Kuliah": "ARSITEKTUR BERORIENTASI LAYANAN", "Semester": "2-24/25", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4580", "Mata_Kuliah": "APPLIED ARTIFICIAL INTELLIGENCE", "Semester": "2-24/25", "SKS": 3, "Nilai": "A"}
    ],
    "transkrip_grade_distribution": {
        "A": 34,
        "B+": 9,
        "B": 2,
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
      "Nama_Kegiatan": "DATA ANALYSIS IN PUBLIC SERVICE (FIRE AND RESCUE)",
      "Nilai_SKKK": 7.5,
      "Periode": "221",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 3,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "KULIAH UMUM - CYBER SECURITY AWARENESS, JUMAT - 25 NOVEMBER 2022",
      "Nilai_SKKK": 1.5,
      "Periode": "221",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 4,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "KULIAH UMUM - WEBINAR \"AUTOMATION AND IT MODERNIZATION\", JUMAT - 14 OKT 2022",
      "Nilai_SKKK": 1.5,
      "Periode": "221",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 5,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "MARINA",
      "Nilai_SKKK": 0.75,
      "Periode": "221",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 6,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "STARTUP SHARING SESSION METAVERSE IN EDUCATION CREATING FUTURE SKILLED WORKFORCE",
      "Nilai_SKKK": 6,
      "Periode": "221",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 7,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "TECHNOLOGY IMPLEMENTATION IN THE FASHION INDUSTRY",
      "Nilai_SKKK": 7.5,
      "Periode": "221",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 8,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "AYE AYE CAPTAIN 2023",
      "Nilai_SKKK": 3,
      "Periode": "222",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 9,
      "Jabatan": "Peserta",
      "Nama_Kegiatan": "BORN TO CARE 2023",
      "Nilai_SKKK": 1,
      "Periode": "222",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 10,
      "Jabatan": "Peserta UKM",
      "Nama_Kegiatan": "KEGIATAN RUTIN UKM BOLA VOLI 2022",
      "Nilai_SKKK": 10,
      "Periode": "222",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 11,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "SEMINAR BETTER PERSON BRIGHTER FUTURE 2023",
      "Nilai_SKKK": 1.5,
      "Periode": "222",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 12,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "SEMINAR WAWASAN KEBANGSAAN TANGGAL 30 MEI 2023",
      "Nilai_SKKK": 6,
      "Periode": "222",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 13,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "TALKSOW THE INFORMATICS ADVOCATE",
      "Nilai_SKKK": 1.5,
      "Periode": "222",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 14,
      "Jabatan": "Anggota HIMA - Anggota Divisi IT",
      "Nama_Kegiatan": "WELCOME, GRATEFUL GENERATION 2023",
      "Nilai_SKKK": 9.9,
      "Periode": "222",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 15,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "GUEST LECTURE SERIES ASPEK HUKUM PERTANAHAN PADA KAWASAN IKN",
      "Nilai_SKKK": 6,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 16,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "GUEST LECTURE SERIES IMPLEMENTASI ETIKA PROFESI PADA DUNIA KONSTRUKSI",
      "Nilai_SKKK": 6,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 17,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "HOW CONSULTANT HELP BUSINESSES CREATE VALUE THROUGH DATA WEBINAR",
      "Nilai_SKKK": 7.5,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 18,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "PEMBELAJARAN KEBERAGAMAN BANGSA INDONESIA DI SD SE-SURABAYA (PENGMAS SL)",
      "Nilai_SKKK": 2,
      "Periode": "231",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 19,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "PENGISIAN FAIP VIA SIMPONI",
      "Nilai_SKKK": 6,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 20,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "PERCEPTION TOWARDS CONCRETE FLOOR",
      "Nilai_SKKK": 6,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 21,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "SL - KOMAL (A,B,C,D) - GENAP 22/23 (6/2/23 - 30/6/23)",
      "Nilai_SKKK": 2,
      "Periode": "231",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 22,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "WHY DO COMPANIES MIGRATE THEIR DATA AND APPLICATIONS TO THE CLOUD WEBINAR",
      "Nilai_SKKK": 7.5,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 23,
      "Jabatan": "Anggota HIMA - Anggota IS",
      "Nama_Kegiatan": "BADAN EKSEKUTIF MAHASISWA 2023-2024",
      "Nilai_SKKK": 22,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 24,
      "Jabatan": "Anggota HIMA - IT",
      "Nama_Kegiatan": "BATTLE OF MINDS 2024",
      "Nilai_SKKK": 9.9,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 25,
      "Jabatan": "Anggota HIMA - Teknologi Informasi",
      "Nama_Kegiatan": "BHARATIKA CREATIVE DESIGN FESTIVAL 2024",
      "Nilai_SKKK": 16.5,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 26,
      "Jabatan": "Anggota HIMA - IT",
      "Nama_Kegiatan": "CAREER SHAPING IN ENTREPRENEURIAL - CAPITAL 2024",
      "Nilai_SKKK": 8.25,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 27,
      "Jabatan": "Peserta",
      "Nama_Kegiatan": "EPICLAIR 2024 (Peserta)",
      "Nilai_SKKK": 6,
      "Periode": "232",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 28,
      "Jabatan": "Koordinator",
      "Nama_Kegiatan": "EPICLAIR 2024 (Koordinator)",
      "Nilai_SKKK": 19.5,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 29,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "EXHIBITION INTERNAL 2024",
      "Nilai_SKKK": 3,
      "Periode": "232",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 30,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "OUTSOURCE INTENSIVE LEADERSHIP TRAINING 2 2024",
      "Nilai_SKKK": 3,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 31,
      "Jabatan": "Juara I",
      "Nama_Kegiatan": "BYTESFEST",
      "Nilai_SKKK": 6,
      "Periode": "241",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 32,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "KEJAR MIMPI WEALTH FEST",
      "Nilai_SKKK": 6,
      "Periode": "251",
      "Bidang": "Pembelajaran"
    }
  ],
  "skkk_total_activities": 32,
  "skkk_success": True,


    # Analisis Video +
    "analisis_video": {
        "analisis_pertanyaan_1": "analisis: Subjek menunjukkan pemahaman yang mendalam terhadap konsep yang ditanyakan, dengan gesture tangan yang mendukung penjelasan. Kontak mata terjaga baik. kesimpulan: 92",
        "analisis_pertanyaan_2": "analisis: Terlihat sedikit gugup di awal namun segera pulih. Mampu memberikan contoh konkret untuk memperkuat argumen dengan intonasi yang stabil. kesimpulan: 85",
        "analisis_pertanyaan_3": "analisis: Subjek menunjukkan antusiasme tinggi saat menjelaskan topik yang dikuasai. Bahasa tubuh terbuka dan responsif terhadap pertanyaan lanjutan. kesimpulan: 90",
        "analisis_pertanyaan_4": "analisis: Jawaban cukup komprehensif meskipun ada jeda beberapa detik untuk berpikir. Ekspresi wajah menunjukkan konsentrasi yang baik. kesimpulan: 82"
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
