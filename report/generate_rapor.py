"""Rapor PDF oluşturucu — Türkçe karakterler dahil."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Türkçe karakter desteği için Arial TTF kayıt et
FONT_DIR = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont("Arial",     os.path.join(FONT_DIR, "arial.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Bold",os.path.join(FONT_DIR, "arialbd.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Italic",os.path.join(FONT_DIR, "ariali.ttf")))
from reportlab.lib.fonts import addMapping
addMapping("Arial", 0, 0, "Arial")
addMapping("Arial", 1, 0, "Arial-Bold")
addMapping("Arial", 0, 1, "Arial-Italic")

FONT      = "Arial"
FONT_BOLD = "Arial-Bold"
FONT_IT   = "Arial-Italic"

OUTPUT = r"C:\Users\gurka\OneDrive\Masaüstü\veri bilimi projesi\report\rapor.pdf"

W, H = A4

# ── Stiller ──────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def style(name, parent="Normal", **kw):
    return ParagraphStyle(name, parent=styles[parent], **kw)

TITLE   = style("MyTitle",  "Title",   fontName=FONT_BOLD, fontSize=20, spaceAfter=4,
                textColor=colors.HexColor("#1f3864"), alignment=TA_CENTER)
SUB     = style("MySub",    "Normal",  fontName=FONT_BOLD, fontSize=11, spaceAfter=2,
                textColor=colors.HexColor("#4472c4"), alignment=TA_CENTER)
META    = style("MyMeta",   "Normal",  fontName=FONT, fontSize=9,  spaceAfter=2,
                textColor=colors.HexColor("#666666"), alignment=TA_CENTER)
H1      = style("MyH1",     "Heading1",fontName=FONT_BOLD, fontSize=13, spaceBefore=14, spaceAfter=4,
                textColor=colors.HexColor("#1f3864"), borderPad=2)
H2      = style("MyH2",     "Heading2",fontName=FONT_BOLD, fontSize=11, spaceBefore=8,  spaceAfter=3,
                textColor=colors.HexColor("#4472c4"))
BODY    = style("MyBody",   "Normal",  fontName=FONT, fontSize=10, leading=15, spaceAfter=6,
                alignment=TA_JUSTIFY)
BULLET  = style("MyBullet", "Normal",  fontName=FONT, fontSize=10, leading=14, spaceAfter=3,
                leftIndent=14, firstLineIndent=0)
CAPTION = style("MyCaption","Normal",  fontName=FONT_IT, fontSize=8, textColor=colors.gray,
                alignment=TA_CENTER, spaceAfter=8)
FOOTER  = style("MyFooter", "Normal",  fontName=FONT, fontSize=8,  textColor=colors.gray,
                alignment=TA_CENTER)

def P(text, st=BODY):  return Paragraph(text, st)
def B(text):           return Paragraph(f"• {text}", BULLET)
def SP(n=6):           return Spacer(1, n)
def HR():              return HRFlowable(width="100%", thickness=0.5,
                                         color=colors.HexColor("#4472c4"),
                                         spaceAfter=4, spaceBefore=4)

# ── İçerik ───────────────────────────────────────────────────────────────────
story = []

# Kapak
story += [
    SP(30),
    P("İstanbul Toplu Ulaşım (İETT)", TITLE),
    P("Saatlik Yolcu Analizi", TITLE),
    SP(6),
    P("Veri Bilimi Dönem Projesi Raporu", SUB),
    SP(20),
    HR(),
    SP(8),
    P("Öğrenci: Gürkan Kılınç &nbsp;&nbsp;|&nbsp;&nbsp; No: 1306240134", META),
    P("Haziran 2026", META),
    SP(4),
    P("Veri Kaynağı: İBB Açık Veri Portalı — Saatlik Toplu Ulaşım Veri Seti (BELBİM A.Ş.)", META),
    HR(),
    PageBreak(),
]

# 1. Giriş
story += [
    P("1. Giriş ve Problem Tanımı", H1), HR(),
    P("Bu proje, İstanbul Büyükşehir Belediyesi (İBB) Açık Veri Portalı'ndan temin edilen "
      "2023 yılı saatlik otobüs yolcu verisi üzerinde uçtan uca bir veri bilimi iş akışı "
      "uygulamayı amaçlamaktadır. 63 milyonun üzerinde kayıt içeren ham veri setinden "
      "otobüs modu seçilerek yaklaşık 41,2 milyon kayıt analiz edilmiştir."),
    P("Analiz beş araştırma sorusu etrafında yapılandırılmıştır:"),
    B("Gün içindeki yolcu sayısı hangi saatlerde tepe yapıyor? Hafta içi ve hafta sonu "
      "profili nasıl değişiyor?"),
    B("Yolcu sayısında mevsimsel bir değişim var mı? (yaz tatili etkisi)"),
    B("Toplam yolcunun büyük kısmını az sayıda hat mı taşıyor? (Pareto / 80-20 etkisi)"),
    B("Hangi ilçeler en yüksek yolcu talebini üretiyor? (coğrafi yoğunlaşma)"),
    B("Ücret tipi dağılımı yolcu tabanının sosyo-ekonomik profilini nasıl yansıtıyor?"),
    SP(),
]

# 2. Veri ve Metodoloji
story += [
    P("2. Veri ve Metodoloji", H1), HR(),
    P("2.1 Veri Seti", H2),
    P("Veri kaynağı: İBB Açık Veri Portalı (data.ibb.gov.tr), BELBİM A.Ş. tarafından sağlanan "
      "Saatlik Toplu Ulaşım Veri Seti. Analizde 2023 yılından dört mevsimi temsil eden aylar "
      "(Ocak, Nisan, Temmuz, Ekim) kullanılmış; yalnızca otobüs modu (transport_type_id = 1) "
      "dahil edilmiştir."),
    P("2.2 Veri Ön İşleme ve Kalite Doğrulaması", H2),
    P("Temizleme adımları:"),
    B("Tarih dönüşümü ve türetilmiş zaman değişkenleri (saat, gün, ay, hafta sonu, tatil)"),
    B("2023 Türkiye resmî tatilleri işaretlendi (<i>tatil_mi</i> değişkeni)"),
    B("Yolcu sayısı aykırı değerleri IQR yöntemiyle işaretlendi; silinmedi"),
    SP(4),
    P("<b>Veri kalitesi doğrulaması:</b> İlçe bazlı analiz sırasında <i>town</i> sütununda "
      "sistematik bir atama hatası tespit edilmiştir. Konumu okunamayan bazı hatların kayıtları, "
      "veritabanı fallback mekanizması nedeniyle tek bir varsayılan ilçeye atanmıştı. "
      "Bu hata, veri güdümlü bir yaklaşımla giderilmiştir: her hat kodu için hatalı ilçe "
      "etiket oranı hesaplanmış; oranı %90'ın üzerinde olan hatların ilçe bilgisi boş (NaN) "
      "olarak işaretlenmiş, yolcu verileri korunmuştur."),
    P("2.3 Modelleme Yaklaşımı", H2),
    P("<b>Hedef değişken:</b> Saat-gün-ay kırılımında toplam yolcu sayısı. "
      "<b>Özellikler:</b> saat, haftanın günü, ay, hafta_sonu_mu, tatil_mi. "
      "<b>Eğitim/test ayrımı:</b> Zamansal bütünlüğü korumak için son ay (Ekim) test seti, "
      "önceki aylar eğitim seti olarak kullanılmıştır. Beş model karşılaştırılmış; "
      "sonuçlar Bölüm 4'te sunulmuştur."),
    SP(),
]

# 3. EDA Bulguları
story += [
    P("3. Keşifsel Veri Analizi Bulguları", H1), HR(),
    P("<b>Soru 1 — Gün-İçi Pik Saatler (Hafta İçi vs Hafta Sonu)</b>", H2),
    P("Hafta içi saatlik talep profili, sabah 08:00 ve akşam 17–18:00 saatlerinde belirgin "
      "çift tepe oluşturur. Bu örüntü, çalışan nüfusun işe gidiş-dönüş davranışıyla birebir "
      "örtüşmektedir. Hafta sonu bu tepeler ortadan kalkar; talep güne daha düz ve geniş "
      "yayılımla dağılır. Bulgu, frekans planlamasının hafta içi/hafta sonu için "
      "farklılaştırılması gerektiğine işaret etmektedir."),
    P("<b>Soru 2 — Mevsimsellik</b>", H2),
    P("Aylık toplam yolcu verisi, Temmuz ayında belirgin bir düşüş ortaya koymaktadır. "
      "Bu düşüş; okul tatili nedeniyle öğrenci abonemanlarının pasifleşmesi ve kurumsal "
      "çalışmaların yavaşlamasıyla açıklanabilir. Diğer üç ay (Ocak, Nisan, Ekim) birbirine "
      "yakın düzeyde seyretmiş; bu da toplam talebin yaz tatilinden en çok etkilendiğini ve "
      "eğitim takviminin toplu taşıma planlaması için kritik bir dış değişken olduğunu "
      "ortaya koymuştur."),
    P("<b>Soru 3 — Pareto Etkisi</b>", H2),
    P("Hat bazlı kümülatif analiz, toplam hatların yalnızca %20'sinin toplam yolcuların "
      "büyük çoğunluğunu taşıdığını göstermiştir. Bu asimetrik dağılım, 80-20 Pareto "
      "örüntüsünü güçlü biçimde doğrular ve kaynak planlamasında az sayıda yoğun koridora "
      "odaklanmanın etkinliğini destekler."),
    P("<b>Soru 4 — Coğrafi Yoğunlaşma</b>", H2),
    P("Veri kalitesi doğrulamasının ardından ilçe bazlı analiz, yolcu talebinin birden fazla "
      "metropoliten eksende dağıldığını ortaya koymaktadır. Bu dağılım, Pareto bulgusunun "
      "mekânsal karşılığını oluşturmaktadır; talep hem hat hem de ilçe kırılımında az sayıda "
      "noktada toplanmaktadır."),
    P("<b>Soru 5 — Ücret Tipi Dağılımı</b>", H2),
    P("Yolcuların yaklaşık üçte ikisi İndirimli Abonman (~%33) ve Tam Kontur (~%31) "
      "kategorilerinde yoğunlaşmaktadır. İndirimli abonmanın baskınlığı, düzenli ve öğrenci "
      "yolcuların büyük bir segment oluşturduğunu; Ücretsiz binişlerin (~%15) ise 65 yaş "
      "üstü ve engelli yolcu kitlesinin görece büyüklüğünü yansıtmaktadır. Bu dağılım, "
      "ücret politikası ve gelir tahmini açısından anlamlı bir sosyo-ekonomik göstergedir."),
    SP(),
]

# 4. Modelleme
story += [
    P("4. Modelleme Sonuçları", H1), HR(),
    P("Saatlik toplam yolcuyu zaman özelliklerinden tahmin etmek için beş model zamansal "
      "train/test ayrımı (son ay = test, gerisi = eğitim) altında karşılaştırılmıştır:"),
    SP(8),
]

tdata = [
    ["Model", "R²", "MAE"],
    ["Gradient Boosting", "0,772", "36.494"],
    ["Random Forest (seçilen)", "0,755", "37.970"],
    ["Karar Ağacı", "0,748", "38.481"],
    ["Baseline (saat ortalaması)", "0,515", "55.413"],
    ["Doğrusal Regresyon", "0,128", "83.624"],
]
tbl = Table(tdata, colWidths=[10*cm, 2.5*cm, 3*cm])
tbl.setStyle(TableStyle([
    ("BACKGROUND",   (0, 0), (-1, 0), colors.HexColor("#1f3864")),
    ("TEXTCOLOR",    (0, 0), (-1, 0), colors.white),
    ("FONTNAME",     (0, 0), (-1, 0), FONT_BOLD),
    ("FONTNAME",     (0, 1), (-1, -1), FONT),
    ("FONTSIZE",     (0, 0), (-1, -1), 9),
    ("ALIGN",        (1, 0), (-1, -1), "CENTER"),
    ("ALIGN",        (0, 0), (0, -1), "LEFT"),
    ("BACKGROUND",   (0, 2), (-1, 2), colors.HexColor("#dce6f1")),
    ("ROWBACKGROUNDS",(0, 1), (-1, -1),
     [colors.HexColor("#f5f8fc"), colors.white]),
    ("GRID",         (0, 0), (-1, -1), 0.5, colors.HexColor("#bbbbbb")),
    ("TOPPADDING",   (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
    ("LEFTPADDING",  (0, 0), (-1, -1), 8),
]))
story += [tbl, SP(4),
          P("Tablo 1: Model karşılaştırması (zamansal ayrım, test ayı = Ekim 2023)", CAPTION)]

story += [
    P("Doğrusal regresyonun baseline'ı da geride bırakması, talep ile zaman değişkenleri "
      "arasındaki ilişkinin doğrusal olmadığını kanıtlamaktadır. Gradient Boosting marjinal "
      "olarak önde çıksa da; yorumlanabilir özellik önemleri ve stabil çapraz doğrulama "
      "davranışı nedeniyle <b>Random Forest</b> tercih edilmiştir. Baseline'a göre MAE "
      "iyileşmesi <b>%31,5</b>'tir."),
    P("4 katlı çapraz doğrulama (birini-dışarıda-bırak aylık): "
      "ortalama <b>R² = 0,762 ± 0,143</b>. Nisan'ın görece düşük skoru (0,532), "
      "Ramazan Bayramı ve 23 Nisan gibi düzensiz tatillerin standart zaman özellikleriyle "
      "tam yakalanamayan talep sapmalarını içermesiyle açıklanmaktadır."),
    P("<b>Özellik önem hiyerarşisi:</b> Saat (%66) ve tatil (%21) talebi belirleyen "
      "baskın etkenlerdir. Bu hiyerarşi, şehir içi ulaşım talebinin öncelikle günün "
      "saatine, ikincil olarak takvim etkisine bağlı olduğunu ortaya koymaktadır."),
    SP(),
]

# 5. Sonuç
story += [
    P("5. Sonuç ve Sınırlamalar", H1), HR(),
    P("Bulgular, İstanbul otobüs talebinin üç temel eksen etrafında şekillendiğini ortaya "
      "koymaktadır: (1) commute odaklı günlük ritim, (2) eğitim takvimine bağlı mevsimsel "
      "dalgalanma, (3) az sayıda yoğun koridorda coğrafi toplanma. Zamansal özelliklerle "
      "eğitilen Random Forest modeli, bu yapıyı R² = 0,755 ile başarıyla temsil etmekte "
      "ve baseline'a göre anlamlı bir iyileşme sunmaktadır."),
    P("<b>Sınırlamalar:</b>"),
    B("Yalnızca 4 ay ve tek ulaşım modu (otobüs) kapsanmıştır; raylı sistem ve deniz ulaşımı "
      "karşılaştırma dışında kalmıştır."),
    B("Hava durumu, büyük kentsel etkinlikler (konser, maç, miting), yol kapanmaları gibi "
      "dış değişkenler modele dahil edilmemiştir."),
    B("Coğrafi town verisi sistematik hata içermekte olup uygulanan veri güdümlü temizlik "
      "hatanın büyük bölümünü gidermiş olmakla birlikte, resmi bir referans veri seti (GPS "
      "koordinatları) olmaksızın tam bütünlük garanti edilememektedir."),
    SP(),
]

# Kaynakça
story += [
    P("Kaynakça", H1), HR(),
    P("İstanbul Büyükşehir Belediyesi Açık Veri Portalı: "
      "https://data.ibb.gov.tr/dataset/hourly-public-transport-data-set"),
    P("Lisans: İstanbul Büyükşehir Belediyesi Açık Veri Lisansı — "
      "https://data.ibb.gov.tr/license"),
]

# ── Oluştur ──────────────────────────────────────────────────────────────────
def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont(FONT, 8)
    canvas.setFillColor(colors.gray)
    canvas.drawCentredString(W / 2, 1.5 * cm,
        f"İETT Yolcu Analizi — Veri Bilimi Dönem Projesi 2026 — Sayfa {doc.page}")
    canvas.restoreState()

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=2.5*cm, rightMargin=2.5*cm,
    topMargin=2.5*cm,  bottomMargin=2.5*cm,
    title="İETT Saatlik Yolcu Analizi — Veri Bilimi Dönem Projesi",
    author="Gürkan Kılınç",
    subject="Veri Bilimi Dönem Projesi Raporu",
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(f"PDF oluşturuldu: {OUTPUT}")
