import datetime

def hitung_diskon(tahun_lahir, harga_tiket):
    tahun_sekarang = datetime.datetime.now().year
    umur = tahun_sekarang - tahun_lahir
    
    if 0 <= umur <= 4:
        diskon = 1.0  # 100% diskon
    elif 5 <= umur <= 11:
        diskon = 0.5  # 50% diskon
    else:
        diskon = 0.0  # Tidak ada diskon
    
    harga_setelah_diskon = harga_tiket * (1 - diskon)
    return umur, diskon, harga_setelah_diskon

def main():
    try:
        tahun_lahir = int(input("Masukkan tahun kelahiran penumpang: "))
        harga_tiket = float(input("Masukkan harga tiket kereta api: "))
        
        umur, diskon, harga_akhir = hitung_diskon(tahun_lahir, harga_tiket)
        
        print(f"\nUmur penumpang: {umur} tahun")
        print(f"Diskon yang diberikan: {diskon*100:.0f}%")
        print(f"Harga tiket setelah diskon: Rp {harga_akhir:,.2f}")
        
    except ValueError:
        print("Input tidak valid. Pastikan Anda memasukkan angka yang benar.")

if __name__ == "__main__":
    main()