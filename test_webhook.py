import requests
import json
from datetime import datetime

# Webhook URL (menggunakan webhook-test)
WEBHOOK_URL = "https://n8n-1.saturn.petra.ac.id/webhook-test/939b69b4-4d28-4531-b451-804809c2399c"

def test_transkrip_upload_event():
    """Test Event 1: Upload Transkrip"""
    print("="*80)
    print("TEST EVENT 1: UPLOAD TRANSKRIP & SKKK")
    print("="*80)

    payload = {
        "session_id": "test_session_001",
        "timestamp": datetime.now().isoformat(),
        "event_type": "transkrip_uploaded",

        # Data Kandidat (jika sudah upload CV)
        "nama": "John Doe Test",
        "email": "john.test@example.com",
        "posisi_dilamar": "Software Engineer",

        # Informasi Mahasiswa dari Transkrip
        "transkrip_nrp": "C14220062",
        "transkrip_nama": "JOHN DOE TEST",
        "transkrip_prodi": "INFORMATIKA",
        "transkrip_fakultas": "TEKNOLOGI INDUSTRI",
        "transkrip_ipk": 3.75,
        "transkrip_total_sks": 144,
        "transkrip_total_mk": 48,
        "transkrip_calculated_ipk": 3.75,

        # Sample Mata Kuliah
        "transkrip_courses": [
            {
                "Kode": "IF1234",
                "Mata_Kuliah": "Pemrograman Berorientasi Objek",
                "Semester": "1-22/23",
                "SKS": 3,
                "Nilai": "A"
            },
            {
                "Kode": "IF5678",
                "Mata_Kuliah": "Basis Data",
                "Semester": "2-22/23",
                "SKS": 4,
                "Nilai": "B+"
            },
            {
                "Kode": "IF9012",
                "Mata_Kuliah": "Algoritma dan Struktur Data",
                "Semester": "1-22/23",
                "SKS": 4,
                "Nilai": "A"
            }
        ],

        # Distribusi Nilai
        "transkrip_grade_distribution": {
            "A": 20,
            "B+": 15,
            "B": 10,
            "C+": 2,
            "C": 1
        },

        # Sample Data SKKK
        "skkk_data": [
            {
                "No": "1",
                "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR",
                "Nama \r\n              Kegiatan": "ACTS 2022",
                "Nilai \r\n              SKKK": "3.000",
                "Periode": "221",
                "Bidang": "PEMBELAJARAN"
            },
            {
                "No": "2",
                "Jabatan": "PANITIA : KETUA PANITIA",
                "Nama \r\n              Kegiatan": "HACKATHON 2023",
                "Nilai \r\n              SKKK": "6.000",
                "Periode": "222",
                "Bidang": "PEMBELAJARAN"
            },
            {
                "No": "3",
                "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR",
                "Nama \r\n              Kegiatan": "SEMINAR NASIONAL AI",
                "Nilai \r\n              SKKK": "1.500",
                "Periode": "221",
                "Bidang": "PEMBELAJARAN"
            }
        ],
        "skkk_total_activities": 3,
        "skkk_success": True,
        "skkk_error": None
    }

    print("\nPayload yang akan dikirim:")
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    print("\n" + "="*80)
    print("Mengirim data ke webhook...")
    print("="*80)

    try:
        response = requests.post(
            WEBHOOK_URL,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=15
        )

        print(f"\nStatus Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")

        if response.status_code == 200:
            print("\n[SUCCESS] Data berhasil dikirim!")
            try:
                response_data = response.json()
                print("\nResponse Body:")
                print(json.dumps(response_data, indent=2, ensure_ascii=False))
            except:
                print("\nResponse Text:")
                print(response.text)
        else:
            print(f"\n[FAILED] HTTP {response.status_code}")
            print(f"Response: {response.text}")

    except requests.Timeout:
        print("\n[TIMEOUT] Webhook tidak merespons dalam 15 detik")
    except requests.RequestException as e:
        print(f"\n[ERROR] Network error: {str(e)}")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")


