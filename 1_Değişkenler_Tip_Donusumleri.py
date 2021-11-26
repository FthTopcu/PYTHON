#tekli yorum satırı
''' 
Coklu 
yorum111111111
satırı
'''
###################
#   veri tipleri  #
###################
#Tipler:int,float,str,bool
# degisken1=34 #int
# degisken2="Kadıköy" #str
# sayi1=10.5 # float
# kontrol=False #bool
# tip=type(degisken1)
# print(tip)

# print(type(degisken2))
# print(type(sayi1))
# print(type(kontrol))


###################
# tip dönüşümleri #
###################
# strSayi = "15"
# intSayi = int(strSayi)

# intSayi = 15
# fltSayi = float(intSayi)

# intSayi = 7895
# strSayi = str(intSayi)

# print(f"strSayi : tipi {type(strSayi)}")
# print(f"intSayi : tipi {type(intSayi)}")
# print(f"fltSayi : tipi {type(fltSayi)}")

###################
#     örnekler    #
# #################

# #kullanıcıdan iki sayı alıp ekrana yazdıran program

# s1 = input("Sayı 1=") # input str tipinde veri döndürür
# s1 = int(s1) # tip dönüşümü yaptık

# s2 = int(input("Sayı 2=")) 

# toplam = s1 + s2 
# print(f"{s1} + {s2} = {toplam}")

###################
#  koşul kontrol  #
###################
# pythonda kod blokları 4 tane boşluk içeri girilerek oluşturulur.
# yani if bloğu yazmak için if satırı altındaki 4 boşluk içeri kısıma yazılır.

# sayi = 9

# if(sayi>5):
#     print("sayı 5 ten büyüktür!")
#     print("Bu kod bloğu sadece koşul sağlanırsa çalışır")
#     print("Burası if içidir")
#     if(sayi>18):
#         print("sayı 18den büyük")
#     elif(sayi>=15):
#         print("Sayı 15-18 arasındadır")
#     elif(sayi>=10):
#         print("Sayı 10-14 arasındadır")
#     else:
#         print("Sayı 5 ile 9 arasındadır")
# else:
#     print("sayı 5 ten değildir!")
#     print("Bu kod bloğu sadece koşul sağlanmassa çalışır")
#     print("Burası ELSE içidir")

############################
#  List,Tuple,Dictionary   #
############################

# rakamlar = [] # Boş Liste tanımladık
# rakamlar = list() # boş liste tanımladık
# rakamlar = [0,1,2,3,4,5,6,7,8,9] # dolu bir liste tanımladık.

#liste ekleme
# rakamlar.append(11) # listenin sonuna ekleme yapar
# print(rakamlar)
# rakamlar.insert(10,10)
# print(rakamlar)

# listem = [10,20,"Kadıköy"]
# listem += [45,"sarıyer"]

# #list okuma
# print(rakamlar[2])
# print(rakamlar.__getitem__(2))

# print(rakamlar[-1]) #sondan birinci eleman
# print(rakamlar[-2]) #sondan ikinci eleman

# list veri silme
# rakamlar.remove(5) #listedeki bulduğu ilk 5 değerini siler
# del rakamlar[7] #listedeki 7.indexi sil
# del rakamlar #listenin tamamını siler

#list metodlar 
# rakamlar.sort() # küçükten büyüğe
# rakamlar.reverse() # sırayı terse çeviri
# rakamlar.count(4) # rakamlar listesinde 4 sayısı

# # print(f"rakamların eleman sayısı :{len(rakamlar)}")

# print(f"rakamlar listesinin ramdeki adresi : {id(rakamlar)}")

# rakamlar2 = rakamlar # yeni liste tanımlamadan aynı listeyi rakamlar2 ismine de eşitlemiş olduk
# print(f"rakamlar2 listesinin ramdeki adresi : {id(rakamlar2)}")
# rakamlar3 = rakamlar.copy()
# print(f"rakamlar3 listesinin ramdeki adresi : {id(rakamlar3)}")



#################
##    TUPLE    ##
#################
#listeden farkı değiştirilemez değiştirilmesi gerekiyorsa liste çevrilir

