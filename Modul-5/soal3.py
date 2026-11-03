def hitung_nilai(nama, nilai_tugas, nilai_uts, nilai_uas):
    nilai_akhir = (nilai_tugas * 0.30) + (nilai_uts * 0.30) + (nilai_uas * 0.40)

    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "A" or grade == "B" or grade == "C":
        status = "Lulus"
    else:
        status = "Tidak Lulus"

    print("Nama Mahasiswa :", nama)
    print("Nilai Tugas    :", nilai_tugas)
    print("Nilai UTS      :", nilai_uts)
    print("Nilai UAS      :", nilai_uas)
    print("Nilai Akhir    :", round(nilai_akhir, 2))
    print("Grade          :", grade)
    print("Status         :", status)


nama = input("Masukkan nama mahasiswa: ")
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

hitung_nilai(nama, nilai_tugas, nilai_uts, nilai_uas)