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
    "nama": "Helena Susan Tanoyo",
    "email": "c14220046@john.petra.ac.id",
    "posisi_dilamar": "Data Scientist",

    # CV Text
    "cv_text": """HELENA SUSAN TANOYO

+628990780276 | helenasusan.tanoyo@gmail.com | linkedin.com/in/helena-susan-tanoyo

Passionate Junior Data Science and Analytics major at Petra Christian University. Actively involved in organizations and volunteer work,
developing skills in teamwork, leadership, time management, and problem-solving. Committed to expanding knowledge and gaining
hands-on experience in data analytics.
Education Level
Petra Christian University - Indonesia Jul 2022 - Mar 2026 (Expected)
Bachelor Degree in Data Science and Analytics, 3.72/4.00
Projects
Food Data Analysis and Clustering (project link)
Analyzed food production data across countries, applying K-Means and DBScan clustering to uncover production patterns. Built an
interactive Streamlit dashboard to visualize insights, highlighting regional trends and differences in food production.
Telco Churned Customer Analysis (project link)
Analyzed factors driving customer churn in the telecommunications sector using R. Created a Power BI dashboard to visualize key
insights, helping identify trends and patterns linked to churn behavior.
Internship at PT Samator Gas Industri
Supported the implementation of the ERP and bottle tracking systems by assisting branch users and resolving technical issues. Created
SQL queries to help the procurement team retrieve data for price analysis. Built dashboard to monitor product distribution performance.
Organizational Experience
Badan Eksekutif Mahasiswa Aug 2023 -Aug 2025
Part of Human Resource Development Department
Developed and managed content strategy as the Content Planner for the @lifeatbempetra Instagram account, enhancing
engagement and community outreach.
Supported the evaluation process of BEM members, assisting in performance reviews and assessment sharing.
Conducted interviews and coordinated intern selection processes.
Chief Committee for Rapat Kerja BEM 2024/2025.
Supervised a team of five HRD members, overseeing their performance and supporting their development to drive effective team
outcomes.
Welcome, Grateful Generation 2023 Mar 2023 - Jul 2023
Member of Event Division
Developed a comprehensive website concept for rally games, integrating storyline, point collection, and in-game store features.
Collaborated with creative and IT teams to create assets and oversee website development, ensuring smooth functionality on event
day.
Supervised rally game execution, coordinating time management across all stations to ensure seamless flow.
Partnered effectively with multiple divisions and external stakeholders to support cohesive event operations.
Contributed as PIC backstage for the Opening of WGG 2023.
Servant Leadership Training 2024 Nov 2023 - Feb 2024
Secretary
Developed a comprehensive proposal and management system for event planning, ensuring organized workflows, and clear
objectives.
Supervised seven divisions with a team of over 70 members, supporting smooth and efficient event execution.
Created and supervised agreements with all external parties involved to ensure smooth event execution.
Coordinated with the leadership team at Petra Christian University to align on key materials and deliverables.
Informatics Rally Games and Logic 2024 Mar 2024 - Nov 2024
Vice Coordinator of Event Division
Planned, conceptualized, and executed a large-scale event, engaging over 350 high school students from across Indonesia.
Supervising the work of event members, including the production of a short film and master of ceremony training.
Collaborated with seven other divisions and external parties.
Oversaw logistical coordination and communication across two separate competition venues.

Skills and Other Experience
Tools: Microsoft Office, Microsoft Power BI, Jupyter Notebook
Language: Python, R, MySQL, Basic Programming""",

    # Transkrip Jawaban Interview
    "transkrip_pertanyaan_1": """Halo Lesti, perkenalkan nama saya Helena. Saya merupakan lulusan Data Science and Analytics. Selain memiliki latar belakang teknis, saya adalah pribadi yang aktif dan senang terlibat dalam perencanaan berbagai kegiatan, yang mengasah kemampuan saya dalam berorganisasi serta bekerja sama dalam tim.""",


    "transkrip_pertanyaan_2": """Saya tertarik bergabung karena PT XYZ dikenal sebagai perusahaan yang dinamis dan terus berinovasi. Sebagai lulusan Data Science, saya ingin menerapkan kemampuan analisis data saya untuk memberikan dampak nyata. Selain itu, saya merasa kepribadian saya yang aktif dan terbiasa dalam perencanaan kegiatan sangat selaras dengan lingkungan kerja di sini yang produktif.""",
    
    
    "transkrip_pertanyaan_3": """Selama masa studi, saya menyelesaikan proyek analisis data di mana saya bertanggung jawab mengolah data mentah hingga menjadi visualisasi yang informatif.""",

    "transkrip_pertanyaan_4": """Saya memiliki kombinasi yang kuat antara keahlian teknis di bidang Data Science dan sikap kerja yang proaktif. Sifat saya yang terbiasa dalam perencanaan memastikan setiap proyek data yang saya kerjakan berjalan terstruktur dan tepat waktu.""",

    # Data Transkrip Akademik
    "transkrip_nrp": "c14220149",
    "transkrip_prodi": "INFORMATIKA",
    "transkrip_ipk": 3.72,
    "transkrip_total_sks": 132,
    "transkrip_total_mk": 45,
    "transkrip_courses": [
      {
      "Kode": "TF4536",
      "Mata_Kuliah": "DASAR PEMROGRAMAN",
      "Semester": "1-22/23",
      "SKS": 4,
      "Nilai": "B+"
    },
    {
      "Kode": "FD4505",
      "Mata_Kuliah": "KALKULUS I",
      "Semester": "1-22/23",
      "SKS": 3,
      "Nilai": "B"
    },
    {
      "Kode": "DU4197",
      "Mata_Kuliah": "AGAMA DAN HIDUP BERMAKNA",
      "Semester": "1-22/23",
      "SKS": 4,
      "Nilai": "B+"
    },
    {
      "Kode": "DU4122",
      "Mata_Kuliah": "BAHASA INDONESIA",
      "Semester": "1-22/23",
      "SKS": 2,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4205",
      "Mata_Kuliah": "DASAR SISTEM KOMPUTER",
      "Semester": "1-22/23",
      "SKS": 2,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4537",
      "Mata_Kuliah": "KONSEP ALGORITMA",
      "Semester": "1-22/23",
      "SKS": 3,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4220",
      "Mata_Kuliah": "PENGANTAR MANAJEMEN DAN BISNIS",
      "Semester": "1-22/23",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "TF4229",
      "Mata_Kuliah": "BASIS DATA",
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
      "Kode": "TF4267",
      "Mata_Kuliah": "KOMUNIKASI INTERPERSONAL",
      "Semester": "2-22/23",
      "SKS": 3,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4245",
      "Mata_Kuliah": "MATEMATIKA DISKRIT",
      "Semester": "2-22/23",
      "SKS": 3,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4253",
      "Mata_Kuliah": "JARINGAN KOMPUTER",
      "Semester": "2-22/23",
      "SKS": 3,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4255",
      "Mata_Kuliah": "REKAYASA PERANGKAT LUNAK",
      "Semester": "1-23/24",
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
      "Kode": "TF4504",
      "Mata_Kuliah": "BAHASA INGGRIS",
      "Semester": "1-23/24",
      "SKS": 2,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4249",
      "Mata_Kuliah": "PENGANTAR AKUNTANSI",
      "Semester": "1-23/24",
      "SKS": 2,
      "Nilai": "A"
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
      "Nilai": "B"
    },
    {
      "Kode": "TF4219",
      "Mata_Kuliah": "STRUKTUR DATA",
      "Semester": "1-23/24",
      "SKS": 3,
      "Nilai": "B+"
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
      "Nilai": "B+"
    },
    {
      "Kode": "DU4163",
      "Mata_Kuliah": "ETIKA PROFESI",
      "Semester": "2-23/24",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "DU4198",
      "Mata_Kuliah": "DIGITAL LEADERSHIP",
      "Semester": "2-23/24",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "TF4551",
      "Mata_Kuliah": "APPLIED STATISTICS",
      "Semester": "2-23/24",
      "SKS": 3,
      "Nilai": "B"
    },
    {
      "Kode": "TF4333",
      "Mata_Kuliah": "DATA MINING",
      "Semester": "2-23/24",
      "SKS": 3,
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
      "Nilai": "B+"
    },
    {
      "Kode": "TF4544",
      "Mata_Kuliah": "CYBER OPERATIONS",
      "Semester": "2-23/24",
      "SKS": 3,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4243",
      "Mata_Kuliah": "SISTEM OPERASI",
      "Semester": "2-23/24",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4247",
      "Mata_Kuliah": "METODE NUMERIK",
      "Semester": "2-23/24",
      "SKS": 2,
      "Nilai": "B+"
    },
    {
      "Kode": "FD4508",
      "Mata_Kuliah": "TECHNOPRENEURSHIP",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4523",
      "Mata_Kuliah": "ANALISIS BIG DATA",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4550",
      "Mata_Kuliah": "PRESENTASI DAN VISUALISASI DATA",
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
      "Kode": "TF4569",
      "Mata_Kuliah": "NETWORK DEFENSE",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4548",
      "Mata_Kuliah": "BUSINESS INTELLIGENCE",
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
      "Kode": "TF4414",
      "Mata_Kuliah": "ENTERPRISE RESOURCE PLANNING",
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
      "Kode": "TF4259",
      "Mata_Kuliah": "METODOLOGI PENELITIAN",
      "Semester": "2-24/25",
      "SKS": 3,
      "Nilai": "B"
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
    "A": 24,
    "B+": 17,
    "B": 4,
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
      "Nama_Kegiatan": "STARTUP SHARING SESSION METAVERSE IN EDUCATION CREATING FUTURE SKILLED WORKFORCE",
      "Nilai_SKKK": 6,
      "Periode": "221",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 4,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "TUTORIAL PEMROGRAMAN SEMESTER GASAL 2022",
      "Nilai_SKKK": 2.3,
      "Periode": "221",
      "Bidang": "Pembelajaran"
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
      "Jabatan": "Anggota HIMA - Perlengkapan dan Keamanan",
      "Nama_Kegiatan": "FESTIVE 2023",
      "Nilai_SKKK": 16.5,
      "Periode": "222",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 8,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "INCLUSIVE CAREER: PELATIHAN MENULIS DOKUMEN KARIR BAGI ANAK-ANAK BERKEBUTUHAN KHUSUS",
      "Nilai_SKKK": 0.75,
      "Periode": "222",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 9,
      "Jabatan": "Peserta UKM",
      "Nama_Kegiatan": "KEGIATAN RUTIN UKM MARTOGRAFI",
      "Nilai_SKKK": 10,
      "Periode": "222",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 10,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "MAXIMIZE YOUR TALENT",
      "Nilai_SKKK": 2.3,
      "Periode": "222",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 11,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "PPM : PELATIHAN FROM SCRATCH TO HATCH, 5 JULI 2023",
      "Nilai_SKKK": 0.75,
      "Periode": "222",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 12,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "SEMINAR BETTER PERSON BRIGHTER FUTURE 2023",
      "Nilai_SKKK": 1.5,
      "Periode": "222",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 13,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "SEMINAR WAWASAN KEBANGSAAN TANGGAL 30 MEI 2023",
      "Nilai_SKKK": 6,
      "Periode": "222",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 14,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "STUDY WITH FUN 2022",
      "Nilai_SKKK": 3,
      "Periode": "222",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 15,
      "Jabatan": "Anggota HIMA - Anggota Divisi Acara",
      "Nama_Kegiatan": "WELCOME, GRATEFUL GENERATION 2023",
      "Nilai_SKKK": 9.9,
      "Periode": "222",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 16,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "FELLOWSHIP LK-KBM 2023",
      "Nilai_SKKK": 3,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 17,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "PEMBELAJARAN KEBERAGAMAN BANGSA INDONESIA DI SD SE-SURABAYA (PENGMAS SL)",
      "Nilai_SKKK": 2,
      "Periode": "231",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 18,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "SL - KOMAL (A,B,C,D) - GENAP 22/23 (6/2/23 - 30/6/23)",
      "Nilai_SKKK": 2,
      "Periode": "231",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 19,
      "Jabatan": "Koordinator/Anggota BKU/BPMF - Acara",
      "Nama_Kegiatan": "TUTORIAL UJIAN AKHIR SEMESTER 2024",
      "Nilai_SKKK": 3.9,
      "Periode": "231",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 20,
      "Jabatan": "Anggota HIMA - Anggota HRD",
      "Nama_Kegiatan": "BADAN EKSEKUTIF MAHASISWA 2023-2024",
      "Nilai_SKKK": 22,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 21,
      "Jabatan": "Pengisi Acara/Pengmas 5Aspek",
      "Nama_Kegiatan": "DIES NATALIS INFORMATIKA KE-26",
      "Nilai_SKKK": 2.1,
      "Periode": "232",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 22,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "DYNAMIC CAREER CHANGES IN THE AGE OF DIGITAL TRANSFORMATION 2024",
      "Nilai_SKKK": 3.8,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 23,
      "Jabatan": "Anggota",
      "Nama_Kegiatan": "EPICLAIR 2024",
      "Nilai_SKKK": 16.5,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 24,
      "Jabatan": "Anggota HIMA - Acara",
      "Nama_Kegiatan": "HUT LK-KBM 2024",
      "Nilai_SKKK": 6.6,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 25,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "LKMM-TM 2024",
      "Nilai_SKKK": 3,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 26,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "OUTSOURCE INTENSIVE LEADERSHIP TRAINING 1 2024",
      "Nilai_SKKK": 3,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 27,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "OUTSOURCE INTENSIVE LEADERSHIP TRAINING 2 2024",
      "Nilai_SKKK": 3,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 28,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "RAPAT AKHIR BEM 2024",
      "Nilai_SKKK": 3,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 29,
      "Jabatan": "Koordinator/Anggota BKU/BPMF - Acara",
      "Nama_Kegiatan": "SARASEHAN ORANG TUA MAHASISWA BARU TAHUN 2024",
      "Nilai_SKKK": 5.9,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 30,
      "Jabatan": "Sekretaris",
      "Nama_Kegiatan": "SERVANT LEADERSHIP TRAINING 2024",
      "Nilai_SKKK": 8.4,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 31,
      "Jabatan": "Sekretaris",
      "Nama_Kegiatan": "TALKSHOW INNOVATE, INVEST, INSPIRE 2024",
      "Nilai_SKKK": 12.6,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 32,
      "Jabatan": "Ketua",
      "Nama_Kegiatan": "RAPAT KERJA BEM PERIODE 2024/2025",
      "Nilai_SKKK": 12,
      "Periode": "241",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 33,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "SOSIALISASI KESEKRETARIATAN DAN KEBENDAHARAAN",
      "Nilai_SKKK": 3,
      "Periode": "241",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 34,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "WORKSHOP INTERNSHIP PREPARATION WITH KINOBI 2024",
      "Nilai_SKKK": 3,
      "Periode": "241",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 35,
      "Jabatan": "Koordinator/Anggota BKU/BPMF - Kepala Departemen HRD",
      "Nama_Kegiatan": "BADAN EKSEKUTIF MAHASISWA 2025 - RISE",
      "Nilai_SKKK": 26,
      "Periode": "242",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 36,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "HUT LK-KBM 2024",
      "Nilai_SKKK": 3,
      "Periode": "242",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 37,
      "Jabatan": "Anggota HIMA - Wakil Koord.Divisi Acara",
      "Nama_Kegiatan": "INFORMATICS RALLY GAMES AND LOGIC 2024",
      "Nilai_SKKK": 13.2,
      "Periode": "242",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 38,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "KEJAR MIMPI WEALTH FEST",
      "Nilai_SKKK": 6,
      "Periode": "251",
      "Bidang": "Pembelajaran"
    }
  ],
  "skkk_total_activities": 38,
  "skkk_success": True,


    # Analisis Video +
    "analisis_video": {
      "analisis_pertanyaan_1": "analisis: Subjek memulai dengan konteks yang tepat kemudian berkembang ke penjelasan detail. Alur logis dan mudah diikuti. kesimpulan: 86",
      "analisis_pertanyaan_2": "analisis: Terlihat sangat nyaman dan percaya diri dalam menyampaikan jawaban. Intonasi ekspresif membuat penjelasan lebih hidup. kesimpulan: 87",
      "analisis_pertanyaan_3": "analisis: Subjek menunjukkan fleksibilitas dalam berpikir, mampu menjawab dari berbagai sudut pandang saat diminta elaborasi. kesimpulan: 88",
      "analisis_pertanyaan_4": "analisis: Jawaban diperkaya dengan contoh kasus nyata yang relevan. Menunjukkan aplikasi praktis dari teori yang dikuasai. kesimpulan: 85"
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
