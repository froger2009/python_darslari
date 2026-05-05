#sonlar

# type() funksiyasi yordamida o'zgaruvchini turini bilishimiz mumkun
a = 12.3#float sonlarni yozishda doim nuqta quyiladi
print(type(a))

#pastki chiziqcha bilan sonlarni ajratish
haridorlar_soni = 34_502
print(haridorlar_soni)

#pythonda birdaniga ko'p o'zgaruvchilarga qiymat berishimiz mumkkun
son_a , son_b , son_d = 123.78 , -21 , 873
print(son_a, son_b, son_d)

#PYTHONDA INT BILAN FLOAT KURINISHIDAGI SON USTIDA AMAL BAJARSAK NATIJA DOIM FLOAT KURINISHIDA CHIQADI

kopayuvchi_1 ,kopayuvchi_2 = 12, 3.3
amal = kopayuvchi_1* kopayuvchi_2
print(amal)

#sonlarni ustida bo'lish amalini qilsak ham natija float kurinishida chiqadi
print(120/4)

#konstanda yani o'zgartirilmaydigan qiymatni belgilashda doimo katta harflardab foydakanamiz
radius = 3
PI = 3.14159
diametr = 2*radius
print(f"aylananing uzunligi= {diametr*PI}")

# string bilan intijr qiymatlarini qo'shib bo'lmaydi konvertatsiya qilish kerak
ism = "abdulaziz"
yosh = 17
yosh = str(yosh)
message = "salom " + ism+ " siz ", yosh+ " yosh ekansiz"
print(message)

#foydalanuvchidan yil sorab yoshini aniqlash
yil = int(input("tug'ilgan yilingizni kiriitng \n"))
yosh = 2026-yil
print(f"sizning yoshingiz hozirda {yosh} yosh ekan")

#Uyga vazifa

#1
son = int(input("istalgan son kiriitng\m"))
print(f"{son} ning kvadrati {son**2} ga teng")
print(f"{son} ning kubi {son**3} ga teng")

#2
yosh2 = int(input("yoshingiz nechada ?\n"))
print(f"siz {2026-yosh2} chi yilda tug'ulgansiz")

son_1 = int(input("1 chi sonni kiriitng \n"))
son_2 = int(input("2 chi sonni kiriitng \n"))
yigindi = son_1 + son_2
ayirma = son_1 - son_2
kopaytma = son_1 * son_2
bolinma = son_1 // son_2
print(f"{son_1} + {son_2} = {yigindi}\n{son_1} - {son_2} = {ayirma}\n{son_1} * {son_2} = {kopaytma}\n{son_1} / {son_2} = {bolinma}\n")