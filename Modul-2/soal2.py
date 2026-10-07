total_belanja = int(input("Masukkan Total Belanja= Rp"))
print("Total Belanja Sebelum Diskon= Rp", total_belanja)

if total_belanja % 100000 == 0:
    total_bayar = 0
    print("Mendapatkan Diskon 100% (Gratis)")
elif total_belanja <=0:
     total_bayar = total_belanja
     print("Masukkan angka yang benar")
elif total_belanja % 50000 == 0:
    total_bayar = total_belanja - (total_belanja * 50//100)
    print("Mendapatkan Diskon 50%")
elif total_belanja % 10000 == 0:
    total_bayar = total_belanja - ( total_belanja * 20//100)
    print("Mendapatkan Diskon 20%")
elif total_belanja >= 200000:
    total_bayar = total_belanja - (total_belanja * 10//100)
    print("Mendapatkan Diskon 10%")
else:
    total_bayar = total_belanja
    print("Tidak Mendapatkan Diskon")
print("Total Belanja Setelah Diskon= Rp", total_bayar)

status_poin = "Point  bertambah" if total_bayar > 0 else "Tidak Mendapat Point"

print("Status point=", status_poin)