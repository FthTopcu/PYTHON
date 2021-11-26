# fonksiyon/Metot:

def MerhabaYaz():
    print("Merhaba")
def MerhabaYaz10Defa():
    for i in range(10):
        print(f"{i+1}.",end="")
        MerhabaYaz()

#parametreli metot
def Topla(s1,s2):
    print(f"Toplam = {s1+s2}")

def UsHesapla(taban,us):
    carpim = 1
    for i in range(us):
        carpim *= taban
    return carpim

def faktoriyel(sayi):
    fakt = 1
    s = 1
    while(s<=sayi):
        fakt = fakt * s
        s += 1
    return fakt

def SayiAl():
    return int(input("Sayi giriniz : "))

# MerhabaYaz()
# print("burada işlem")
# MerhabaYaz()

# MerhabaYaz10Defa()


# Topla(10,90)
# print(UsHesapla(20,4))

# print(faktoriyel(5))

#UsHesapla(us=2,taban=7)# parametreleri belirterek değer gönderdik


# kullanıcıdan aldığı sayıyı int olarak döndüren sayiAl metodunu tanımlayınız

sayi = SayiAl()
print(f"sayi {sayi}  tipi {type(sayi)}" )