def test_interview_complete_event():
    """Test Event 2: Interview Selesai"""
    print("\n\n")
    print("="*80)
    print("TEST EVENT 2: INTERVIEW SELESAI (LENGKAP)")
    print("="*80)

    payload = {
        "session_id": "test_session_001",
        "timestamp_completed": datetime.now().isoformat(),

        # Data Kandidat
        "nama": "John Doe Test",
        "email": "john.test@example.com",
        "posisi_dilamar": "Software Engineer",

        # CV Text
        "cv_text": "JOHN DOE\nSoftware Engineer\n\nEDUCATION\nUniversitas Kristen Petra - Informatika\nGPA: 3.75/4.00\n\nEXPERIENCE\nIntern at Tech Company (2023)\n- Developed web applications\n- Worked with React and Node.js",

        # Transkrip Jawaban Interview
        "transkrip_pertanyaan_1": "Saya tertarik dengan posisi ini karena saya memiliki passion di bidang teknologi dan ingin berkontribusi dalam mengembangkan solusi inovatif.",
        "transkrip_pertanyaan_2": "Kelebihan saya adalah problem solving yang baik, kemampuan bekerja dalam tim, dan cepat belajar teknologi baru.",
        "transkrip_pertanyaan_3": "Saya pernah mengerjakan project aplikasi mobile untuk manajemen tugas mahasiswa menggunakan React Native dan Firebase.",
        "transkrip_pertanyaan_4": "5 tahun ke depan saya ingin menjadi tech lead yang dapat memimpin tim dalam mengembangkan produk berkualitas tinggi.",

        # Data Transkrip Akademik
        "transkrip_nrp": "C14220062",
        "transkrip_prodi": "INFORMATIKA",
        "transkrip_ipk": 3.75,
        "transkrip_total_sks": 144,
        "transkrip_total_mk": 48,
        "transkrip_courses": [
            {
                "Kode": "IF1234",
                "Mata_Kuliah": "Pemrograman Berorientasi Objek",
                "Semester": "1-22/23",
                "SKS": 3,
                "Nilai": "A"
            },
            {
                "Kode": "IF5678",
                "Mata_Kuliah": "Basis Data",
                "Semester": "2-22/23",
                "SKS": 4,
                "Nilai": "B+"
            }
        ],
        "transkrip_grade_distribution": {
            "A": 20,
            "B+": 15,
            "B": 10,
            "C+": 2,
            "C": 1
        },

        # Data SKKK
        "skkk_data": [
            {
                "No": "1",
                "Jabatan": "WAKIL MAHASISWA : PESERTA/PENDENGAR",
                "Nama \r\n              Kegiatan": "ACTS 2022",
                "Nilai \r\n              SKKK": "3.000",
                "Periode": "221",
                "Bidang": "PEMBELAJARAN"
            }
        ],
        "skkk_total_activities": 1,
        "skkk_success": True,

        # Analisis Video
        "analisis_video": {
            "analisis_pertanyaan_1": "Confidence: High\nBody Language: Positive\nEye Contact: Good\nSpeech Clarity: Clear",
            "analisis_pertanyaan_2": "Confidence: Medium\nBody Language: Neutral\nEye Contact: Moderate\nSpeech Clarity: Clear",
            "analisis_pertanyaan_3": "Confidence: High\nBody Language: Engaged\nEye Contact: Excellent\nSpeech Clarity: Very Clear",
            "analisis_pertanyaan_4": "Confidence: High\nBody Language: Confident\nEye Contact: Good\nSpeech Clarity: Clear"
        }
    }

    print("\nPayload yang akan dikirim:")
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    print("\n" + "="*80)
    print("Mengirim data ke webhook...")
    print("="*80)

    try:
        response = requests.post(
            WEBHOOK_URL,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=15
        )

        print(f"\nStatus Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")

        if response.status_code == 200:
            print("\n[SUCCESS] Data berhasil dikirim!")
            try:
                response_data = response.json()
                print("\nResponse Body:")
                print(json.dumps(response_data, indent=2, ensure_ascii=False))
            except:
                print("\nResponse Text:")
                print(response.text)
        else:
            print(f"\n[FAILED] HTTP {response.status_code}")
            print(f"Response: {response.text}")

    except requests.Timeout:
        print("\n[TIMEOUT] Webhook tidak merespons dalam 15 detik")
    except requests.RequestException as e:
        print(f"\n[ERROR] Network error: {str(e)}")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")


if __name__ == "__main__":
    print("\n" + "="*80)
    print(" " * 25 + "WEBHOOK TEST SCRIPT")
    print(" " * 20 + "n8n Webhook Testing")
    print("="*80)

    while True:
        print("\n\nPilih test yang ingin dijalankan:")
        print("1. Test Event 1 - Upload Transkrip & SKKK")
        print("2. Test Event 2 - Interview Selesai (Lengkap)")
        print("3. Test Kedua Event (berurutan)")
        print("0. Exit")

        choice = input("\nPilihan (0-3): ").strip()

        if choice == "1":
            test_transkrip_upload_event()
        elif choice == "2":
            test_interview_complete_event()
        elif choice == "3":
            test_transkrip_upload_event()
            input("\nTekan Enter untuk lanjut ke Event 2...")
            test_interview_complete_event()
        elif choice == "0":
            print("\nTerima kasih! Goodbye.")
            break
        else:
            print("\nPilihan tidak valid!")
