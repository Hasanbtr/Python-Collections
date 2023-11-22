#Python Collections (Arrays)

#Pythonda 4 farklı liste tipi vardır. Bunlar; List, Tuple, Set ve 

#Dictionary veri tipleridir.

#List, elemanları sıralanabilir, güncellenebilir ayrıca her bir eleman liste içerisinde birden fazla tekrarlanabilir.

#Tuple, elemanları sıralanabilir ancak güncellenemez ve her bir eleman liste içerisinde birden fazla tekrarlanabilir.

#Set, elemanları sıralanamaz ve indekslenemez ayrıca her bir eleman liste içerisinde sadece bir tane olabilir.

#Dictionary, key ve value şeklinde değer alırlar. Aynı key bilgisiyle birden fazla eleman olamaz.

#Pythonda Liste

#String veri tipindeki her bir karakter bir grubun yani string karakter dizisinin bir elemanıdır ve her bir elemana indeks numarası ile ulaşabiliriz.

#Gene aynı mantıkla list veri tipinde ise tek bir karakter yerine farklı veri tiplerindeki bilgileri gruplayabiliyoruz. Karakter dizilerinde (string) olduğu gibi her bir eleman indekslenebilir.

#Ornek

message="Hello there my name is sadik turan".split()
print(message)
print(message[0])

#message ismindeki bir karakter dizisini (string) split() metodu ile bir listeye çevirebiliriz ve listenin 0.indeksindeki elemanı ekrana yazdırırsak karşımıza 'Hello' ifadesi gelir. Çünkü artık elimizde bir list mevcuttur.

#Liste Tanımlama

#Liste elemanlarından her biri farklı veri tipinde olabilir.

list1=[1,2,3]
list2=["1",2,True,"3"]

#Birinci liste elemanlarının hepsi aynı veri tipindeyken ikinci liste elemanları farklı veri tipinde tanımlanabilir dolayısıyla Python listeleri homojen bir yapıda olmayabilir.,
#İki farklı listeyi bir liste içinde gruplayabiliriz.

list3=[1,2,3]
list4=[4,5,6]
numbers=list3+list4
print(numbers)
print(list1+list2)

#Liste içinde farklı listelerde tanımlayabiliriz.
#Bu durumda list1 içinde 4 eleman var diyebiliriz ilk 3 eleman bir liste 4.eleman ise number türünde bir değer.
list5=[[1,2,3],[4,5],5]
print(list5[1])

#Örnek

kullaniciA=["Sadik",45]
kullaniciB=["Cinar",56]
kullanicilar=[kullaniciA,kullaniciB]
print(kullanicilar)

#Burada ise ilk olarak her bir kullanici bilgisini ayrı bir liste de tanımlayıp sonrasında kullanicilar isminde bir liste içinde gruplama yapabiliriz.

#Listelerde Eleman Sayısı

#Python listelerinde eleman sayısını len() metodu ile öğrenebiliriz. Aynı metodu string içinde kullanıp karakter sayısını öğrenebiliriz.

#Örnek

list1=["one","two","three"] 
list2=[[1,2,3],[4,5,6],[7,8,9],10]
print("1.listenin eleman sayisi :"+str(len(list1)))
print("2.listenin eleman sayisi :"+str(len(list2)))

#Liste Elemanlarına Erişim

#Python listelerindeki her bir elemanına soldan itibaren 0' dan başlayarak indeks numarası ile ulaşabiliriz. Aynı şekilde sağdan -1. indeks numarasından başlamalıyız.

#Örnek
message=["hello","there","my","name","is","sadik","turan"]
print(message[0],message[1],message[6])

#Aynı şekilde liste içinde bir başka liste tanımladığımızda ise alt liste elemanı içinde [ ] kullanmamız gerekir. 

#Örnek
print(list2[0][1])

#Liste Elemanlarına Döngü ile Erişim

#Liste elamanlarına indeks numaraları ile nasıl erişebileceğimizi öğrendik ancak her bir elemana indeks numarası ile tek tek ulaşmak bazen zor olabilir dolayısıyla liste elemanlarına bazen döngü ile ulaşmak isteriz.
#Burada 3 elemanlı names listesi içindeki her bir eleman sırasıyla name değişkeni içerisine kopyalanır ve print() metodu ile ekrana yazdırılır. 
names=["Ahmet","Mehmet","Cenk"]
for name in names:
    print(name)

#Liste Parçalama

#Listeden tek bir eleman seçmek yerine bir aralık belirtip eleman grubunu seçebiliriz.
#0 ve 2. indeks aralığında elemanlar seçilir ancak 0.indeks dahil 2.indeks dahil değildir.
#Sıfırdan başladığımızdan dolayı 0 değerini vermemiş olsak bile aynı sonucu alırız.

#Örnek
message=["hello","there","my","name"]
print(message[:3])

#Örnek

message = ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan'] 
print(message[:2])

#Burada [:2] diyerek baştan başla ancak 2. indekse kadar git demiş oluyoruz.

#Örnek

message = ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan'] 
print(message[2:])

#Burada ise [2:] diyerek 2.indeksten başla (başlangıç indeksi dahil) ve sona kadar git demiş oluyoruz.

#Örnek

message = ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan'] 
print(message[-3:-1])

#Burada ise -3. indeksten başla (dahil) ve -1. indekse (dahil değil) kadar git demiş oluyoruz.

message = ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan'] 
print(message[::]) 

#[::] diyerek tüm listeyi seçmiş oluyoruz.

#Liste Elemanlarını Güncelleme

#Liste elemanlarını güncellemek istediğimizde ilk olarak elemanı seçmemiz gerekiyor.

list1 = ['one','two','there'] 
list1[1] = 'updated' 
print(list1)

#1.indeksteki elemanı seçip 'updated' bilgisiyle güncelliyoruz.

#Python Liste Örnekleri

#1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar=["Bmw","Mercedes","Opel","Mazda"]
print(arabalar)

#2- Liste Kaç elemanlıdır ?
print(len(arabalar))

#3- Listenin ilk ve son elemanı nedir ?
print("ilk eleman :"+arabalar[0],"\n son eleman :"+arabalar[3],"\n Ayrica -1 indeks ile son eleman :"+arabalar[-1])

#4- Mazda değerini Toyota ile değiştirin.
arabalar[3]="Toyota"
print(arabalar)

#5- Mercedes listenin bir elemanı mıdır ?
soru1='Mercedes' in arabalar
print(soru1)

#6- Listenin -2 indeksindeki değer nedir ?
soru2=arabalar[-2]
print(soru2)

#7- Listenin ilk 3 elemanını alın.
print(arabalar[:3])
print(arabalar[:-1])

#8- Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
arabalar[-2:]="Toyota","Renault"
print(arabalar)

#9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
ekle=arabalar+["Audi","Nissan"]
print(ekle)

#10- Listenin son elemanını silin.
del arabalar[-1]
print(arabalar)

#11- Liste elemanlarını tersten yazdırınız.
tersten=arabalar[::-1]
print(tersten)
