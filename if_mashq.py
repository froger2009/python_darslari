#1 voyaha yetganlik aniqlash
yosh = int(input("yoshingizni kiriitng  \n"))
if yosh > 18:
    print("voyaga yetgan")
else:
    print("voyaga yetmagan")

#2 juft toq aniqlash
int_son = int(input("son kiriting"))
if int_son % 2 == 0:
    print("juft son")
else:
    print("toq son")

#3 eng katta sson aniqlash
son_1 = int(input("1 chi sonni kiriting  \n"))
son_2 = int(input("2 chi sonni kiriting  \n"))
son_3 = int(input("3 chi sonni kiriting  \n"))
sonlar = [ son_1, son_2, son_3]
print(f"eng katta qiymat {max(sonlar)}")

#4 bal baholash
bal = int(input("bal kiriting"))
if bal>= 90 and bal <=100:
    print("A'lo baho")
elif bal >= 70 and bal <=89:
    print("Yaxshi")
elif bal >= 50 and bal <=69:
    print("Qoniqarli")
elif bal >= 0 and bal <=49:
    print("Qoniqarsiz")
else:
    print("Xato ko'rsatma !!! qaytadan uruning")

#5 5 ta son ichidan faqat musbat va juftlarini chiqarish
qiymat_1 = int(input("1 chi son kiriting  \n"))
qiymat_2 = int(input("2 chi son kiriting  \n"))
qiymat_3 = int(input("3 chi son kiriting  \n"))
qiymat_4 = int(input("4 chi son kiriting  \n"))
qiymat_5 = int(input("5 chi son kiriting  \n"))
qiymatlar = [qiymat_1, qiymat_2, qiymat_3, qiymat_4, qiymat_5]
for qiymat in qiymatlar:
    if qiymat > 0 and qiymat % 2 == 0:
        print(qiymat)