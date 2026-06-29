# Prompt Günlüğü

Bu projenin geliştirilmesinde yapay zekâ kodlama asistanı ile kullanılan önemli
promptlar, kronolojik sırayla ve hangi fazda kullanıldığı belirtilerek listelenmiştir.
Her prompt'un altında üretilen çıktının ne işe yaradığına dair kısa bir not vardır.

> Not: Aşağıdaki promptlar gerçek geliştirme akışını yansıtır. Çalışırken kendi
> ifadenle ufak değişiklikler yaparsan, bu günlüğü de ona göre güncelle ki kayıt
> dürüst kalsın.

---

## Faz 0 — Planlama ve tema seçimi

**1.** Veri Bilimi dersinde final yerine dönem projesi verildi. İETT / toplu taşıma
temasında hangi açık veri setini kullanmam mantıklı olur? Bana uçtan uca bir yol
haritası çıkarır mısın?
*Not: İBB Saatlik Toplu Ulaşım Veri Seti'ne ve faz bazlı plana karar verildi.*

**2.** Seçtiğim bu veri seti için analizle yanıtlanabilecek 3 tane somut araştırma
sorusu öner.
*Not: Pik saatler, mevsimsellik ve hat bazlı yoğunluk (Pareto) soruları belirlendi.*

## Faz 1 — Veri toplama

**3.** İBB portalındaki aylık CSV'leri tek tek indirmek yerine; 2023'ün Ocak, Nisan,
Temmuz ve Ekim aylarını indirip tek bir CSV dosyasında birleştiren bir Python betiği
yaz. Dosyaları data/raw klasörüne kaydetsin.
*Not: download_data.py oluşturuldu; requests ile indirip pandas ile birleştiriyor.*

**4.** İndirdiğim CSV'de Türkçe karakterler bozuk görünüyor. Encoding sorununu nasıl
çözerim, betiğe nasıl eklerim?
*Not: utf-8 başarısız olursa ISO-8859-9 ile okuma eklendi.*

## Faz 2 — Veri tanıma ve temizleme

**5.** df.info() ve df.head() çıktım şöyle: [...]. Tarih sütununu datetime'a çevirip
bundan saat, haftanın günü, hafta sonu mu ve ay sütunlarını türeten kodu yaz.
*Not: Zaman temelli türetilmiş sütunlar oluşturuldu; EDA ve modelin temeli bunlar.*

**6.** Ulaşım türü sütununda sadece otobüs (OTOBÜS) kayıtlarını bırakmak istiyorum,
tema İETT olduğu için. Bunu nasıl filtrelerim?
*Not: Veri otobüse filtrelendi, satır sayısı yönetilebilir hale geldi.*

**7.** Yolcu sayısı sütunundaki aykırı değerleri IQR yöntemiyle tespit eden bir kod
yaz ve yöntemin mantığını adım adım açıkla.
*Not: Üst aykırı sınır hesaplandı; mantığı teslimde anlatabilmek için öğrenildi.*

**8.** Bu veri setinde eksik değerleri silmek mi yoksa doldurmak mı daha doğru olur?
Hangisini neden önerirsin?
*Not: Eksik kayıtların "o saatte veri yok" anlamına gelebileceği değerlendirildi.*

## Faz 3 — Keşifsel veri analizi (EDA)

**9.** Saate göre ortalama yolcu sayısını gösteren bir çizgi grafik için matplotlib
kodu yaz, başlık ve eksen etiketleri Türkçe olsun.
*Not: 1. görselleştirme — saatlik çizgi grafik.*

**10.** Hafta içi ve hafta sonu saatlik yolcu profilini aynı grafikte karşılaştırmak
istiyorum.
*Not: Soru 1'i yanıtlayan karşılaştırmalı grafik.*

**11.** Saat ve haftanın günü kırılımında ortalama yolcu sayısını gösteren bir ısı
haritası (heatmap) oluştur.
*Not: 4. görselleştirme — yoğunluğun zaman içindeki desenini gösteriyor.*

**12.** Hangi otobüs hatlarının toplam yolcunun büyük kısmını taşıdığını bulmak için
bir Pareto analizi yap; kümülatif yüzde hesapla.
*Not: Soru 3'ü (80-20 etkisi) yanıtladı.*

## Faz 4 — Modelleme

**13.** Saatlik yolcu sayısını saat, haftanın günü, ay ve hafta sonu gibi zaman
özelliklerinden tahmin eden bir RandomForest regresyon modeli kur; R² ve MAE hesapla,
gerçek-vs-tahmin grafiği çiz.
*Not: Tek savunulabilir model kuruldu ve değerlendirildi.*

**14.** Modelin özellik önemlerini (feature importance) yatay bar grafikte göster;
hangi değişkenin en belirleyici olduğunu yorumla.
*Not: Saatin en güçlü belirleyici olup olmadığı incelendi.*

## Faz 5 — Yorum ve rapor

**15.** Bulgularımı 3-5 sayfalık rapor için akademik bir dille özetle: pik saatler,
yaz aylarındaki düşüş ve hat bazlı yoğunluk. Her birini sonuçların anlamıyla birlikte yaz.
*Not: Raporun "Bulgular" bölümü için taslak metin üretildi.*

**16.** Projenin "Sınırlamalar" bölümü için 3-4 madde öner.
*Not: Dar kapsam, dış değişkenlerin eksikliği gibi sınırlamalar listelendi.*

