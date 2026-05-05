#1 temperatura
temperatura = int(input("bugungi haroratni kiriting  \n"))
if temperatura <= 0: print("Sovuq. Kiyinib chiqing!!")
elif temperatura <= 20: print("Salqin havo")
else: print("issiq havo")

#2 list bilan solishtirish
mevalar = ["olma", "nok", "uzum", "shaftoli", "gilos", "o'rik"]
meva = input("meva kiriting  \n")
if meva.lower() in mevalar: print(f"{meva} bizda bor")
else: print(f"{meva} bizda yo'q")

#3 maoshga ko'ra soliq aniqlash
soliq = 0
ish_haqi = int(input("ish haqi kiriting  \n"))
if ish_haqi <= 1_000_000:
    soliq = 0
elif ish_haqi <= 5_000_000:
    soliq = soliq + 10
else:
    soliq = soliq + 20
print(f"sizning ish solig'ingiz {soliq}% ni tashkil etadi")

#4 ism qidirib yoq bolsa qo'shish
oquvchilar = ["ali", "vali", "soli", "hasan", "husan"]
ism = input("Ism kiriting  \n")
if ism in oquvchilar:
    print("o'quvchi topildi")
else:
    print("Yangi o'quvchi qo'shildi")
    oquvchilar.append(ism)
print(oquvchilar)

#5 xarid summasiga qarab chegirma ajratish
mahsulotlar = []
narxlar = []
chegirma = 0
for n in range(1, 4):
    mahsulotlar.append(input(f"{n} chi mahsulotni kiriting  \n"))
    narxlar.append(int(input(f"{n} chi mahsulotning narxini kiriting  \n")))
umumiy_narx = sum(narxlar)
if umumiy_narx <= 100_000:
    chegirma = 0
elif umumiy_narx <= 300_000:
    chegirma = chegirma + 10
else:
    chegirma = chegirma + 20
chegirmali_narx = umumiy_narx - (umumiy_narx * chegirma / 100)
print(f"umumiy narx {umumiy_narx} som")
print(f"chegirmali narx {chegirmali_narx}  som")