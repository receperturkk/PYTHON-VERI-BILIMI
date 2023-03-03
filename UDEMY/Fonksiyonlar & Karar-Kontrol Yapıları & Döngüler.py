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
