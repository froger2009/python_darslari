# if elif else
# elif operatori yordamida yosshga ko'ra narx belgilash
yosh =  int(input("yoshingizni kiriiting  \n"))
if yosh <= 7:print("sizga kirish bepul")
elif yosh <= 18: print("sizga kirish 10 ming so'm")
else: print("sizga kirish 20 ming so'm")
    

# print operatori bilan takrorlashsiz natija chiqarish
tugilgan_yil = int(input("tugilgan yilingizni kiriting  \n"))
if 2026 -tugilgan_yil <= 7:
    narx = 0
elif 2026 - tugilgan_yil <= 18:
    narx = 10_000
else:
    narx = 20_000   
print(f"sizga kirish {narx} som")

# or operatorilari ga misol
detal = input(" pc dan eng kerakli detal nima? \n")
if detal.lower() == "gpu" or detal.lower() == "cpu": print("siz to'g'ri topdingiz")
else: print("noto'g'ri... \nqaytadan uruning")

# and operatori ga misol
gpu = input("gpu turini kiriting \n")
brend = input("qaysi brendga tegishli? \n")
narxi = int(input("narxi necha $ ?\n"))
if (gpu.lower() == "rtx 3070" or gpu.lower() == "rtx 3070ti" or gpu.lower() == "rtx 4070" or gpu.lower() == "rtx 5070") and (brend.lower() == "asus" or brend.lower() == "msi" or brend.lower() == "gigabayte" or brend.lower() == "palit") and narxi <= 300: print("가성비")
else: print("비례가 부재 !!!")

# boolean qiymatlar ga missol
umumiy_narx = 500

sichqoncha = True
klaviatura = False
if sichqoncha and klaviatura:
    umumiy_narx = umumiy_narx+ 50
elif sichqoncha or klaviatura:
    umumiy_narx = umumiy_narx+ 25
print(f"sizdan opshi {umumiy_narx} dollar")

# har bir if ni alohida tekshirish
pc_narx = 0
cpu = False
gpu = True
case = True
ssd = False
ram = True
plata = False
blok = False
cooler = 1 # true o'rniga 1 yoki false o'rniga 0 dan foydalansak ham hech narsa o'zgarmaydi
if cpu:
    print("cpu oldiz")
    pc_narx = pc_narx + 120
if gpu:
    print("gpu oldiz")
    pc_narx = pc_narx + 300
if case:
    print("case oldiz")
    pc_narx = pc_narx + 50
if ssd:
    print("ssd oldiz")
    pc_narx = pc_narx + 60
if ram: 
    print("ram oldiz") 
    pc_narx = pc_narx + 100
if plata:
    print("plata oldiz")
    pc_narx = pc_narx + 90
if blok:
    print("blok oldiz")
    pc_narx = pc_narx + 60
if cooler:
    print("cooler oldingiz")
    pc_narx = pc_narx + 80
print(f"sizdan opshi {pc_narx} dollar")

# in operatoris
detallar = ["cpy", "gpu", "ram", "ssd", "case", "plata", "blok", "cooler"]
if "ram" in detallar:
    print("xa")
else:
    print("yo'q")

    #kichik dastur
xarid = input("nima xarid qilmoqchisiz?  \n")
if xarid not in detallar:# not in operatori bo'lmasa deb tarjima qilinadi
    print("afsuski kechagina tugab qogandi")
else:
    
    print("axa bizda bu detal mavjud")

#for va in yordamida 2 ta listni solishtirish
gpus = ["rtx 3070", "rtx 3060", "rtx 2060 super", "gtx 1660 super", "rtx 4060ti"]
importants = ["gtx 1660 super", "rtx 2060 super", "rtx 3050", "rtx 4060", "rx 580"]
if importants:
    print(f"ro'yxatda umumiy {len(importants)} ta buyurtma mavjud")
    for important in importants:
        if important in  gpus:
            print(f"bizda {important} mavjud")
        else:  
            print(f"bizda {important}  mavjud emaws")
else:
    print("ro'yxat bo'sh")