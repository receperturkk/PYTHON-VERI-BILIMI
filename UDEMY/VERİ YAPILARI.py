def _liste():
    #****LISTE OLUŞTURMA****
    """
    -[]
    -list()
    """
    notlar = [90,80,70,60,50]
    print(type(notlar))
    print(len(notlar))
    print(notlar[0])
    print(notlar[1])
    print(notlar[2])
    print(notlar[3])
    print(notlar[4])

    print("***************************************************************")

    liste = ["a",40,30.5,notlar]
    print(len(liste))
    print(type(liste[0]))
    print(type(liste[1]))
    print(type(liste[2]))
    print(type(liste[3]))

    print(liste[0])
    print(liste[1])
    print(liste[2])
    print(liste[3])
    print(liste[0:3])
    print(liste[:3])
    print(liste[1:])

    print(liste[3][0])
    print(liste[3][1])
    print(liste[3][2])
    print(liste[3][3])
    print(liste[3][4])

    print("***************************************************************")

    tumListe = [notlar,liste]
    print(tumListe)

    print("***************************************************************")

    liste1 = ["ali","veli","berkcan","ayse"]
    print(liste1)

    liste1[1] = "velinin babası"
    print(liste1)
    liste1[0:3] = "alinin bababsı","velinin babası","berkcanın babası"
    print(liste1)

    liste1 = liste1+["kemal"]
    print(liste1)

    liste1 = ["ali","veli","berkcan","ayse"]
    del liste1[2]
    print(liste1)

    print("***************************************************************")

    liste2 = ["ahmet","recep","fatma","kadir"]
    print(liste2)

    liste2.append("berkcan")#sona ekleme yapar.
    print(liste2)

    liste2.remove("berkcan")
    print(liste2)#içine yazılanı siler.

    liste2.insert(0,"ayşe")#indexte istenilen yere ekleme yapar.
    liste2.insert(len(liste2),"beren")#len() ile direk sona ekleme yapılır
    print(liste2)

    liste2.pop(0)#indexten silme işlemi yapar. boş bırakılırsa sondan siler.
    print(liste2)

    print("***************************************************************")

    liste3 = ['ayşe', 'ahmet', 'recep', 'fatma', 'kadir', 'beren',"recep","recep","kadir"]

    print(liste3)

    print(liste3.count("recep"))#listede o elemandan kaç tane olduğunu sayar.
    print(liste3.count("kadir"))
    print(liste3.count("beren"))

    liste3Yedek = liste3.copy()
    print(liste3Yedek)

    liste3Yedek.extend(notlar)#listeleri birleştirmeye yarar.
    print(liste3Yedek)

    print(liste3.index("ahmet"))#değerin listede hangi indexte olduğnu gösterir.

    liste3.reverse()#listeyi ters çevirir.
    print(liste3)

    liste3.sort()#küçükten büyüğe doğru sıralar.
    print(liste3)

    liste3.clear()
    print(liste3)

    print("***************************************************************")
#_liste()
 
def _tuple():
    #Tuple

    t = ("ali","veli",1,2,3.2,[1,2,3,4])
    print(t)

    t2 = "ali","veli",1,2,3.2,[1,2,3,4]
    print(t2)

    #tuple()

    t3 = ("eleman",)
    print(type(t3))

    #typle eleman işlemleri

    t4 = ("ali","veli",1,2,3.2,[1,2,3,4])
    print(t4[0])
    print(t4[1])
    print(t4[2])
    print(t4[:3])
    #t4[4] = 3  #tuple üzerinde değişlik yapılamaz
#_tuple()


def _sozluk():
    sozluk = {
        "REG" : "Regrasyon Modeli",
        "LOJ" : "Lojistik Regrasyon",
        "CART" : "Classification and Regrasyon"
    }
    print(sozluk)
    print(len(sozluk))

    sozluk1 = {
        "REG": 10,
        "LOJ": 20,
        "CART": 30
    }
    print(sozluk1)
    print(len(sozluk1))

    sozluk2 = {
        "REG": ["RMSE",10],
        "LOJ": ["MSE",20],
        "CART": ["SSE",30]
    }
    print(sozluk2)
    print(len(sozluk2))

    sozluk3 = {
        "REG": "Regrasyon Modeli",
        "LOJ": "Lojistik Regrasyon",
        "CART": "Classification and Regrasyon"
    }
    print(sozluk3)
    print(len(sozluk3))
    print(sozluk3["REG"])
    print(sozluk3["LOJ"])
    print(sozluk3["CART"])

    sozluk4 = {
        "REG": ["RMSE", 10],
        "LOJ": ["MSE", 20],
        "CART": ["SSE", 30]
    }
    print(sozluk4)
    print(len(sozluk4))
    print(sozluk4["REG"][0])
    print(sozluk4["LOJ"][1])
    print(sozluk4["CART"][0])

    sozluk5 = {
        "REG": {"RMSE" : 10,
                "MSE" : 20,
                "SSE" : 30
                },

        "LOJ": {"RMSE" : 10,
                "MSE" : 20,
                "SSE" : 30
                },

        "CART": {"RMSE" : 10,
                "MSE" : 20,
                "SSE" : 30
                }
    }
    print(sozluk5)
    print(len(sozluk5))
    print(sozluk5["REG"]["RMSE"])
    print(sozluk5["LOJ"]["MSE"])
    print(sozluk5["CART"]["SSE"])

    sozluk6 = {
        "REG": "Regrasyon Modeli",
        "LOJ": "Lojistik Regrasyon",
        "CART": "Classification and Regrasyon"
    }
    sozluk6["GBM"] = "Gradient Boosting Mac" #Ekleme yapıyor
    print(sozluk6)

    print(sozluk6["REG"])
    sozluk6["REG"] = "Çoklu Doğrusal Regrasyon Modeli" #Değişim yapıyor
    print(sozluk6["REG"])

    sozluk6[1] = "Yapay Sinir Ağları"
    print(sozluk6[1])

    t = ("tuple",)
    sozluk6[t] = "Yeni Bir Şey"
    print(sozluk6)

_sozluk()