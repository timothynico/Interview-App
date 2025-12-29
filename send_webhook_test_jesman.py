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
    "nama": "Jesica Amanda",
    "email": "c14220046@john.petra.ac.id",
    "posisi_dilamar": "Frontend Developer",

    # CV Text
    "cv_text": """JESICA AMANDA
081336248282 | jesicaamandaa877@gmail.com | https://www.linkedin.com/in/jesica-amanda-a25939368?
utm_source=share_via&utm_content=profile&utm_medium=member_android | Portofolio : petra.id/portoJesica
Jalan Sono Indah VII no 37, Sonokwijenan, Sukomanunggal, Surabaya
Enthusiastic Informatics student skilled in visual design, public relations, team coordination, and creative
production. Experienced in managing events and digital content, with growing expertise in web development and
programming. Motivated to contribute to technical and creative projects.

Work Experiences
Petra Christian University - Surabaya Jan 2025 - Present
Laboratory Assistant
Assisted lecturers in managing lab sessions for 15–20 students per class, ensuring smooth workflow, timely completion of experiments,
and proper functioning of all lab equipment, reducing setup time by 20%.
Petra Christian University - Surabaya Aug 2025 - Present
Assistant Lecturer
Prepared teaching materials and mentored 15–20 students per class, improving student understanding and engagement by 20%.
Education Level
UK Petra - Surabaya Aug 2023 - Jun 2027 (Expected)
Bachelor of Undergraduate Student of Informatics study program, 3.84/4.00
SMA Kristen Petra 1 - Surabaya Jul 2020 - May 2023
Senior High School, Science Program
Organisational Experience
HIMAINFRA - Petra Christian University Jun 2025 - Present
Deputy Head of Creative and Branding Department
HIMAINFRA is the student association of the Informatics Department, focusing on creative initiatives, branding, and community
engagement.
Supported the department head in managing 10+ branding projects per semester.
Coordinated design tasks, monitored deadlines, and guided team members, improving departmental efficiency by 25%.
Festive Youth Intersalon 2025 - Surabaya Dec 2024 - Jun 2025
Coordinator of Public Relation and Sponsorship
Festive Youth Intersalon is an annual youth event that gathers students from schools across Indonesia for competitions, workshops, and
collaborative activities.
Led a 3-member team managing invitations, media partnerships, and sponsorships for 200+ participants over 6 months.
Increased event visibility by 50% and secured funding through successful sponsorship campaigns.
Informatics Rally Games and Logic 2025 - Surabaya Mar 2025 - Nov 2025
Coordinator of Creative Division
An annual competitive event challenging participants’ logic and programming skills, attracting both local and online audiences.
Oversaw a 7-member creative team producing 30+ design deliverables including posters, banners, and social media content within 7
months.
Increased online viewership by 553.6%, from 1,637 to 10,700+
Training Divisi Panitia 2024 - Petra Christian University Nov 2023 - Mar 2024
Speaker
Explained the division’s roles, responsibilities, and workflow within the committee, while providing insights on design tools, publication
concepts, and cross-division collaboration.
Successfully conducted an interactive and informative training session for 50+ new committee members.
Improved participants’ understanding of creative processes and teamwork dynamics.
Fostered motivation and enthusiasm within the Creative Division for upcoming projects.
Skills, Achievements & Other Experience
Participant of BluAmbassador  (2024)""",

    # Transkrip Jawaban Interview
    "transkrip_pertanyaan_1": """Halo perkenalkan nama saya Jesica Amanda, saya merupakan mahasiswa semester 5 di Universitas Kristen Petra jurusan informatika """,


    "transkrip_pertanyaan_2": """Karena menurut saya perusahaan anda merupakan perusahaan yang bagus dan terkenal di Indonesia. Dan saya dengar juga kalau lulusan magang dari sini itu menghasilkan kualitas yang bagus""",
    
    
    "transkrip_pertanyaan_3": """Beberapa kali saya membuat project membuat website menggunakan laravel. Selain tugas-tugas kuliah juga saya aktif dalam berorganisasi untuk melatih soft skill yang saya miliki seperti bersosialisasi, kepemimpinan, kerja sama, problem solving""",

    "transkrip_pertanyaan_4": """Saya mau belajar hal-hal yang baru dan saya mau belajar di perusahaan ini untuk mengembangkan kemampuan saya""",

    # Data Transkrip Akademik
    "transkrip_nrp": "C14230042",
    "transkrip_prodi": "INFORMATIKA",
    "transkrip_ipk": 3.84,
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
        "Nilai": "B+"
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
        "Kode": "TF4229",
        "Mata_Kuliah": "BASIS DATA",
        "Semester": "2-23/24",
        "SKS": 3,
        "Nilai": "B+"
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
        "Nilai": "B"
      },
      {
        "Kode": "TF4267",
        "Mata_Kuliah": "KOMUNIKASI INTERPERSONAL",
        "Semester": "2-23/24",
        "SKS": 3,
        "Nilai": "A"
      },
      {
        "Kode": "TF4235",
        "Mata_Kuliah": "PEMROGRAMAN BERORIENTASI OBYEK",
        "Semester": "2-23/24",
        "SKS": 3,
        "Nilai": "B+"
      },
      {
        "Kode": "TF4219",
        "Mata_Kuliah": "STRUKTUR DATA",
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
        "Kode": "TF4270",
        "Mata_Kuliah": "DESAIN DAN ANALISIS ALGORITMA",
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
        "Kode": "TF4343",
        "Mata_Kuliah": "TEKNOLOGI WEB",
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
        "Kode": "DU4210",
        "Mata_Kuliah": "KEWARGANEGARAAN",
        "Semester": "1-24/25",
        "SKS": 2,
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
        "Kode": "DU4198",
        "Mata_Kuliah": "DIGITAL LEADERSHIP",
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
        "Nilai": "B+"
      },
      {
        "Kode": "TF4592",
        "Mata_Kuliah": "ASSOCIATE DATA SCIENTIST",
        "Semester": "2-24/25",
        "SKS": 3,
        "Nilai": "A"
      },
      {
        "Kode": "TF4578",
        "Mata_Kuliah": "ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING (AIML)",
        "Semester": "2-24/25",
        "SKS": 3,
        "Nilai": "B+"
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
      }
    ],
    "transkrip_grade_distribution": {
      "A": 24,
      "B+": 6,
      "B": 1,
      "C+": 0
    },

    # Data SKKK
    
   "skkk_data": [
    {
      "No": 1,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "HOW CONSULTANT HELP BUSINESSES CREATE VALUE THROUGH DATA",
      "Nilai_SKKK": 7.5,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 2,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "KULIAH INDUSTRI DESAIN INTERIOR (KIDI) 2023",
      "Nilai_SKKK": 6,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 3,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "TECHNICAL PROGRAM MANAGEMENT IN B2B VS B2C WEBINAR",
      "Nilai_SKKK": 7.5,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 4,
      "Jabatan": "Peserta",
      "Nama_Kegiatan": "WEBINAR TIPS KESEHATAN MATA DI ERA DIGITAL",
      "Nilai_SKKK": 3,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 5,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "WHY DO COMPANIES MIGRATE THEIR DATA AND APPLICATIONS TO THE CLOUD WEBINAR",
      "Nilai_SKKK": 7.5,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 6,
      "Jabatan": "Anggota HIMA - Publikasi, Dekorasi, Dokumentasi",
      "Nama_Kegiatan": "DYNAMIC CAREER CHANGES IN THE AGE OF DIGITAL TRANSFORMATION 2024",
      "Nilai_SKKK": 8.3,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 7,
      "Jabatan": "Anggota HIMA - Public Relation & Sponsor",
      "Nama_Kegiatan": "FESTIVE 2024",
      "Nilai_SKKK": 16.5,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 8,
      "Jabatan": "Peserta UKM",
      "Nama_Kegiatan": "KEGIATAN RUTIN UKM MARTOGRAFI 2024",
      "Nilai_SKKK": 10,
      "Periode": "232",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 9,
      "Jabatan": "Anggota",
      "Nama_Kegiatan": "PANITIA WISUDA KE-85",
      "Nilai_SKKK": 6.6,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 10,
      "Jabatan": "Peserta",
      "Nama_Kegiatan": "SERVANT LEADERSHIP TRAINING 2024",
      "Nilai_SKKK": 3,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 11,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "SL - KOMAL (A,B,C,D) - GENAP 23/24 (5/2/24 - 28/6/24)",
      "Nilai_SKKK": 2,
      "Periode": "232",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 12,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "STUDY WITH FUN 2023",
      "Nilai_SKKK": 3,
      "Periode": "232",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 13,
      "Jabatan": "Anggota HIMA - Asisten Pengajar",
      "Nama_Kegiatan": "BEBRAS CHALLENGE 2024",
      "Nilai_SKKK": 1.25,
      "Periode": "241",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 14,
      "Jabatan": "Koordinator/Anggota BKU/BPMF - Divisi PDD",
      "Nama_Kegiatan": "HUNTING BESAR SARANGAN 2025",
      "Nilai_SKKK": 7.8,
      "Periode": "241",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 15,
      "Jabatan": "Anggota HIMA - Divisi Publikasi, Dokumentasi dan Dekorasi",
      "Nama_Kegiatan": "IMPARTATION CAMP (I-CAMP) 2024",
      "Nilai_SKKK": 6.6,
      "Periode": "241",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 16,
      "Jabatan": "Anggota",
      "Nama_Kegiatan": "PANITIA WISUDA 86",
      "Nilai_SKKK": 6.6,
      "Periode": "241",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 17,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "PEMATERI PCU EXPO",
      "Nilai_SKKK": 3.8,
      "Periode": "241",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 18,
      "Jabatan": "Anggota HIMA - Pelatih",
      "Nama_Kegiatan": "PENGABDIAN MASYARAKAT BEBRAS TRAINING : INSIGHTFUL MINDS",
      "Nilai_SKKK": 1.25,
      "Periode": "241",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 19,
      "Jabatan": "Peserta",
      "Nama_Kegiatan": "SL KOLABORASI SERVICE LEARNING MK. PANCASILA, KEWARGANEGARAAN,-BHS. INDONESIA GASAL 24/25",
      "Nilai_SKKK": 2,
      "Periode": "241",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 20,
      "Jabatan": "Anggota HIMA - Divisi PDD",
      "Nama_Kegiatan": "STUDY WITH FUN 2024",
      "Nilai_SKKK": 6.6,
      "Periode": "241",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 21,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "CAREER SHAPING IN ENTREPRENEURIAL 2025",
      "Nilai_SKKK": 3.8,
      "Periode": "242",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 22,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "DIES NATALIS INFORMATIKA 27",
      "Nilai_SKKK": 1.5,
      "Periode": "242",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 23,
      "Jabatan": "Koordinator/Anggota BKU/BPMF - Divisi Public Relation dan Sponsor",
      "Nama_Kegiatan": "FESTIVE YOUTH INTERSALON 2025",
      "Nilai_SKKK": 15.6,
      "Periode": "242",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 24,
      "Jabatan": "Anggota HIMA - Divisi Creative",
      "Nama_Kegiatan": "INFORMATICS RALLY GAMES AND LOGIC 2024",
      "Nilai_SKKK": 13.2,
      "Periode": "242",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 25,
      "Jabatan": "Anggota UKM - Keanggotaan",
      "Nama_Kegiatan": "KEGIATAN RUTIN UKM MARTOGRAFI 2024/2025",
      "Nilai_SKKK": 14,
      "Periode": "242",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 26,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "KEGIATAN SERVICE LEARNING MK.DIGITAL LEADERSHIP, KELAS B2 (BU JANICE B),GASAL 24/25",
      "Nilai_SKKK": 2,
      "Periode": "242",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 27,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "NUNI INTERNATIONAL SEMINAR SERIES #9 COMPLEX NETWORKS: TOPOLOGICAL ANALYSIS OF CONNECTIVITY",
      "Nilai_SKKK": 7.5,
      "Periode": "242",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 28,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "NUNI INTERNATIONAL SEMINAR SERIES #9 FINANCIAL LITERACY AND FINTECH",
      "Nilai_SKKK": 7.5,
      "Periode": "242",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 29,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "NUNI INTERNATIONAL SEMINAR SERIES #9 UNDERSTANDING AND ANALYZING WORK MOTIVATION THROUGH DATA",
      "Nilai_SKKK": 7.5,
      "Periode": "242",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 30,
      "Jabatan": "Anggota",
      "Nama_Kegiatan": "PANITIA WISUDA KE 87",
      "Nilai_SKKK": 6.6,
      "Periode": "242",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 31,
      "Jabatan": "Anggota HIMA",
      "Nama_Kegiatan": "TRAINING DIVISI PANITIA 2024",
      "Nilai_SKKK": 3.3,
      "Periode": "242",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 32,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "TRASHURE 2025",
      "Nilai_SKKK": 4.5,
      "Periode": "242",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 33,
      "Jabatan": "Anggota",
      "Nama_Kegiatan": "PANITIA WISUDA PCU KE 88",
      "Nilai_SKKK": 3.3,
      "Periode": "251",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 34,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "PEMBUATAN APLIKASI DATA JEMAAT UNTUK GEREJA KRISTEN INDONESIA MAJELIS JEMAAT PONDOK TJANDRA",
      "Nilai_SKKK": 1,
      "Periode": "251",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 35,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "PHOTO CONTEST: PCU LIBRARY THROUGH MY LENS",
      "Nilai_SKKK": 3,
      "Periode": "251",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 36,
      "Jabatan": "Anggota HIMA - Divisi Creative",
      "Nama_Kegiatan": "WORKSHOP LINKEDIN 404 : \"WEAK LINKEDIN NOT FOUND\"",
      "Nilai_SKKK": 6.6,
      "Periode": "251",
      "Bidang": "Organisasi & Kepemimpinan"
    }
  ],
  "skkk_total_activities": 36,
  "skkk_success": True,


    # Analisis Video +
    "analisis_video": {
       "analisis_pertanyaan_1": "analisis: Subjek terlihat kurang yakin saat menjawab, sering melihat ke bawah dan menghindari kontak mata. Artikulasi kurang jelas dengan beberapa kata yang terputus-putus. kesimpulan: 62",
      "analisis_pertanyaan_2": "analisis: Terlihat sangat nervous dengan banyak filler words seperti 'ehm', 'jadi', dan 'itu'. Jawaban kurang terstruktur dan cenderung melompat dari satu poin ke poin lain. kesimpulan: 58",
      "analisis_pertanyaan_3": "analisis: Subjek kesulitan menjelaskan konsep dengan jelas. Beberapa kali meminta pengulangan pertanyaan dan terlihat bingung dengan terminologi teknis yang digunakan. kesimpulan: 55",
      "analisis_pertanyaan_4": "analisis: Jawaban sangat singkat dan kurang detail. Subjek tampak ingin segera mengakhiri penjelasan tanpa elaborasi yang cukup. Bahasa tubuh tertutup. kesimpulan: 60"
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
