# İstanbul Toplu Ulaşım (İETT) Saatlik Yolcu Analizi

Veri Bilimi dersi dönem projesi. İBB Açık Veri Portalı'ndaki **Saatlik Toplu Ulaşım Veri Seti** üzerinde
uçtan uca bir veri bilimi iş akışı uygulanır: veri toplama → temizleme → keşifsel veri analizi (EDA) →
görselleştirme → basit modelleme → yorumlama.

## Proje Ekibi

| Öğrenci No | Ad Soyad |
|------------|----------|
| `________` | `________` |
| `________` | `________` |  <!-- bireysel ise bu satırı silin -->

## Araştırma Soruları

1. Gün içindeki yolcu sayısı hangi saatlerde tepe yapıyor? Hafta içi ve hafta sonu bu profil nasıl değişiyor?
2. Yolcu sayısında mevsimsel bir değişim var mı? (örn. yaz tatili etkisi)
3. Toplam yolcunun büyük kısmını az sayıda hat mı taşıyor? (Pareto / 80-20 etkisi)

## Veri Kaynağı

- **Veri seti:** Saatlik Toplu Ulaşım Veri Seti
- **Portal:** https://data.ibb.gov.tr/dataset/hourly-public-transport-data-set
- **Sağlayıcı:** BELBİM A.Ş. (İstanbulkart işletmecisi)
- **Lisans:** İstanbul Büyükşehir Belediyesi Açık Veri Lisansı — https://data.ibb.gov.tr/license
- **Kapsam:** Saatlik bazda, ulaşım türü ve hat kırılımında yolcu ve yolculuk sayıları.
  Bu projede 2023 yılından mevsimleri temsil eden 4 ay (Ocak, Nisan, Temmuz, Ekim) kullanılır
  ve `OTOBÜS` ulaşım türüne odaklanılır.

## Proje Yapısı

```
iett-veri-bilimi-projesi/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── download_data.py        # Aylık CSV'leri indirip tek dosyada birleştirir
├── data/
│   ├── raw/                    # İndirilen ham CSV'ler (git'e dahil edilmez)
│   └── processed/              # Temizlenmiş veri (git'e dahil edilmez)
├── notebooks/
│   └── analiz.ipynb            # Yükleme, temizleme, EDA, modelleme — tek dosya
├── prompts/
│   └── prompt_gunlugu.md       # Geliştirmede kullanılan önemli promptlar (kronolojik)
├── report/
│   └── RAPOR_TASLAGI.md        # Kısa raporun taslağı (PDF'e dönüştürülecek)
└── figures/                    # Notebook'tan dışa aktarılan grafikler
```

## Kurulum ve Çalıştırma

1. Depoyu klonlayın ve sanal ortam kurun:
   ```bash
   git clone <REPO_LINKINIZ>
   cd iett-veri-bilimi-projesi
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Veriyi indirin (veri toplama adımı). Bu, aylık CSV'leri `data/raw/` altına indirip
   `data/raw/iett_2023_raw.csv` olarak birleştirir:
   ```bash
   python src/download_data.py
   ```
3. Notebook'u açın ve baştan sona çalıştırın:
   ```bash
   jupyter notebook notebooks/analiz.ipynb
   ```

## Kullanılan Kütüphaneler

pandas, numpy, matplotlib, seaborn, scikit-learn, requests, jupyter
(Sürümler için `requirements.txt`.)

## Geliştirme Yöntemi

Proje "vibe coding" yöntemiyle, bir yapay zekâ kodlama asistanı birincil geliştirme ortağı olarak
kullanılarak geliştirilmiştir. Kullanılan başlıca promptlar `prompts/prompt_gunlugu.md` içinde
kronolojik olarak listelenmiştir. Üretilen tüm kod ekip tarafından anlaşılmış ve doğrulanmıştır.
