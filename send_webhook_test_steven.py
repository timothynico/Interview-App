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
    "nama": "Steven Harsono",
    "email": "c14220053@john.petra.ac.id",
    "posisi_dilamar": "Backend Developer",

    # CV Text
    "cv_text": """ABOUT ME
I am a 3rd-year Informatics student at Petra Christian
University, specializing in Full Stack Development. I possess
strong communication and collaboration skills, enabling
effective teamwork and problem-solving. I am passionate
about developing websites and applications that provide
practical solutions and improve the user experience.

EXPERIENCE

082233557768
stevenharsono02@gmail.com
Surabaya, 02 May 2005
Bukit Darmo Golf Regency C-5 Surabaya

EDUCATION
Petra Christian University,
Major in Informatics - Full
Stack Development
3.60 GPA
The Top 10%
Freshman of 2022
With Outstanding
Academic
Achievement
2022 - 2026

Petra Christian 1 Senior
High School
2019 - 2022
SKILLS

CERTIFICATE
Programming
Python
Java
C++
Web Development
HTML
CSS
Java Script
Android Development
Kotlin
Microsoft Office
Microsoft Excel
Canva
Problem Solving
Team Collaboration
Communication

Java Programming 1
MOOC.FI

Petra Christian University Student Ministry August 2023
University Service Coordination: Assisted in organizing the weekly
university services, ensuring smooth operations and active
participation from students.
Student Ministry Fellowship: Assisted in coordinating weekly
fellowship meetings, fostering community and spiritual growth.
Bible Study Group Coordination: Managed the grouping of
students for Bible study sessions, facilitating meaningful
discussions and spiritual guidance.
Member

PROJECTS
Youth Church Community August 2024 - Present

In this project, we focused on developing the front-end for two
key components of a website: the Login page and the Profile page.
Develop a responsive and secure login page.
User Interface (UI) Design: created a clean and simple layout to
provide an intuitive experience using PHP, HTML, Tailwind, CSS,
and JavaScript.
Maintain responsive and accessible design.
Website Development

Academic Information System
University Website Development
In this project, we focused on developing the front-end for an
academic information system for a university, ensuring it was
user-friendly and accessible to a diverse range of users.
User Experience (UX) and Accessibility
User-Friendly Design: Developed an intuitive interface with
clear navigation to ensure all users, regardless of
background, could easily access academic information.
Accessibility Features: Implemented accessibility
standards, ensuring compatibility with screen readers and
providing high-contrast modes for visually impaired users.
April - June 2024

Computer Graphics Project
Website Development with 3D Objects

February- June 2024

3D Object Development
Basic 3D Object Creation: Used WebGL to build basic 3D
objects such as cubes, spheres, and other primitives.
Mesh Manipulation: Implemented transformations (scaling,
rotation, translation) to create dynamic movement and
realistic object behavior.
Three.js Implementation
Scene Management: Utilized Three.js to manage the
rendering of 3D scenes, optimizing object loading, material
management, and textures.
Lighting and Shadows: Applied various lighting techniques,
including point lights and ambient lighting, to create
realistic shadows and enhance the visual quality of the
scene.
Camera Configuration
Cinematographic Effects: Configured camera settings such
as field of view, depth of field, and perspective to create
immersive, cinematic visuals within the 3D environment
.

Wedding Invitation Website
Website for Wedding Invitation with Animations
In this project, we developed the back-end for an admin page and
utilized cloud hosting services to manage the project.
Back-End Development
Admin Page Functionality: Developed a back-end using
PHP and JQuery to enable administrators to manage guest
lists, invitations, and event details.
Dynamic Data Handling: Implemented real-time updates
and AJAX requests to improve the responsiveness and
interactivity of the admin interface.
Cloud Hosting with AWS
AWS Academy: Utilized AWS Academy for project hosting,
ensuring scalability, security, and high availability.
Deployment & Maintenance: Managed deployment
processes, optimized server configurations, and ensured
seamless updates for a reliable user experience.

November - December 2023

Game Development with Java OOP
Encapsulation: Organized game logic by encapsulating data
and behavior within well-defined classes, ensuring
modularity and data security.
Abstraction: Designed abstract classes and interfaces to
manage game entities like players, enemies, and items,
making the codebase easier to extend and maintain.
Inheritance: Applied inheritance to create specialized game
objects from base classes, minimizing redundancy and
improving code reuse.
Polymorphism: Implemented polymorphism to handle
different types of game objects and behaviors dynamically,
enhancing flexibility and reducing complexity.
Build Automation with Gradle
Gradle Integration: Utilized Gradle for project build
automation, managing dependencies and ensuring smooth
compilation and deployment processes.""",

    # Transkrip Jawaban Interview
    "transkrip_pertanyaan_1": """perkenalkan saya Steven Harsono.
Saya adalah mahasiswa Informatika tahun ketiga di Universitas Kristen Petra, dengan konsentrasi Full Stack Development. Saya memiliki minat kuat dalam pengembangan website dan aplikasi yang berfokus pada solusi praktis serta peningkatan user experience.
Selama perkuliahan, saya telah mengerjakan berbagai proyek pengembangan sistem, mulai dari website akademik universitas, website undangan pernikahan berbasis cloud (AWS), hingga pengembangan game menggunakan Java OOP dan grafik 3D menggunakan WebGL dan Three.js. Dari proyek-proyek tersebut, saya terbiasa bekerja dengan teknologi seperti HTML, CSS, JavaScript, PHP, Java, Python, Kotlin, serta memahami konsep UI/UX, back-end, dan deployment.
Selain kemampuan teknis, saya juga memiliki kemampuan komunikasi, kerja tim, dan problem solving yang baik, yang saya kembangkan melalui pengalaman organisasi dan pelayanan kampus. Saya terbiasa bekerja secara kolaboratif dan cepat beradaptasi dengan lingkungan kerja baru, serta memiliki motivasi tinggi untuk terus belajar dan berkembang di bidang teknologi informasi. """,


    "transkrip_pertanyaan_2": """Saya tertarik melamar di PT XYZ karena perusahaan ini dikenal sebagai perusahaan yang terus berkembang dan adaptif terhadap teknologi, serta memiliki komitmen untuk menghadirkan solusi yang berdampak nyata bagi bisnis dan pengguna. Nilai tersebut sejalan dengan minat saya sebagai mahasiswa Informatika yang fokus pada pengembangan aplikasi yang tidak hanya berjalan secara teknis, tetapi juga memberikan nilai guna dan pengalaman pengguna yang baik.""",
    
    
    "transkrip_pertanyaan_3": """Saya memiliki pengalaman yang relevan sebagai Backend Developer melalui berbagai proyek akademik dan mandiri selama perkuliahan. Saya terbiasa mengembangkan logika server, mengelola data, serta memastikan aplikasi berjalan stabil dan efisien.
Salah satu pengalaman utama saya adalah mengembangkan backend untuk website undangan pernikahan, di mana saya membangun admin panel menggunakan PHP dan jQuery untuk mengelola data tamu, undangan, dan detail acara. Pada proyek ini, saya menangani pengolahan data secara dinamis, implementasi AJAX, serta memastikan sinkronisasi data berjalan dengan baik. Proyek tersebut juga saya deploy menggunakan AWS, sehingga saya mendapatkan pengalaman langsung terkait deployment, konfigurasi server, dan maintenance aplikasi backend.
Selain itu, saya juga memiliki pengalaman mengembangkan sistem informasi akademik universitas, di mana saya terlibat dalam perancangan alur data dan integrasi antara front-end dan back-end agar informasi akademik dapat diakses secara akurat dan efisien. Saya memahami pentingnya struktur data, validasi input, dan pengelolaan API untuk menjaga konsistensi dan keamanan data.""",

    "transkrip_pertanyaan_4": """Perusahaan dapat mempertimbangkan saya karena saya memiliki fondasi teknis backend yang kuat, kemauan belajar yang tinggi, dan sikap kerja yang bertanggung jawab. Saya terbiasa membangun logika backend, mengelola data, serta memastikan sistem berjalan stabil dan terstruktur melalui berbagai proyek yang telah saya kerjakan.
Sebagai mahasiswa Informatika dengan fokus Full Stack Development, saya memahami alur aplikasi secara menyeluruh, namun memiliki minat khusus di backend. Hal ini membuat saya mampu berkolaborasi dengan tim frontend, memahami kebutuhan sistem secara end-to-end, serta menghasilkan solusi backend yang efektif dan scalable.
Selain kemampuan teknis, saya memiliki komunikasi yang baik, disiplin, dan mudah beradaptasi dengan lingkungan kerja baru. Saya terbiasa menerima feedback, cepat belajar teknologi baru, dan memiliki komitmen untuk memberikan hasil kerja yang berkualitas. Saya percaya dengan kombinasi tersebut, saya dapat memberikan kontribusi nyata sekaligus berkembang bersama PT XYZ dalam jangka panjang.""",

    # Data Transkrip Akademik
    "transkrip_nrp": "C14220053",
    "transkrip_prodi": "INFORMATIKA",
    "transkrip_ipk": 3.70,
    "transkrip_total_sks": 130,
    "transkrip_total_mk": 40,
    "transkrip_courses": [
        # /* ===================== */
        # /* SEMESTER 1-22/23     */
        # /* ===================== */
        {"Kode":"DU4197","Mata_Kuliah":"Agama dan Hidup Bermakna","Semester":"1-22/23","SKS":4,"Nilai":"B+"},
        {"Kode":"DU4122","Mata_Kuliah":"Bahasa Indonesia","Semester":"1-22/23","SKS":2,"Nilai":"A"},
        {"Kode":"TF4205","Mata_Kuliah":"Dasar Sistem Komputer","Semester":"1-22/23","SKS":2,"Nilai":"B+"},
        {"Kode":"FD4505","Mata_Kuliah":"Kalkulus I","Semester":"1-22/23","SKS":3,"Nilai":"C+"},
        {"Kode":"TF4537","Mata_Kuliah":"Konsep Algoritma","Semester":"1-22/23","SKS":3,"Nilai":"A"},
        {"Kode":"TF4536","Mata_Kuliah":"Dasar Pemrograman","Semester":"1-22/23","SKS":4,"Nilai":"A"},
        {"Kode":"TF4220","Mata_Kuliah":"Pengantar Manajemen dan Bisnis","Semester":"1-22/23","SKS":2,"Nilai":"A"},

        # /* ===================== */
        # /* SEMESTER 2-22/23     */
        # /* ===================== */
        {"Kode":"DU4101","Mata_Kuliah":"Pancasila","Semester":"2-22/23","SKS":2,"Nilai":"A"},
        {"Kode":"TF4227","Mata_Kuliah":"Statistika Dasar","Semester":"2-22/23","SKS":3,"Nilai":"A"},
        {"Kode":"TF4267","Mata_Kuliah":"Komunikasi Interpersonal","Semester":"2-22/23","SKS":3,"Nilai":"B+"},
        {"Kode":"TF4245","Mata_Kuliah":"Matematika Diskrit","Semester":"2-22/23","SKS":3,"Nilai":"B+"},
        {"Kode":"TF4235","Mata_Kuliah":"Pemrograman Berorientasi Objek","Semester":"2-22/23","SKS":3,"Nilai":"A"},
        {"Kode":"TF4253","Mata_Kuliah":"Jaringan Komputer","Semester":"2-22/23","SKS":3,"Nilai":"A"},
        {"Kode":"TF4229","Mata_Kuliah":"Basis Data","Semester":"2-22/23","SKS":3,"Nilai":"B+"},

        # /* ===================== */
        # /* SEMESTER 1-23/24     */
        # /* ===================== */
        {"Kode":"TF4249","Mata_Kuliah":"Pengantar Akuntansi","Semester":"1-23/24","SKS":2,"Nilai":"B+"},
        {"Kode":"TF4255","Mata_Kuliah":"Rekayasa Perangkat Lunak","Semester":"1-23/24","SKS":3,"Nilai":"B+"},
        {"Kode":"FD4507","Mata_Kuliah":"Aljabar Linier","Semester":"1-23/24","SKS":3,"Nilai":"B+"},
        {"Kode":"TF4270","Mata_Kuliah":"Desain dan Analisis Algoritma","Semester":"1-23/24","SKS":3,"Nilai":"B"},
        {"Kode":"TF4372","Mata_Kuliah":"Arsitektur dan Organisasi Komputer","Semester":"1-23/24","SKS":3,"Nilai":"B"},
        {"Kode":"TF4219","Mata_Kuliah":"Struktur Data","Semester":"1-23/24","SKS":3,"Nilai":"B+"},
        {"Kode":"DU4164","Mata_Kuliah":"Pendidikan Kewarganegaraan","Semester":"1-23/24","SKS":2,"Nilai":"A"},
        {"Kode":"TF4343","Mata_Kuliah":"Teknologi Web","Semester":"1-23/24","SKS":3,"Nilai":"A"},

        # /* ===================== */
        # /* SEMESTER 2-23/24     */
        # /* ===================== */
        {"Kode":"DU4198","Mata_Kuliah":"Digital Leadership","Semester":"2-23/24","SKS":2,"Nilai":"A"},
        {"Kode":"TF4327","Mata_Kuliah":"Analisis dan Desain Sistem Informasi","Semester":"2-23/24","SKS":3,"Nilai":"B"},
        {"Kode":"TF4504","Mata_Kuliah":"Bahasa Inggris","Semester":"2-23/24","SKS":2,"Nilai":"A"},
        {"Kode":"TF4544","Mata_Kuliah":"Cyber Operations","Semester":"2-23/24","SKS":3,"Nilai":"B+"},
        {"Kode":"TF4415","Mata_Kuliah":"Grafika Komputer","Semester":"2-23/24","SKS":3,"Nilai":"A"},
        {"Kode":"TF4243","Mata_Kuliah":"Sistem Operasi","Semester":"2-23/24","SKS":3,"Nilai":"B+"},
        {"Kode":"TF4247","Mata_Kuliah":"Metode Numerik","Semester":"2-23/24","SKS":2,"Nilai":"B"},
        {"Kode":"TF4409","Mata_Kuliah":"Kecerdasan Buatan","Semester":"2-23/24","SKS":3,"Nilai":"B+"},
        {"Kode":"TF4237","Mata_Kuliah":"Interaksi Manusia dan Komputer","Semester":"2-23/24","SKS":3,"Nilai":"B+"},

        # /* ===================== */
        # /* SEMESTER 1-24/25     */
        # /* ===================== */
        {"Kode":"FD4508","Mata_Kuliah":"Technopreneurship","Semester":"1-24/25","SKS":3,"Nilai":"A"},
        {"Kode":"TF4579","Mata_Kuliah":"Web Frameworks and Deployment","Semester":"1-24/25","SKS":3,"Nilai":"A"},
        {"Kode":"TF4509","Mata_Kuliah":"Cloud Computing","Semester":"1-24/25","SKS":3,"Nilai":"A"},
        {"Kode":"TF4507","Mata_Kuliah":"Sistem Terdistribusi","Semester":"1-24/25","SKS":3,"Nilai":"A"},
        {"Kode":"TF4317","Mata_Kuliah":"Manajemen Proyek Teknologi Informasi","Semester":"1-24/25","SKS":3,"Nilai":"A"},
        {"Kode":"TF4516","Mata_Kuliah":"Pengembangan Aplikasi Android","Semester":"1-24/25","SKS":3,"Nilai":"A"},
        {"Kode":"TF4587","Mata_Kuliah":"Software Testing and Quality Assurance","Semester":"1-24/25","SKS":3,"Nilai":"B+"},
        {"Kode":"TF4569","Mata_Kuliah":"Network Defense","Semester":"1-24/25","SKS":3,"Nilai":"B+"},

        # /* ===================== */
        # /* SEMESTER 2-24/25     */
        # /* ===================== */
        {"Kode":"TF4374","Mata_Kuliah":"Teknologi Open Source","Semester":"2-24/25","SKS":3,"Nilai":"A"},
        {"Kode":"TF4259","Mata_Kuliah":"Metodologi Penelitian","Semester":"2-24/25","SKS":3,"Nilai":"B+"},
        {"Kode":"TF4540","Mata_Kuliah":"Industrial Training","Semester":"2-24/25","SKS":6,"Nilai":"A"},
        {"Kode":"TF4261","Mata_Kuliah":"Kerja Praktek","Semester":"2-24/25","SKS":2,"Nilai":"A"},
        {"Kode":"TF4539","Mata_Kuliah":"Professional Development","Semester":"2-24/25","SKS":6,"Nilai":"A"}
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
        "analisis_pertanyaan_1": "analisis: Subjek menunjukkan ketenangan yang luar biasa dengan intonasi suara yang stabil. Kontak mata terjaga dengan baik sepanjang sesi. kesimpulan: 85",
        
        "analisis_pertanyaan_2": "analisis: Subjek menjawab dengan antusias dan menggunakan gestur tangan untuk memperjelas poin. Ekspresi wajah sangat positif. kesimpulan: 90",
        
        "analisis_pertanyaan_3": "analisis: Subjek tampak fokus meskipun ada sedikit keraguan saat menjelaskan istilah teknis. Namun, postur tetap profesional. kesimpulan: 78",
        
        "analisis_pertanyaan_4": "analisis: Subjek memberikan jawaban yang ringkas namun padat. Meskipun terlihat agak kaku, pesan tersampaikan dengan sangat jelas. kesimpulan: 70"
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
