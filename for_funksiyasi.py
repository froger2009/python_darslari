# for operatori

# forga oddiy misol 
pc = ["cpu", "gpu", "ssd", "ram", "case", "blok pitaniya", "cooler", "plata"]
for jihoz in pc:
    print(f"bizga kerak {jihoz}")

# for sikl ichida listdagi elementlar tugamaguncha kodni takrorlaydi
for jihoz in pc:
    print(f"{jihoz} kerakku")
    print("lekun pul yo'q")

# for bilan sonlar ustida ishlash
sonlar = list(range(1, 11))
for son in sonlar:
    print(f"{son} ning kubi {son**3} ga teng")

# son kvadratini aniqlab listga yig'ish 
sonlar_2 = list(range(11))
saqlash = []
for son_2 in sonlar_2:
    saqlash.append(son_2**2)
print(saqlash)

animelar = []
print("yoqtirgan 5ta animelaringizni kiriting")
for raqam in range(1, 6):
    animelar.append(input(f"{raqam} inchi animeyingizni kiriting \n>>>"))
print(f"siz yoqtiradigan animelar to'plami \n{animelar}")

