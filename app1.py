import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Burcuna Göre Kaos Haritan",
    page_icon="✨",
    layout="centered"
)

# ---------------------------------------------------
# Arka plan resmi varsa kullan
# Dosya adı: arka_plan.png
# Aynı klasörde olmalı
# ---------------------------------------------------
def get_base64_image(image_path):
    path = Path(image_path)
    if path.exists():
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

bg_base64 = get_base64_image("arka_plan.png")

# ---------------------------------------------------
# CSS
# ---------------------------------------------------
page_bg = f"""
<style>
html, body, [class*="css"] {{
    font-family: 'Segoe UI', sans-serif;
}}

.stApp {{
    {"background: linear-gradient(rgba(10,10,25,0.45), rgba(10,10,25,0.45)), url('data:image/png;base64," + bg_base64 + "');" if bg_base64 else "background: linear-gradient(135deg, #1b1530 0%, #2d1f4f 40%, #1b274a 100%);"}
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

.main-title {{
    text-align: center;
    font-size: 38px;
    font-weight: 800;
    margin-top: 10px;
    margin-bottom: 6px;
}}

.sub-text {{
    text-align: center;
    font-size: 16px;
    opacity: 0.9;
    margin-bottom: 24px;
}}

.form-card {{
    border-radius: 24px;
    padding: 24px;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.20);
    border: 1px solid rgba(255,255,255,0.14);
    margin-top: 10px;
}}

.success-box,
.result-box,
.info-box {{
    border-radius: 20px;
    padding: 18px 20px;
    margin-top: 16px;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    transition: all 0.3s ease;
    box-shadow: 0 8px 30px rgba(0,0,0,0.18);
}}

.result-box {{
    border: 1px solid rgba(255,255,255,0.16);
}}

.info-box {{
    border: 1px solid rgba(255,255,255,0.12);
}}

.success-box {{
    font-weight: 600;
    border: 1px solid rgba(255,255,255,0.12);
}}

.result-title {{
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 6px;
}}

.result-subtitle {{
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 10px;
}}

.result-text {{
    font-size: 16px;
    line-height: 1.7;
    margin-top: 10px;
}}

.risk-text {{
    font-size: 18px;
    font-weight: 700;
    margin-top: 8px;
    margin-bottom: 6px;
}}

.risk-bar-container {{
    width: 100%;
    height: 14px;
    background: rgba(180,180,180,0.25);
    border-radius: 999px;
    overflow: hidden;
    margin-top: 10px;
    margin-bottom: 8px;
}}

.risk-bar {{
    height: 100%;
    border-radius: 999px;
    transition: width 0.7s ease;
}}

.low {{
    background: linear-gradient(90deg, #00c6ff, #33ffcc);
}}

.medium {{
    background: linear-gradient(90deg, #ffd166, #fca311);
}}

.high {{
    background: linear-gradient(90deg, #ff4d6d, #ff006e);
}}

.footer-note {{
    text-align: center;
    font-size: 13px;
    opacity: 0.75;
    margin-top: 20px;
    margin-bottom: 8px;
}}

.success-box,
.result-box,
.info-box,
.success-box h1,
.success-box h2,
.success-box h3,
.success-box p,
.result-box h1,
.result-box h2,
.result-box h3,
.result-box p,
.info-box h1,
.info-box h2,
.info-box h3,
.info-box p,
.info-box span,
.form-card,
.main-title,
.sub-text {{
    color: inherit;
}}

div[data-baseweb="select"] > div {{
    border-radius: 14px !important;
}}

.stNumberInput > div > div > input {{
    border-radius: 14px !important;
}}

.stButton > button {{
    width: 100%;
    border-radius: 16px !important;
    padding: 0.75rem 1rem;
    font-size: 17px;
    font-weight: 700;
    border: none;
    background: linear-gradient(90deg, #a855f7, #ec4899);
    color: white;
    box-shadow: 0 6px 20px rgba(168,85,247,0.30);
}}

.stButton > button:hover {{
    opacity: 0.92;
}}

@media (prefers-color-scheme: dark) {{
    .main-title,
    .sub-text,
    .form-card {{
        color: #ffffff;
    }}

    .form-card {{
        background: rgba(15, 20, 40, 0.72);
    }}

    .result-box {{
        background: rgba(15, 20, 40, 0.82);
        color: #ffffff;
    }}

    .info-box {{
        background: rgba(25, 35, 70, 0.68);
        color: #ffffff;
    }}

    .success-box {{
        background: rgba(0, 200, 120, 0.18);
        color: #b9ffd9;
    }}

    .risk-bar-container {{
        background: rgba(255,255,255,0.18);
    }}
}}

@media (prefers-color-scheme: light) {{
    .main-title,
    .sub-text,
    .form-card {{
        color: #111111;
    }}

    .form-card {{
        background: rgba(255, 255, 255, 0.78);
    }}

    .result-box {{
        background: rgba(255, 255, 255, 0.84);
        color: #111111;
    }}

    .info-box {{
        background: rgba(245, 245, 255, 0.82);
        color: #111111;
    }}

    .success-box {{
        background: rgba(0, 150, 80, 0.12);
        color: #006644;
    }}

    .risk-bar-container {{
        background: rgba(80,80,80,0.15);
    }}
}}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ---------------------------------------------------
# Burç hesaplama
# ---------------------------------------------------
def burc_hesapla(gun, ay):
    if (ay == 3 and gun >= 21) or (ay == 4 and gun <= 19):
        return "Koç"
    elif (ay == 4 and gun >= 20) or (ay == 5 and gun <= 20):
        return "Boğa"
    elif (ay == 5 and gun >= 21) or (ay == 6 and gun <= 20):
        return "İkizler"
    elif (ay == 6 and gun >= 21) or (ay == 7 and gun <= 22):
        return "Yengeç"
    elif (ay == 7 and gun >= 23) or (ay == 8 and gun <= 22):
        return "Aslan"
    elif (ay == 8 and gun >= 23) or (ay == 9 and gun <= 22):
        return "Başak"
    elif (ay == 9 and gun >= 23) or (ay == 10 and gun <= 22):
        return "Terazi"
    elif (ay == 10 and gun >= 23) or (ay == 11 and gun <= 21):
        return "Akrep"
    elif (ay == 11 and gun >= 22) or (ay == 12 and gun <= 21):
        return "Yay"
    elif (ay == 12 and gun >= 22) or (ay == 1 and gun <= 19):
        return "Oğlak"
    elif (ay == 1 and gun >= 20) or (ay == 2 and gun <= 18):
        return "Kova"
    elif (ay == 2 and gun >= 19) or (ay == 3 and gun <= 20):
        return "Balık"
    else:
        return "Bilinmiyor"

# ---------------------------------------------------
# Yorum verileri
# ---------------------------------------------------
yorumlar = {
    "Koç": {
        "alışveriş": {
            "puan": 82,
            "risk": "Yüksek",
            "yorum": "Bu alanda kaos enerjin oldukça yüksek görünüyor. Özellikle hızlı karar verme, ani hevesler ve ilk gördüğüne yönelme eğilimin alışveriş sırasında gereksiz harcamalara ya da sonradan pişman olacağın seçimlere neden olabilir.",
            "güçlü": "Hızlı karar verirsin, enerjin yüksektir, cesur davranırsın.",
            "zayıf": "Sabırsızlık ve anlık heveslerle gereksiz risk alabilirsin.",
            "motto": "Önce sepete ekle, sonra bir daha düşün."
        },
        "mesajlaşma": {
            "puan": 76,
            "risk": "Yüksek",
            "yorum": "Mesajlaşırken hızın bazen duygularının önüne geçebilir. Düşünmeden cevap verme eğilimin küçük yanlış anlaşılmaları büyütebilir.",
            "güçlü": "Samimi, net ve enerjik iletişim kurarsın.",
            "zayıf": "Ani çıkışların ve sabırsızlığın sorun yaratabilir.",
            "motto": "Göndermeden önce bir kez daha oku."
        },
        "hazırlanma": {
            "puan": 68,
            "risk": "Orta",
            "yorum": "Son dakikaya bırakma eğilimin olsa da enerjin sayesinde toparlayabiliyorsun. Kaos var ama kontrol edilebilir düzeyde.",
            "güçlü": "Pratik ve hızlı toparlanırsın.",
            "zayıf": "Plansızlık seni gereksiz strese sokabilir.",
            "motto": "Hız iyidir, panik değil."
        },
        "plan yapma": {
            "puan": 71,
            "risk": "Yüksek",
            "yorum": "Plan yaparken ilk heyecanın çok güçlü ama uzun vadeli sabır konusunda zorlanabilirsin.",
            "güçlü": "Başlatma gücün çok yüksektir.",
            "zayıf": "Sürdürülebilirlik kısmında zorlanabilirsin.",
            "motto": "Başlamak kadar sürdürmek de önemli."
        },
        "sosyalleşme": {
            "puan": 84,
            "risk": "Yüksek",
            "yorum": "Sosyalleşmede çok enerjik ve dikkat çekicisin. Ama bazen ortamın ritmini fazla yükseltebilirsin.",
            "güçlü": "Lider ruhlu ve girişkensin.",
            "zayıf": "Fazla baskın durabilirsin.",
            "motto": "Parla ama herkese de alan bırak."
        }
    },

    "Boğa": {
        "alışveriş": {
            "puan": 45,
            "risk": "Orta",
            "yorum": "Alışverişte genelde temkinlisin ama konfor alanına hitap eden şeylerde dayanıklılığın düşebilir.",
            "güçlü": "Kaliteli seçim yaparsın, kolay kolay dağılmazsın.",
            "zayıf": "Lüks ve rahatlık seni fazla çekebilir.",
            "motto": "İhtiyaç mı, keyif mi?"
        },
        "mesajlaşma": {
            "puan": 38,
            "risk": "Düşük",
            "yorum": "Mesajlaşmada daha sakin ve kontrollüsün. Genelde ani kaos çıkarmazsın.",
            "güçlü": "İstikrarlı ve güven verici bir üslubun vardır.",
            "zayıf": "Bazen fazla geç dönüş yapabilirsin.",
            "motto": "Yavaş ama sağlam."
        },
        "hazırlanma": {
            "puan": 41,
            "risk": "Orta",
            "yorum": "Hazırlanırken acele etmeyi sevmezsin. Bu yüzden gecikme riski oluşabilir ama genel olarak düzenlisin.",
            "güçlü": "Özenli ve estetik seçimler yaparsın.",
            "zayıf": "Fazla rahat davranabilirsin.",
            "motto": "Sakin hazırlan, zamanı unutma."
        },
        "plan yapma": {
            "puan": 34,
            "risk": "Düşük",
            "yorum": "Plan yaparken sabırlı ve gerçekçisin. Kaos üretmekten çok düzen kurmaya yatkınsın.",
            "güçlü": "Kararlı ve güvenilirsin.",
            "zayıf": "Esneklik konusunda zorlanabilirsin.",
            "motto": "Plan varsa huzur vardır."
        },
        "sosyalleşme": {
            "puan": 47,
            "risk": "Orta",
            "yorum": "Sosyalleşmede seçicisin. Her ortama hemen açılmazsın ama açıldığında samimi ve istikrarlısın.",
            "güçlü": "Güven veren ve sıcak bir enerjin vardır.",
            "zayıf": "İnatçılık bazen seni geri tutabilir.",
            "motto": "Az kişi, öz bağ."
        }
    },

    "İkizler": {
        "alışveriş": {
            "puan": 67,
            "risk": "Orta",
            "yorum": "Alışverişte merak duygun seni farklı şeylere çekebilir. Kararsızlıkla ani heves arasında gidip gelebilirsin.",
            "güçlü": "Trendleri hızlı fark edersin.",
            "zayıf": "Fikir değiştirmen çok hızlı olabilir.",
            "motto": "Her parlak şey gerekli değildir."
        },
        "mesajlaşma": {
            "puan": 88,
            "risk": "Yüksek",
            "yorum": "Mesajlaşma alanı senin doğal sahnen. Ama hız, espri ve çok yönlülük bazen karışıklık yaratabilir.",
            "güçlü": "Zeki, hızlı ve eğlenceli iletişim kurarsın.",
            "zayıf": "Ciddiyet gereken yerde dağılabilirsin.",
            "motto": "Hızlı yaz ama net kal."
        },
        "hazırlanma": {
            "puan": 59,
            "risk": "Orta",
            "yorum": "Hazırlanırken dikkatini birden fazla şeye dağıtabilirsin. Bu da minik kaoslar doğurur.",
            "güçlü": "Çabuk adapte olursun.",
            "zayıf": "Dikkat dağınıklığı yaşayabilirsin.",
            "motto": "Bir anda üç şey değil, önce bir şey."
        },
        "plan yapma": {
            "puan": 63,
            "risk": "Orta",
            "yorum": "Plan yapmayı seversin ama sürekli yeni fikirler çıktığı için planda kalmakta zorlanabilirsin.",
            "güçlü": "Yaratıcı ve esnek düşünürsün.",
            "zayıf": "Süreklilik zorlayabilir.",
            "motto": "Fikir çoksa filtre şart."
        },
        "sosyalleşme": {
            "puan": 90,
            "risk": "Yüksek",
            "yorum": "Sosyalleşmede çok rahatsın. Ancak aynı anda her yere yetişmeye çalışmak enerjini dağıtabilir.",
            "güçlü": "Uyumlu, konuşkan ve hareketlisin.",
            "zayıf": "Yüzeysellik hissi oluşturabilirsin.",
            "motto": "Her sohbet derin olmak zorunda değil ama anlamlı olabilir."
        }
    },

    "Yengeç": {
        "alışveriş": {
            "puan": 52,
            "risk": "Orta",
            "yorum": "Duygusal anlarında alışveriş bir kaçış alanına dönüşebilir. Ruh halin seçimlerini etkileyebilir.",
            "güçlü": "İçgüdülerin kuvvetlidir.",
            "zayıf": "Duygusal karar verebilirsin.",
            "motto": "Kalbin güzel, bütçen de öyle kalsın."
        },
        "mesajlaşma": {
            "puan": 61,
            "risk": "Orta",
            "yorum": "Mesajlaşmada duygusal tonlara çok açıksın. Bir cümleyi fazla düşünme eğilimin olabilir.",
            "güçlü": "İlgili ve hassas iletişim kurarsın.",
            "zayıf": "Yanlış anlamaya açık olabilirsin.",
            "motto": "Her nokta trip değildir."
        },
        "hazırlanma": {
            "puan": 49,
            "risk": "Orta",
            "yorum": "Hazırlanırken ruh halin belirleyici olabilir. Bazen hızlı, bazen çok yavaş ilerleyebilirsin.",
            "güçlü": "Özenli ve dikkatli davranırsın.",
            "zayıf": "Mooduna göre tempon çok değişebilir.",
            "motto": "Duygu tamam, saat de önemli."
        },
        "plan yapma": {
            "puan": 44,
            "risk": "Orta",
            "yorum": "Planlarında güven ve rahatlık ararsın. Genel olarak kontrollüsün ama duygusal etkiler planı değiştirebilir.",
            "güçlü": "Koruyucu ve düşünceli planlar yaparsın.",
            "zayıf": "Geçmişe fazla takılabilirsin.",
            "motto": "Güven iyidir, erteleme değil."
        },
        "sosyalleşme": {
            "puan": 58,
            "risk": "Orta",
            "yorum": "Sosyalleşirken ortamın enerjisini çok hissedersin. Güvende hissettiğin yerde çok sıcak olursun.",
            "güçlü": "Samimi ve derin bağlar kurarsın.",
            "zayıf": "Kolay içine kapanabilirsin.",
            "motto": "Az ama gerçek bağlar."
        }
    },

    "Aslan": {
        "alışveriş": {
            "puan": 74,
            "risk": "Yüksek",
            "yorum": "Gösterişli ve dikkat çekici seçimlere yönelmen alışverişte bütçeyi zorlayabilir.",
            "güçlü": "Tarzın nettir, ne istediğini bilirsin.",
            "zayıf": "İmaj uğruna abartıya kaçabilirsin.",
            "motto": "Parlamak güzel, ölçü daha güzel."
        },
        "mesajlaşma": {
            "puan": 65,
            "risk": "Orta",
            "yorum": "Mesajlaşmada sıcak ve dikkat çekicisin. Ama bazen ilgi bekleme düzeyin yükselirse gerilim oluşabilir.",
            "güçlü": "Etkileyici ve canlı bir iletişimin vardır.",
            "zayıf": "Geri dönüş beklerken sabırsızlanabilirsin.",
            "motto": "Işığın zaten var, zorlamana gerek yok."
        },
        "hazırlanma": {
            "puan": 72,
            "risk": "Yüksek",
            "yorum": "Hazırlanırken görünüş senin için önemlidir. Bu yüzden süre uzayabilir ve son dakika telaşı oluşabilir.",
            "güçlü": "Şık ve özgüvenli görünürsün.",
            "zayıf": "Detaylara fazla takılabilirsin.",
            "motto": "Hazır olmak, mükemmel olmaktan daha önemli."
        },
        "plan yapma": {
            "puan": 55,
            "risk": "Orta",
            "yorum": "Plan yaparken büyük düşünürsün ama bazen detayları gözden kaçırabilirsin.",
            "güçlü": "Vizyoner ve motive edicisin.",
            "zayıf": "Uygulama kısmında dağılabilirsin.",
            "motto": "Sahne güzel, kulis de gerekli."
        },
        "sosyalleşme": {
            "puan": 86,
            "risk": "Yüksek",
            "yorum": "Sosyalleşmede ortamın yıldızı olabilirsin. Fakat fazla merkezde kalmak bazen dengesizlik yaratabilir.",
            "güçlü": "Karizmatik ve enerjik bir duruşun vardır.",
            "zayıf": "Baskın görünme riskin vardır.",
            "motto": "Işığını paylaş, tek başına yakma."
        }
    },

    "Başak": {
        "alışveriş": {
            "puan": 31,
            "risk": "Düşük",
            "yorum": "Alışverişte dikkatli ve seçicisin. Gereksiz harcamalara karşı kontrollü davranırsın.",
            "güçlü": "Mantıklı ve detaycısın.",
            "zayıf": "Fazla inceleyip yorulabilirsin.",
            "motto": "Karar netse huzur da net."
        },
        "mesajlaşma": {
            "puan": 43,
            "risk": "Orta",
            "yorum": "Mesajlaşırken kelimeleri dikkatli seçersin. Ama bazen fazla analiz etmek işleri zorlaştırabilir.",
            "güçlü": "Net ve düzenli iletişim kurarsın.",
            "zayıf": "Aşırı düşünme seni yavaşlatabilir.",
            "motto": "Her mesaj tez olmak zorunda değil."
        },
        "hazırlanma": {
            "puan": 37,
            "risk": "Düşük",
            "yorum": "Hazırlanırken oldukça düzenlisin. Kaos değil sistem kurarsın.",
            "güçlü": "Planlı ve temiz ilerlersin.",
            "zayıf": "Mükemmeliyetçilik geciktirebilir.",
            "motto": "Yeterince iyi de güzeldir."
        },
        "plan yapma": {
            "puan": 29,
            "risk": "Düşük",
            "yorum": "Plan yapmak senin alanın. Düzen, sıralama ve detay konusunda çok iyisin.",
            "güçlü": "Organizasyon gücün yüksektir.",
            "zayıf": "Esneklik zor gelebilir.",
            "motto": "Liste varsa umut vardır."
        },
        "sosyalleşme": {
            "puan": 46,
            "risk": "Orta",
            "yorum": "Sosyalleşirken seçici ve ölçülüsün. Her ortamda hemen açılmayabilirsin.",
            "güçlü": "Gözlem gücün yüksektir.",
            "zayıf": "Çekingen ya da mesafeli görünebilirsin.",
            "motto": "Az konuş, doğru konuş."
        }
    },

    "Terazi": {
        "alışveriş": {
            "puan": 69,
            "risk": "Orta",
            "yorum": "Güzellik ve uyum duygun alışverişte seni etkileyebilir. Kararsızlık da tabloya eklenince işler uzayabilir.",
            "güçlü": "Estetik gözün kuvvetlidir.",
            "zayıf": "Seçim yapmakta zorlanabilirsin.",
            "motto": "Hepsi güzel olabilir ama biri yeter."
        },
        "mesajlaşma": {
            "puan": 58,
            "risk": "Orta",
            "yorum": "Mesajlaşmada nazik ve dengeli davranırsın. Ancak karşı tarafı kırmama çaban netliği azaltabilir.",
            "güçlü": "Kibar ve uyumlu bir üslubun vardır.",
            "zayıf": "Açık olmak yerine yuvarlayabilirsin.",
            "motto": "Nazik ol ama net kal."
        },
        "hazırlanma": {
            "puan": 64,
            "risk": "Orta",
            "yorum": "Hazırlanırken uyum ve görünüş senin için önemlidir. Bu yüzden zaman zaman karar vermek uzayabilir.",
            "güçlü": "Şık ve dengeli görünürsün.",
            "zayıf": "Kararsızlık geciktirebilir.",
            "motto": "Ayna tamam diyorsa çık."
        },
        "plan yapma": {
            "puan": 50,
            "risk": "Orta",
            "yorum": "Plan yaparken herkesin mutlu olmasını istersin. Bu da bazen seni fazla düşünmeye iter.",
            "güçlü": "Adil ve dengeli plan kurarsın.",
            "zayıf": "Karar süreci uzayabilir.",
            "motto": "Mükemmel denge yok, yeterli denge var."
        },
        "sosyalleşme": {
            "puan": 77,
            "risk": "Yüksek",
            "yorum": "Sosyalleşmede uyumlu ve çekicisin. Ancak herkese göre şekillenmeye çalışırsan yorulabilirsin.",
            "güçlü": "İnsan ilişkilerinde doğalsın.",
            "zayıf": "Onay ihtiyacı seni zorlayabilir.",
            "motto": "Herkesi memnun etmek görev değil."
        }
    },

    "Akrep": {
        "alışveriş": {
            "puan": 48,
            "risk": "Orta",
            "yorum": "Alışverişte dışarıdan kontrollü görünsen de bir şeyi gerçekten istersen çok net yönelirsin.",
            "güçlü": "Kararlı ve güçlü seçim yaparsın.",
            "zayıf": "Takıntılı bir odak gelişebilir.",
            "motto": "İstek netse bile sınır önemli."
        },
        "mesajlaşma": {
            "puan": 72,
            "risk": "Yüksek",
            "yorum": "Mesajlaşmada sezgilerin kuvvetli ama derin anlam yükleme eğilimin gerilim yaratabilir.",
            "güçlü": "Yoğun ve güçlü bağ kurarsın.",
            "zayıf": "Fazla yorum yapabilirsin.",
            "motto": "Her sessizlik gizem değildir."
        },
        "hazırlanma": {
            "puan": 53,
            "risk": "Orta",
            "yorum": "Hazırlanırken dışarıdan sakin görünürsün ama içten içe yoğun bir odak yaşarsın.",
            "güçlü": "Kontrollü ve güçlü görünürsün.",
            "zayıf": "Kendi içinde gereksiz gerilim yaratabilirsin.",
            "motto": "Kontrol tamam, baskı gereksiz."
        },
        "plan yapma": {
            "puan": 60,
            "risk": "Orta",
            "yorum": "Plan yaparken stratejik ve sezgiselsin. Ancak esneklik gerektiğinde zorlanabilirsin.",
            "güçlü": "Derin ve güçlü analiz yaparsın.",
            "zayıf": "Bırakman gereken yerde tutunabilirsin.",
            "motto": "Her şeyi kontrol etmek zorunda değilsin."
        },
        "sosyalleşme": {
            "puan": 62,
            "risk": "Orta",
            "yorum": "Sosyalleşmede herkese açılmazsın ama açıldığında çok etkili bir iz bırakabilirsin.",
            "güçlü": "Gizemli ve çekici bir enerjin vardır.",
            "zayıf": "Mesafeli görünebilirsin.",
            "motto": "Az kişi, derin bağ."
        }
    },

    "Yay": {
        "alışveriş": {
            "puan": 66,
            "risk": "Orta",
            "yorum": "Alışverişte özgürlük ve heyecan ararsın. Ani ilhamlarla kontrolsüz seçim yapabilirsin.",
            "güçlü": "Cesur ve farklı şeylere açıksın.",
            "zayıf": "Düşünmeden hareket edebilirsin.",
            "motto": "Macera güzel, fiş de gerçek."
        },
        "mesajlaşma": {
            "puan": 70,
            "risk": "Yüksek",
            "yorum": "Mesajlaşırken çok doğal ve filtresizsin. Bu bazen fazla açık ya da düşüncesiz algılanabilir.",
            "güçlü": "Eğlenceli ve dürüst iletişim kurarsın.",
            "zayıf": "Patavatsız görünebilirsin.",
            "motto": "Doğruluk iyidir, doz da önemli."
        },
        "hazırlanma": {
            "puan": 57,
            "risk": "Orta",
            "yorum": "Hazırlanırken özgür davranırsın. Rutin ve detay seni biraz sıkabilir.",
            "güçlü": "Pratik ve rahat ilerlersin.",
            "zayıf": "Düzensizleşebilirsin.",
            "motto": "Rahat ol ama unutma."
        },
        "plan yapma": {
            "puan": 62,
            "risk": "Orta",
            "yorum": "Plan yaparken büyük resim hoşuna gider ama detaylar seni bunaltabilir.",
            "güçlü": "Vizyonun ve motivasyonun yüksektir.",
            "zayıf": "Detay takibi zorlayabilir.",
            "motto": "Hayal büyük, adım net olsun."
        },
        "sosyalleşme": {
            "puan": 85,
            "risk": "Yüksek",
            "yorum": "Sosyalleşmede eğlenceli, enerjik ve açık bir yapın var. Fakat sınır tanımayan enerji bazen dağılım yaratabilir.",
            "güçlü": "Neşeli ve çekici bir enerjin vardır.",
            "zayıf": "Ciddiyet gereken yerde kaçabilirsin.",
            "motto": "Eğlen ama uçma."
        }
    },

    "Oğlak": {
        "alışveriş": {
            "puan": 33,
            "risk": "Düşük",
            "yorum": "Alışverişte oldukça kontrollüsün. Fayda ve uzun vadeli kullanım senin için önemlidir.",
            "güçlü": "Mantıklı ve disiplinli seçim yaparsın.",
            "zayıf": "Fazla katı davranabilirsin.",
            "motto": "Kalıcı olan kazandırır."
        },
        "mesajlaşma": {
            "puan": 40,
            "risk": "Orta",
            "yorum": "Mesajlaşmada net ve ciddi bir tonun olabilir. Bu bazen mesafe gibi algılanabilir.",
            "güçlü": "Açık ve ölçülü konuşursun.",
            "zayıf": "Soğuk görünebilirsin.",
            "motto": "Az yaz, net yaz."
        },
        "hazırlanma": {
            "puan": 36,
            "risk": "Düşük",
            "yorum": "Hazırlanırken düzen ve sorumluluk ön plandadır. Kaos ihtimali düşüktür.",
            "güçlü": "Dakik ve kontrollüsün.",
            "zayıf": "Rahatlamayı unutabilirsin.",
            "motto": "Planlı olmak şıklığın gizli hali."
        },
        "plan yapma": {
            "puan": 24,
            "risk": "Düşük",
            "yorum": "Plan yapmak senin güçlü alanlarından biri. Yapı kurmak ve hedefe ilerlemek konusunda iyisin.",
            "güçlü": "Disiplinli ve kararlısın.",
            "zayıf": "Kendine fazla yüklenebilirsin.",
            "motto": "Adım adım, sağlam sağlam."
        },
        "sosyalleşme": {
            "puan": 42,
            "risk": "Orta",
            "yorum": "Sosyalleşmede seçici ve dengelisin. Her ortama açılman zaman alabilir.",
            "güçlü": "Güvenilir ve ciddi bir izlenim bırakırsın.",
            "zayıf": "Resmî ya da mesafeli görünebilirsin.",
            "motto": "Az ama saygın."
        }
    },

    "Kova": {
        "alışveriş": {
            "puan": 54,
            "risk": "Orta",
            "yorum": "Alışverişte sıradan olan değil ilginç olan dikkatini çeker. Bu da bazen gereksiz ama özgün seçimler doğurabilir.",
            "güçlü": "Farklı ve yaratıcı seçimler yaparsın.",
            "zayıf": "Pratikliği ikinci plana atabilirsin.",
            "motto": "Özgünlük güzel, işlev de lazım."
        },
        "mesajlaşma": {
            "puan": 63,
            "risk": "Orta",
            "yorum": "Mesajlaşmada zeki ve özgün bir tarzın var. Ama bazen fazla mesafeli ya da beklenmedik görünebilirsin.",
            "güçlü": "Yaratıcı ve farklı iletişim kurarsın.",
            "zayıf": "Duygusal sıcaklık eksik kalabilir.",
            "motto": "Farklı ol ama kopma."
        },
        "hazırlanma": {
            "puan": 47,
            "risk": "Orta",
            "yorum": "Hazırlanırken standart dışı çözümler üretebilirsin. Bazen bu yaratıcılık biraz karışıklık da doğurur.",
            "güçlü": "Özgün ve bağımsızsın.",
            "zayıf": "Düzensizlik oluşabilir.",
            "motto": "Yaratıcılık iyi, süre daha iyi."
        },
        "plan yapma": {
            "puan": 51,
            "risk": "Orta",
            "yorum": "Plan yaparken klasik değil farklı düşünürsün. Ama uygulanabilirlik kısmı zaman zaman zorlayabilir.",
            "güçlü": "Vizyonun yenilikçidir.",
            "zayıf": "Gerçekçilikten uzaklaşabilirsin.",
            "motto": "Fikir uçabilir ama ayak yerde kalsın."
        },
        "sosyalleşme": {
            "puan": 73,
            "risk": "Yüksek",
            "yorum": "Sosyalleşmede farklı ve dikkat çekici bir enerjin vardır. Ama bazen kopuk ya da fazla bağımsız kalabilirsin.",
            "güçlü": "Özgün ve ilgi çekicisin.",
            "zayıf": "Mesafe koyma eğilimin olabilir.",
            "motto": "Bağımsız ol, görünmez değil."
        }
    },

    "Balık": {
        "alışveriş": {
            "puan": 57,
            "risk": "Orta",
            "yorum": "Duyguların ve anlık ruh halin alışveriş kararlarını etkileyebilir. Hayal gücü bazen ihtiyacın önüne geçer.",
            "güçlü": "Sezgisel ve yaratıcı tercihler yaparsın.",
            "zayıf": "Gerçekçilikten uzaklaşabilirsin.",
            "motto": "Kalbin güzel, bütçen de korunsun."
        },
        "mesajlaşma": {
            "puan": 69,
            "risk": "Orta",
            "yorum": "Mesajlaşmada hassas ve duygusal bir tonun vardır. Küçük detaylara büyük anlam yükleyebilirsin.",
            "güçlü": "Empatin yüksektir.",
            "zayıf": "Yanlış anlama riskin vardır.",
            "motto": "Hisset ama hemen karar verme."
        },
        "hazırlanma": {
            "puan": 55,
            "risk": "Orta",
            "yorum": "Hazırlanırken dalgınlık nedeniyle ufak aksilikler yaşayabilirsin. Ama iç dünyan güçlü olduğu için yaratıcı çözümler de bulursun.",
            "güçlü": "Esnek ve sezgiselsin.",
            "zayıf": "Dalgınlık yaşayabilirsin.",
            "motto": "Hayal güzel, çanta da tam olsun."
        },
        "plan yapma": {
            "puan": 58,
            "risk": "Orta",
            "yorum": "Plan yaparken sezgiyle ilerlersin. Fakat net yapı kurmakta zorlanabilirsin.",
            "güçlü": "İlhamın yüksektir.",
            "zayıf": "Belirsizlik uzayabilir.",
            "motto": "Hayal et ama yaz da."
        },
        "sosyalleşme": {
            "puan": 64,
            "risk": "Orta",
            "yorum": "Sosyalleşmede sıcak ve uyumlu görünürsün. Ancak ortamın enerjisinden fazla etkilenebilirsin.",
            "güçlü": "Empatik ve yumuşak bir enerjin vardır.",
            "zayıf": "Sınır koymak zor olabilir.",
            "motto": "Hisset ama kendini kaybetme."
        }
    }
}

# ---------------------------------------------------
# Yardımcılar
# ---------------------------------------------------
def risk_class(puan):
    if puan <= 40:
        return "low"
    elif puan <= 70:
        return "medium"
    return "high"

def ay_gecerli_mi(gun, ay):
    gun_sayilari = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    return 1 <= ay <= 12 and 1 <= gun <= gun_sayilari[ay]

alan_gosterim = {
    "alışveriş": "Alışveriş",
    "mesajlaşma": "Mesajlaşma",
    "hazırlanma": "Hazırlanma",
    "plan yapma": "Plan Yapma",
    "sosyalleşme": "Sosyalleşme"
}

# ---------------------------------------------------
# Başlık
# ---------------------------------------------------
st.markdown('<div class="main-title">✨ Burcuna Göre Kaos Haritan</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-text">Doğum tarihini ve günlük yaşam alanını seç, kaos enerjini keşfet.</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------
# Form
# ---------------------------------------------------
st.markdown('<div class="form-card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    gun = st.number_input("Doğduğun gün", min_value=1, max_value=31, step=1)
with col2:
    ay = st.number_input("Doğduğun ay", min_value=1, max_value=12, step=1)

alan = st.selectbox(
    "Kaos haritanı hangi alanda görmek istiyorsun?",
    ["alışveriş", "mesajlaşma", "hazırlanma", "plan yapma", "sosyalleşme"],
    format_func=lambda x: alan_gosterim[x]
)

hesapla = st.button("Kaos Haritamı Göster")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# Sonuç
# ---------------------------------------------------
if hesapla:
    if not ay_gecerli_mi(gun, ay):
        st.error("Geçerli bir doğum tarihi gir.")
    else:
        burc = burc_hesapla(gun, ay)
        veri = yorumlar[burc][alan]
        puan = veri["puan"]
        risk = veri["risk"]
        yorum = veri["yorum"]
        guclu = veri["güçlü"]
        zayif = veri["zayıf"]
        motto = veri["motto"]
        bar_class = risk_class(puan)

        st.markdown(
            f"""
            <div class="success-box">
                Burcun bulundu: <b>{burc}</b>
            </div>

            <div class="result-box">
                <div class="result-title">♈ {burc} - {alan_gosterim[alan]}</div>
                <div class="risk-text">Kaos Puanı: {puan} / 100</div>

                <div class="risk-bar-container">
                    <div class="risk-bar {bar_class}" style="width: {puan}%;"></div>
                </div>

                <div class="result-subtitle">Risk Seviyesi: {risk}</div>

                <p class="result-text">
                    {yorum}
                </p>
            </div>

            <div class="info-box">
                ⭐ <b>Güçlü Yönün:</b> {guclu}
            </div>

            <div class="info-box">
                ⚠️ <b>Zayıf Yönün:</b> {zayif}
            </div>

            <div class="info-box">
                📝 <b>Motto:</b> {motto}
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown('<div class="footer-note">Modern astroloji temalı mini uygulama</div>', unsafe_allow_html=True)
