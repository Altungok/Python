# Ömer Faruk Altungök

# Bankamatik Uygulaması

# 1- Hesap Bilgileri tutulacak. (dict)
# 2- Menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonları tanımlanacak.
# 3- Çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.

hesaplar = [
    { 
        "ad" : "Ömer Faruk Altungök",
        "hesapNo":"23001",
        "bakiye":20000,
        "ekHesap":3500,
        "username":"altungok",
        "password":"1234"
    },
    {
        "ad" : "Sibel Yılmaz",
        "hesapNo":"61001",
        "bakiye":90000,
        "ekHesap":14500,
        "username":"yılmaz",
        "password":"1234"
    }
]

def menu(hesap):
    print("\n")

    print(f"Merhaba, {hesap["ad"]}")

    print("1- Bakiye Sorgulama")
    print("2- Para çekme")
    print("3- Para Yatırma")
    print("4- Toplam Paranız")

    islem = int(input("Yapmak İstediğiniz İşlemi Seçiniz : "))

    if islem == 1:
        bakiyeSorgula(hesap)
        
    elif islem == 2:
        paraCekme(hesap)

    elif islem == 3:
        paraYatirma(hesap)

    elif islem == 4:
        toplamPara(hesap)

    else :
        print("Yanlış seçim yaptiniz")

    menu(hesap)

def bakiyeSorgula(hesap):
    print(f"Bakiyeniz :  {hesap["bakiye"]}")
    print(f"Ek hesap Bakiyeniz : {hesap["ekHesap"]}")

def paraCekme(hesap):
    cekilecekTutar = float(input("Çekilecek Tutar : "))
    if (hesap["bakiye"]>cekilecekTutar):
        hesap["bakiye"]-=cekilecekTutar
        print(f"Yeni Hesap Bakiyeniz :{hesap["bakiye"]}")
    else :  
        toplam = hesap["bakiye"]+hesap["ekHesap"]

        if toplam >= cekilecekTutar:
            ekHesapKullanimİzni=input("Ek hesap Kullanılsınmı : ")

            if ekHesapKullanimİzni=="e":
                kullanılcakMiktar = cekilecekTutar - hesap["bakiye"]
                hesap["bakiye"]=0
                hesap["ekHesap"]-=kullanılcakMiktar
                
                print(f"Kalan bakiyeniz : {hesap["ekHesap"]}")
            else:
                print("Bakiyeniz yetersizdir.")
        else:
              print("Bakiyeniz yetersizdir.")
                

def paraYatirma(hesap):
    yatirilacakTutar= int(input("Yatırılacak Tutarı Giriniz : "))
    hesap["bakiye"]=hesap["bakiye"]+yatirilacakTutar
    print(f"Yeni Hesap Bakiyeniz : {hesap["bakiye"]}")

def toplamPara(hesap):
    toplamPara=hesap["bakiye"]+hesap["ekHesap"]
    print(f"Hesabınızdaki Toplam Paranız :{toplamPara}")

def login():
    username = input("Kullanıcı Adı : ")
    password = input("Şifre         : ")

    isLogginIn = False

    for hesap in hesaplar:
        if hesap["username"] == username and hesap["password"] == password:
            isLogginIn = True
            menu(hesap)
            break
    if not(isLogginIn):
        print("Kullanıcı adı veya Parolanız yanlış.")
login()