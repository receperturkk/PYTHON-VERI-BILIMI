#FONKSİYONLARA GİRİŞ VE FONKSİYON OKURYAZARLIĞI
print("a","b",sep ="_")

#MATEMATİKSEL İŞLEMLER
'''
4*4
4/4
5-1
6+3
3**2 KUVVET ALMA
'''

#FONKSİYON NASIL YAZILIR
def kare_al(x):
    sonuc = x**2
    print(sonuc)

kare_al(3)

#BİLGİ NOTUYLA ÇIKTI ÜRETMEK
def kare_al_2(y):
    sonuc_2 = y**2
    print("Girilen Sayı:",str(y),"Karesi:",sonuc_2)

kare_al_2(4)

#İKİ ARGÜMANLI FONKSİYON TANIMLAMAK
def carpma_yap(a,b):
    sonuc_3 = a*b
    print("Girilen Sayılar:",str(a),",",str(b),"Çarpımı:",sonuc_3)

carpma_yap(4,5)

#ÖN TANIMLI ARGÜMANLAR 
def carpma_yap_2(c,d=1):
    sonuc_4 = c*d
    print("Girilen Sayılar:",str(c),",",str(d),"Çarpımı:",sonuc_4)

carpma_yap_2(4)
carpma_yap_2(4,5)

#ARGÜMANLARIN SIRALAMASI
def cıkarma_yap(k,l=0):
    sonuc_5 = k-l
    print("Girilen Sayılar:",str(k),",",str(l),"Sonucu:",sonuc_5)

cıkarma_yap(3,1)
cıkarma_yap(l=1,k=3)
cıkarma_yap(1,3)

#ÇIKTIYI GİRDİ OLARAK KULLANMAK
def gno_hesaplama(d,d1,d2,d3):
    ortalama = (d+d1+d2+d3)/4
    return ortalama
    
print(gno_hesaplama(50, 30, 40, 50))
gno = gno_hesaplama(50, 30, 40, 50)
print(gno)

#LOCAL VE GLOBAL DEĞİŞKENLER
#global değişkenler
x = 10
y = 20
#local değişkenler
def carpma_yap_3(x,y):
    print(x*y)

carpma_yap_3(2,3)

#LOCAL ETKİ ALANINDAN GLOBAL ETKİ ALANINI DEĞİŞTİRMEK
x = []

def eleman_ekle(y):
    x.append(y)
    print(str(y),"İfadesi eklendi")

eleman_ekle(1)
eleman_ekle("merhaba")
print(x)

#KARAR & KONTROL YAPILARI

#TRUE-FALSE SORGULAMALARI
sinir = 5000
print(sinir == 5000)
print(sinir == 4000)

#İF
sinir = 50000
gelir = 40000
if gelir < sinir:
    print("Gelri sinirdan küçük")

#ELSE
else:
    print("gelir sinirden büyük")

#ELİF
maas = 5000
gider = 4000
if maas == gider:
    print("Bu ayki birikiminiz: 0")
elif maas < gider:
    print("Bu ay açığınız var")
else:
    birikim = maas - gider
    print("Bu ayki birikiminiz:",birikim)

#MİNİ UYGULAMA
def uygulama():
    sinir = 50000
    magaza_adi = input("Mağaza Adı Giriniz:")
    gelir = int(input("Gelirinizi Giriniz:"))
    if gelir > sinir:
        print("Tebrikler, promosyon kazandınız!")
    elif gelir < sinir:
        print("Uyarı!!!")
    else:
        print("Takibe devam")
#uygulama()

#FOR DÖNGÜSÜ
ogrenci = ["ali","veli","ışık","berk"]
for i in ogrenci:
    print(i)

maaslar = [1000, 2000, 3000, 4000, 5000]
for i in maaslar:
    print(i)   

print("-------------------------------------")

#DÖNGÜ VE FONKSİYONLARIN BİRLİKTE KULLANIMI 
maaslar = [1000, 2000, 3000, 4000, 5000]
for i in maaslar:
    print(i)  

#maaslara %20 zam yapılıcak gerekli kodları yazınız.
'''def zam (x,y):
    yeni_maas = x+x*(y/100)
    print(yeni_maas)
y = int(input("Yüzde kaç zam yapılıcak \'20,30,40\'şeklinde yazınız: "))
for x in maaslar:
    zam(x, y)'''
print("-------------------------------------")

#if,for ve fonksiyonların birlikte kullanımı
maaslar = [1000, 2000, 3000, 4000, 5000]

#maası 3000'den az olana %20 fazla olanlara %1o zam yapılcak
def zam (x,y):
    yeni_maas = x+x*(y/100)
    print(yeni_maas)

for x in maaslar:
    if x < 3000:
        y = 20
        zam(x, y)
    else:
        y = 10
        zam(x, y)

#BREAK & CONTİNUE
maaslar = [8000, 5000, 2000, 1000, 3000, 7000,4000,1000]
maaslar.sort()
for i in maaslar:
    if i == 4000:
        print("kesildi")
        break
    print(i)

for i in maaslar:
    if i == 4000:
        continue
    print(i)

#WHİLE
sayi = 1 
while sayi < 10:
    sayi += 1
    print(sayi) 

