import PyPDF2
import re
import pandas as pd
from typing import List, Dict

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Ekstrak teks dari file PDF
    """
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def parse_student_info(text: str) -> Dict[str, str]:
    """
    Ekstrak informasi mahasiswa dari transkrip
    """
    info = {}
    
    # Ekstrak nama - lebih fleksibel
    nama_match = re.search(r'Nama\s*:([A-Z\s]+?)(?:Fakultas|NRP)', text)
    if nama_match:
        info['Nama'] = nama_match.group(1).strip()
    
    # Ekstrak NRP
    nrp_match = re.search(r'NRP\s*:([A-Z0-9]+)', text)
    if nrp_match:
        info['NRP'] = nrp_match.group(1).strip()
    
    # Ekstrak Tempat/Tanggal Lahir
    ttl_match = re.search(r'Tempat/Tgl\.Lahir:\s*([A-Z\s]+,\s*\d{2}/\d{2}/\d{4})', text)
    if ttl_match:
        info['Tempat_Tgl_Lahir'] = ttl_match.group(1).strip()
    
    # Ekstrak Fakultas
    fakultas_match = re.search(r'Fakultas\s*:([A-Z\s]+?)(?:NRP|Program)', text)
    if fakultas_match:
        info['Fakultas'] = fakultas_match.group(1).strip()
    
    # Ekstrak Program Studi
    prodi_match = re.search(r'Program Studi\s*:([A-Z\s]+?)(?:Tempat|Program)', text)
    if prodi_match:
        info['Program_Studi'] = prodi_match.group(1).strip()
    
    # Ekstrak Program
    program_match = re.search(r'Program:\s*([A-Z\s]+?)(?:Tahun|Program Pendidikan)', text)
    if program_match:
        info['Program'] = program_match.group(1).strip()
    
    # Ekstrak IPK
    ipk_match = re.search(r'Indeks Prestasi Kumulatif\s*:\s*([0-9.]+)', text)
    if ipk_match:
        info['IPK'] = float(ipk_match.group(1))
    
    # Ekstrak Total SKS
    sks_match = re.search(r'Jumlah SKS\s*:\s*([0-9]+)\s*SKS', text)
    if sks_match:
        info['Total_SKS'] = int(sks_match.group(1))
    
    # Ekstrak Tahun Masuk
    tahun_match = re.search(r'Tahun Masuk\s*:\s*(\d-\d{4}/\d{4})', text)
    if tahun_match:
        info['Tahun_Masuk'] = tahun_match.group(1).strip()
    
    # Ekstrak Program Pendidikan
    prog_pend_match = re.search(r'Program Pendidikan:\s*([A-Z0-9]+)', text)
    if prog_pend_match:
        info['Program_Pendidikan'] = prog_pend_match.group(1).strip()
    
    return info

def parse_courses(text: str) -> List[Dict[str, str]]:
    """
    Ekstrak data mata kuliah dari transkrip
    Menggunakan approach split per entry berdasarkan kode MK
    """
    courses = []
    seen_courses = set()

    # Cari semua kemunculan kode mata kuliah dan posisinya
    # Pattern: kode (2 huruf + 4 angka) diikuti oleh huruf kapital atau spasi
    pattern_kode = r'([A-Z]{2}\d{4})(?=[A-Z\s])'

    # Split text berdasarkan posisi kode mata kuliah
    matches = list(re.finditer(pattern_kode, text))

    for i, match in enumerate(matches):
        kode = match.group(1)

        # Ambil text mulai dari kode ini sampai kode berikutnya (atau akhir text)
        start_pos = match.end()
        if i < len(matches) - 1:
            end_pos = matches[i + 1].start()
        else:
            end_pos = len(text)

        fragment = text[start_pos:end_pos]

        # Bersihkan fragment: hilangkan newline jadi spasi
        fragment_clean = re.sub(r'\s+', ' ', fragment).strip()

        # Skip jika fragment terlalu pendek (kemungkinan noise)
        if len(fragment_clean) < 10:
            continue

        # Cari semester, SKS, dan nilai di dalam fragment
        # Pattern: SEMESTER SKS NILAI (dengan atau tanpa spasi)
        pattern_data = r'(\d-\d{2}/\d{2})\s*(\d+)\s*([A-E]\+?)'
        data_match = re.search(pattern_data, fragment_clean)

        if not data_match:
            continue

        semester = data_match.group(1)
        sks = int(data_match.group(2))
        nilai = data_match.group(3)

        # Nama mata kuliah adalah text sebelum semester
        nama_end_pos = data_match.start()
        mata_kuliah = fragment_clean[:nama_end_pos].strip()

        # Bersihkan nama mata kuliah
        # Hilangkan multiple spaces
        mata_kuliah = re.sub(r'\s+', ' ', mata_kuliah)
        # Hilangkan trailing slash
        mata_kuliah = re.sub(r'\s*/\s*$', '', mata_kuliah).strip()

        # Filter noise
        if (len(mata_kuliah) < 5 or
            'Kode' in mata_kuliah or
            'Mata Kuliah' in mata_kuliah or
            'SMT' in mata_kuliah):
            continue

        # Cek duplikat
        course_id = f"{kode}-{semester}"
        if course_id in seen_courses:
            continue

        courses.append({
            'Kode': kode,
            'Mata_Kuliah': mata_kuliah,
            'Semester': semester,
            'SKS': sks,
            'Nilai': nilai
        })
        seen_courses.add(course_id)

    return courses

def calculate_grade_point(grade: str) -> float:
    """
    Konversi nilai huruf ke bobot nilai
    """
    grade_mapping = {
        'A': 4.00,
        'B+': 3.50,
        'B': 3.00,
        'C+': 2.50,
        'C': 2.00,
        'D': 1.00,
        'E': 0.00
    }
    return grade_mapping.get(grade, 0.0)

def get_grade_description(grade: str) -> str:
    """
    Mendapatkan deskripsi nilai
    """
    descriptions = {
        'A': 'Istimewa',
        'B+': 'Baik Sekali',
        'B': 'Baik',
        'C+': 'Cukup Baik',
        'C': 'Cukup',
        'D': 'Kurang',
        'E': 'Sangat Kurang'
    }
    return descriptions.get(grade, '')

def analyze_transcript(courses: List[Dict[str, str]]) -> Dict:
    """
    Analisis data transkrip
    """
    analysis = {
        'total_courses': len(courses),
        'grade_distribution': {},
        'semester_summary': {},
        'total_sks': 0,
        'weighted_sum': 0.0,
        'year_summary': {}
    }
    
    # Hitung distribusi nilai
    for course in courses:
        grade = course['Nilai']
        analysis['grade_distribution'][grade] = analysis['grade_distribution'].get(grade, 0) + 1
        
        # Hitung total SKS dan weighted sum untuk verifikasi IPK
        sks = course['SKS']
        grade_point = calculate_grade_point(grade)
        analysis['total_sks'] += sks
        analysis['weighted_sum'] += sks * grade_point
        
        # Summary per semester
        semester = course['Semester']
        if semester not in analysis['semester_summary']:
            analysis['semester_summary'][semester] = {
                'courses': 0,
                'total_sks': 0,
                'weighted_sum': 0.0,
                'course_list': []
            }
        
        analysis['semester_summary'][semester]['courses'] += 1
        analysis['semester_summary'][semester]['total_sks'] += sks
        analysis['semester_summary'][semester]['weighted_sum'] += sks * grade_point
        analysis['semester_summary'][semester]['course_list'].append(course)
        
        # Summary per tahun akademik
        year = semester.split('-')[1]  # Ambil tahun dari semester (e.g., "22/23" dari "1-22/23")
        if year not in analysis['year_summary']:
            analysis['year_summary'][year] = {
                'courses': 0,
                'total_sks': 0,
                'weighted_sum': 0.0
            }
        
        analysis['year_summary'][year]['courses'] += 1
        analysis['year_summary'][year]['total_sks'] += sks
        analysis['year_summary'][year]['weighted_sum'] += sks * grade_point
    
    # Hitung IPK
    if analysis['total_sks'] > 0:
        analysis['calculated_ipk'] = round(analysis['weighted_sum'] / analysis['total_sks'], 2)
    
    # Hitung IPS per semester
    for semester in analysis['semester_summary']:
        sem_data = analysis['semester_summary'][semester]
        if sem_data['total_sks'] > 0:
            sem_data['ips'] = round(sem_data['weighted_sum'] / sem_data['total_sks'], 2)
    
    # Hitung IP per tahun
    for year in analysis['year_summary']:
        year_data = analysis['year_summary'][year]
        if year_data['total_sks'] > 0:
            year_data['ip'] = round(year_data['weighted_sum'] / year_data['total_sks'], 2)
    
    return analysis

def display_detailed_semester_report(analysis: Dict):
    """
    Tampilkan laporan detail per semester
    """
    print("\n" + "="*110)
    print("DETAIL MATA KULIAH PER SEMESTER")
    print("="*110)
    
    semester_order = sorted(analysis['semester_summary'].keys(), 
                           key=lambda x: (x.split('-')[1], int(x.split('-')[0])))
    
    for semester in semester_order:
        sem_data = analysis['semester_summary'][semester]
        print(f"\n{'='*110}")
        print(f"SEMESTER {semester} - {sem_data['courses']} Mata Kuliah | {sem_data['total_sks']} SKS | IPS: {sem_data['ips']}")
        print(f"{'='*110}")
        print(f"{'No':<4} {'Kode':<10} {'Mata Kuliah':<65} {'SKS':<5} {'Nilai':<7} {'Bobot':<5}")
        print(f"{'-'*110}")
        
        for idx, course in enumerate(sem_data['course_list'], 1):
            mk_name = course['Mata_Kuliah'][:62] + '...' if len(course['Mata_Kuliah']) > 65 else course['Mata_Kuliah']
            bobot = calculate_grade_point(course['Nilai'])
            print(f"{idx:<4} {course['Kode']:<10} {mk_name:<65} {course['SKS']:<5} {course['Nilai']:<7} {bobot:<5.2f}")

def display_year_summary(analysis: Dict):
    """
    Tampilkan ringkasan per tahun akademik
    """
    print("\n" + "="*110)
    print("RINGKASAN PER TAHUN AKADEMIK")
    print("="*110)
    print(f"{'Tahun':<15} {'Jumlah MK':<15} {'Total SKS':<15} {'IP':<15}")
    print("-"*110)
    
    for year in sorted(analysis['year_summary'].keys()):
        year_data = analysis['year_summary'][year]
        year_label = f"20{year.split('/')[0]}/20{year.split('/')[1]}"
        print(f"{year_label:<15} {year_data['courses']:<15} {year_data['total_sks']:<15} {year_data['ip']:<15.2f}")

def main():
    """
    Fungsi utama untuk membaca dan menganalisis transkrip
    """
    import os

    # Path untuk Windows
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(base_dir, '[SIA PETRA] Transkrip.pdf')
    output_dir = os.path.join(base_dir, 'outputs')

    # Buat folder output jika belum ada
    os.makedirs(output_dir, exist_ok=True)
    
    print("="*110)
    print(" "*30 + "SISTEM PEMBACA TRANSKRIP AKADEMIK")
    print(" "*35 + "UNIVERSITAS KRISTEN PETRA")
    print("="*110)
    
    # Ekstrak teks dari PDF
    print("\n[1/5] Membaca file PDF...")
    text = extract_text_from_pdf(pdf_path)

    # Parse informasi mahasiswa
    print("[2/5] Mengekstrak informasi mahasiswa...")
    student_info = parse_student_info(text)
    
    print("\n" + "="*110)
    print("INFORMASI MAHASISWA")
    print("="*110)
    print(f"{'Nama':<25}: {student_info.get('Nama', 'N/A')}")
    print(f"{'NRP':<25}: {student_info.get('NRP', 'N/A')}")
    print(f"{'Tempat/Tanggal Lahir':<25}: {student_info.get('Tempat_Tgl_Lahir', 'N/A')}")
    print(f"{'Fakultas':<25}: {student_info.get('Fakultas', 'N/A')}")
    print(f"{'Program Studi':<25}: {student_info.get('Program_Studi', 'N/A')}")
    print(f"{'Program':<25}: {student_info.get('Program', 'N/A')}")
    print(f"{'Program Pendidikan':<25}: {student_info.get('Program_Pendidikan', 'N/A')}")
    print(f"{'Tahun Masuk':<25}: {student_info.get('Tahun_Masuk', 'N/A')}")
    print(f"{'IPK (dari transkrip)':<25}: {student_info.get('IPK', 'N/A')}")
    print(f"{'Total SKS':<25}: {student_info.get('Total_SKS', 'N/A')}")
    
    # Parse mata kuliah
    print("\n[3/5] Mengekstrak data mata kuliah...")
    courses = parse_courses(text)

    print(f"   > Total: {len(courses)} mata kuliah berhasil diekstrak")

    if len(courses) == 0:
        print("\n[!] Tidak ada mata kuliah yang berhasil diekstrak.")
        return

    # Buat DataFrame
    df = pd.DataFrame(courses)

    # Analisis transkrip
    print("[4/5] Menganalisis transkrip...")
    analysis = analyze_transcript(courses)
    
    print("\n" + "="*110)
    print("RINGKASAN AKADEMIK")
    print("="*110)
    print(f"Total Mata Kuliah         : {analysis['total_courses']} mata kuliah")
    print(f"Total SKS Diambil         : {analysis['total_sks']} SKS")
    print(f"IPK (dari transkrip)      : {student_info.get('IPK', 'N/A')}")
    print(f"IPK (hasil perhitungan)   : {analysis['calculated_ipk']}")
    
    if student_info.get('IPK') and abs(student_info.get('IPK') - analysis['calculated_ipk']) > 0.01:
        print(f"\n[!] PERHATIAN: Ada perbedaan antara IPK transkrip ({student_info.get('IPK')}) dan hasil perhitungan ({analysis['calculated_ipk']})")
        print("   Ini mungkin karena ada mata kuliah yang tidak ter-ekstrak atau perbedaan pembulatan.")
    
    print("\n" + "-"*110)
    print("DISTRIBUSI NILAI:")
    print("-"*110)
    for grade in ['A', 'B+', 'B', 'C+', 'C', 'D', 'E']:
        count = analysis['grade_distribution'].get(grade, 0)
        if count > 0:
            percentage = (count / analysis['total_courses']) * 100
            bar = '#' * int(percentage / 2)
            desc = get_grade_description(grade)
            print(f"  {grade:<3} ({desc:<15}) : {count:>3} mata kuliah ({percentage:>5.1f}%) {bar}")
    
    # Display ringkasan per tahun
    display_year_summary(analysis)
    
    # Display detail per semester
    display_detailed_semester_report(analysis)
    
    # Simpan ke file
    print("\n" + "="*110)
    print("[5/5] Menyimpan data ke file...")

    output_csv = os.path.join(output_dir, 'transkrip_data.csv')
    df.to_csv(output_csv, index=False, encoding='utf-8-sig')
    print(f"   > Data mata kuliah: {output_csv}")
    
    # Simpan ringkasan per semester
    summary_data = []
    for semester in sorted(analysis['semester_summary'].keys(), 
                          key=lambda x: (x.split('-')[1], int(x.split('-')[0]))):
        sem_data = analysis['semester_summary'][semester]
        summary_data.append({
            'Semester': semester,
            'Jumlah_MK': sem_data['courses'],
            'Total_SKS': sem_data['total_sks'],
            'IPS': sem_data['ips']
        })
    
    summary_df = pd.DataFrame(summary_data)
    output_summary = os.path.join(output_dir, 'transkrip_ringkasan_semester.csv')
    summary_df.to_csv(output_summary, index=False, encoding='utf-8-sig')
    print(f"   > Ringkasan per semester: {output_summary}")

    # Simpan ringkasan per tahun
    year_data = []
    for year in sorted(analysis['year_summary'].keys()):
        year_info = analysis['year_summary'][year]
        year_label = f"20{year.split('/')[0]}/20{year.split('/')[1]}"
        year_data.append({
            'Tahun_Akademik': year_label,
            'Jumlah_MK': year_info['courses'],
            'Total_SKS': year_info['total_sks'],
            'IP': year_info['ip']
        })

    year_df = pd.DataFrame(year_data)
    output_year = os.path.join(output_dir, 'transkrip_ringkasan_tahun.csv')
    year_df.to_csv(output_year, index=False, encoding='utf-8-sig')
    print(f"   > Ringkasan per tahun: {output_year}")

    # Simpan info mahasiswa
    student_df = pd.DataFrame([student_info])
    output_student = os.path.join(output_dir, 'info_mahasiswa.csv')
    student_df.to_csv(output_student, index=False, encoding='utf-8-sig')
    print(f"   > Informasi mahasiswa: {output_student}")

    # Simpan Excel dengan multiple sheets
    try:
        output_excel = os.path.join(output_dir, 'transkrip_lengkap.xlsx')
        with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
            student_df.to_excel(writer, sheet_name='Info Mahasiswa', index=False)
            df.to_excel(writer, sheet_name='Mata Kuliah', index=False)
            summary_df.to_excel(writer, sheet_name='Ringkasan Semester', index=False)
            year_df.to_excel(writer, sheet_name='Ringkasan Tahun', index=False)
        print(f"   > File Excel lengkap: {output_excel}")
    except ImportError:
        print("   [!] openpyxl tidak tersedia, skip pembuatan file Excel")

    print("\n" + "="*110)
    print("PROSES SELESAI!")
    print("="*110)
    print(f"\nTotal file yang dihasilkan:")
    print(f"  - CSV data mata kuliah")
    print(f"  - CSV ringkasan per semester")
    print(f"  - CSV ringkasan per tahun")
    print(f"  - CSV informasi mahasiswa")
    print(f"  - Excel lengkap (jika tersedia)")
    
    return student_info, df, analysis

if __name__ == "__main__":
    student_info, courses_df, analysis = main()