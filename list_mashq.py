mevalar = ["olma", "nok", "uzum", "shaftoli"]
mevalar.append("gilos")
print(mevalar)

#2
sonlar = [10, 20, 30, 40, 50]
sonlar[3] = 99
print(sonlar)

#3
shaharlar = ['toshkent',"samarqand", "buxoro", "namangan", "andijon"]
del shaharlar[2]
shaharlar.insert(2, "qarshi")
shaharlar.insert(3, "termiz")
print(shaharlar)

#4
raqamlar = [5, 3, 8 ,1 ,9,2 , 7]
ohirigi_element = raqamlar.pop(-1)
print(ohirigi_element)

#5
aralash = ["python", 42, "java", 99, "rust", 7]
aralash.remove(99)
aralash.remove(42)
aralash.remove(7)
print(aralash)

# list 2 uyga vazifa

davlatlar = ["xitoy", "yaponiya", "korea", "o'zbekiston", "aqsh", "ispaniya", "canada", "hindiston"]
print(davlatlar)
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
davlatlar.reverse()
print(davlatlar)

davlatlar.sort()
print(davlatlar)

davlatlar.sort(reverse=True)
print(davlatlar)

juft_sonlar = list(range(120, 1201, 2))
print(juft_sonlar)

print(sum(juft_sonlar))

print(max(juft_sonlar) - min(juft_sonlar))

print(len(juft_sonlar))

print(juft_sonlar[0:20] , juft_sonlar[:-20])

taomlar = ["osh" , "manti", "somsa", "mastava", "shorva"]
nonushta = taomlar[:]
nonushta.remove('somsa')
nonushta.remove('mastava')
nonushta.remove('shorva')
nonushta.extend(["lavash", "gamburger"])
print(nonushta)
print(taomlar)
nonushta = tuple(nonushta)
print(type(nonushta))
nonushta[0] = "qaymoq va non"
print(nonushta)