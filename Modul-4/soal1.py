baris=int(input("Masukkan jumlah baris lampu= "))
jumlah=int(input("Masukkan jumlah lampu untuk setiap baris= "))

for i in range(1, baris + 1):
    print("Baris", i)
    for j in range(1, jumlah + 1):
        if j % 3 == 0:
            print("Lampu", j, "mengalami gangguan")
        elif j % 2 ==0:
            print("lampu", j, "mengalami eror")
        else:
            print("Lampu", j, "berfungsi")

print("periksa sumber listrik utama")