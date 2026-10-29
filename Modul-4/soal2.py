total_gaji = 0

for hari in range(1, 8):
    print("Hari ke-", hari)

    lembur = int(input("Masukkan jam lembur: "))

    while lembur < 0 or lembur == 5 or lembur == 7 or lembur > 8:
        if lembur > 8:
            print("Jam lembur melebihi batas yang ditentukan")
        else:
            print("Jam lembur tidak sesuai ketentuan")

        lembur = int(input("Masukkan ulang jam lembur: "))

    gaji_pokok = 100000

    if lembur >= 1 and lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    elif lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0

    shift = input("Bekerja shift malam? (ya/tidak): ")

    if shift == "ya":
        tambahan = 50000
    else:
        tambahan = 0

    gaji_harian = gaji_pokok + upah_lembur + tambahan
    total_gaji = total_gaji + gaji_harian

    print("Gaji hari ini: Rp", gaji_harian)

print("Total gaji mingguan: Rp", total_gaji)
