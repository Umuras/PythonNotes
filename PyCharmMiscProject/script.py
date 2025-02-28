# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(type(2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# type ile objenin tipine bakabilirsin type(2) int gibi
# int(2.4) float sayıyı tam sayıya dönüştürür. 2 olur
# float(4) 4.0 olur
# 3 // 2 şeklinde yazdığında 1 olarak döner int türünde bölme yapıyor, . dan sonrasını yazmıyor, eğer biri float olursa da yine o sayının bu 0'doğru yuvarlanmış
#halini alıyor, mesela 7 //2.2 normalde 3.18 bir şey çıkacak ama 3.0 verecek sonucu
# 3 ** 2 de ise üs alma işlemi yani 9 oluyor.
print(7 // 2.2)
print(3 ** 2)

# Stringler bir şeyin string olduğunu belirtmek için "" ya da '' içine yazıyouruz. Bunu bir karakter dizisi olarak algılıyor
# Hangisi ile başladıysan onunla bitirmelisin, "''" '""' bu şekilde de yazabilirsin.
# String türü Non-scaler bir veri tipidir, içinde daha alt parçalar barındırır , mesela bir isim değişkeninin "ali" a-l-i karakterlerinden oluşmasıdır.
# Aynı zamanda immutable bir veri tipidir, yani gidip isim diye bir değişken oluşturup ona değer atayıp sonra isim[0] = "b" diye bir atama yapamazsın.
isim = "AliUmur"
print(isim[0]) #bu şekilde A harfini basacaktır.
print(isim[0:3]) #bu şekilde A harfinden başlayıp 3.indise kadar gidecektir ama o dahil değildir. Yani Ali yazacaktır.
print(isim[0].lower()) #harfi küçültecektir.
# Escape sequences ile "içinde """ kullanabiliyoruz, ikinci yazılan tırnakları bir string ifade gibi algılamasını sağlıyor.
print("Bana \"Bugün ne yapıyorsun\" dedi") #Bu şekilde \ slash sonrasında olan " çift tırnağı string ifade olarak algıladı.
print('Bugün Kadıköy\'e gidiyorum')
print("hey \nnasılsın") # \n bir alt satıra geçiyor \t 4 adet boşluk bırakıyor
print("hmm \\") #Escape sequence olarak değil normal tek bir tane \ slash olarak davranıyor

ehliyet = False
araba = True

if ehliyet and araba:
    print("Araba kullanabilirsin")
elif araba and not ehliyet: #not ehliyet false olan değişkeni trueya, true ise false'a dönüştürecek
    print("Bizim sürücü kursumuza başvurabilirsin.")
elif ehliyet or araba:
    print("Araba kullanmana çok az kaldı")
else:
    print("Araba kullanman için çok zaman var")

if not ehliyet:
    print("ehliyetin yok")

heat = 29

if heat >= 30:
    print("Hava çok sıcak")
elif heat <= 0:
    print("Hava çok soğuk")
elif heat == 40:
    print("Hava 40 derece")
else:
    print("Hava çok güzel")


# Askerlik Ödevi
age = int(input("Yaşınızı giriniz: "))
isGoingToSchool=bool(input("Okula gidiyor musun?(yes/No): "))

if age >= 18 and not isGoingToSchool:
    print("Askere Gelme Yaşınız Geldi!")
elif age >= 18 and isGoingToSchool:
    print("Okulunuz bittiğinde askere geleceksiniz")
else:
    print("Askerlik yaşınız daha gelmedi")


#While Döngüsü
i = 1
while i <= 5:
    print(i)
    i += 1

#Diziler
employees = ["Mehmet","Ahmet","Abdullah","Kerim","Ali"]
#sondaki kişiyi yazmak istersen -1 yazıyorsun.
#bir indisten belli bir indise kadar yazdırmak istiyorsan
#employees[0:3] 0,1,2. indisteki elemanları yazar, 3. dahil değil
print(employees[0])
print(employees[len(employees)-1])

#Successive Concatenation(Ardışık Birleştirme)
# * operatörü sayı objeleri için çarpım olarak tanımlanmışken, stringler için ard arda birleştirme yapıyor
#Örnek
print(4*"hey") #bu şekilde 4 kere yan yan hey yazacak
#len() ile string içinde kaç karakter veya bir dizinin uzunluğunu söyler
print(len("123"))
print("Ali"[0]) # Bu şekilde de indeksleme yapabiliyorsun

#Slicing (Dilimleme)
print(employees[0:3]) #Bu yapıya slicing deniyor. 0'dan 3.indise kadar olan elemanları getiriyor. 0 dahil 3.indis dahil değil
print(employees[:3]) #Bu ile yukarıdaki aynı 0 yazmazsan default 0 dır.
print(employees[0:]) #Sonuna kadar tüm elemanları getirir bu şekilde
print(employees[:]) #Bu da tüm elemanları getirir.
#Slicing yaparken bitiş olarak verdiğimiz değer en büyük indeksimizden büyükse hata almayız, sonun kadar alır(sadece indeksing yaparken en büyük indeximden
# büyük olan değerler için hata alırım)
# Örnek
print(employees[0:20]) # Hata almazsın, tüm elemanlar gelir.
#print(employees[20]) # Hata alırsın çünkü böyle index yok.
# başlangıç:bitiş olarak slicing yapabileceğimiz gibi, başlangıç:bitiş:adım formunda da slicing yapabiliriz. Buradki adım parametresi kaçar kaçar gideceğimizi
#belirler
print(employees[0:4:2]) #Mehmet, Abdullah yazdıracaktır.
print(employees[5:0:-1]) #Tersten gidecek şekilde de yapabiliyoruz
print(employees[5::-1]) #Terseten sona gider
print(employees[::-1]) #Tersten sona gider
print(employees[::-2]) #Tersten sona ikişer ikişer gider

#String Casting
a = "5"
b = "5.3"
print(int(a))
print(float(b))
print(int(float(b))) #float bir sayı olduğu için b önce floata sonra int yapabilmek için inte çeviriyoruz, string ifade floatu temsil ediyorsa direk int yapamazsın

y=int(input("Ondalık bir sayı giriniz: ")) #Klavyeden ondalık sayı girersen hata alırsın, çünkü 0.25 olarak gelen string bir ifadeyi inte dönüştürmeye
#çalışıyorsun, önce float sonra o sonucu inte dönüştürmen lazım
sonuc=y*4
print(sonuc)
"""
buraya yazılan her şey yorum olarak algılanıyor
asdasd
asdasda
"""

#Short-circuit
#Burada sol tarafa eğer True ise sağ taraftaki işlem yapılır ama bunu & mantıksal operatörü ile yapamazsın. Sol taraf false ise
#sağ tarafa bakmaz ve false döndürür
(5 < 3) and print("hey")
#Burada sol taraf false ise sağ tarafa bakmaya ihtiyaç duyar çünkü normalde sol taraf True olduğun sağ taraf ne olursa olsun Truedur
#Özetle sol taraf false ise sağ tarafın işlemini yapar, ama sol taraf True ise onu döndürür ve sağ taraftaki işleme bakmaz.
(5 < 3) or print("hey")


z = int(input("Bir sayı giriniz: "))
if z % 2 == 0 and z % 3 == 0:
    print("Sayı hem 3 hem 2 ye bölünüyor")
print("Program bitti.")

#Ternary Operators
h = int(input("Bir sayı giriniz: "))
#Buranın çalışma şekli if sağında yazan şart True ise solunda ifade değişkene atılır yanlış ise elsein sağındaki atanır.
answerTest = True if h == 2 else False
print(answerTest)


#For döngüsü
# for <degisken> in <obje> objenin her elemanını teker teker dönüyoruz
for c in "hey": #string karakter dizisi olduğu için c, h, e, y harflerini alıp yazdırılacak
    print(c)

for i in range(5): #0'dan 5'e birer birer artarak 5 dahil olmadan ekrana yazıyoruz.
    print(i)

#List, list içinde string, int, farklı bir liste, boolean türlerini tutabilirsin.
ogrnot_1 = 60
ogrnot_2 = 70
ogrnot_3 = 40
ogrnot_4 = 45
ogrnot_5 = 65
notlar = [78,80,43,65,90,80]
notlar2 = [ogrnot_1, ogrnot_2, ogrnot_3, ogrnot_4, ogrnot_5]
#Stringdeki indexing ve slicing yapılabiliyor
print(notlar[0])
print(notlar[0:3])
print(notlar[-1])
print(notlar[:200])
#Listler mutable veri tipleridir, elemanlarını güncelleyebiliriz.
notlar[1] += 5
#Slicing ile veri değiştirme yapabiliyorsun
notlar[0:3] = 30,40,60 #0,1,2.nci indisin değerleri sırasıyla değişiyor
notlar[0:3] = 30,40 #sadece 0 ve 1.inci indisinide değiştirebiliyorsun.
notlar[0:3] = 30 #Ama bunu yapamazsın hata iterable olması gerekiyor. bunu yapabilmek için
notlar[0:3] = [30] #yapmalısın ve bu şekilde notlar = [30,65,90]'a dönüşüyor
len(notlar) #Kaç eleman olduğunu veriyor
#Listin sonuna eleman eklemek append
notlar.append(95)
#extend() içine birden çok elemanı listenin sonuna ekler
notlar.extend([55,65,78]) #[78,80,43,65,90,55,65,78] olur
#Spesifik bir indexe eleman eklemek
notlar.index(0,100) #0.indise 100 koyup diğer elemanlar bir indis ileri gidiyor.
#Belirli bir elemanı listeden silmek
notlar.remove(80) #bu şekilde listedeki iki tane 80 de silinmeyecek sadece ilk 80 silinecek
#eğer remove edeceğin eleman listede yoksa hata alırsın bunun önüne geçmek için try catch yapısını kullan
try:
    notlar.remove(99)
except ValueError:
    pass
#pop ile hem listeden siliyor hem de o değeri bize getiriyor
print(notlar.pop(3) + 5) #Eğer o indiste eleman yok ise hata alırsın.
#count ile listeden bir elemanın kaç defa görüldüğünü görüyoruz
print(notlar.count(5)) #Eğer listede bu eleman yoksa 0 döner
#bir listeyi kopyalamak
notlarKopya = notlar.copy()
#Listing concatenation iki listeyi birbiri ile toplayıp yeni liste oluşturabilirsin bu var olan listeleri değiştirmez
notlarTest = [44,52,61]
print(notlar + notlarTest) #notların yanına notlarTest'yi ekler
#78,80,43,65,90,80,44,52,61] şeklinde

#Eleman Index bulma
notlar.index(65) #3 gelir, eğer eleman listede yoksa hata verir, eğer aynı elemandan iki tane varsa en yakın index değer gelir

#Listeyi tersine çevirmek
notlar.reverse() #liste artık güncellenmiş olur, eğer listenin değerlerini korumak istersen kopyasını alıp onun üzerinde devam et
#Slicing ile reverse
nt = notlar[::-1]

#Listeyi sıralamak, sayılar küçükten büyüğe, harfler alfabetik, sort var olan listeyi günceller
notlar.sort()
letters = ["b","c","a","d","x","n"]
letters.sort()
#sorted ise güncellemez
sorted(letters)
#Eğer hem harf hem sayılar varsa önce sayılar sonra harfler sıralanır ama sayılar string türde olmalı yoksa hata alırsın
test = ["a","b","d","c","2","1","5"]
#Liste içinde listeleri sort edersen iki listenin ilk elemanına göre küçükten büyüğe göre sıralar
test2 = [[20,5,17],[15,5,88]]
test2.sort()
test3 = [[150,"a",6],[45,"b",78]] #bu da ilk başta 150 ve 45'e bakacak 45 daha küçük olduğu için başa gelecek
#iki liste elemanlarında biri int biri string olursa hata alırsın.


#TUPLE: veri tipi listeler gibi birden çok veri tipini bir arada tutmamızı sağlar.
#listelerden farklı olarak tuple immutabledır. Farklı veri tipleri alabilir, list bile
position = (10,34) #artık position tupleının değerleri değiştirilemez.
#position[0] = 100 hata yapamazsın
t = (1,2,3,4,"a") #olur
t2 = ((1,2),4) #tuple içinde tuple tanımlayabilirsin.
t3 = ([1,2,3],[4,8,9]) #tuple içinde liste tanımlayabilirsin.
print(t3[0][0]) #ilk elemanı listeye erişip, listenin ilk elemanına erişiyor
#Elemanların değerlerini değiştirmek
x = 5
y = 4
(x,y) = (y,x)
x,y = y,x
[x,y] = [y,x] #listeler içinde yapılabiliyor
#parentez koymadan da yapabilirsin pyhton onu tuple olarak algılar
ac = 1,2,3,4,5

#Belirli bir elemanı listede veya tuple var mı diye in ile kontrol edebiliyoruz
print(40 in t) #true veya false döner
print(78 in notlar)

#Dictionaries, key value çifti olarak çalışır, search hızı yüksektir, key üzerinden aradığı için
notes = {"Deniz": 80, "Ege": 72, "Gizem": 88}
print(notes["Deniz"]) #keyi ile 80'i alırız
#Dictionary keyleri immutable herhangi bir yapıda olabilir, valuelar mutable ya da immutable olabilir, int, float, bool,
#string, list, tuple, set gibi.
ogrenciler = {"Deniz": {"not":80,"ogrencino":703}, "Ege": {"not":72,"ogrencino":408}, "Gizem": {"not":95, "ogrencino":690}}
print(ogrenciler["Deniz"]["not"])
#Olmayan bir elemanı yani keyi sorgularsan hata alırsın
notes["Deniz"] = 85
notes["Deniz"] += 5

#Eleman eklemek, silmek, len
notes["Mert"] = 45 #Yeni key ismi yazılıp valuesu atanır
len(notes) #key sayısı öğrenilir
del notes["Mert"] #Mert key value çifti silinir.
#Sadece immutable tipindeki veriler key olabilir, list veremezsin çünkü mutable
#Boş dictionary oluşturmak
d = {}
#in ile kontrol
print("Mert" in notes)

#Fonksiyonlar değer döndürmeyen void fonksiyon
def calculate(num):
    num*num

#Geri dönüş değeri olan fonksiyon
def square(x):
    result = x*x
    print(result)
    return result

res = square(5)

#Geri dönüş değeri olup if ile kontrol yapma
def f(num):
    result = num * num
    if num % 2 == 0:
        print("Sayı çifttir")
        return result
    else:
        print("Sayı tektir")
        return result

#Fonksiyon içinde for döngüsü kullanma
def f2(num):
    for i in range(5):
        num += 5

    print(num)
    return num

#Fonksiyon içinde listeye eleman ekleme
def f3(num):
    res = num
    l = []
    """
    Deneme
    """
    #Döngü ile değer arttırıp listeye her elemanı ekliyoruz
    for i in range(10):
        res += 20
        l.append(res)

    return l

#Fonksiyon hakkında bilgi öğrenme
#?f3(4)
#??f3(4)

#Birden çok input alma
def f4(x,y):
    return x + y
#Birden çok result dönme
def f5(num1,num2):
    return 2*num1,4*num2
(a,b) = f5(3,4) #bu bize sonucu tuple olarak döner

#Ön tanımlı fonksiyonlar, bu fonksiyonlarda eğer parametreye değer atanmazsa method içinde tanımlanan değer çalışır
#Predefined değerler yazılırken en sona yazılmalıdır yoksa hata alırız
def f6(str1, str2="World"):
    print(str1 +" "+ str2)

f6("Hello")

#Argümanların değerlerinin değişip değişemeceği durumlar
#int ve float türündeki değişkenlerin değerleri değişmez
num5 = 4
def f7(num5):
    num5 = 5
    return num5
#Ama listenin değişir, çünkü o referans türde
#Değişmemesi için ya argüman olarak göndermeden kopyasını alıp göndermelisin ya da fonksiyon içinde
#kopyasını alıp işlem yapmalısın
l = [1,2,3,4]

def changeValue(l):
    l[0] = 5
    return l
changeValue(l)

#First-class function, pyhton da yazdığımız her fonksiyon bir first-class functiondır
#Bu şu demek bir fonksiyon değişkene atılabilir
a = changeValue(l)
a(5)

#Bir fonksiyon başka bir fonksiyona argüman olarak verilebilir
def sqr(num):
    return num*num

def test(num1, fs):
    return sqr(num1)*5
test(5,sqr)

#Bu fonksiyon ile listedeki her elemanın karesini alıp ona eşitliyoruz
def apply(l,f):
    n = len(l)

    for i in range(n):
        l[i] = f(l[i])
    return l
apply(l,sqr)

#Underscore Placeholders büyük sayıları ayırmada kullanıyoruz
n1 = 9_000_000 #bu şekilde underscore olmadan da olarak da aynı sonucu veriyor bize okuma kolaylığı sağlıyor
n2 = 0.12_14_16 #floatta da yapılabilir

#fstring ile değerlerimizi direk string içine koyabiliriz
x = 15
print("Ben {x} yaşındayım",x)
#veya içinde fonksiyon bile çalıştırabiliriz
print("{x}'in karesi {sqr(x)}")
l21 = [1,2,3,4]
#listede yazabiliriz
print("Liste {l21}")

ad = "Ali Umur"
print("Benim adım {ad}")