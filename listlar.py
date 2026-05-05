#tuple
#oddiy list
meva = "olma"
raqam = 12
tillar = ["python", "java", "react" , "php", meva, raqam]
print(tillar)

# elementniindeksi buyicha chaqirish
mashina_brendlar = ['chevrolet', "mersades", "bmw", "jeep"]
print(mashina_brendlar[2])

#ro'yxatni ohiridagi elementni chaqiirsh uchun - dan foydalanammiz
print(mashina_brendlar[-3])

# elementlarni o'zgartirish eng oddiy
davlatlar = ["yaponiya", "koreya", "Uzbekiston", "rossiya", "germaniya", "britaniya"]
davlatlar[4] = "fransiya".title()# yangisiga uzgartirib unga title metodini qulladik
print(davlatlar)

# listga yangi element qushish append metodi
davlatlar.append("braziliya")
print(davlatlar)

# extend metodi yordamida listga yana bir listni qo'sha olamiz yoki bir nechta qiymat
davlatlar.extend(["afrika", "sudan", "chexiya"])
print(davlatlar)

# insert metodi yordamida listni istalgan joyiga element joylay olamiz
davlatlar.insert(2, "xitoy")
print(davlatlar)

# bosh list yasab uni to'ldirib borish
pc_resurslar = []
pc_resurslar.append("protsessor")
pc_resurslar.append("plata")
pc_resurslar.append("keys")
pc_resurslar.append("kuller")
pc_resurslar.append("monoblok")
pc_resurslar.append("blok pitaniya")
pc_resurslar.append('monitor')
pc_resurslar.append("ssd")
pc_resurslar.append("ram")
pc_resurslar.insert(1, "videokarta")
print(pc_resurslar)

# del kalit so'zi yordamida elementni o'chirib tashlash mumkun
del pc_resurslar[-3]
print(pc_resurslar)

# remove metodi yordamida listni ichidagi elementni indeksiga murojat qilmay nomi bilan o'chirib tashlash mumkun
pc_resurslar.remove("monoblok")
print(pc_resurslar)

# pop metodi yordami listdagi elementni sug'urib olishimiz mumkun
zarur = pc_resurslar.pop(1)
print(zarur)  
#pop metodiga index berilmasa avto listni oxiridagi elementni oladi

#kichik dasturcha
zarur2 = pc_resurslar.pop(0)
print(f"menga shu kunlarda eng zarur narsa bu {zarur2}")
print(f"{pc_resurslar} bular esa zarur emas")

# list part 2

# sort() metodi yordamida listni alifbo ketma ketlifida taxlash olamiz
sinf = ['ali', 'zuxra', "elyor", "farangiz", "laylo", "shavkat", "g'ulom", "ergash","alisher", "ulug'bek"]# katta harf birinchi chiqadi
sonlar = [12, 657, -12, -654, 0, 1, 6, 900]
sinf.sort()
print(sinf)
sonlar.sort()
print(sonlar)

# sort metodiga argument berib alifbo teskarisiga chiqarish mumkun
sinf.sort(reverse=True)
print(sinf)

# sorted metodi yordamida asl listga tegmay faqat chiqayotgan natijani o'zgartira olamiz
print(sinf)

# reverse metodi yordamida ro'yxatni teskariga aylantirishimiz mumkun
sinf.reverse()
print(sinf)

# len funksiya yordamida list ichidagi elementlar sonini o'lachash mumkun
print(len(sinf))
print(len(sonlar))

# range funksiyasi yordamida malum bir oraliqdagi sonlarni yarata olamiz
sonlar_2 = list(range(2, 10))
print(list(range(0, 21, 2)))
print(sonlar_2)

# max min funksiyasi eng katta va eng kichik sonni topadi
max_son = max(sonlar_2)
print(max_son)#max

min_son = min(sonlar_2)
print(min_son)

# sun funksiyasi yordamida sonlarni bir biriga qushgandagi yig'indisini topa olamiz
print(sum(sonlar))
# kichik dastur
narxlar = [150, 300, 55, 100, 45]
print(f"aniqlashimizga ko'ra bu yerda eng qimmati {max(narxlar)} va eng arzoni {min(narxlar)} \nva umumiy qancha bolishini bilmoqchi bolsangiz {sum(narxlar)}")

# pythonda malum bir indekslar orasidagi elementlarni chiqarish uchun list_nomi[1: 5]
print(sonlar[2 :-1])
print(sonlar[:2])# birinchi element indeksi berilmasa avto 0  indexdagini oladi
print(sonlar[2:]) # ohirigi index berilmasa avto ohiridagi indexdagi sonni oladi

# listdan nusxa olish
yangi_sonlar = list(range(10, 21))
kochirilgan_sonlar = yangi_sonlar[:]
del kochirilgan_sonlar[0]
print(kochirilgan_sonlar)
print(yangi_sonlar)

# tuple ro'yxat turi list bilan oxsahsh indeks bilan chaqirsak boladi elementlarini lekin royxatga hech qanday o'zgaritirish kirita olmaymiz
ozgarmas_royxat = ('otmish', "istak", "otgan ish", "damas qatnovi")
print(ozgarmas_royxat[-1])

# tuple bolsa ham list metodi yordamida list kurinishiga keltirib ustida ishlay olamiz

ozgarmas_royxat = list(ozgarmas_royxat) 
del ozgarmas_royxat[1]
print(ozgarmas_royxat)