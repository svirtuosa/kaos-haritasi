import streamlit as st

st.set_page_config(
    page_title="Burcuna Göre Senin Haritan",
    page_icon="✨",
    layout="centered"
)

YORUMLAR = {
    "Koç": {
        "alışveriş": {
            "kaos_tipi": "Hızlı ve dürtüsel karar veren",
            "risk": 82,
            "guclu": "Hızlı karar alman",
            "zayif": "Sonradan pişman olabilmen",
            "uyari": "Sepete atmadan önce 10 saniye düşün.",
            "motto": "Hız güzel, kontrol daha güzel."
        },
        "mesajlaşma": {
            "kaos_tipi": "Anlık tepki veren",
            "risk": 75,
            "guclu": "Açık ve net olman",
            "zayif": "Sabırsız yazman",
            "uyari": "İlk yazdığını hemen gönderme.",
            "motto": "Netlik iyidir, hız her zaman değil."
        },
        "hazırlanma": {
            "kaos_tipi": "Son anda hızlanan",
            "risk": 80,
            "guclu": "Krizde toparlanman",
            "zayif": "Aceleden bir şeyi unutman",
            "uyari": "Çıkmadan önce son kontrol yap.",
            "motto": "Koşmak yerine planla."
        },
        "plan yapma": {
            "kaos_tipi": "Başlatan ama çabuk sıkılan",
            "risk": 70,
            "guclu": "Enerjik başlangıç yapman",
            "zayif": "Sabırsızlık",
            "uyari": "Büyük planı küçük adımlara böl.",
            "motto": "Başlamak kadar sürdürmek de önemli."
        },
        "sosyalleşme": {
            "kaos_tipi": "Ortama hızlı giren",
            "risk": 68,
            "guclu": "Özgüvenin",
            "zayif": "Fazla baskın olabilmen",
            "uyari": "Biraz da karşı tarafı dinle.",
            "motto": "Enerjin güçlü, dozu önemli."
        }
    },
    "Boğa": {
        "alışveriş": {
            "kaos_tipi": "Kaliteye takılan seçici",
            "risk": 55,
            "guclu": "Mantıklı seçim yapman",
            "zayif": "Fazla oyalanman",
            "uyari": "Mükemmel ürün diye fazla bekleme.",
            "motto": "İyi seçim sakin kafayla gelir."
        },
        "mesajlaşma": {
            "kaos_tipi": "Yavaş ama sağlam cevap veren",
            "risk": 48,
            "guclu": "Düşünerek yazman",
            "zayif": "Geç dönmen",
            "uyari": "Bazen kısa cevap da yeterlidir.",
            "motto": "Az ama öz."
        },
        "hazırlanma": {
            "kaos_tipi": "Rahatına göre hazırlanan",
            "risk": 50,
            "guclu": "Sakin kalman",
            "zayif": "Fazla yavaş olman",
            "uyari": "Konfor uğruna geç kalma.",
            "motto": "Rahatlık güzel, zaman da değerli."
        },
        "plan yapma": {
            "kaos_tipi": "Güvenli alanda kalan",
            "risk": 45,
            "guclu": "İstikrarın",
            "zayif": "Değişime direnmen",
            "uyari": "Esneklik bazen işleri kolaylaştırır.",
            "motto": "Sağlam plan, açık zihinle güçlenir."
        },
        "sosyalleşme": {
            "kaos_tipi": "Seçici ama sıcak",
            "risk": 42,
            "guclu": "Güven veren tavrın",
            "zayif": "İlk etapta mesafeli olman",
            "uyari": "Herkesin sana alışması biraz zaman alabilir.",
            "motto": "Yavaş yakınlaşmak da bir güçtür."
        }
    },
    "İkizler": {
        "alışveriş": {
            "kaos_tipi": "Kararsız ama meraklı",
            "risk": 78,
            "guclu": "Çok seçenek değerlendirebilmen",
            "zayif": "Karar verememen",
            "uyari": "İki seçenekten sonra fazlasını kapat.",
            "motto": "Her seçenek gerekli değil."
        },
        "mesajlaşma": {
            "kaos_tipi": "Hızlı ve dağınık iletişim kuran",
            "risk": 83,
            "guclu": "Sohbeti akıtman",
            "zayif": "Konudan konuya atlaman",
            "uyari": "Bir mesajda tek konuya odaklan.",
            "motto": "Zeka hızla parlar, netlikle kalır."
        },
        "hazırlanma": {
            "kaos_tipi": "Aynı anda beş şey yapan",
            "risk": 74,
            "guclu": "Çabuk hareket etmen",
            "zayif": "Dikkat dağınıklığı",
            "uyari": "Önce kıyafet, sonra çanta.",
            "motto": "Çok şey değil, doğru sıra."
        },
        "plan yapma": {
            "kaos_tipi": "Çok fikirli ama dağılmaya açık",
            "risk": 79,
            "guclu": "Yaratıcılığın",
            "zayif": "İstikrar sorunu",
            "uyari": "İki hedef seç, on tane değil.",
            "motto": "Az plan, daha çok sonuç."
        },
        "sosyalleşme": {
            "kaos_tipi": "Ortamın nabzını alan konuşkan",
            "risk": 60,
            "guclu": "Uyum sağlayabilmen",
            "zayif": "Yüzeysellik",
            "uyari": "Bazen daha derin bağ kur.",
            "motto": "İletişim sadece hız değil, bağdır."
        }
    },
    "Yengeç": {
        "alışveriş": {
            "kaos_tipi": "Duygusal karar veren",
            "risk": 69,
            "guclu": "İçine sinen şeyi seçmen",
            "zayif": "Duygusal etkilenme",
            "uyari": "Mood alışverişi yapma.",
            "motto": "His önemli, bütçe de öyle."
        },
        "mesajlaşma": {
            "kaos_tipi": "İma arayan hassas iletişimci",
            "risk": 77,
            "guclu": "Duyguları sezmen",
            "zayif": "Gereğinden fazla anlam yüklemen",
            "uyari": "Her kısa cevap soğukluk değildir.",
            "motto": "Kalbin kadar mantığını da dinle."
        },
        "hazırlanma": {
            "kaos_tipi": "Ruh hâline göre ilerleyen",
            "risk": 63,
            "guclu": "Ortama uygun hazırlanman",
            "zayif": "Kararsız kalman",
            "uyari": "İlk seçtiğine biraz güven.",
            "motto": "Duygu yön verir, karar bitirir."
        },
        "plan yapma": {
            "kaos_tipi": "Güvenli alan planlayıcısı",
            "risk": 58,
            "guclu": "Detay düşünmen",
            "zayif": "Fazla endişelenmen",
            "uyari": "Olmamış sorunlar için yorulma.",
            "motto": "Huzur, kontrolle değil dengeyle gelir."
        },
        "sosyalleşme": {
            "kaos_tipi": "Yakın hissetmeden açılmayan",
            "risk": 52,
            "guclu": "Samimi bağ kurman",
            "zayif": "Alınmaya açık olman",
            "uyari": "Herkes senin kadar derin olmayabilir.",
            "motto": "Samimiyet seçicilikle güzeldir."
        }
    },
    "Aslan": {
        "alışveriş": {
            "kaos_tipi": "İddialı seçim yapan",
            "risk": 72,
            "guclu": "Kendine yakışanı seçmen",
            "zayif": "Gösterişli olana kayman",
            "uyari": "Parlak olan her zaman gerekli değildir.",
            "motto": "Işıltı güzel, denge daha güzel."
        },
        "mesajlaşma": {
            "kaos_tipi": "İlgi bekleyen net iletişimci",
            "risk": 66,
            "guclu": "Kendini açık ifade etmen",
            "zayif": "Yanıt beklerken sabırsız olman",
            "uyari": "Herkes senin hızında yaşamıyor.",
            "motto": "Özgüven iyi, sabır da bir güç."
        },
        "hazırlanma": {
            "kaos_tipi": "Etkileyici görünmeye odaklanan",
            "risk": 64,
            "guclu": "Stil sahibi olman",
            "zayif": "Fazla zaman harcaman",
            "uyari": "Mükemmel görünmek için geç kalma.",
            "motto": "Işıltı zamanında daha çok parlar."
        },
        "plan yapma": {
            "kaos_tipi": "Büyük düşünen lider",
            "risk": 57,
            "guclu": "Yön belirlemen",
            "zayif": "Detay atlaman",
            "uyari": "Vizyon kadar uygulama da gerek.",
            "motto": "Büyük hedef, sağlam adımla yürür."
        },
        "sosyalleşme": {
            "kaos_tipi": "Ortamı canlandıran merkez",
            "risk": 61,
            "guclu": "Çekiciliğin",
            "zayif": "Bazen fazla görünür olman",
            "uyari": "Işıltını paylaş, domine etme.",
            "motto": "Parlamak güzel, alan açmak daha güzel."
        }
    },
    "Başak": {
        "alışveriş": {
            "kaos_tipi": "İnce eleyip sık dokuyan",
            "risk": 44,
            "guclu": "Karşılaştırma yapman",
            "zayif": "Fazla detayda boğulman",
            "uyari": "Yüz yorum okumak zorunda değilsin.",
            "motto": "Detay faydalıdır, fazlası yorar."
        },
        "mesajlaşma": {
            "kaos_tipi": "Ölçülü ve dikkatli yazan",
            "risk": 46,
            "guclu": "Düzgün iletişim kurman",
            "zayif": "Fazla düzeltme yapman",
            "uyari": "Mesaj tez değil.",
            "motto": "Kusursuzluk yerine yeterlilik."
        },
        "hazırlanma": {
            "kaos_tipi": "Kontrollü hazırlanan",
            "risk": 38,
            "guclu": "Düzenli olman",
            "zayif": "Küçük şeylere takılman",
            "uyari": "Her şey tam olmak zorunda değil.",
            "motto": "Düzen iyi, esneklik rahatlatır."
        },
        "plan yapma": {
            "kaos_tipi": "Mükemmeliyetçi planlayıcı",
            "risk": 52,
            "guclu": "Organizasyon becerin",
            "zayif": "Küçük aksaklıklara fazla takılman",
            "uyari": "Planın amacı kontrol değil kolaylıktır.",
            "motto": "İyi plan sade plandır."
        },
        "sosyalleşme": {
            "kaos_tipi": "Seçici ve gözlemci",
            "risk": 41,
            "guclu": "İnsanları iyi analiz etmen",
            "zayif": "Fazla eleştirel görünmen",
            "uyari": "Herkes senden aynı düzeni beklemez.",
            "motto": "İnce bak, sert bakma."
        }
    },
    "Terazi": {
        "alışveriş": {
            "kaos_tipi": "Kararsız ama estetik odaklı",
            "risk": 73,
            "guclu": "Zevkli seçim yapman",
            "zayif": "İki seçenek arasında kalman",
            "uyari": "En güzel değil, en doğru olanı da düşün.",
            "motto": "Denge, karar vermekle başlar."
        },
        "mesajlaşma": {
            "kaos_tipi": "Nazik ama fazla düşünen",
            "risk": 68,
            "guclu": "Kibar iletişimin",
            "zayif": "Yanıtı fazla düzenlemen",
            "uyari": "Her cevap diplomatik olmak zorunda değil.",
            "motto": "Netlik de kibarlığın parçasıdır."
        },
        "hazırlanma": {
            "kaos_tipi": "Kombin arasında sıkışan",
            "risk": 76,
            "guclu": "Uyum duygun",
            "zayif": "Seçim gecikmesi",
            "uyari": "İlk iki seçenekten birini seç.",
            "motto": "Zarafet, kararla tamamlanır."
        },
        "plan yapma": {
            "kaos_tipi": "Herkese uyan plan arayan",
            "risk": 67,
            "guclu": "Denge kurman",
            "zayif": "Kararsızlık",
            "uyari": "Herkesi memnun etmek tek hedef olmasın.",
            "motto": "Denge bazen seçim yapmaktır."
        },
        "sosyalleşme": {
            "kaos_tipi": "Uyumlu ve sevilen",
            "risk": 50,
            "guclu": "Ortamı yumuşatman",
            "zayif": "Hayır diyememen",
            "uyari": "Uyum uğruna kendini yorma.",
            "motto": "Zarafet sınırla güçlenir."
        }
    },
    "Akrep": {
        "alışveriş": {
            "kaos_tipi": "Az ama iddialı seçim yapan",
            "risk": 58,
            "guclu": "Ne istediğini bilmen",
            "zayif": "Takıntılı karşılaştırma yapman",
            "uyari": "Gizli anlam aramayı bırak.",
            "motto": "Seçim netse huzur da nettir."
        },
        "mesajlaşma": {
            "kaos_tipi": "Satır arası okuyan yoğun iletişimci",
            "risk": 84,
            "guclu": "Derin sezgin",
            "zayif": "Fazla analiz etmen",
            "uyari": "Her nokta koyma bir mesaj değildir.",
            "motto": "Derinlik güzel, kurgu yorar."
        },
        "hazırlanma": {
            "kaos_tipi": "Kontrollü ama gizli stresli",
            "risk": 56,
            "guclu": "Krizi belli etmeden yönetmen",
            "zayif": "İçten gerilmen",
            "uyari": "Her şeyi tek başına taşımaya çalışma.",
            "motto": "Kontrol sakinlikle güçlenir."
        },
        "plan yapma": {
            "kaos_tipi": "Stratejik ve kuşkucu",
            "risk": 60,
            "guclu": "İleri düşünmen",
            "zayif": "Fazla ihtimal kurman",
            "uyari": "Her olasılık tehdit değildir.",
            "motto": "Strateji güvenle yürür."
        },
        "sosyalleşme": {
            "kaos_tipi": "Mesafeli ama etkileyici",
            "risk": 54,
            "guclu": "Güçlü duruşun",
            "zayif": "Kolay açılmaman",
            "uyari": "Gizem güzel ama duvar olmasın.",
            "motto": "Derinlik bağlantıyla anlam kazanır."
        }
    },
    "Yay": {
        "alışveriş": {
            "kaos_tipi": "Hevesle alan özgür ruh",
            "risk": 71,
            "guclu": "Rahat karar vermen",
            "zayif": "Anı yaşarken bütçeyi unutman",
            "uyari": "İndirim heyecanı bütçe planı değildir.",
            "motto": "Özgürlük, kontrolü dışlamaz."
        },
        "mesajlaşma": {
            "kaos_tipi": "Samimi ama filtresiz",
            "risk": 74,
            "guclu": "Doğal olman",
            "zayif": "Pat diye yazman",
            "uyari": "Espri dozu kişiye göre değişir.",
            "motto": "Dürüstlük nezaketle güçlenir."
        },
        "hazırlanma": {
            "kaos_tipi": "Son dakika ama yüksek enerji",
            "risk": 72,
            "guclu": "Pratik olman",
            "zayif": "Detay atlaman",
            "uyari": "Çanta kontrolü yapmadan çıkma.",
            "motto": "Özgür akışa küçük kontrol ekle."
        },
        "plan yapma": {
            "kaos_tipi": "Büyük düşünüp detayı sevmeyen",
            "risk": 70,
            "guclu": "Vizyonun",
            "zayif": "Süreci küçümsemen",
            "uyari": "Yol haritası da maceranın parçası.",
            "motto": "Heyecan planla daha uzağa gider."
        },
        "sosyalleşme": {
            "kaos_tipi": "Rahat ve enerjik",
            "risk": 52,
            "guclu": "Pozitifliğin",
            "zayif": "Fazla rahat davranman",
            "uyari": "Her ortam senin hızında olmayabilir.",
            "motto": "Özgür ruh, ölçüyle parıldar."
        }
    },
    "Oğlak": {
        "alışveriş": {
            "kaos_tipi": "İhtiyaç odaklı gerçekçi",
            "risk": 34,
            "guclu": "Mantıklı davranman",
            "zayif": "Fazla kuralcı olman",
            "uyari": "Bazen keyif için de seçim yapılır.",
            "motto": "Disiplin güzeldir, katılık değil."
        },
        "mesajlaşma": {
            "kaos_tipi": "Kısa ve net",
            "risk": 39,
            "guclu": "Açıklığın",
            "zayif": "Soğuk görünmen",
            "uyari": "Bir emoji dünyayı değiştirebilir.",
            "motto": "Ciddiyet, sıcaklıkla dengelenir."
        },
        "hazırlanma": {
            "kaos_tipi": "Disiplinli hazırlanan",
            "risk": 30,
            "guclu": "Zaman yönetimin",
            "zayif": "Esnek olmaman",
            "uyari": "Küçük aksaklıklarda panik yapma.",
            "motto": "Plan seni taşır, sertlik değil."
        },
        "plan yapma": {
            "kaos_tipi": "Stratejik ve güçlü planlayıcı",
            "risk": 28,
            "guclu": "Sistem kurman",
            "zayif": "Fazla yük alman",
            "uyari": "Her şeyi sen yapmak zorunda değilsin.",
            "motto": "Yük paylaşılınca hedef büyür."
        },
        "sosyalleşme": {
            "kaos_tipi": "Mesafeli ama güvenilir",
            "risk": 35,
            "guclu": "Ciddiyetin",
            "zayif": "Ulaşılmaz görünmen",
            "uyari": "Biraz yumuşamak seni küçültmez.",
            "motto": "Güven, sıcaklıkla tamamlanır."
        }
    },
    "Kova": {
        "alışveriş": {
            "kaos_tipi": "Sıradışı seçim yapan",
            "risk": 57,
            "guclu": "Özgün zevkin",
            "zayif": "Fazla farklıya yönelmen",
            "uyari": "İlginç olan her zaman işlevsel değildir.",
            "motto": "Özgünlük, kullanışlılıkla parlar."
        },
        "mesajlaşma": {
            "kaos_tipi": "Bazen çok ilgili bazen kayıp",
            "risk": 72,
            "guclu": "Orijinal iletişimin",
            "zayif": "Tutarsız dönüşlerin",
            "uyari": "İnsanlar zihnini okuyamaz.",
            "motto": "Özgürlük açık iletişimle güçlenir."
        },
        "hazırlanma": {
            "kaos_tipi": "Rahat ama beklenmedik",
            "risk": 58,
            "guclu": "Pratik çözümler bulman",
            "zayif": "Rutin dışına savrulman",
            "uyari": "Yaratıcı olmak unutkanlığı kapatmaz.",
            "motto": "Farklı olmak düzeni dışlamaz."
        },
        "plan yapma": {
            "kaos_tipi": "Alışılmadık yollar bulan",
            "risk": 54,
            "guclu": "Yenilikçi düşünmen",
            "zayif": "Klasik adımları küçümsemen",
            "uyari": "Bazı basit şeyler işe yarar çünkü basittir.",
            "motto": "Yenilik temelle güçlenir."
        },
        "sosyalleşme": {
            "kaos_tipi": "Özgün ama mesafeli",
            "risk": 49,
            "guclu": "Farklı bakış açın",
            "zayif": "Duygusal mesafe",
            "uyari": "Bağ kurmak fikir paylaşmaktan fazlasıdır.",
            "motto": "Özgünlük yakınlıkla daha anlamlı."
        }
    },
    "Balık": {
        "alışveriş": {
            "kaos_tipi": "Mood odaklı seçen",
            "risk": 70,
            "guclu": "Estetik sezgin",
            "zayif": "Anı yaşarken kontrolden çıkman",
            "uyari": "Duygusal boşluğu alışverişle doldurma.",
            "motto": "Hislerin güzel, sınırların da olsun."
        },
        "mesajlaşma": {
            "kaos_tipi": "Duygusal ve hayal gücü yüksek",
            "risk": 79,
            "guclu": "Samimi olman",
            "zayif": "Fazla anlam yüklemen",
            "uyari": "Sessizlik her zaman kötüye işaret değildir.",
            "motto": "Kalp sezsin, zihin denge kursun."
        },
        "hazırlanma": {
            "kaos_tipi": "Dalgın ama sezgisel",
            "risk": 73,
            "guclu": "Ortamın enerjisini yakalaman",
            "zayif": "Eşya unutman",
            "uyari": "Çıkmadan telefon-anahtar kontrolü yap.",
            "motto": "Akıntıya kapılma, kendini topla."
        },
        "plan yapma": {
            "kaos_tipi": "Hayal kuran ama dağılabilen",
            "risk": 76,
            "guclu": "Yaratıcılığın",
            "zayif": "Somutlaştırma zorluğun",
            "uyari": "Hayali takvime dök.",
            "motto": "Hayal planla gerçeğe döner."
        },
        "sosyalleşme": {
            "kaos_tipi": "Empatik ama sınır koymakta zorlanan",
            "risk": 62,
            "guclu": "Yumuşak iletişimin",
            "zayif": "Fazla etkilenmen",
            "uyari": "Başkasının enerjisi senin yükün değil.",
            "motto": "Şefkat sınırla güçlenir."
        }
    }
}


