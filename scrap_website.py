import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import Dict, List, Optional


def scrape_skkk_data(nrp: str) -> Dict:
    """
    Scrape data SKKK Non Wajib dari sportfolio berdasarkan NRP

    Args:
        nrp: Nomor Registrasi Pokok mahasiswa

    Returns:
        Dictionary berisi:
        - success: bool
        - data: list of dict (jika berhasil)
        - total_activities: int
        - error: str (jika gagal)
    """
    try:
        url = "http://sportfolio.petra.ac.id/bakabootsrap/baka/skkk.php"
        payload = {"nrp": nrp, "Submit": "Submit"}

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/119.0 Safari/537.36",
            "Referer": url,
            "Origin": "http://sportfolio.petra.ac.id",
        }

        # Request ke website
        s = requests.Session()
        s.get(url, headers=headers)
        r = s.post(url, data=payload, headers=headers, allow_redirects=True, timeout=10)

        # Parsing hasil POST
        soup = BeautifulSoup(r.text, "html.parser")

        # Cari tabel SKKK Non Wajib (id='example')
        table = soup.find("table", id="example")

        if not table:
            return {
                "success": False,
                "error": "Tabel SKKK tidak ditemukan. Mungkin NRP tidak valid atau tidak ada data SKKK.",
                "data": [],
                "total_activities": 0
            }

        # Extract headers
        header_elements = table.find("thead").find_all("th")
        headers = [th.get_text(strip=True) for th in header_elements]

        # Extract rows
        rows = []
        for tr in table.find("tbody").find_all("tr"):
            cols = [td.get_text(strip=True) for td in tr.find_all("td")]
            if cols:
                rows.append(cols)

        # Convert ke list of dictionaries
        skkk_data = []
        for row in rows:
            if len(row) == len(headers):
                skkk_data.append(dict(zip(headers, row)))

        return {
            "success": True,
            "data": skkk_data,
            "total_activities": len(skkk_data),
            "headers": headers
        }

    except requests.Timeout:
        return {
            "success": False,
            "error": "Timeout: Website sportfolio tidak merespons",
            "data": [],
            "total_activities": 0
        }
    except requests.RequestException as e:
        return {
            "success": False,
            "error": f"Network error: {str(e)}",
            "data": [],
            "total_activities": 0
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Error scraping SKKK: {str(e)}",
            "data": [],
            "total_activities": 0
        }


def save_skkk_to_csv(skkk_data: List[Dict], output_path: str = "skkk_non_wajib.csv") -> bool:
    """
    Simpan data SKKK ke file CSV

    Args:
        skkk_data: List of dictionaries berisi data SKKK
        output_path: Path untuk menyimpan file CSV

    Returns:
        True jika berhasil, False jika gagal
    """
    try:
        if not skkk_data:
            print("Tidak ada data SKKK untuk disimpan")
            return False

        df = pd.DataFrame(skkk_data)
        df.to_csv(output_path, index=False, encoding='utf-8-sig')
        print(f"✅ Data SKKK berhasil disimpan ke {output_path}")
        return True
    except Exception as e:
        print(f"❌ Error menyimpan CSV: {str(e)}")
        return False


# Untuk testing langsung dari command line
if __name__ == "__main__":
    # Hardcoded NRP untuk testing
    test_nrp = "C14220062"

    print(f"=== Scraping SKKK untuk NRP: {test_nrp} ===\n")
    result = scrape_skkk_data(test_nrp)

    if result["success"]:
        print(f"✅ Berhasil! Total kegiatan: {result['total_activities']}")
        print("\n=== Data SKKK Non Wajib ===")

        df = pd.DataFrame(result["data"])
        print(df)

        # Simpan ke CSV
        save_skkk_to_csv(result["data"])
    else:
        print(f"❌ Gagal: {result['error']}")
