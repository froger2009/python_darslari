# UYga vazifa
#1 har bir ismga javob qaytarish
ismlar = ["sardor", "elyor", "jamshid","husniddin", "samandar", "sunnatillo"]
soni = 0
for ism in ismlar:
    soni+=1
    ism = ism.title()
    print(f"salom {ism}")
    print(f"tanishganimdan hursandman {ism}")
    print(soni)
#2 umumiy nechta ism borligini aniqlash
print(f"kod {soni} marta takrorlandi")

#3 10 dan 100 gacha oraliqdagi toq sonlarni kubini topish
toq_sonlar = list(range(11, 101, 2))
for toq_son in toq_sonlar:
    print(toq_son**3)

#4 foydalanuvchidan yoqtirgan 5 ta kinosini so'rab konsolga chiqarish
kinolar = []
print("eng yoqtirgan kinolaringizni kiriting")
for s in range(1,6):
    kinolar.append(input(f"{s} nchi yoqtirgan kinoyingizni kiriting  \n>>>"))
print(f"siz yoqtirgan top {len(kinolar)} kinolar \n{kinolar}")

#5 necha kishi bilan uchrashganligini so'rab ismini bilib u ismlarni konsolga chiqarish
daily_uchrashgan_odam = int(input("bugun necha kishi bilan uchrashdingiz ???\n>>>"))
uchrashganlar = []
for shaxs in range(daily_uchrashgan_odam):
    uchrashganlar.append(input(f"{shaxs+1} inchi uchrashgan odamingizning ismi nima"))
print(uchrashganlar)