def tarih_gecerli_mi(gun: int, ay: int) -> bool:
    gun_sayilari = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if ay not in gun_sayilari:
        return False
    return 1 <= gun <= gun_sayilari[ay]


def burc_bul(gun: int, ay: int) -> str | None:
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
    return None


ALANLAR = ["alışveriş", "mesajlaşma", "hazırlanma", "plan yapma", "sosyalleşme"]

st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 2.3rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 1.2rem;
    }
    .result-card {
        background: #f6f6fb;
        padding: 18px;
        border-radius: 16px;
        border: 1px solid #e4e4ef;
        margin-top: 10px;
    }
    .mini-box {
        background: #ffffff;
        padding: 12px;
        border-radius: 12px;
        border: 1px solid #ececf3;
        height: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">✨ Burcuna Göre Kaos Haritan ✨</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Doğum tarihini gir, alanını seç ve kaos profilini keşfet.</div>',
    unsafe_allow_html=True
)

with st.form("kaos_formu"):
    col1, col2 = st.columns(2)
    with col1:
        gun = st.number_input("Doğum günü", min_value=1, max_value=31, value=14, step=1)
    with col2:
        ay = st.number_input("Doğum ayı", min_value=1, max_value=12, value=4, step=1)

    alan = st.selectbox("Bugün hangi alanda kaosunu görmek istiyorsun?", ALANLAR)

    submitted = st.form_submit_button("Kaos Haritamı Göster")

