koreya = "안녕하세용"
print(koreya)

#+bilann birlashtirish
ism = "abdulaziz"
familiya = "MAMASOLIYEV"
davlat = "yaponiya"
print("mening davlatim " + davlat)
print("mening davlatim",davlat)
print(ism+ " " +familiya)#string sifatida bosh joyni ishlatish mumkun

#f string usuli
print(f"{ism} {familiya}")
son_a = 12
son_b = 56
print(f"{son_a}ga {son_b}ni qo'shsak javob {son_a + son_b} bo'ladi")

#\t \n \r maxsus belgilari
print("yangi \nline")#yangi linega olib tushadi
print("ko'p bosh \tjoy" )
print("oldingi \rso'zlarnini o'chiradi")

#string metodlari
print(ism.upper())# .upper() metodi yordamida stringni barcha harflarini katta holatga o'zgartira olamiz
print(familiya.lower())# .lower() metodi yordamida stringni barcha harflarini kichkinaga o'zgartira olamiz
print(f"{ism} {familiya}".title())# .title() metodi yordamida stringni har bir so'ziningbirinchi harfini kattaga o'zgartiradi

print(f"{ism}{familiya}")
ism_familiya = f"{ism} {familiya}".title()
print(ism_familiya)

print(ism_familiya.capitalize())# .capitalie() metodi yordamida stringni ichidagi birinchi so'zni birinchi harfidan boshqa hamma so'zlar kichik harfga o'zgaradi

#l r strpit bo'sh joylarni qirqish metodi
niyyat = "  yaponiya    "
print(f"men {niyyat.strip()}ga bormoqchiman")# l\r yoki .strip() orqali matndagi keraksiz bo'sh joylarni qirqib tashlay olamiz

#input funksiyasi
data = input("ismingizni kiriting\n")
print(f"arbuz arbuz privet {data}")#input funksiyasi yordamida userdan malumot qabul qilib ola olamiz


#Uyga vazifa
#!
kocha = input("ko'changizni kiriting\n")
mahalla = input("mahallangizni kiriting\n")
tuman = input("tumaningizni kiriting\n")
viloyat = input("viloyatingizni kiriting\n")
manzil = f"{kocha.capitalize()} ko'chasi, {mahalla.capitalize()} mahallasi, {tuman} tumani , {viloyat.capitalize()} viloyati"
print(manzil)
