import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Burcuna Göre Kaos Haritan",
    page_icon="✨",
    layout="centered"
)

def get_base64_image(image_path):
    path = Path(image_path)
    if path.exists():
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

bg_base64 = get_base64_image("arka_plan.png")

page_bg = f"""
<style>
html, body, [class*="css"] {{
    font-family: 'Segoe UI', sans-serif;
}}

.stApp {{
    {"background: linear-gradient(rgba(20,12,45,0.55), rgba(18,16,55,0.60)), url('data:image/png;base64," + bg_base64 + "');" if bg_base64 else "background: linear-gradient(135deg, #24164a 0%, #2e1d5c 45%, #1d2758 100%);"}
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* Genel yazılar */
.main-title {{
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-top: 20px;
    margin-bottom: 10px;
    color: #ffffff !important;
}}

.sub-text {{
    text-align: center;
    font-size: 18px;
    color: rgba(255,255,255,0.88) !important;
    margin-bottom: 30px;
}}

.footer-note {{
    text-align: center;
    font-size: 13px;
    color: rgba(255,255,255,0.55) !important;
    margin-top: 22px;
    margin-bottom: 8px;
}}

/* Label yazıları */
label, .stNumberInput label, .stSelectbox label, .stTextInput label {{
    color: rgba(255,255,255,0.92) !important;
    font-weight: 600 !important;
}}

/* Streamlit input label düzeltme */
div[data-testid="stNumberInput"] label,
div[data-testid="stSelectbox"] label {{
    color: rgba(255,255,255,0.92) !important;
    font-weight: 600 !important;
}}

/* Input kutuları */
.stNumberInput > div > div > input {{
    background: rgba(255,255,255,0.92) !important;
    color: #1a1a1a !important;
    border-radius: 16px !important;
    border: none !important;
}}

div[data-baseweb="select"] > div {{
    background: rgba(255,255,255,0.92) !important;
    color: #1a1a1a !important;
    border-radius: 16px !important;
    border: none !important;
}}

/* Büyük üst beyaz barı gizlemesin diye spacing ayarı */
.block-container {{
    padding-top: 2rem;
    padding-bottom: 2rem;
}}

/* Buton */
.stButton > button {{
    width: auto;
    min-width: 220px;
    border-radius: 18px !important;
    padding: 0.85rem 1.2rem;
    font-size: 17px;
    font-weight: 700;
    border: none;
    color: white;
    background: linear-gradient(90deg, #a855f7, #ec4899);
    box-shadow: 0 8px 24px rgba(236,72,153,0.32);
}}

.stButton > button:hover {{
    opacity: 0.95;
}}

/* Sonuç kutuları */
.success-box,
.result-box,
.info-box {{
    border-radius: 20px;
    padding: 18px 20px;
    margin-top: 16px;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    transition: all 0.3s ease;
    box-shadow: 0 8px 30px rgba(0,0,0,0.20);
}}

.success-box {{
    background: rgba(0, 200, 120, 0.16);
    color: #c7ffe1;
    border: 1px solid rgba(255,255,255,0.10);
    font-weight: 600;
}}

.result-box {{
    background: rgba(12, 18, 38, 0.78);
    color: #ffffff;
    border: 1px solid rgba(255,255,255,0.14);
}}

.info-box {{
    background: rgba(25, 35, 70, 0.62);
    color: #ffffff;
    border: 1px solid rgba(255,255,255,0.10);
}}

.result-title {{
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 6px;
    color: #ffffff;
}}

.result-subtitle {{
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 10px;
    color: #ffffff;
}}

.result-text {{
    font-size: 16px;
    line-height: 1.7;
    margin-top: 10px;
    color: rgba(255,255,255,0.92);
}}

.risk-text {{
    font-size: 18px;
    font-weight: 700;
    margin-top: 8px;
    margin-bottom: 6px;
    color: #ffffff;
}}

.risk-bar-container {{
    width: 100%;
    height: 14px;
    background: rgba(255,255,255,0.18);
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

/* Streamlit varsayılan bazı koyu yazıları bastır */
p, h1, h2, h3, h4, h5, h6, span, div {{
    color: inherit;
}}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

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
    return "Bilinmiyor"

yorumlar = {
    "Koç": {
        "alışveriş": {
            "puan": 82,
            "risk": "Yüksek",
            "yorum": "Bu alanda kaos enerjin oldukça yüksek görünüyor. Özellikle hızlı karar verme, ani hevesler ve ilk gördüğüne yönelme eğilimin alışveriş sırasında gereksiz harcamalara ya da sonradan pişman olacağın seçimlere neden olabilir.",
            "güçlü": "Hızlı karar verirsin, enerjin yüksektir, cesur davranırsın.",
            "zayıf": "Sabırsızlık ve anlık heveslerle gereksiz risk alabilirsin.",
            "motto": "Önce sepete ekle, sonra bir daha düşün."
        }
    }
}

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

st.markdown('<div class="main-title">✨ Burcuna Göre Kaos Haritan</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Doğum tarihini ve günlük yaşam alanını seç, kaos enerjini keşfet.</div>', unsafe_allow_html=True)

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

if hesapla:
    if not ay_gecerli_mi(gun, ay):
        st.error("Geçerli bir doğum tarihi gir.")
    else:
        burc = burc_hesapla(gun, ay)
        if burc == "Koç":
            veri = yorumlar["Koç"]["alışveriş"] if alan not in yorumlar["Koç"] else yorumlar["Koç"][alan]
        else:
            veri = {
                "puan": 60,
                "risk": "Orta",
                "yorum": "Bu alan için yorum hazırlandı. Burcunun enerjisi burada orta düzeyde kaos gösteriyor.",
                "güçlü": "Uyum sağlama gücün yüksek.",
                "zayıf": "Bazen kararsız kalabilirsin.",
                "motto": "Dengeyi koru."
            }

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
                <div class="result-title">{burc} - {alan_gosterim[alan]}</div>
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
