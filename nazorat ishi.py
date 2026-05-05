#1 bosh harfi bilan ism chiqarish
ismlar = ["azamat", "shohida", "piter", "arima"]
for ism in ismlar:
    print(ism.title())

#2 100 dan katta sonlarni chiqarish
sonlar = [45, 120, 33, 200, 89, 150, 12, 300]
for son in sonlar:
    if 100<son:
        print(son)

#3 alifbo tartibida shahar nomini chiqarish
shaharlar = []
print("5 ta shahar nomini kiriting")
for raqam in range(5):
    shaharlar.append(input(f"{raqam+1} shahar nomini kiriting"))
shaharlar.sort()
print(shaharlar)

#4 takrorlanuvchi elementlarni o'chirish
##if aralash in 2:
#    for 2 in aralash:
#        aralash.remove(2)
#print(aralash)  o'xshamadi

#5 juft son yig'indi topish
juft_sonlar = list(range(0, 51, 2))
print(sum(juft_sonlar))

#6 listni teskari holda chiqarish
davlatlar = ["uzbekiston", "rossiya", "xitoy", "germaniya"]
davlatlar.reverse()
print(davlatlar)

#7
input_son = int(input("son kiriitng  \n"))
sonlar_2 = range(1, input_son)
for input_son in sonlar_2:
    print(input_son**2)

#8 hali listlarni birlashtirishni o'rganmaganman

#9 100 dan kamayuvchi sonlar
kamayuvchi_sonlar = list(range(0, 100, 10))
kamayuvchi_sonlar.reverse()
for kamayuvchi_son in kamayuvchi_sonlar:
    print(kamayuvchi_son, "\n")

#10 eng uzun ism topish
ismlar_2 = ["ali", "husniddin", "sarvar", "jo'rabek", "iqbol"]
uzunlik = []
for ism_2 in ismlar_2:
    uzunlik.append(len(ism_2))
print(max(uzunlik))

#                                                               10\8.5