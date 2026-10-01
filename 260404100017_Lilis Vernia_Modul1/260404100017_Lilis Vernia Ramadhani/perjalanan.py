jarak_pergi = float(input("Jarak pergi (km): "))
jarak_pulang = float(input("Jarak pulang (km): "))
konsumsi_motor = float(input("Konsumsi motor (km/liter): "))
bensin_tersedia = float(input("Bensin yang tersedia (liter): "))
harga_bensin = int(input("Harga bensin per liter: Rp"))

total_jarak = jarak_pergi + jarak_pulang
kebutuhan_bensin = total_jarak / konsumsi_motor
bensin_dibeli = kebutuhan_bensin - bensin_tersedia
biaya = bensin_dibeli * harga_bensin


print("Total jarak =", total_jarak, "km")
print("Kebutuhan bensin =", kebutuhan_bensin, "liter")
print("Bensin yang harus dibeli =", bensin_dibeli, "liter")
print("Total biaya = Rp", biaya)