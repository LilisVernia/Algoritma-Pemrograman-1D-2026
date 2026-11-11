asisten_awal = []

while True:
    nama = input("Masukkan nama asisten (ketik cukup untuk selesai): ")

    if nama == "cukup":
        break

    asisten_awal.append(nama)

asisten_awal = tuple(asisten_awal)

tambahan = input("Masukkan nama asisten tambahan: ")
  
asisten_akhir = asisten_awal + (tambahan,)

hari_tugas = []

while True:
    hari = input("Masukkan hari tugas (ketik cukup untuk selesai): ")

    if hari == "cukup":
        break

    hari_tugas.append(hari)

hari_tugas = tuple(hari_tugas)

pengecualian_nama = input("Nama asisten yang dikecualikan: ")
pengecualian_hari = input("Hari yang dikecualikan: ")

print("Jadwal Shift Asisten:")

for nama in asisten_akhir:
    for hari in hari_tugas:

        if nama == pengecualian_nama and hari == pengecualian_hari:
            continue

        print(nama, "-", hari)