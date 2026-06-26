# Kısa Rapor Taslağı (3-5 sayfa)

> Bu taslağı doldurduktan sonra PDF'e dönüştürün (örn. notebook'tan veya bir
> Markdown→PDF aracıyla). Teslimde çıktısı elden verilecek.

## 1. Problem Tanımı
İstanbul toplu ulaşımında yolcu yoğunluğunun zamana (saat, gün, mevsim) göre nasıl
değiştiğini anlamak. Üç araştırma sorusu: (1) gün-içi pik saatler, (2) mevsimsellik,
(3) hat bazında yoğunluk dağılımı.

## 2. Veri Seti ve Kaynağı
- Kaynak: İBB Açık Veri Portalı — Saatlik Toplu Ulaşım Veri Seti (BELBİM A.Ş.)
- Lisans: İstanbul Büyükşehir Belediyesi Açık Veri Lisansı
- Kapsam: 2023 yılı Ocak/Nisan/Temmuz/Ekim ayları, OTOBÜS türü.
- Satır sayısı, sütunlar: (notebook'tan doldurun)

## 3. Yöntem
- Veri toplama: aylık CSV'lerin indirilip birleştirilmesi (`download_data.py`).
- Temizleme: tarih dönüşümü, türetilmiş zaman sütunları, eksik/aykırı değer işleme.
- EDA: (kullanılan 4 görselleştirme türünü yazın).
- Model: (regresyon / kümeleme — hangisi ve neden).

## 4. Bulgular
- Soru 1 bulgusu: ...
- Soru 2 bulgusu: ...
- Soru 3 bulgusu: ...
- Model performansı: (R² / MAE veya küme yorumu)

## 5. Sınırlamalar
- Yalnızca 4 ay ve tek ulaşım türü kullanıldı.
- Hava durumu, tatil günleri gibi dış değişkenler dahil edilmedi.
- ...

## 6. Öğrenilenler
- Teknik: ...
- Süreç (vibe coding): ...
