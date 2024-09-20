cuaca = "cerah"

if cuaca == "cerah":
    print ("Kamu keluar rumah")
print('\n')


# Variable akan bernilai false jika string kosong, 0, (), {}
uang = 0

if uang:
    print("Kamu pergi ke pasar")

else:
    print("Pergi ke rumah teman")
print('\n')

nilai = 7

if nilai % 2 == 0:
    print("genap")

else:
    print("ganjil")

print ('\n')
umur = int(input("Masukkan umur anda: "))

if umur <= 10:
    print("anak-anak")
elif umur <= 18:
    print("remaja")
elif umur <= 32:
    print("dewasa")
elif umur <= 60:
    print("tua")
elif umur >= 80:
    print("fosil")
else:
    print("humanoid")