# if else

# shart operatorlaridan oddiy foydalanish
detallar = ["gpu", "cpu", "plata", "blok", "cooler", "case", "ssd", "ram"]
for detal in detallar:
    if detal == "gpu" or detal == "cpu":
        print(detal.upper())
    else:
        print(detal.title())

# teng yoki yo'qligini aniqlash
ism = "abdulaziz"
if ism == "abdulaziz":
    print("xa")
elif ism != "abdulaziz":# != tenf emaslifini so'rashda fotdalaniladi
    print("yo'q")

# ism tekshirish 
ism_2 = input("ismingizni kiriting  \n>>>")
if ism_2.lower() != "abdulaziz":
    print(f"uzur {ism_2.title()} siz biz qidirayotgan odam emassiz")
else:
    print("salom abdulaziz")

# shart operatorlari bilan sonlar ustida ishlash
javob = int(input("8 x 12 javobi necha?? \n>>>"))
if javob != 96:
    print(f"javob {javob} emas xato")

# yosh buyicha dastur
yosh = int(input("yoshingizni kiritng \n"))
if yosh >= 16:
    print("tomosha qilishingiz mumkun")
else:
    print(f"siz {yosh} yoshligingiz uchun tomosha qilish taqiqlanadi !!!")

# parol sonini aniqlash


parol = input("parol kiriting  \n")
if len(parol) <= 8:
    print("kechirasiz...\nparol kamida 8 xonali sondan iborat bo'lishi kerak \nqaytadan urunib ko'ring")
else:
    print("parol muvaffaqiyatli o'rnatildi")

# tug'ulgan yil buyicha yosh buyicha cheklash
tugilgan_yil = int(input("tug'ilgan yilingizni kiriting \n"))
if 2026-tugilgan_yil<16:
    print(f"kechirasiz...\nyoshingiz {2026 - tugilgan_yil} yoshligi uhcun sizga kirish mumkun emas")
else:
    print("hush kelibsiz")

# uylanish kerak bulgan yosh anqilash va bir qatorda yozish
yosh_2 = int(input("yoshingizni kiriitng  \n>>>"))
if yosh_2 >= 30: print("siz allaqachon uylanishingiz kerak ekan")

# if va else operatorlarini bir qatorda yozish
son_1 , son_2 = 120, 500
print(f"{son_1}>{son_2}") if son_1 > son_2 else print(f"{son_1}<{son_2}")