if submitted:
    if not tarih_gecerli_mi(int(gun), int(ay)):
        st.error("Geçerli bir tarih gir.")
    else:
        burc = burc_bul(int(gun), int(ay))
        if not burc:
            st.error("Burç hesaplanamadı.")
        else:
            sonuc = YORUMLAR[burc][alan]

            st.success(f"Burcun bulundu: {burc}")

            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.subheader(f"{burc} • {alan.title()}")

            c1, c2 = st.columns([1, 1])
            with c1:
                st.metric("Risk Puanı", f"{sonuc['risk']}/100")
            with c2:
                if sonuc["risk"] >= 70:
                    risk_seviye = "Yüksek"
                elif sonuc["risk"] >= 50:
                    risk_seviye = "Orta"
                else:
                    risk_seviye = "Düşük"
                st.metric("Risk Seviyesi", risk_seviye)

            st.markdown(f"**Kaos Tipi:** {sonuc['kaos_tipi']}")

            a, b = st.columns(2)
            with a:
                st.markdown(
                    f"""
                    <div class="mini-box">
                    <strong>Güçlü Yönün</strong><br><br>
                    {sonuc['guclu']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with b:
                st.markdown(
                    f"""
                    <div class="mini-box">
                    <strong>Zayıf Yönün</strong><br><br>
                    {sonuc['zayif']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown("")
            st.info(f"**Mini Uyarı:** {sonuc['uyari']}")
            st.markdown(f"### Motto\n_{sonuc['motto']}_")
            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Python + Streamlit ile hazırlanmıştır.")
