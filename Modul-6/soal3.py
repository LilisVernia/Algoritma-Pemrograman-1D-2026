def evaluasi_pc(pc):
    if pc[1] == "Normal" and pc[2] >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

inventaris = []

jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    print("Data PC ke-", i + 1)

    nama_pc = input("Masukkan nama PC: ")
    status = input("Masukkan status (Normal/Rusak): ")
    ram = input("Masukkan kapasitas RAM (GB): ")

    pc = [nama_pc, status, ram]

    inventaris.append(pc)

print("Hasil evaluasi:")

for pc in inventaris:

    try:
        pc[2] = int(pc[2])
        hasil = evaluasi_pc(pc)

    except ValueError:
        hasil = "Format RAM Kacau"

    output = '{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }'

    print(output)