# sabitListe = () # boş tuple
# sabitListe = tuple() # boş tuple
# sabitListe = (10,2,30) # dolu tuple

# liste = list(sabitListe) # tuple ı listeye çevirdik
# liste.append(40)
# sabitListe = tuple(liste)
# print(sabitListe)


##################
##  Dictionary  ##
##################

# sozluk = {} # bos dictionary
# sozluk = dict()
# sozluk = {"red":"kırmızı","white":"beyaz","key":"anahtar"}

# #veriye erişim c

# print(sozluk["red"])
# print(sozluk["key"])
# print(sozluk["white"])


# print(sozluk.keys()) # anahtarları listele
# print(sozluk.values()) # değerleri listele

# veri ekleme

# sozluk["puprle"] = "mor"
# sozluk["red"] = "al" # varolan anahtara yeni değer
# sozluk["crimson"]="al"

###################
##    döngüler   ##
###################


# listemiz = ["Kadıköy","Beşiktaş","Fatih","Eminönü","Üsküdar"]
# for eleman in listemiz:
#     print(eleman)


# for key in sozluk.keys():
#     print(key,end=" => ")
#     print(sozluk[key])

# print()

# for val in sozluk.values():
#     print(val)

# range(5)      # => [0,1,2,3,4] 
# range(2,8)    # => [2,3,4,5,6,7]
# range(2,14,2) # => [2,4,6,8,10,12]

# #0-5 arası ekrana yazdıran program 5 dahil değil
# for i in range(5):
#     print(i,end=" ")

# #0-100 arası 100 100 dahil çift sayıları yazdıran pr
# for i in range(0,101,2):
#     print(i)

# print("Mehmet","Ahmet","Selda","Müslüm",sep="-")
#kullanıcıdan aldığın 10 sayıyı listeye atıp toplamlarını ekrana yazdıran program

# list = []
# toplam = 0
# for i in range(0,10):
#     list.append(int(input(f"{i+1}.sayı :")))
#     toplam+=list[i]

# toplam metodu => sum(list)

# print(toplam)

#kullanıcı -1 girene kadar girilen sayıları toplayıp ekrana yazdıran program

# toplam = 0
# while (True):
#     s = int(input("s : "))
#     if(s==-1):
#         break
#     else:
#         toplam += s
# print(toplam)

# listem = [True,"Mehmet",15,45.3,15,"Demir",15,30]

# SORU 1: Kullanıcıdan alınan isimleri isimler isminde bir listeye atınız.
# isim girilmeden enter tuşuna basılana kadar isim girilebilsin
# listedeki elemanların ilk yarısını ekrana yazdırın 
# isimler = []
# while(True):
#     isim = input("isim giriniz :")
#     if(isim == ""):
#         break
#     else:
#         isimler.append(isim)
# boyut = int(len(isimler)/2)
# for i in range(0,boyut):
#     print(isimler[i])

# print()
# for i in range(boyut,len(isimler)):
#     print(isimler[i])
###################

# liste = [15,20,30,45]

# print(25 in liste) # 25 listede varsa true yoksa false


# if(25 in liste):
#     print("25 listede var.")
# else:
#     print("25 listede yok")

# Soru : klavyeden bitir girilene kadar girilen kelimeleri listeye ekleyen pr
# listede varsa ekle




# isimler = []
# while(True):
#     isim = input("isim giriniz :")
#     if(isim != ""):
#         if(isim == "bitir"):
#             break        
#         else:
#             if(isim in isimler):
#                 print("bu isim listede var ")
#             else:
#                 isimler.append(isim)
#     else:
#         print("boş girilemez.")

# print(isimler)

# SORU : uzunKelimeler liste olsun 
# klavyeden girilen stringlerin uzunluğu 8den büyükse eklesin
# aynı kelimeyi eklemesin
# aynı kelime ikinci kelime girilirse listeden silsin
uzunKelimeler = []

while(True):
    isim = input("Giriniz : ")
    if(isim == "bitir"):
       break
    else: 
        if(len(isim)>8):
            if(isim not in uzunKelimeler):
                uzunKelimeler.append(isim)
            else:
                uzunKelimeler.remove(isim)
        else:
            print("Kelime gereği kadar büyük değil")
       
print(uzunKelimeler)











