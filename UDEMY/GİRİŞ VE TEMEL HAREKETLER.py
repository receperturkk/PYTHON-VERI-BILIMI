#************************** DEĞİŞKEN TÜRLERİ **************************
def degiskenTurleri():
    a="ahmet"
    print(a,type(a))

    b=30
    print(b,type(b))

    z=41.5
    print(z,type(z))

    c=2j+1
    print(c,type(c))

    d='3,7,9'
    print(d,type(d))

    e="4,6,9"
    print(e,type(e))

    f="Ahmet,Ali,Musa"
    print(f,type(f))

    x = ["apple","banana","cherry"]
    print(x,type(x))

    x =range(6)
    print(x,type(x))

    x =True
    print(x,type(x))

    x = b"Hello"
    print(x,type(x))

    x ={"apple","banana","cherry"}
    print(x,type(x))

    x =frozenset({"apple","banana","cherry"})
    print(x,type(x))

    x = bytes(5)
    print(x,type(x))

    x=bytearray(4)
    print(x,type(x))
#degiskenTürleri()

#************************** SAYILAR VE STRINGLERE GİRİŞ **************************
def sayilarStringler():
    print("r"+"e"+"c"+"e"+"p")
    print("a "*3)
#sayilarStringler()

#************************** STRING METODLARI **************************
"""
-len()
-upper() & lower()  
-isupper() & islower()
-replace()
-strip()
"""
def stringMetodlari():
    gel_yaz = "geleceği yazanlar"
    print(len(gel_yaz))#karakter sayısını gösterir.

    a = 9
    b = 10
    print(a*b)

    rke = "Recep Kadir ERTÜRK"
    print(rke.upper())#karakterleri küçük harf yapar.
    print(rke.lower())#karakterleri büyük harf yapar.

    hw = "hello world"
    print(hw.islower())#içeriğin küçük olup olmadığını kontrol eder.

    HW = "HELLO WORLD"
    print(HW.isupper())#içeriğin büyük olup olmadığını kontrol eder.

    cer = "erebe"
    print(cer)
    car = cer.replace("e","a")#karakter değiştirmeye yarar.
    print(car)

    gel_yaz = " geleceği yazanlar "
    print(gel_yaz)
    gel_yaz1 = gel_yaz.strip()#baştaki ve sondaki boşlukları siler.
    print(gel_yaz1)

    gel_yaz = "*geleceği yazanlar*"
    print(gel_yaz)
    gel_yaz1 = gel_yaz.strip("*")  # baştaki ve sondaki '*' sembolünü siler.
    print(gel_yaz1)

    print(dir(rke))#.dir o değişkenin alabileceği metodları gösterir.

    print(rke.capitalize())#ilk harfi büyük yapar.
    print(rke.title())#tüm kelimelerin ilk harfini büyütür.
#stringMetodları()

#************************** SUBSTRINGLER **************************
def substringler():
    gel_yaz = "geleceği yazanlar"
    print(gel_yaz[1])#indexten istediğimiz indexi seçmeye yarıyor.
    print(gel_yaz[0:9])#indexten istenilen aralığı seçmeye yarıyor ["başlangıç indexi dahil":"bitiş indexi+1 dahil değil"].
    print(gel_yaz[9:18])
substringler()









