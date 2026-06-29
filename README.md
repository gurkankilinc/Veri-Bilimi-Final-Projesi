# İstanbul Toplu Ulaşım (İETT) Saatlik Yolcu Analizi

Veri Bilimi dersi dönem projesi. İBB Açık Veri Portalı'ndaki **Saatlik Toplu Ulaşım Veri Seti** üzerinde
uçtan uca bir veri bilimi iş akışı uygulanır: veri toplama → temizleme & veri kalitesi doğrulaması →
keşifsel veri analizi (EDA) → görselleştirme → makine öğrenmesi modellemesi → yorumlama.

## Proje Ekibi

| Öğrenci No | Ad Soyad |
|---|---|
| 1306240134 | Gürkan Kılınç |

Bu proje **bireysel** olarak hazırlanmıştır.

## Araştırma Soruları

1. Gün içindeki yolcu sayısı hangi saatlerde tepe yapıyor? Hafta içi ve hafta sonu profili nasıl değişiyor?
2. Yolcu sayısında mevsimsel bir değişim var mı? (yaz tatili etkisi)
3. Toplam yolcunun büyük kısmını az sayıda hat mı taşıyor? (Pareto / 80-20 etkisi)
4. Hangi ilçeler en yüksek yolcu talebini üretiyor? (coğrafi yoğunlaşma)
5. Ücret tipi dağılımı yolcu tabanının sosyo-ekonomik profilini nasıl yansıtıyor?

## Veri Kaynağı

- **Veri seti:** Saatlik Toplu Ulaşım Veri Seti
- **Portal:** https://data.ibb.gov.tr/dataset/hourly-public-transport-data-set
- **Sağlayıcı:** BELBİM A.Ş. (İstanbulkart işletmecisi)
- **Lisans:** İstanbul Büyükşehir Belediyesi Açık Veri Lisansı — https://data.ibb.gov.tr/license
- **Kapsam:** 2023 yılından mevsimleri temsil eden 4 ay (Ocak, Nisan, Temmuz, Ekim), yalnızca otobüs modu.
  Toplam 63 M+ kayıt içinden otobüs modu (transport_type_id=1) seçilerek tüm ~41.2 M kayıt kullanılmıştır.

## Proje Yapısı

```
Veri-Bilimi-Final-Projesi/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── download_data.py        # Aylık CSV'leri indirip tek dosyada birleştirir
├── data/
│   ├── raw/                    # İndirilen ham CSV'ler (git'e dahil edilmez)
│   └── processed/              # Temizlenmiş veri (git'e dahil edilmez)
├── notebooks/
│   └── analiz.ipynb            # Yükleme → temizleme → EDA → modelleme
├── prompts/
│   └── prompt_gunlugu.md       # Geliştirmede kullanılan önemli promptlar (kronolojik)
├── report/
│   └── rapor.pdf               # Kısa rapor (bulgular ve yorumlar)
└── figures/                    # Notebook'tan dışa aktarılan grafikler (15 görsel)
```

## Kurulum ve Çalıştırma

1. Depoyu klonlayın ve sanal ortam kurun:
   ```bash
   git clone https://github.com/gurkankilinc/Veri-Bilimi-Final-Projesi.git
   cd Veri-Bilimi-Final-Projesi
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Veriyi indirin (aylık CSV'ler `data/raw/` altına indirilir ve birleştirilir):
   ```bash
   python src/download_data.py
   ```

3. Notebook'u baştan sona çalıştırın:
   ```bash
   jupyter notebook notebooks/analiz.ipynb
   ```
   > **Not:** Hücreler sırayla çalıştırılmalıdır. Adım 3.1b'deki veri kalitesi
   > doğrulama bloğu, ilçe analizinden önce mutlaka tamamlanmış olmalıdır.

## Temel Bulgular

| Soru | Bulgu |
|---|---|
| Pik saatler | Hafta içi 08:00 ve 17–18:00 çift tepeli profil; hafta sonu düz dağılım |
| Mevsimsellik | Temmuz'da belirgin düşüş — eğitim takvimi baskın etken |
| Pareto | Hatların %20'si toplam yolcunun büyük çoğunluğunu taşıyor |
| Coğrafi | Talep belirli metropoliten eksenlerde yoğunlaşıyor |
| Ücret tipi | İndirimli Abonman (%33) + Tam Kontur (%31) üçte ikiyi oluşturuyor |
| Model | RandomForest R² = 0.755, MAE iyileşmesi %31.5 (baseline'a göre) |

## Kullanılan Kütüphaneler

`pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `requests`, `jupyter`  
(Sürümler için `requirements.txt`.)

## Geliştirme Yöntemi

Proje "vibe coding" yöntemiyle, bir yapay zekâ kodlama asistanı birincil geliştirme ortağı olarak
kullanılarak geliştirilmiştir. Kullanılan başlıca promptlar `prompts/prompt_gunlugu.md` içinde
kronolojik olarak listelenmiştir. Veri kalitesi doğrulaması ve coğrafi atama hataları tespiti
de bu sürecin kritik bir parçasını oluşturmuştur.
