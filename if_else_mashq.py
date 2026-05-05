# Uyga Vazifa

#1 faqat gm ni katta harfda chiqarish
cars = ['toyota', "mazda", "hyundai", "gm", "kia"]
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())

#2 huddi shu amalni teskari != belgisi yordamida bajarish
for car_2 in cars:
    if car_2 != "gm":
        print(car_2.title())
    else:
        print(car_2.upper())

#3 admin dasturi
login = input("login kiriitng  \n>>>")
if login.lower() == "admin":
    print(f"hush kelibsiz, {login.title()}. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Hush kelibsiz, {login.title()}")

#4 teng sonlarni aniqlash
son_1 = int(input("1 chi sonni kiriting \n"))
son_2 = int(input("2 chi sonni kiriting \n"))
if son_1 == son_2:
    print("sonlar teng")
else:
    print("sonlar teng emas")

#5manfiy musbat son aniqlash
istalgan_son = int(input("istalgan soningizni kiriting  \n"))
if istalgan_son>0:
    print("musbat son")
elif istalgan_son<0:
    print("manfiy son")
else:
    print('bu son 0 ga teng')

#6 musbat sonni ildizini topish
ildiz_son = int(input("son kiriting \n"))
if ildiz_son > 0:
    print(ildiz_son ** 0.5)
else:
    print("musbat son kiriting")