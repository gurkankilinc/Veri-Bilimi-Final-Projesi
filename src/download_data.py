"""
download_data.py
----------------
İBB Açık Veri Portalı "Saatlik Toplu Ulaşım Veri Seti" içinden seçili aylık
CSV dosyalarını indirir ve tek bir ham dosyada (data/raw/iett_2023_raw.csv)
birleştirir. Bu, projenin "veri toplama" adımıdır.

Kaynak : https://data.ibb.gov.tr/dataset/hourly-public-transport-data-set
Lisans : İstanbul Büyükşehir Belediyesi Açık Veri Lisansı

Çalıştırma:
    python src/download_data.py
"""

from pathlib import Path
import sys
import pandas as pd
import requests

# Proje kök dizini (bu dosya src/ içinde olduğu için bir üst klasör)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"

# 2023 yılından mevsimleri temsil eden 4 ay. Her ay için portaldaki gerçek
# indirme bağlantısı. Daha fazla ay eklemek istersen bu sözlüğe satır ekle.
BASE = ("https://data.ibb.gov.tr/dataset/"
        "a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource")

MONTHS = {
    "202301": f"{BASE}/afc1cec1-fd43-44a9-b5c0-977d3b1d60d7/download/hourly_transportation_202301.csv",
    "202304": f"{BASE}/862a4927-7d69-4a06-a74e-24f1562d438f/download/hourly_transportation_202304.csv",
    "202307": f"{BASE}/f0c798c8-bab4-479e-841b-e82422e38e7f/download/hourly_transportation_202307.csv",
    "202310": f"{BASE}/db5d0618-05fc-417a-9bbe-16afda910832/download/hourly_transportation_202310.csv",
}

OUTPUT_FILE = RAW_DIR / "iett_2023_raw.csv"


def download_month(yyyymm: str, url: str) -> Path:
    """Tek bir aylık CSV'yi indirir ve data/raw altına kaydeder."""
    target = RAW_DIR / f"hourly_transportation_{yyyymm}.csv"
    if target.exists():
        print(f"  [atlandı] {target.name} zaten mevcut")
        return target

    print(f"  [indiriliyor] {yyyymm} ...")
    response = requests.get(url, timeout=120)
    response.raise_for_status()
    target.write_bytes(response.content)
    print(f"  [tamam] {target.name} ({target.stat().st_size // 1024} KB)")
    return target


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    print("Aylık dosyalar indiriliyor...")

    paths = []
    for yyyymm, url in MONTHS.items():
        try:
            paths.append(download_month(yyyymm, url))
        except requests.RequestException as exc:
            print(f"  [HATA] {yyyymm} indirilemedi: {exc}", file=sys.stderr)

    if not paths:
        sys.exit("Hiçbir dosya indirilemedi. İnternet bağlantını kontrol et.")

    print("\nDosyalar birleştiriliyor...")
    frames = []
    for path in paths:
        # Karakter kodlaması için önce utf-8, olmazsa Türkçe için latin-5 dene
        try:
            df = pd.read_csv(path, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(path, encoding="ISO-8859-9")
        df["kaynak_dosya"] = path.name
        frames.append(df)

    combined = pd.concat(frames, ignore_index=True)
    combined.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

    print(f"\nBirleştirildi -> {OUTPUT_FILE}")
    print(f"Toplam satır: {len(combined):,}")
    print(f"Sütunlar    : {list(combined.columns)}")


if __name__ == "__main__":
    main()
