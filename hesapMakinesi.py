# Ömer Faruk Altungök
# çok başarılı olmasada uğraşarak hesap makinesi yaptım kendimi geliştirmeye devam ediyorum iyi günler diliyorum 


import os
os.system('cls')
devam = True
(topla,cikar,bol,carp) = (0,0,0,1)
def  toplam(a):
    global topla
    topla += a
    print(f"Sonuc : {topla}")

def cikar(a,b):
    global cikar
    cikar = a-b
    print(f"Sonuc : {cikar}") 

def bol(a,b):
    global bol
    bol = a/b
    print(f"Sonuc : {bol}")

def carp(a,b):
    global carp
    carp = a*b
    print(f"Sonuc : {carp}")
def usAl(a,b):
    print(f"Sonuc : {a**b}")

print("""
    1- Toplama 
    2- Çikarma
    3- Bölme 
    4- Çarpma
    5- Üs Alma
    6- Bitir
""")

while devam :
    sec = int(input("Seçiniz :"))
    if   (sec == 1 ):
        while True:
            a = int(input("Toplanacak sayi(Çikmak için '0') : "))
            if  (a != 0) :
                toplam(a)
            elif (a == 0):
                toplam(0)
                break
    elif (sec == 2 ):
        sayA = float(input("1.sayi(Çıkmak için '0') : "))
        sayB = float(input("2.sayi(Çıkmak için '0') : "))
        cikar(sayA,sayB)
    elif (sec == 3 ):
        sayA = float(input("1.sayi(Çıkmak için '0') : "))
        sayB = float(input("2.sayi(Çıkmak için '0') : "))
        bol(sayA,sayB)
    elif (sec == 4 ):
        sayA = float(input("1.sayi(Çıkmak için '0') : "))
        sayB = float(input("2.sayi(Çıkmak için '0') : "))  
        carp(sayA,sayB)     
    elif (sec == 5 ):
        sayA = float(input("kuvvetini almak istediğin sayıyı giriniz : "))
        sayB = float(input("sayının kaçıncı kuvvetini istiyorsunuz   : "))
        usAl(sayA,sayB)

    elif (sec == 6 ):
        devam = False 

    else :
        ("Hatalı Seçim")
