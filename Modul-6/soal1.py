anggota = []

while True:
    nama = input("Masukkan nama anggota (ketik selesai untuk berhenti): ")

    if nama in anggota:
        print("Nama sudah di inputkan")
    elif nama == "selesai":
        break
    else:
        anggota.append(nama)

print("Evaluasi Nama Anggota:")

for nama in anggota:
    if nama == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
    else:
        print(nama, "valid")

penyusup = input("Masukkan nama penyusup yang ingin dihapus: ")

if penyusup in anggota:
    anggota.remove(penyusup)
    print("Nama", penyusup, "berhasil dihapus.")
else:
    print("Nama", penyusup, "tidak ditemukan.")

print("Daftar anggota akhir:")
print(anggota)