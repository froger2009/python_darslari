#1 juft son aniqlash
son = int(input("juft son kiriitng  \n"))
if son % 2 == 0:
    print("raxmat")
else:
    print("Bu juft son emas!!!")

# yoshga ko'ra narx belgilash
yosh = int(input("yoshingizni kiriting  \n"))
narx = 0
if yosh <=4 or yosh > 60:
    narx = 0
elif yosh < 18:
    narx= narx + 10_000
elif yosh > 18:
    narx = narx + 20_000
print(f"sizga kirish {narx} so'm")

#3 sonlarni solishtirish
son_1 = int(input("1 chi sonni kiriting  \n"))
son_2 = int(input("2 chi sonni kiriting  \n"))
if son_1 > son_2: print(f"{son_1} {son_2} ga qaraganda kattaroq")
elif son_1 < son_2: print(f"{son_2} {son_1} ga qaraganda kattaroq")
else: print("ikkov son ham teng")

#4 mahsulot solishtirish
mahsulotlar = ['guruch', "yog'", "sabzi", "piyoz", "kartoshka", "gugurt", "tamat", "tuz", "shakar","periprava"]
savat = []
for i in range(1, 6):
    savat.append(input(f"{i} inchi mahsulotni kiriting  \n"))

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"{mahsulot} do'konimizda mavjud")
    else:
        print(f"{mahsulot} do'konimizda mavjud emas")

#5 bor yo'q mahsulot aniqlash
bor_mahsulotlar = []
yoq_mahsulotlar = []
savat_2 = []
for n in range(1, 6):
    savat_2.append(input(f"{n} inchi mahsulotni kiriting  \n"))
for mahsulot_2 in savat_2:
    if mahsulot_2 in mahsulotlar:
        bor_mahsulotlar.append(mahsulot_2)
    else:
        yoq_mahsulotlar.append(mahsulot_2)
if yoq_mahsulotlar:
    print(F"ushbu mahsulotlar do'konimizda yo'q {yoq_mahsulotlar}")
else:
    print("siz so'ragan barcha mahssulotlar bizning do'konimizda majvud ekan")

#6 login tekshirish
foydalanuvchilar = ["echi@gmail.com", "super@gmail.com", "men@gmail.com", "sen@gmail.com", "biz@gmail.com"]
login = input("login kiriting  \n")
if login in foydalanuvchilar:
    print("login band, yangi login tanlang")
else:
    print("Hush kelibsiz")

#7 qoldiqsiz bo'linuvchi aniqlash
butun_son = int(input("butun son kiriting  \n"))
for s in range(2, 19):
    if butun_son % s == 0:
        print(f"{butun_son} {s} ga qoldiqsiz bo'linadi")