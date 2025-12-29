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
    "nama": "Matthew Benedict",
    "email": "c14220065@john.petra.ac.id",
    "posisi_dilamar": "Frontend Developer",

    # CV Text
    "cv_text": """Matthew Benedict

PROFESSIONAL EXPERIENCE

EDUCATION
+62 813-3726-2939 | iammattbenedict@gmail.com | matthewbenedictdev.vercel.app

linkedin.com/in/matthew-benedictt | Surabaya, Indonesia

Petra Christian University | Surabaya, Indonesia | Aug 2022 – March 2026 (Expected)
Concetrations: Full-Stack Development; Bachelor of Informatics Engineering | GPA: 3.7 / 4.0
Front-End Developer Intern — PT. Dutakom Wibawa Putra (D~NET); Surabaya, Indonesia
Built customer & admin dashboards for PT. Omadata Padma Indonesia using React, Material
UI and GraphQL APIs, improving usability for 100+ users.
Implemented 10+ automated Playwright test cases, reducing production bugs.
Collaborated with a other developers and system analysts, delivering 11 new features for the
dashboards.
Jan 2025 – Jul 2025

Vice Coordinator, IT Division — Petra Christian University INDEX 2024; Surabaya, Indonesia
Led 6 developers to build an exhibition website using Laravel, supporting the registration
process for 50+ attendees.
Coordinated with the creative division to align UI design and branding assets.
Developed homepage layout with Tailwind CSS and JavaScript libraries.
Jul 2024 – Aug 2024

Member, IT Division — Petra Christian University EPICLAIR 2024; Surabaya, Indonesia
Built homepage, landing, and registration pages for the event’s website using Laravel,
supporting 500+ participants.
Optimized responsiveness across mobile and desktop, improving accessibility for all users.
Collaborated with the creative team to ensure consistent UI and design assets.
Dec 2023 – Jun 2024

Volunteered teaching elementary students programming fundamentals using Scratch.

SKILLS & INTERESTS
Technical Skills: React, Next.js, JavaScript, TypeScript, GraphQL, Tailwind CSS, Material UI, Ant
Design, SCSS, Playwright, Laravel, Git, Golang, Vue.js
Languages: Native in Bahasa Indonesia; Fluent in English
Achievements: 1st Place, Bytesfest 2024 Web Design Competition; 3rd Place, Infinity Hackathon
OJK-Ekraf 2025
Certifications: Duolingo English Test (140/160); AWS Cloud Developing; AWS Cloud Foundations
Interests: Front-end Development, UI/UX, Web3, Blockchain, Crypto, Trading, Investment""",

    # Transkrip Jawaban Interview
    "transkrip_pertanyaan_1": """Halo, nama saya Matthew Benedict, saya fresh graduate lulusan informatika Petra Christian University dan saya memiliki pengalaman 2 tahun sebagai frontend developer """,


    "transkrip_pertanyaan_2": """Saya melihat bahwa perusahaan ini memiliki track record yang baik dan bisa menjadi tempat bagi saya untuk mengasah skill dan terus bertumbuh.""",
    
    
    "transkrip_pertanyaan_3": """Saya pernah menjalani magang selama 5 tahun di PT. ABC sebagai frontend developer dan dari magang tersebut saya belajar banyak bagaimana cara mengaplikasikan kemampuan koding website dengan dunia kerja.""",

    "transkrip_pertanyaan_4": """Karena saya adalah orang yang terus mau belajar dan mudah beradaptasi sehingga saya bisa menyesuaikan kebutuhan yang dibutuhkan oleh PT. XYZ dan dengan pengalaman kerja saya selama 5 tahun sebagai frontend developer, saya yakin saya adalah kandidat yang relevan untuk posisi yang saya lamar di perusahaan ini.""",

    # Data Transkrip Akademik
    "transkrip_nrp": "C14220065",
    "transkrip_prodi": "INFORMATIKA",
    "transkrip_ipk": 3.70,
    "transkrip_total_sks": 132,
    "transkrip_total_mk": 40,
    "transkrip_courses": [
        {"Kode": "DU4197", "Mata_Kuliah": "Agama dan Hidup Bermakna", "Semester": "1-22/23", "SKS": 4, "Nilai": "B+"},
        {"Kode": "DU4122", "Mata_Kuliah": "Bahasa Indonesia", "Semester": "1-22/23", "SKS": 2, "Nilai": "A"},
        {"Kode": "TF4205", "Mata_Kuliah": "Dasar Sistem Komputer", "Semester": "1-22/23", "SKS": 2, "Nilai": "B+"},
        {"Kode": "FD4505", "Mata_Kuliah": "Kalkulus I", "Semester": "1-22/23", "SKS": 3, "Nilai": "C+"},
        {"Kode": "TF4537", "Mata_Kuliah": "Konsep Algoritma", "Semester": "1-22/23", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4536", "Mata_Kuliah": "Dasar Pemrograman", "Semester": "1-22/23", "SKS": 4, "Nilai": "A"},
        {"Kode": "TF4220", "Mata_Kuliah": "Pengantar Manajemen dan Bisnis", "Semester": "1-22/23", "SKS": 2, "Nilai": "A"},
        {"Kode": "DU4101", "Mata_Kuliah": "Pancasila", "Semester": "2-22/23", "SKS": 2, "Nilai": "A"},
        {"Kode": "TF4227", "Mata_Kuliah": "Statistika Dasar", "Semester": "2-22/23", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4267", "Mata_Kuliah": "Komunikasi Interpersonal", "Semester": "2-22/23", "SKS": 3, "Nilai": "B+"},
        {"Kode": "TF4245", "Mata_Kuliah": "Matematika Diskrit", "Semester": "2-22/23", "SKS": 3, "Nilai": "B+"},
        {"Kode": "TF4235", "Mata_Kuliah": "Pemrograman Berorientasi Objek", "Semester": "2-22/23", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4253", "Mata_Kuliah": "Jaringan Komputer", "Semester": "2-22/23", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4229", "Mata_Kuliah": "Basis Data", "Semester": "2-22/23", "SKS": 3, "Nilai": "B+"},
        {"Kode": "TF4249", "Mata_Kuliah": "Pengantar Akuntansi", "Semester": "1-23/24", "SKS": 2, "Nilai": "B+"},
        {"Kode": "TF4255", "Mata_Kuliah": "Rekayasa Perangkat Lunak", "Semester": "1-23/24", "SKS": 3, "Nilai": "B+"},
        {"Kode": "FD4507", "Mata_Kuliah": "Aljabar Linier", "Semester": "1-23/24", "SKS": 3, "Nilai": "B+"},
        {"Kode": "TF4270", "Mata_Kuliah": "Desain dan Analisis Algoritma", "Semester": "1-23/24", "SKS": 3, "Nilai": "B"},
        {"Kode": "TF4372", "Mata_Kuliah": "Arsitektur dan Organisasi Komputer", "Semester": "1-23/24", "SKS": 3, "Nilai": "B"},
        {"Kode": "TF4219", "Mata_Kuliah": "Struktur Data", "Semester": "1-23/24", "SKS": 3, "Nilai": "B+"},
        {"Kode": "DU4164", "Mata_Kuliah": "Pendidikan Kewarganegaraan", "Semester": "1-23/24", "SKS": 2, "Nilai": "A"},
        {"Kode": "TF4343", "Mata_Kuliah": "Teknologi Web", "Semester": "1-23/24", "SKS": 3, "Nilai": "A"},
        {"Kode": "DU4198", "Mata_Kuliah": "Digital Leadership", "Semester": "2-23/24", "SKS": 2, "Nilai": "A"},
        {"Kode": "TF4327", "Mata_Kuliah": "Analisis dan Desain Sistem Informasi", "Semester": "2-23/24", "SKS": 3, "Nilai": "B"},
        {"Kode": "TF4504", "Mata_Kuliah": "Bahasa Inggris", "Semester": "2-23/24", "SKS": 2, "Nilai": "A"},
        {"Kode": "TF4544", "Mata_Kuliah": "Cyber Operations", "Semester": "2-23/24", "SKS": 3, "Nilai": "B+"},
        {"Kode": "TF4415", "Mata_Kuliah": "Grafika Komputer", "Semester": "2-23/24", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4243", "Mata_Kuliah": "Sistem Operasi", "Semester": "2-23/24", "SKS": 3, "Nilai": "B+"},
        {"Kode": "TF4247", "Mata_Kuliah": "Metode Numerik", "Semester": "2-23/24", "SKS": 2, "Nilai": "B"},
        {"Kode": "TF4409", "Mata_Kuliah": "Kecerdasan Buatan", "Semester": "2-23/24", "SKS": 3, "Nilai": "B+"},
        {"Kode": "TF4237", "Mata_Kuliah": "Interaksi Manusia dan Komputer", "Semester": "2-23/24", "SKS": 3, "Nilai": "B+"},
        {"Kode": "FD4508", "Mata_Kuliah": "Technopreneurship", "Semester": "1-24/25", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4579", "Mata_Kuliah": "Web Frameworks and Deployment", "Semester": "1-24/25", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4509", "Mata_Kuliah": "Cloud Computing", "Semester": "1-24/25", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4507", "Mata_Kuliah": "Sistem Terdistribusi", "Semester": "1-24/25", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4317", "Mata_Kuliah": "Manajemen Proyek Teknologi Informasi", "Semester": "1-24/25", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4516", "Mata_Kuliah": "Pengembangan Aplikasi Android", "Semester": "1-24/25", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4587", "Mata_Kuliah": "Software Testing and Quality Assurance", "Semester": "1-24/25", "SKS": 3, "Nilai": "B+"},
        {"Kode": "TF4569", "Mata_Kuliah": "Network Defense", "Semester": "1-24/25", "SKS": 3, "Nilai": "B+"},
        {"Kode": "TF4374", "Mata_Kuliah": "Teknologi Open Source", "Semester": "2-24/25", "SKS": 3, "Nilai": "A"},
        {"Kode": "TF4259", "Mata_Kuliah": "Metodologi Penelitian", "Semester": "2-24/25", "SKS": 3, "Nilai": "B+"},
        {"Kode": "TF4540", "Mata_Kuliah": "Industrial Training", "Semester": "2-24/25", "SKS": 6, "Nilai": "A"},
        {"Kode": "TF4261", "Mata_Kuliah": "Kerja Praktek", "Semester": "2-24/25", "SKS": 2, "Nilai": "A"},
        {"Kode": "TF4539", "Mata_Kuliah": "Professional Development", "Semester": "2-24/25", "SKS": 6, "Nilai": "A"}
    ],
    "transkrip_grade_distribution": {
        "A": 22,
        "B+": 14,
        "B": 3,
        "C+": 1
    },

    # Data SKKK
    
  "skkk_data": [
    {"No": 1, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "BANK PANITIA INFORMATICS COMMITTEE CLUB 2022", "Nilai_SKKK": 1.5, "Periode": "221", "Bidang": "PEMBELAJARAN"},
    {"No": 2, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "KULIAH UMUM - CYBER SECURITY AWARENESS, JUMAT - 25 NOVEMBER 2022", "Nilai_SKKK": 1.5, "Periode": "221", "Bidang": "PEMBELAJARAN"},
    {"No": 3, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "MARINA", "Nilai_SKKK": 0.75, "Periode": "221", "Bidang": "PENGABDIAN MASYARAKAT"},
    {"No": 4, "Jabatan": "ANGGOTA/ANGGOTA HIMA", "Nama_Kegiatan": "SATGAS UPACARA 10 NOVEMBER 2022", "Nilai_SKKK": 6.6, "Periode": "221", "Bidang": "ORGANISASI & KEPEMIMPINAN"},
    {"No": 5, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "SEMINAR NASIONAL OUTLOOKING THE INVESTMENT WORLD", "Nilai_SKKK": 6.0, "Periode": "221", "Bidang": "PEMBELAJARAN"},
    {"No": 6, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "STARTUP SHARING SESSION METAVERSE IN EDUCATION CREATING FUTURE SKILLED WORKFORCE", "Nilai_SKKK": 6.0, "Periode": "221", "Bidang": "PEMBELAJARAN"},
    {"No": 7, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "TECHNOLOGY IMPLEMENTATION IN THE FASHION INDUSTRY", "Nilai_SKKK": 7.5, "Periode": "221", "Bidang": "PEMBELAJARAN"},
    {"No": 8, "Jabatan": "PENGISI ACARA/PENGMAS 5ASPEK", "Nama_Kegiatan": "VERITAS SEMINAR GANJIL 2022", "Nilai_SKKK": 4.2, "Periode": "221", "Bidang": "PARTISIPASI/PRESTASI"},
    {"No": 9, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "AYE AYE CAPTAIN 2023", "Nilai_SKKK": 3.0, "Periode": "222", "Bidang": "PEMBELAJARAN"},
    {"No": 10, "Jabatan": "ANGGOTA/ANGGOTA HIMA PERLENGKAPAN DAN KEAMANAN", "Nama_Kegiatan": "DONOR DARAH 3", "Nilai_SKKK": 3.3, "Periode": "222", "Bidang": "ORGANISASI & KEPEMIMPINAN"},
    {"No": 11, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "KAMP MAHASISWA 2023", "Nilai_SKKK": 3.0, "Periode": "222", "Bidang": "PEMBELAJARAN"},
    {"No": 12, "Jabatan": "PESERTA UKM", "Nama_Kegiatan": "KEGIATAN RUTIN DIKRU UKM EMR", "Nilai_SKKK": 10.0, "Periode": "222", "Bidang": "PARTISIPASI/PRESTASI"},
    {"No": 13, "Jabatan": "PENGISI ACARA/PENGMAS 5ASPEK", "Nama_Kegiatan": "NATAL UNIVERSITAS 2022", "Nilai_SKKK": 4.2, "Periode": "222", "Bidang": "PARTISIPASI/PRESTASI"},
    {"No": 14, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "RETREAT KADER 2023", "Nilai_SKKK": 3.0, "Periode": "222", "Bidang": "PEMBELAJARAN"},
    {"No": 15, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "SEMINAR BETTER PERSON BRIGHTER FUTURE 2023", "Nilai_SKKK": 1.5, "Periode": "222", "Bidang": "PEMBELAJARAN"},
    {"No": 16, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "SEMINAR WAWASAN KEBANGSAAN TANGGAL 30 MEI 2023(1)", "Nilai_SKKK": 6.0, "Periode": "222", "Bidang": "PEMBELAJARAN"},
    {"No": 17, "Jabatan": "ANGGOTA/ANGGOTA HIMA PERLENGKAPAN", "Nama_Kegiatan": "VERITAS SEMINAR GENAP 2023", "Nilai_SKKK": 16.5, "Periode": "222", "Bidang": "ORGANISASI & KEPEMIMPINAN"},
    {"No": 18, "Jabatan": "ANGGOTA/ANGGOTA HIMA ANGGOTA DIVISI PERAN", "Nama_Kegiatan": "WELCOME, GRATEFUL GENERATION 2023", "Nilai_SKKK": 9.9, "Periode": "222", "Bidang": "ORGANISASI & KEPEMIMPINAN"},
    {"No": 19, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "LOGOS 2023", "Nilai_SKKK": 3.0, "Periode": "231", "Bidang": "PEMBELAJARAN"},
    {"No": 20, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "PEMBELAJARAN KEBERAGAMAN BANGSA INDONESIA DI SD SE-SURABAYA (PENGMAS SL)", "Nilai_SKKK": 2.0, "Periode": "231", "Bidang": "PENGABDIAN MASYARAKAT"},
    {"No": 21, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "SL - KOMAL (A,B,C,D) - GENAP 22/23 (6/2/23 - 30/6/23)", "Nilai_SKKK": 2.0, "Periode": "231", "Bidang": "PENGABDIAN MASYARAKAT"},
    {"No": 22, "Jabatan": "PESERTA", "Nama_Kegiatan": "EPICLAIR 2024", "Nilai_SKKK": 6.0, "Periode": "232", "Bidang": "PARTISIPASI/PRESTASI"},
    {"No": 23, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "EXHIBITION INTERNAL 2024", "Nilai_SKKK": 3.0, "Periode": "232", "Bidang": "PARTISIPASI/PRESTASI"},
    {"No": 24, "Jabatan": "ANGGOTA", "Nama_Kegiatan": "FUNGSIONARIS PELAYAN MAHASISWA 2024", "Nilai_SKKK": 22.0, "Periode": "232", "Bidang": "ORGANISASI & KEPEMIMPINAN"},
    {"No": 25, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "LOGOS 2024", "Nilai_SKKK": 2.3, "Periode": "232", "Bidang": "PEMBELAJARAN"},
    {"No": 26, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "RETREAT KADER 2024", "Nilai_SKKK": 3.0, "Periode": "232", "Bidang": "PEMBELAJARAN"},
    {"No": 27, "Jabatan": "KOORDINATOR/ANGGOTA BKU/BPMF KOORDINATOR", "Nama_Kegiatan": "VERITAS SEMINAR GASAL 2023-2024", "Nilai_SKKK": 7.8, "Periode": "232", "Bidang": "ORGANISASI & KEPEMIMPINAN"},
    {"No": 28, "Jabatan": "ANGGOTA/ANGGOTA HIMA VOLUNTEER", "Nama_Kegiatan": "NATAL UNIVERSITAS 2024", "Nilai_SKKK": 6.6, "Periode": "241", "Bidang": "ORGANISASI & KEPEMIMPINAN"},
    {"No": 29, "Jabatan": "ANGGOTA/ANGGOTA HIMA PERKAP", "Nama_Kegiatan": "PENGUTUSAN WISUDAWAN GANJIL 2024", "Nilai_SKKK": 6.6, "Periode": "241", "Bidang": "ORGANISASI & KEPEMIMPINAN"},
    {"No": 30, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "PERSEKUTUAN PROGRAM STUDI SYNTHESIS 1 \"BYTES & BALANCING LIFE WITH HIS GRACE\"", "Nilai_SKKK": 1.5, "Periode": "241", "Bidang": "PEMBELAJARAN"},
    {"No": 31, "Jabatan": "ANGGOTA/ANGGOTA HIMA ANGGOTA BIDANG PEMURIDAN", "Nama_Kegiatan": "PENGURUS PELMA 2024-2025", "Nilai_SKKK": 22.0, "Periode": "242", "Bidang": "ORGANISASI & KEPEMIMPINAN"},
    {"No": 32, "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR", "Nama_Kegiatan": "RETREAT KADER 2025", "Nilai_SKKK": 3.0, "Periode": "242", "Bidang": "PEMBELAJARAN"},
    {"No": 33, "Jabatan": "ANGGOTA/ANGGOTA HIMA TRANSAKOM", "Nama_Kegiatan": "LOGOS 2025", "Nilai_SKKK": 6.6, "Periode": "251", "Bidang": "ORGANISASI & KEPEMIMPINAN"}
  ],
  "skkk_total_activities": 33,
  "skkk_success": True,


    # Analisis Video +
    "analisis_video": {
        "analisis_pertanyaan_1": "analisis: Subjek terlihat sangat percaya diri, artikulasi jelas, dan mampu menjawab pertanyaan teknis dengan lancar tanpa terlihat ragu. kesimpulan: 95",
        
        "analisis_pertanyaan_2": "analisis: Subjek sesekali melihat ke arah lain saat berpikir, namun tetap mampu menjaga alur pembicaraan dengan baik dan profesional. kesimpulan: 80",
        
        "analisis_pertanyaan_3": "analisis: Jawaban yang diberikan sangat terstruktur. Meskipun nada bicara agak datar, poin-poin penting tersampaikan dengan sangat detail. kesimpulan: 88",
        
        "analisis_pertanyaan_4": "analisis: Subjek tampak sedikit terburu-buru dalam menjelaskan solusi, namun secara teknis jawaban yang diberikan sudah tepat sasaran. kesimpulan: 75"
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
