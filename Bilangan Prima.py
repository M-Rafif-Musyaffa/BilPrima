import datetime

# input nilai
lower = int(input("Masukan Angka Awal : "))
upper = int(input("Masukan Angka Akhir : "))

# waktu
now = datetime.datetime.now()
print("Waktu Awal")
print(now.strftime("%H:%M:%S"))

# Hasil
print("bilangan prima antara", lower, "dan", upper, ":")

for i in range(lower, upper + 1):
    if i > 1:
        for n in range(2, i):
            if (i % n) == 0:
                break
        else:
            print(i)
now = datetime.datetime.now()
print("Waktu akhir")
print(now.strftime("%H:%M:%S"))
