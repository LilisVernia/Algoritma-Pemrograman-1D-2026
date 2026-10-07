password = int(input("Masukkan 3 digit password= "))

digit1 = password //100
digit2 = (password // 10) % 10
digit3 = password % 10

nilai_pelacak = digit1 * digit3

print("Digit Pertama=", digit1,)
print("Digit Kedua=", digit2)
print("Digit Ketiga=", digit3)
print("Nilai Pelacak Awal=", nilai_pelacak)


if digit2 % 2 != 0:
    perubahan_tahap1 = nilai_pelacak + 25
else:
    perubahan_tahap1 = nilai_pelacak - digit2
print("Nilai Pelacak Setelah Tahap Pertama=", perubahan_tahap1)

if perubahan_tahap1 % 3 == 0:
    perubahan_tahap2 = perubahan_tahap1 // 3
else:
    perubahan_tahap2 = perubahan_tahap1 * 2
print("Nilai Pelacak Setelah Tahap Kedua=", perubahan_tahap2)


if perubahan_tahap2 > 50:
    print("Kategori A")
elif perubahan_tahap2 > 20:
    print("Kategori B")
else:
    print("Password Ditolak")

if perubahan_tahap2 % 2 == 0:
    print("Siklus Genap")
else:
    print("Siklus Ganjil")

