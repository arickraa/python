# Program untuk menghitung diskon tarif kereta api berdasarkan umur

# Input data tahun kelahiran dan harga tiket
tahun_kelahiran = int(input("Masukkan tahun kelahiran penumpang: "))
harga_tiket = float(input("Masukkan harga tiket kereta api: "))

# Tahun saat ini
tahun_sekarang = 2024
umur = tahun_sekarang - tahun_kelahiran

# Menentukan harga tiket setelah diskon
if umur <= 4:
    harga_akhir = 0.0  # Diskon 100%
elif umur <= 11:
    harga_akhir = harga_tiket * 0.5  # Diskon 50%
else:
    harga_akhir = harga_tiket  # Tidak ada diskon

# Menampilkan hasil
print(f"Umur penumpang: {umur} tahun")
print(f"Harga tiket setelah diskon: Rp {harga_akhir:.2f}")
