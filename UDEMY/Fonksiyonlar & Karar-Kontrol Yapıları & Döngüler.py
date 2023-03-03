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

