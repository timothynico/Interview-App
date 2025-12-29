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
    "nama": "Alicia Claresta",
    "email": "c14220046@john.petra.ac.id",
    "posisi_dilamar": "Data Scientist",

    # CV Text
    "cv_text": """ALICIA CLARESTA
+62 81233827873 | aliciaclarestaa@gmail.com | linkedin.com/in/alicia-claresta | https://github.com/licalice
An active fourth-year student majoring in Data Science and Analytics with a focus on Python, data visualization, and analytics. Eager to
apply technical skills to solve real-world challenges to generate insights and solutions that drive impactful decision-making.
Education
Petra Christian University Jun 2022 - Feb 2026 (Expected)
Undergraduate Data Science and Analytics (7th semester), 3.78/4.00
Experiences
Samator Group Jan 2025 - Jun 2025
Business Analyst Intern
Participated in implementing ERP and its adaptation for branch operations
Performed asset data mapping and administration
Used software to analyze cylinder tracking problems, including asset deactivation, barcode updates, and error fixing
Informatics PCU Jul 2024 - Present
Laboratory Assistant
Maintained laboratory functionality, including software and hardware
Acted as Algorithm Design & Analysis and Data Structure subject coordinator
Informatics PCU May 2023 - Present
Assistant Lecturer
Assisted in teaching Algorithm Programming, Algorithm Design & Analysis, Basic Statistics, and Data Structure
Organisational
Petra Parade 2025 Jul 2025 - Aug 2025
Vice Coordinator of Event Division
Managed the execution of a large-scale campus promotion event with approximately 4000 high school students from various schools
Facilitated communication between internal university departments and external school partners
Informatics Rally Games and Logic 2024 Apr 2024 - Nov 2024
Coordinator of Event Division
Managing the execution of the event with over 350 high school student participants from seven provinces around Indonesia
Led and coordinated a team of four members for planning and execution of the event
Welcome, Grateful Generation Informatics Program 2024 Apr 2024 - Jul 2024
Coordinator of Event Division
Managing the conceptualizing, planning, and execution of one-day orientation event for 170+ new Informatics students
Supervised a team of five members and coordinated the execution of event, including game flow and campus tour
Welcome, Grateful Generation 2023 Mar 2023 - Jul 2023
Member of Event Division
Planned, conceptualized, and executed Talkshow Alumni sub- event for 1000+ new students, facilitating interactions with industry
professionals and alumni
Skills, Achievements & Other Experience
Achievements : Winner of 3rd Scranton Essay Contest 2024, 4th Runner-Up at LKTIN Dies Natalis AMN ke-1 2023
Languages: Python, SQL, NoSQL, R, Java, Basic Web Programming
Tools: Microsoft Office, PowerBI, Tableau, Looker Studio, Jupyter Notebook, MySQL, SSMS
Telco Customer Churn Analysis Project : Created a report and dashboard on churn behavior with the Telco dataset with logistic
regression using PowerBI and R
Recipe Finder by Ingredient and Dietary Preferences Project : Created a recipe search tool, allowing users to input ingredient,
dietary preferences, and exclude unwanted ingredient using Python, Spoonacular API and Streamlit
Regression Modelling Project : Created a regression modelling using insurance dataset to predict insurance price based on few
categories using Decision Tree, Random Forest, and Gradient Boosting""",

    # Transkrip Jawaban Interview
    "transkrip_pertanyaan_1": """Selamat pagi, perkenalkan nama saya Alicia Claresta. Saat ini saya sedang menempuh perkuliahan semester tujuh di Program Studi Data Science and Analytics di Universitas Kristen Petra dan akan lulus di sekitar bulan februari
Selama perkuliahan saya punya ketertarikan yang besar pada analisis dan bersosialisasi dengan banyak orang. Ketertarikan itu yang mendorong saya untuk aktif sebagai asisten dosen maupun di kepanitian sebagai koordinator divisi acara. Dari pengalaman-pengalaman ini saya terbiasa bekerja secara sistematis, berinteraksi dan berkoordinasi dengan banyak orang. Ke depan saya ingin mengembangkan kemampuan analisis saya sekaligus berkontribusi langsung di dunia kerja""",


    "transkrip_pertanyaan_2": """Saya tertarik melamar di perusahaan ini karena kompleksitas dan skala tantangannya. Ini adalah industri yang melayani jutaan konsumen di seluruh dunia, yang berarti solusi teknologi apa pun harus kuat dan scalable. Bekerja di lingkungan ini akan mendorong saya untuk mengembangkan keterampilan saya dalam banyak hal. Menjadi bagian dari perusahaan yang secara aktif berupaya mentransformasi industrinya sejalan dengan minat saya dalam menciptakan dampak yang berarti melalui data dan inovasi yang tentu saja sejalan dengan keahlian saya""",
    
    
    "transkrip_pertanyaan_3": """"Selama perkuliahan saya punya ketertarikan yang besar pada analisis dan bersosialisasi dengan banyak orang. Ketertarikan itu yang mendorong saya untuk aktif sebagai asisten dosen maupun di kepanitian sebagai coordinator divisi acara. Sebelumnya saya juga pernah menjalani internship sebagai Business Analyst di Samator Group di mana saya terlibat dalam implementasi ERP, pemetaan dan validasi data aset.
Sebagai asisten dosen, saya membantu mengajar praktikum mata kuliah Algoritma dan Pemrograman atau dasar coding untuk mahasiswa baru, serta Desain dan Analisis Algoritma dan Struktur Data untuk mahasiswa semester tiga. Bagi saya, mengajar bukan sekadar membantu secara langsung, tapi lebih ke bagaimana saya bisa menyampaikan materi dan menciptakan suasana yang membuat mahasiswa lebih mudah memahami konsep pemrograman itu sendiri. 
Di kepanitiaan, khususnya sebagai koordinator divisi acara, saya belajar menganalisis kebutuhan peserta, mengatur alur acara, dan mengkoordinasikan tim agar setiap kegiatan berjalan efektif. Dari pengalaman-pengalaman ini saya terbiasa bekerja secara sistematis, berinteraksi dan berkoordinasi dengan banyak orang.""",

    "transkrip_pertanyaan_4": """Menurut saya, Bapak/Ibu dapat menerima saya karena saya membawa kombinasi yang seimbang antara kemampuan analitis, komunikasi, dan adaptasi. Latar belakang saya di Data Science and Analytics membuat saya terbiasa memecahkan masalah secara terstruktur dan berbasis data. Di sisi lain, pengalaman saya sebagai asisten dosen dan asisten laboratorium melatih saya menjelaskan hal teknis dengan jelas, bekerja rapi, dan bertanggung jawab dalam menjaga kelancaran operasional. Selain itu, saya cepat belajar dan nyaman bekerja dengan banyak orang serta lintas tim, sehingga saya siap berkontribusi dan berkembang bersama perusahaan.""",

    # Data Transkrip Akademik
    "transkrip_nrp": "c14220322",
    "transkrip_prodi": "INFORMATIKA",
    "transkrip_ipk": 3.78,
    "transkrip_total_sks": 130,
    "transkrip_total_mk": 44,
    "transkrip_courses": [
     {
      "Kode": "DU4122",
      "Mata_Kuliah": "BAHASA INDONESIA",
      "Semester": "1-22/23",
      "SKS": 2,
      "Nilai": "B+"
    },
    {
      "Kode": "DU4197",
      "Mata_Kuliah": "AGAMA DAN HIDUP BERMAKNA",
      "Semester": "1-22/23",
      "SKS": 4,
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
      "Kode": "FD4505",
      "Mata_Kuliah": "KALKULUS I",
      "Semester": "1-22/23",
      "SKS": 3,
      "Nilai": "B"
    },
    {
      "Kode": "TF4205",
      "Mata_Kuliah": "DASAR SISTEM KOMPUTER",
      "Semester": "1-22/23",
      "SKS": 2,
      "Nilai": "B"
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
      "Nilai": "B+"
    },
    {
      "Kode": "DU4101",
      "Mata_Kuliah": "PANCASILA",
      "Semester": "2-22/23",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "TF4253",
      "Mata_Kuliah": "JARINGAN KOMPUTER",
      "Semester": "2-22/23",
      "SKS": 3,
      "Nilai": "B"
    },
    {
      "Kode": "TF4227",
      "Mata_Kuliah": "STATISTIKA DASAR",
      "Semester": "2-22/23",
      "SKS": 3,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4267",
      "Mata_Kuliah": "KOMUNIKASI INTERPERSONAL",
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
      "Kode": "TF4245",
      "Mata_Kuliah": "MATEMATIKA DISKRIT",
      "Semester": "2-22/23",
      "SKS": 3,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4229",
      "Mata_Kuliah": "BASIS DATA",
      "Semester": "2-22/23",
      "SKS": 3,
      "Nilai": "A"
    },
    {
      "Kode": "TF4219",
      "Mata_Kuliah": "STRUKTUR DATA",
      "Semester": "1-23/24",
      "SKS": 3,
      "Nilai": "B+"
    },
    {
      "Kode": "DU4164",
      "Mata_Kuliah": "PENDIDIKAN KEWARGANEGARAAN",
      "Semester": "1-23/24",
      "SKS": 2,
      "Nilai": "A"
    },
    {
      "Kode": "TF4243",
      "Mata_Kuliah": "SISTEM OPERASI",
      "Semester": "1-23/24",
      "SKS": 3,
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
      "Kode": "TF4255",
      "Mata_Kuliah": "REKAYASA PERANGKAT LUNAK",
      "Semester": "1-23/24",
      "SKS": 3,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4270",
      "Mata_Kuliah": "DESAIN DAN ANALISIS ALGORITMA",
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
      "Kode": "DU4163",
      "Mata_Kuliah": "ETIKA PROFESI",
      "Semester": "2-23/24",
      "SKS": 2,
      "Nilai": "B+"
    },
    {
      "Kode": "TF4551",
      "Mata_Kuliah": "APPLIED STATISTICS",
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
      "Nilai": "A"
    },
    {
      "Kode": "TF4544",
      "Mata_Kuliah": "CYBER OPERATIONS",
      "Semester": "2-23/24",
      "SKS": 3,
      "Nilai": "B+"
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
      "Nilai": "A"
    },
    {
      "Kode": "TF4548",
      "Mata_Kuliah": "BUSINESS INTELLIGENCE",
      "Semester": "1-24/25",
      "SKS": 3,
      "Nilai": "A"
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
      "A": 28,
      "B+": 11,
      "B": 5,
      "C+": 0,
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
      "Jabatan": "Pengisi Acara",
      "Nama_Kegiatan": "KONSER MAGNIFICAT 3 DESEMBER 2022",
      "Nilai_SKKK": 4.2,
      "Periode": "221",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 4,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "KULIAH UMUM - CYBER SECURITY AWARENESS, JUMAT - 25 NOVEMBER 2022",
      "Nilai_SKKK": 1.5,
      "Periode": "221",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 5,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "KULIAH UMUM - WEBINAR \"AUTOMATION AND IT MODERNIZATION\", JUMAT - 14 OKT 2022",
      "Nilai_SKKK": 1.5,
      "Periode": "221",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 6,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "WORKSHOP GETTING FAMILIAR WITH DJANGO 2022",
      "Nilai_SKKK": 2.3,
      "Periode": "221",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 7,
      "Jabatan": "Pengisi Acara",
      "Nama_Kegiatan": "CONCERT CHARITY PART OF YOU 2023",
      "Nilai_SKKK": 8.4,
      "Periode": "222",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 8,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "DATA SCIENCE: THE KEY TO UNLOCKING YOUR CAREER POTENTIAL WEBINAR",
      "Nilai_SKKK": 7.5,
      "Periode": "222",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 9,
      "Jabatan": "Peserta UKM",
      "Nama_Kegiatan": "KEGIATAN KLUB ORKESTRA 2022-2023",
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
      "Jabatan": "Pengisi Acara/Pengmas 5Aspek",
      "Nama_Kegiatan": "PENGISI ACARA DIES NATALIS INFORMATIKA 25 MEI 2023",
      "Nilai_SKKK": 2.1,
      "Periode": "222",
      "Bidang": "Partisipasi/Prestasi"
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
      "Jabatan": "Anggota HIMA - Anggota Divisi Acara",
      "Nama_Kegiatan": "WELCOME, GRATEFUL GENERATION 2023",
      "Nilai_SKKK": 9.9,
      "Periode": "222",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 14,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "ACCOUNTING TALK",
      "Nilai_SKKK": 7.5,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 15,
      "Jabatan": "Harapan 1",
      "Nama_Kegiatan": "DIES NATALIS AMN SURABAYA KE-1",
      "Nilai_SKKK": 6,
      "Periode": "231",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 16,
      "Jabatan": "Anggota HIMA - Acara",
      "Nama_Kegiatan": "IRGL 2023 - SABTU, 21 OKTOBER 2023",
      "Nilai_SKKK": 9.9,
      "Periode": "231",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 17,
      "Jabatan": "Harapan 1",
      "Nama_Kegiatan": "LOMBA KARYA TULIS ILMIAH NASIONAL",
      "Nilai_SKKK": 6,
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
      "Nama_Kegiatan": "SL - KOMAL (A,B,C,D) - GENAP 22/23 (6/2/23 - 30/6/23)",
      "Nilai_SKKK": 2,
      "Periode": "231",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 20,
      "Jabatan": "Anggota HIMA - Acara",
      "Nama_Kegiatan": "SOSIALISASI KESEKRETARIATAN DAN KEBENDAHARAAN 2023/2024",
      "Nilai_SKKK": 6.6,
      "Periode": "231",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 21,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "ADVANCEMENTS IN AI TEXT2SQL RAG AND VECTOR DATABASES",
      "Nilai_SKKK": 7.5,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 22,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "BOOTCAMP PCU CHOIR AND ORCHESTRA 2024",
      "Nilai_SKKK": 1.5,
      "Periode": "232",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 23,
      "Jabatan": "Pengisi Acara/Pengmas 5Aspek",
      "Nama_Kegiatan": "DIES NATALIS INFORMATIKA KE-26",
      "Nilai_SKKK": 2.1,
      "Periode": "232",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 24,
      "Jabatan": "Anggota HIMA - Acara",
      "Nama_Kegiatan": "DYNAMIC CAREER CHANGES IN THE AGE OF DIGITAL TRANSFORMATION 2024",
      "Nilai_SKKK": 8.3,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 25,
      "Jabatan": "Pengisi Acara/Pengmas 5Aspek",
      "Nama_Kegiatan": "KONSER GABUNGAN PETRA YOUTH ORCHESTRA",
      "Nilai_SKKK": 5.3,
      "Periode": "232",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 26,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "OPENING WGG 2024 (ORKESTRA)",
      "Nilai_SKKK": 3,
      "Periode": "232",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 27,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "ORCHESTRA NATAL HE IS COMING",
      "Nilai_SKKK": 3,
      "Periode": "232",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 28,
      "Jabatan": "Pengisi Acara/Pengmas 5Aspek",
      "Nama_Kegiatan": "PASKAH UNIVERSITAS 2024",
      "Nilai_SKKK": 4.2,
      "Periode": "232",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 29,
      "Jabatan": "Anggota",
      "Nama_Kegiatan": "PELATIHAN MICROSOFT OFFICE, GOOGLE DOCS DAN CANVA UNTUK SISWA SD KRISTEN YBPK SURABAYA",
      "Nilai_SKKK": 1,
      "Periode": "232",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 30,
      "Jabatan": "Anggota HIMA - Acara",
      "Nama_Kegiatan": "PENGABDIAN MASYARAKAT \"SCRATCH THE COMMANDER\" 2024",
      "Nilai_SKKK": 1,
      "Periode": "232",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 31,
      "Jabatan": "Sekretaris/Bendahara UKM",
      "Nama_Kegiatan": "PENGURUS ORCHESTRA 23/24",
      "Nilai_SKKK": 20,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 32,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "PPM : PELATIHAN MICROSOFT OFFICE, GOOGLE DOCS DAN CANVA, 2 FEBRUARI - 7 JUNI 2024,GENAP",
      "Nilai_SKKK": 0.75,
      "Periode": "232",
      "Bidang": "Pengabdian Masyarakat"
    },
    {
      "No": 33,
      "Jabatan": "Pengisi Acara/Pengmas 5Aspek",
      "Nama_Kegiatan": "PRE COMPETITION SICF 2024 (PENGISI)",
      "Nilai_SKKK": 4.2,
      "Periode": "232",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 34,
      "Jabatan": "Anggota",
      "Nama_Kegiatan": "SERVANT LEADERSHIP TRAINING 2024",
      "Nilai_SKKK": 6.6,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 35,
      "Jabatan": "Anggota HIMA - Acara",
      "Nama_Kegiatan": "TALKSHOW FROM CAMPUS TO CAREER 2024",
      "Nilai_SKKK": 3.3,
      "Periode": "232",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 36,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "TALKSHOW INNOVATE, INVEST, INSPIRE 2024",
      "Nilai_SKKK": 4.5,
      "Periode": "232",
      "Bidang": "Pembelajaran"
    },
    {
      "No": 37,
      "Jabatan": "Anggota HIMA - Coach",
      "Nama_Kegiatan": "INFORMATICS COMMITTEE CLUB 2024",
      "Nilai_SKKK": 3.3,
      "Periode": "241",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 38,
      "Jabatan": "Koordinator/Anggota BKU/BPMF - Divisi Acara",
      "Nama_Kegiatan": "WELCOME GRATEFUL GENERATION PROGRAM STUDI INFORMATIKA 2024",
      "Nilai_SKKK": 3.9,
      "Periode": "241",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 39,
      "Jabatan": "Pengisi Acara/Pengmas 5Aspek",
      "Nama_Kegiatan": "WELCOME, GRATEFUL GENERATION 2024",
      "Nilai_SKKK": 4.2,
      "Periode": "241",
      "Bidang": "Partisipasi/Prestasi"
    },
    {
      "No": 40,
      "Jabatan": "Koordinator/Anggota BKU/BPMF - Koord.Divisi Acara",
      "Nama_Kegiatan": "INFORMATICS RALLY GAMES AND LOGIC 2024",
      "Nilai_SKKK": 15.6,
      "Periode": "242",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 41,
      "Jabatan": "Koordinator/Anggota BKU/BPMF - Acara (Wakil)",
      "Nama_Kegiatan": "PETRA PARADE 2025",
      "Nilai_SKKK": 11.7,
      "Periode": "242",
      "Bidang": "Organisasi & Kepemimpinan"
    },
    {
      "No": 42,
      "Jabatan": "Wakil Mahasiswa - Peserta/Pendengar",
      "Nama_Kegiatan": "KEJAR MIMPI WEALTH FEST",
      "Nilai_SKKK": 6,
      "Periode": "251",
      "Bidang": "Pembelajaran"
    }
  ],
  "skkk_total_activities": 42,
  "skkk_success": True,


    # Analisis Video +
    "analisis_video": {
      "analisis_pertanyaan_1": "analisis: Subjek menunjukkan pemahaman yang solid dengan struktur jawaban yang jelas. Kontak mata terjaga baik dan bahasa tubuh menunjukkan keyakinan. kesimpulan: 87",
    "analisis_pertanyaan_2": "analisis: Penjelasan disampaikan dengan artikulasi yang baik dan tempo yang stabil. Mampu memberikan contoh konkret untuk mendukung argumen utama. kesimpulan: 84",
    "analisis_pertanyaan_3": "analisis: Subjek responsif terhadap pertanyaan lanjutan dan mampu mengelaborasi poin-poin penting dengan detail yang memadai. kesimpulan: 88",
    "analisis_pertanyaan_4": "analisis: Jawaban komprehensif dengan insight yang menunjukkan pemahaman mendalam. Ekspresi wajah menunjukkan antusiasme terhadap topik. kesimpulan: 85"
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
