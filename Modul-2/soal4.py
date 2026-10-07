pin = int(input("Masukkan 3 Digit PIN="))
jam = int(input("Masukkan Jam Kedatangan (0-23)="))

digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

print("Digit Pertama=", digit1)
print("Digit Kedua=", digit2)
print("Digit Ketiga=", digit3)

if pin % 5 == 0:
    if jam < 12:
        print("Garasi Pagi Terbuka")
    else:
        print("Garasi Malam Terbuka, Lampu Di Nyalakan")
elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        print("Garasi VIP Terbuka Khusus BOS")
    else:
        print("Kode Genap Di tolak, Alaram Berbunyi")
else:
    print("Akses Ditolak Sepenuhnya")


status_cctv = "Mode Merekam Malam" if jam > 18 else "Mode Siang Standby"
print("Status Kamera  CCTV Markas=", status_cctv)