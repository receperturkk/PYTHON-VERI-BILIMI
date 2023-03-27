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


class Employees_yeni():
    def __init__(self, FirstName, LastName, Adress):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Adress = Adress
ali = Employees_yeni("ali", "veli", "konya")
print(ali.Adress, ali.FirstName, ali.LastName)

print("--------------------------------------------")

#Python'da Fonksiyonel Programlama

#Fonksiyonlar dilin bastacidir.
#(Birinci sinif nesnelerdir)
#Yan etkisiz fonksiyonlar. (stateless, girdi-cikti)
#Yuksek seviye fonksiyonlar.
#Vektorel operasyonlar.

#Yan Etkisiz Fonksiyonlar (Pure Functions)

#Ornek1:Bağımsızlık
A = 5
def impure_sum(b):
    return b + A

def pure_sum(a,b):
    return a + b

print(impure_sum(3))
print(pure_sum(4, 7))

#Ornek2: Olumcul yan etkiler
#00P:

class LineCounter:
    def __init__(self, filename):
        self.file = open(filename,"r")
        self.lines = []

    def read(self):
        self.lines = [line for line in self.file]

    def count(self):
        return len(self.lines)

lc = LineCounter("C:/Users/recep/Documents/GitHub/work/PYTHON/deneme.txt")

print(lc.lines)
print(lc.count())

lc.read()

print(lc.lines)
print(lc.count())

#FP

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

def count(lines):
    return len(lines)

example_lines = read("C:/Users/recep/Documents/GitHub/work/PYTHON/deneme.txt")
lines_count = count(example_lines)
lines_count

print("--------------------------------------------")

#İsimsiz Fonksiyonlar 
def old_sum(a,b):
    return a +b

print(old_sum(4,5))

new_sum = lambda a,b : a + b
print(new_sum(4,5))

sirasiz_liste = [("b",3),("a",8),("d",12),("c",1)] 
print(sirasiz_liste)

sirali_liste = sorted(sirasiz_liste, key = lambda x: x[1]) 
print(sirali_liste)

print("--------------------------------------------")

#Vektörel Operasyonlar
#OOP

a = [1,2,3,4]
b = [2,3,4,5]

ab = []

for i in range (0, len(a)):
    ab.append(a[i]*b[i])

print(ab)

#FP

import numpy as np 

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

print(a*b)

print("--------------------------------------------")

#map & filter & reduce

liste = [1,2,3,4,5]

for i in liste:
    print(i+10)

print(list(map(lambda x: x + 10, liste)))

#filter

liste1 = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(lambda x: x % 2 == 0, liste1)))

#reduce
from functools import reduce
liste2 = [1,2,3,4]

print(reduce(lambda a,b: a + b, liste2))

print("--------------------------------------------")

#Modül Oluşturma

import HesapModülü
HesapModülü.yeni_maas(2000)

import HesapModülü as hm 
hm.yeni_maas(3000)

from HesapModülü import yeni_maas
yeni_maas(4000)

print(hm.maaslar)

print("--------------------------------------------")

#Hatalar İstisnalar exceptions
#ZeroDivisionError hatası

a = 10
b = 0

try:    
    print(a/b)
except ZeroDivisionError:
    print("Paydada sıfır olamaz")

#Tip hatası

a = 10 
b = "2"

try:
    print(a/b)
except TypeError:
    print("Sayı ve string birbirine bölünemez.") 

