#NESNE YÖNELİMLİ PROGRAMLAMA

#SINIF ÖZELLİKLERİ (CLASS ATTRİBUTES)
class VeriBilimci():
    bolum = ""
    sql = "Evet"
    deneyim_yili = 0
    bildigi_diller = []

#Sınıfların Özelliklerine Erişmek
print(VeriBilimci.sql)
print(VeriBilimci.deneyim_yili)

#Sınıdların özelliklerini değiştirmek
VeriBilimci.sql = "Hayır"
print(VeriBilimci.sql)

print("--------------------------------------------")
#Sınıf örneklendirmesi (instantiation)
ali = VeriBilimci()
print(ali.sql)
ali.bildigi_diller.append("Python")
print(ali.bildigi_diller)

veli = VeriBilimci()
print(veli.bildigi_diller)

print("--------------------------------------------")
#Örnek özellikleri
class VeriBilimci():
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ""


ali = VeriBilimci()
print(ali.bildigi_diller)
ali.bildigi_diller.append("Python")
print(ali.bildigi_diller)
ali.bolum = "İstatistik"
print(ali.bolum)

veli = VeriBilimci()
print(veli.bildigi_diller)
veli.bildigi_diller.append("Html")
print(veli.bildigi_diller)
veli.bolum = "Matematik"
print(veli.bolum)

print("--------------------------------------------")
#Örnek metodları
class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ""
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)
    
ali = VeriBilimci()
print(ali.bildigi_diller)
print(ali.bolum)
ali.dil_ekle("Python")
print(ali.bildigi_diller)

veli = VeriBilimci()
print(veli.bildigi_diller)
print(veli.bolum)

print("--------------------------------------------")
#Miras yapıları (inheritance)
class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Adress = ""


class DataScien(Employees):
    def __init__(self):
        self.Programming = ""

veribilimci1 = DataScien()


class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""

mar1 = Marketing()


'''class Employees_yeni():
    def __init__(self, FirstName, LastName, Adress):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Adress = Adress
ali = Employees_yeni("ali", "veli", "konya")
print(ali.Adress, ali.FirstName, ali.LastName)'''

asdasdasd