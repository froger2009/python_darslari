#1
ism = input("ismingizni kiriting\n")
print(ism.upper())
#2
ism2 = input("ismingizni kiriting\n")
familiya2 = input("familiyangizni kiriting\n")
print(f"{ism2} {familiya2}".title())
#3
data = input("malumot kiriitng\n")
data = data.replace(" ", "")
print(len(data))
#4
data2 = input("malumot kiriitng\n")
data2 = data2.replace(" ", "-")
print(data2)
#5
email = input("email kiriitng\n")
if "@" in email:
    print("to'g'ri email")
else:
    print("qaytadan urining")