## Faz 3+ — Ek zenginleştirme analizleri

**17.** Veri setindeki `town` (ilçe) sütununu kullanarak en çok yolcu üreten ilçeleri
yatay bar grafikle göster; eksik ilçeleri çıkar.
*Not: Mekânsal boyut eklendi — talep merkez ilçelerde yoğunlaşıyor.*

**18.** `transaction_type_desc` sütununa göre ücret tiplerinin (Tam/İndirimli/Ücretsiz/
Abonman) toplam yolcudaki payını çıkar ve görselleştir.
*Not: Yolcu profilinin sosyo-ekonomik dağılımı incelendi.*

**19.** Otobüs hatlarını saatlik talep profillerinin şekline göre KMeans ile kümele;
her hattı kendi tepe değerine normalize et ve küme merkezlerini saatlik profil olarak çiz.
*Not: İkinci model tekniği — işe-gidiş hatları ile gün-içi hatları ayrıştırdı.*

**20.** Isı haritası rengini "düşük=yeşil, yüksek=kırmızı" mantığına çevir; histogramı
aşırı çarpık dağılım için log ölçeğe al.
*Not: Görsel okunabilirlik ve sezgisellik artırıldı.*

## Faz 6 — Veri Kalitesi ve Sistem Doğrulama

**21.** `town` sütununda veri sızıntısı var: Anadolu yakası hatları (11–19 prefix), Metrobüs
(34) ve ekspres serisi (500, 522) GPS okunamadığında otomatik `BAKIRKOY` atıyor ve ilçe
grafiğini şişiriyor. Bu satırları silmeden `town = NaN` yapan bir temizlik bloğu ekle,
örneklemi de %10'dan %20'ye çıkar.
*Not: Prefix tabanlı ilk temizlik bloğu eklendi; Bakırköy baskınlığı azaldı fakat
tamamen giderilmedi — sınır prefix listesi çok dardı.*

**22.** Temizlik sonrası bile Bakırköy 29 milyon yolcuyla açık ara birinci çıkıyor. 29
milyon gerçekçi değil. Başka ilçelerin veya NaN değerlerin Bakırköy'e kayması mı var?
Neden diğer ilçelerin sayısı bu kadar düşük?
*Not: 405 farklı hat Bakırköy etiketli görünüyordu; top 3 hattın payı yalnızca %5.4 —
bu, büyük ölçekli varsayılan atama örüntüsünün klasik imzasıdır.*

**23.** Her hat kodu için BAKIRKOY kayıt oranını hesapla; oran %90'ı geçiyorsa o hattın
tüm kayıtlarında `town = NaN` yap. Gerçek bir Bakırköy hattı diğer ilçelerde de kayıt
üretir, hiçbir hattın %100'ü BAKIRKOY olamaz.
*Not: Veri güdümlü temizlik uygulandı; 203 hat NaN'a çekildi, BAKIRKOY'un tüm
kayıtlardaki payı %11.7'ye geriledi, ilçe grafiği artık makul bir dağılım gösteriyor.*

## Faz 7 — Profesyonelleştirme ve Raporlama

**24.** Tüm "Bulgu" hücrelerini güncel verilere göre yenile. Sonuçlar/Öğrenilenler
bölümünü daha kapsamlı ve akademik bir dille yaz; veri kalitesi sorununu çok ön plana
çıkarmadan ama dürüstçe belirt. Grafik başlıklarından "BAKIRKOY sızıntısı temizlenmiş"
ifadesini kaldır. rapor.pdf ve README'yi de doğru bulguları yansıtacak biçimde güncelle.
*Not: Section 7 komple yeniden yazıldı — 5 araştırma sorusu özeti, model karşılaştırma
tablosu (gerçek sayılarla), 4 sınırlama maddesi ve vibe coding öz-değerlendirme eklendi.
rapor.pdf yeniden üretildi (Arial TTF, 113 KB, Türkçe karakterler doğru).*

**25.** Grafiklerdeki yolcu sayıları gerçekten 8 milyona sınırlandırılmış örneklemi mi
kullanıyor, yoksa 41 milyonluk tam veriyi mi kapsıyor? Eğer 8 milyona sınırlıysa
%20 ifadesine gerek yok, kaldıralım ve verinin %100'ünü kullanalım.
*Not: Tüm grafikler `otobus` DataFrame üzerinden çalıştığı için örneklemeye tabiydi;
sampling kaldırılıp 41 M kayıtla tam veri kullanımına geçildi, başlık etiketleri temizlendi.*

## Faz 8 — Örneklem Optimizasyonu ve Keşif

**26.** `town = BAKIRKOY` olan kayıtlarda `number_of_passenger` toplamı en yüksek 20 hattı
sıralı listele. Sonra veriyi tekrar kısıtlayalım: %25 örneklem uygula ve bunu tüm
grafiklere yansıt.
*Not: Top 20 Bakırköy hattı listelendi — 97 (2.8 M), 10 (2.6 M), 418 (1.7 M) başı
çekiyor; bunlar temizlik sonrası gerçek yerel Bakırköy hatları. `frac=0.25` ile
~10.3 M kayıt örneklemi kuruldu, tüm EDA ve model hücreleri otomatik bu veri üzerinden çalışıyor.*
