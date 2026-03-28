import streamlit as st
import base64
import random
from pathlib import Path

st.set_page_config(
    page_title="Burcuna Göre Kaos Haritan",
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

TAROT_KARTLARI = [
    {
        "kart": "Gunes",
        "anahtar": "aciklik ve guven",
        "yorum_dusuk": "Bu kart, {alan} alaninda daha acik, net ve rahat bir akisa girdigini gosteriyor. Bugun kendine daha cok guvenerek hareket edebilirsin.",
        "yorum_orta": "Bu kart, {alan} konusunda icindeki netligi bulursan islerin kolaylasacagini soyluyor. Kucuk bir kararsizlik olsa da ic sesin sana yardim edebilir.",
        "yorum_yuksek": "Bu kart, {alan} alanindaki karmasayi biraz sakinlik ve ozguvenle yumusatabilecegini soyluyor. Bugun panik yerine netlige donmek sana iyi gelir."
    },
    {
        "kart": "Yildiz",
        "anahtar": "umut ve denge",
        "yorum_dusuk": "Bu kart, {alan} konusunda daha hafif ve dengeli bir enerji tasidigini gosteriyor. Olaylara daha pozitif yaklasman seni rahatlatabilir.",
        "yorum_orta": "Bu kart, {alan} alaninda icini rahatlatacak bir denge aradigini soyluyor. Her seyi ayni anda cozmeye calismak yerine sakin ilerlemek daha iyi olabilir.",
        "yorum_yuksek": "Bu kart, {alan} konusunda biraz durup nefes alman gerektigini soyluyor. Her sey karisik gelse bile toparlanma sansin hala guclu."
    },
    {
        "kart": "Ay",
        "anahtar": "belirsizlik ve sezgi",
        "yorum_dusuk": "Bu kart, {alan} alaninda sezgilerinin guclu oldugunu ama yine de her seyi fazla anlamlandirmaman gerektigini hatirlatiyor.",
        "yorum_orta": "Bu kart, {alan} konusunda bazen olaylari oldugundan daha karmasik hissedebilecegini soyluyor. Biraz netlik aramak iyi gelebilir.",
        "yorum_yuksek": "Bu kart, {alan} alaninda belirsizlik hissinin artabilecegini gosteriyor. Bugun hemen sonuc cikarmak yerine bir adim geri cekilmek daha iyi olabilir."
    },
    {
        "kart": "Kule",
        "anahtar": "ani degisim",
        "yorum_dusuk": "Bu kart, {alan} alaninda beklenmedik ama yonetilebilir kucuk degisimlere acik oldugunu gosteriyor. Esnek kalirsan sorun buyumeden gecebilir.",
        "yorum_orta": "Bu kart, {alan} konusunda plan disi bir gelisme olabilecegini soyluyor. Ancak buna hizli uyum saglama sansin da var.",
        "yorum_yuksek": "Bu kart, {alan} alaninda ani bir karisiklik ya da beklenmedik bir aksaklik yasayabilecegini soyluyor. Panik yapmak yerine toparlanmaya odaklanman en iyisi olur."
    },
    {
        "kart": "Adalet",
        "anahtar": "denge ve karar",
        "yorum_dusuk": "Bu kart, {alan} konusunda daha olculu ve dengeli bir noktada oldugunu gosteriyor. Kararlarini sakinlikle verebilirsin.",
        "yorum_orta": "Bu kart, {alan} alaninda duygularinla mantigini ayni cizgide tutman gerektigini soyluyor. Biraz dusunerek ilerlemek seni rahatlatir.",
        "yorum_yuksek": "Bu kart, {alan} alaninda acele kararlarin seni yorabilecegini soyluyor. Bugun dengeyi korumak her zamankinden daha onemli olabilir."
    },
    {
        "kart": "Guc",
        "anahtar": "ic dayaniklilik",
        "yorum_dusuk": "Bu kart, {alan} alaninda zaten sakin ve dengeli bir guc gosterdigini anlatir. Kucuk ayrintilar seni kolay kolay sarsmaz.",
        "yorum_orta": "Bu kart, {alan} konusunda biraz sabir ve ic kontrol ile her seyi toparlayabilecegini soyluyor. Hemen tepki vermemek bugunun gucu olabilir.",
        "yorum_yuksek": "Bu kart, {alan} alanindaki kaosu disaridan degil iceriden yonetmen gerektigini soyluyor. Bugun en buyuk destegin kendi sakinligin olabilir."
    },
    {
        "kart": "Ermis",
        "anahtar": "geri cekilip dusunmek",
        "yorum_dusuk": "Bu kart, {alan} konusunda fazla hizlanmak yerine biraz icine donmenin sana iyi gelebilecegini hatirlatiyor.",
        "yorum_orta": "Bu kart, {alan} alaninda herkesi degil once kendini dinlemen gerektigini soyluyor. Kisa bir durup dusunme ani faydali olabilir.",
        "yorum_yuksek": "Bu kart, {alan} konusunda fazla uyaranla yorulabilecegini gosteriyor. Bugun biraz geri cekilip sade dusunmek seni toparlayabilir."
    },
    {
        "kart": "Kader Carki",
        "anahtar": "degisen akis",
        "yorum_dusuk": "Bu kart, {alan} alaninda akisin senin lehine donebilecegini soyluyor. Kucuk bir aciklik sana iyi firsatlar getirebilir.",
        "yorum_orta": "Bu kart, {alan} konusunda bir degisim enerjisi oldugunu soyluyor. Esnek kalirsan bu durum seni zorlamaktan cok destekleyebilir.",
        "yorum_yuksek": "Bu kart, {alan} alaninda olaylarin hizli degisebilecegini gosteriyor. Kontrol etmek yerine uyum saglamak seni daha az yorabilir."
    },
    {
        "kart": "Deli",
        "anahtar": "cesaret ve ilk adim",
        "yorum_dusuk": "Bu kart, {alan} konusunda daha rahat ve hafif ilerleyebilecegini gosteriyor. Fazla dusunmeden ama dengeli bir sekilde akabilirsin.",
        "yorum_orta": "Bu kart, {alan} alaninda biraz daha cesur ama dikkatli davranman gerektigini soyluyor. Yeni bir tavir denemek iyi gelebilir.",
        "yorum_yuksek": "Bu kart, {alan} konusunda kontrolsuz bir aceleye kapilmaman gerektigini hatirlatiyor. Cesaret guzel, ama yonunu kaybetmeden ilerlemek daha iyi."
    }
]

ALANLAR = ["alışveriş", "mesajlaşma", "hazırlanma", "plan yapma", "sosyalleşme"]


def image_to_base64(image_path):
    path = Path(image_path)
    if not path.exists():
        return None
    return base64.b64encode(path.read_bytes()).decode()


def risk_seviyesi_ve_emoji(risk):
    if risk >= 70:
        return "Yüksek", "🔴"
    elif risk >= 50:
        return "Orta", "🟡"
    return "Düşük", "🟢"


def uzun_risk_yorumu(alan, kaos_tipi, risk):
    seviye, _ = risk_seviyesi_ve_emoji(risk)

    if seviye == "Yüksek":
        return (
            f"Bu alanda kaos enerjin bugün oldukça {seviye.lower()} görünüyor. "
            f"Özellikle '{kaos_tipi.lower()}' bir eğilim göstermeye daha açık olabilirsin. "
            f"Bu yüzden {alan} sırasında aceleci davranmak ya da ilk tepkinle hareket etmek "
            f"seni gereksiz bir karışıklığın içine çekebilir."
        )
    elif seviye == "Orta":
        return (
            f"Bu alandaki risk seviyen {seviye.lower()} düzeyde. "
            f"'{kaos_tipi.lower()}' tarafın zaman zaman öne çıkabilir; ancak dikkatli davranırsan "
            f"dengeyi koruman mümkün görünüyor. Yani küçük bir kontrol ile durumu lehine çevirebilirsin."
        )
    else:
        return (
            f"Bu alanda risk seviyen {seviye.lower()} görünüyor. "
            f"'{kaos_tipi.lower()}' bir eğilimin olsa da bunu yönetme konusunda daha dengeli kalabilirsin. "
            f"Yine de küçük ayrıntıları tamamen göz ardı etmemek iyi olabilir."
        )


def uzun_guclu_yorum(metin):
    return (
        f"Bu alandaki en güçlü tarafın, {metin.lower()}. "
        f"Bu özellik seni hem daha etkili hem de daha dikkat çekici kılar. "
        f"Doğru kullandığında bulunduğun durumu kendi lehine çevirmene gerçekten yardımcı olabilir."
    )


def uzun_zayif_yorum(metin):
    return (
        f"Zayıf tarafında ise {metin.lower()} öne çıkıyor. "
        f"Bu durum bazen seni gereksiz yere yorabilir ya da küçük bir konuyu olduğundan daha büyük hissettirebilir. "
        f"Özellikle stres arttığında bu yönün daha belirgin hâle gelebilir."
    )


def uzun_uyari_yorumu(metin):
    return (
        f"Bugün kendine küçük bir hatırlatma olarak şunu aklında tutabilirsin: {metin} "
        f"Küçük bir durup düşünme anı, hem daha rahat hissetmeni hem de daha dengeli karar vermeni sağlayabilir."
    )


def tarot_karti_secimi_hazirla(oturum_anahtari):
    if st.session_state.get("tarot_oturum_anahtari") != oturum_anahtari:
        st.session_state["tarot_oturum_anahtari"] = oturum_anahtari
        st.session_state["acik_tarot_kartlari"] = random.sample(TAROT_KARTLARI, 3)
        st.session_state["secilen_tarot_index"] = None


def tarot_yorumu_getir(kart, risk, alan):
    if risk >= 70:
        temel_yorum = kart["yorum_yuksek"].format(alan=alan.lower())
    elif risk >= 50:
        temel_yorum = kart["yorum_orta"].format(alan=alan.lower())
    else:
        temel_yorum = kart["yorum_dusuk"].format(alan=alan.lower())

    return (
        f"Seçtiğin {kart['kart']} kartı, bugün özellikle {alan.lower()} alanında öne çıkan enerjine ışık tutuyor. "
        f"Bu kartın ana teması '{kart['anahtar']}' olarak görünüyor. "
        f"{temel_yorum} "
        f"Yani bugün vereceğin küçük kararlar, göstereceğin sabır ve olaylara yaklaşım biçimin günün genel akışını düşündüğünden daha fazla etkileyebilir."
    )


background_b64 = image_to_base64("foto.png")
tarot_b64 = image_to_base64("tarot.png")

background_css = ""
if background_b64:
    background_css = f"""
    .stApp {{
        background:
            linear-gradient(rgba(8, 10, 20, 0.74), rgba(8, 10, 20, 0.78)),
            url("data:image/png;base64,{background_b64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    """

tarot_back_html = ""
if tarot_b64:
    tarot_back_html = f'<img src="data:image/png;base64,{tarot_b64}" alt="Tarot Karti" />'
else:
    tarot_back_html = '<div class="tarot-fallback">🔮</div>'

st.markdown(
    f"""
    <style>
    {background_css}

    .main-title {{
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
        color: white;
        text-shadow: 0 2px 10px rgba(0,0,0,0.35);
    }}

    .subtitle {{
        text-align: center;
        color: #e5e7eb;
        margin-bottom: 1.4rem;
    }}

    .mini-box {{
        background: rgba(17, 24, 39, 0.88);
        color: white;
        padding: 16px;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.10);
        min-height: 165px;
        backdrop-filter: blur(6px);
    }}

    .mini-box strong {{
        color: #f9fafb;
        font-size: 1.02rem;
    }}

    .tarot-card-back {{
        background: rgba(17, 24, 39, 0.88);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 18px;
        padding: 14px 10px;
        text-align: center;
        min-height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        backdrop-filter: blur(6px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.20);
        margin-bottom: 10px;
    }}

    .tarot-card-back img {{
        width: 100%;
        max-width: 120px;
        border-radius: 12px;
        margin-bottom: 10px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.25);
    }}

    .tarot-fallback {{
        font-size: 3rem;
        margin-bottom: 8px;
    }}

    .tarot-label {{
        color: #e5e7eb;
        font-size: 0.95rem;
        margin-top: 6px;
    }}

    .tarot-card-front {{
        background: linear-gradient(180deg, rgba(31,41,55,0.92), rgba(17,24,39,0.95));
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 18px;
        padding: 20px 16px;
        text-align: center;
        color: white;
        margin-top: 10px;
        box-shadow: 0 10px 24px rgba(0,0,0,0.25);
    }}

    .tarot-front-title {{
        font-size: 1.2rem;
        font-weight: 700;
        margin-top: 2px;
        margin-bottom: 6px;
    }}

    .tarot-front-key {{
        color: #d1d5db;
        font-size: 0.95rem;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

if "sonuc_hazir" not in st.session_state:
    st.session_state["sonuc_hazir"] = False
if "form_hata" not in st.session_state:
    st.session_state["form_hata"] = None

st.markdown('<div class="main-title">✨ Burcuna Göre Kaos Haritan ✨</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Doğum tarihini gir, alanını seç ve burcuna göre minik kaos profilini gör.</div>',
    unsafe_allow_html=True
)

with st.form("kaos_formu"):
    col1, col2 = st.columns(2)

    with col1:
        gun = st.number_input("Doğum günü", min_value=1, max_value=31, value=14, step=1)

    with col2:
        ay = st.number_input("Doğum ayı", min_value=1, max_value=12, value=4, step=1)

    alan = st.selectbox("Bugün hangi alanda kaosunu görmek istiyorsun?", ALANLAR)

    submitted = st.form_submit_button("Kaos Haritamı Aç")

if submitted:
    if not tarih_gecerli_mi(int(gun), int(ay)):
        st.session_state["form_hata"] = "Geçerli bir tarih gir."
        st.session_state["sonuc_hazir"] = False
    else:
        burc = burc_bul(int(gun), int(ay))
        if not burc:
            st.session_state["form_hata"] = "Burç hesaplanamadı."
            st.session_state["sonuc_hazir"] = False
        else:
            st.session_state["form_hata"] = None
            st.session_state["sonuc_hazir"] = True
            st.session_state["burc"] = burc
            st.session_state["alan"] = alan
            st.session_state["sonuc"] = YORUMLAR[burc][alan]

if st.session_state.get("form_hata"):
    st.error(st.session_state["form_hata"])

if st.session_state.get("sonuc_hazir"):
    burc = st.session_state["burc"]
    alan = st.session_state["alan"]
    sonuc = st.session_state["sonuc"]

    risk_seviye, risk_emoji = risk_seviyesi_ve_emoji(sonuc["risk"])

    st.success(f"Burcun bulundu: {burc}")
    st.markdown(f"### {risk_emoji} {burc} • {alan.title()}")
    st.progress(sonuc["risk"] / 100)

    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.metric("Risk Puanı", f"{sonuc['risk']}/100")
    with col_m2:
        st.metric("Risk Seviyesi", risk_seviye)

    st.markdown(f"**Kaos Tipi:** {sonuc['kaos_tipi']}")
    st.markdown(f"**Risk Yorumu:** {uzun_risk_yorumu(alan, sonuc['kaos_tipi'], sonuc['risk'])}")

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown(
            f"""
            <div class="mini-box">
                <strong>⭐ Güçlü Yönün</strong><br><br>
                {uzun_guclu_yorum(sonuc['guclu'])}
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_b:
        st.markdown(
            f"""
            <div class="mini-box">
                <strong>⚠️ Zayıf Yönün</strong><br><br>
                {uzun_zayif_yorumu(sonuc['zayif'])}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.info(f"**Bugünün Uyarısı:** {uzun_uyari_yorumu(sonuc['uyari'])}")
    st.markdown(f"### Motto\n_{sonuc['motto']}_")

    tarot_oturum_anahtari = f"{burc}-{alan}-{sonuc['risk']}"
    tarot_karti_secimi_hazirla(tarot_oturum_anahtari)

    st.markdown("### 🔮 Bugünün Tarot Seçimi")
    st.write("Aşağıdaki üç karttan birini seç ve bugünkü mini tarot yorumunu gör.")

    tarot_cols = st.columns(3)

    for i, kart in enumerate(st.session_state["acik_tarot_kartlari"]):
        with tarot_cols[i]:
            st.markdown(
                f"""
                <div class="tarot-card-back">
                    {tarot_back_html}
                    <div class="tarot-label">Kart {i+1}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(f"Kart {i+1} seç", key=f"tarot_sec_{i}"):
                st.session_state["secilen_tarot_index"] = i

    secilen_index = st.session_state.get("secilen_tarot_index")

    if secilen_index is not None:
        secilen_kart = st.session_state["acik_tarot_kartlari"][secilen_index]
        tarot_yorum = tarot_yorumu_getir(secilen_kart, sonuc["risk"], alan)

        st.markdown(
            f"""
            <div class="tarot-card-front">
                <div class="tarot-front-title">{secilen_kart['kart']}</div>
                <div class="tarot-front-key">{secilen_kart['anahtar']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("#### Tarot Yorumu")
        st.write(tarot_yorum)

    if st.button("Kartları Yeniden Karıştır", key="tarot_yenile"):
        st.session_state["acik_tarot_kartlari"] = random.sample(TAROT_KARTLARI, 3)
        st.session_state["secilen_tarot_index"] = None
        st.rerun()

st.markdown("---")
st.caption("Eğlence amaçlıdır gerçekleri yansıtmamaktadır ✨")
