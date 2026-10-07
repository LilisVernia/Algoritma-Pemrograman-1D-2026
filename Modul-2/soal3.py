suhu = float(input("Masukkan Suhu Reaktor (°C) = "))
tekanan = float(input("Masukkan Tekanan Gas (Bar) = "))
print("Suhu Reaktor =", suhu, "°C")
print("Tekanan Gas =", tekanan, "Bar")

if suhu > 1000:
    if tekanan > 50:
        print("MELTDOWN! SEGERA EVAKUASI!")
    else:
        print("Bahaya Suhu: Segera Turunkan Daya!")
elif suhu > 500:
    if  tekanan > 30:
        print("Tekanan Tidak Stabil")
    else:
        print("Operator  Reaktor Normal")
else:
    print("Reaktor Belum Cukup Panas")

status_operasional = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"
print("Status Operasional Pompa Air=", status_operasional)