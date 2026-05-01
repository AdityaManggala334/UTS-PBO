# ============================================================
# TUGAS UTS PEMROGRAMAN BERORIENTASI OBJEK (PBO)
# SISTEM MONITORING IRIGASI SAWAH (SM IRIGASI)
# ============================================================
# KONSEP: POLYMORPHISM (Polimorfisme)
# Tema: Satu tombol "Hitung" untuk menghitung PAJAK, DISKON, dan ASURANSI
# ============================================================

# ============================================================
# IMPLEMENTASI KONSEP POLYMORPHISM - SISTEM MONITORING IRIGASI
# ============================================================

# ---------- MEMBUAT KELAS INDUK SEBAGAI BLUEPRINT (KERANGKA) ----------
class KomponenBiaya:
    """
    KELAS INDUK: KomponenBiaya
    Kelas ini berfungsi sebagai blueprint / kerangka untuk semua kelas
    yang berkaitan dengan perhitungan biaya di sistem irigasi.
    """
    
    def hitung(self):
        """
        METHOD YANG AKAN DI-OVERRIDE (DITULIS ULANG) OLEH KELAS ANAK.
        Di kelas induk, method ini hanya berisi 'pass' (tidak melakukan apa-apa)
        karena implementasi sesungguhnya akan berbeda di setiap kelas anak.
        pass berfungsi sebagai placeholder / tempat kosong sementara.
        """
        pass  # Pass = placeholder, tidak ada eksekusi


# ---------- KELAS ANAK 1: MENGHITUNG PAJAK AIR ----------
# Kelas ini mewarisi dari KomponenBiaya (tanda kurung menunjukkan pewarisan)
class PajakAir(KomponenBiaya):
    """
    KELAS ANAK (CHILD CLASS): PajakAir
    Kelas ini digunakan untuk menghitung PAJAK air irigasi.
    """
    
    def __init__(self, debit):
        """
        CONSTRUCTOR: Method ini dipanggil otomatis saat objek dibuat.
        Parameter: debit (debit air dalam Liter per detik)
        """
        self.debit = debit          # Menyimpan data debit air (L/dtk)
        self.tarif = 500            # Tarif pajak Rp 500 per liter/detik (data riil)
    
    def hitung(self):
        """
        IMPLEMENTASI METHOD HITUNG UNTUK PAJAK (POLYMORPHISM).
        Method ini memiliki NAMA yang SAMA dengan method hitung() di kelas induk,
        tetapi IMPLEMENTASinya BERBEDA (khusus untuk menghitung PAJAK).
        Rumus: Pajak = Debit air x Tarif pajak
        Contoh: 120 L/dtk x Rp 500 = Rp 60.000
        """
        return self.debit * self.tarif  # Mengembalikan hasil perhitungan pajak


# ---------- KELAS ANAK 2: MENGHITUNG DISKON BIAYA ----------
class DiskonIrigasi(KomponenBiaya):
    """
    KELAS ANAK (CHILD CLASS): DiskonIrigasi
    Kelas ini digunakan untuk menghitung DISKON biaya irigasi.
    """
    
    def __init__(self, total_biaya):
        """
        CONSTRUCTOR untuk DiskonIrigasi.
        Parameter: total_biaya (total biaya sebelum diskon dalam Rupiah)
        """
        self.total_biaya = total_biaya  # Menyimpan total biaya (Rp)
        self.persen_diskon = 0.15       # Diskon 15% (0.15 = 15/100) data riil
    
    def hitung(self):
        """
        IMPLEMENTASI METHOD HITUNG UNTUK DISKON (POLYMORPHISM).
        Method ini memiliki NAMA yang SAMA dengan method hitung() di kelas induk,
        tetapi IMPLEMENTASinya BERBEDA (khusus untuk menghitung DISKON).
        Rumus: Diskon = Total biaya x Persentase diskon
        Contoh: Rp 5.000.000 x 15% = Rp 750.000
        """
        return self.total_biaya * self.persen_diskon  # Mengembalikan nilai diskon


# ---------- KELAS ANAK 3: MENGHITUNG PREMI ASURANSI ----------
class PremiAsuransi(KomponenBiaya):
    """
    KELAS ANAK (CHILD CLASS): PremiAsuransi
    Kelas ini digunakan untuk menghitung PREMI ASURANSI sawah.
    """
    
    def __init__(self, luas_sawah):
        """
        CONSTRUCTOR untuk PremiAsuransi.
        Parameter: luas_sawah (luas area sawah dalam Hektar)
        """
        self.luas_sawah = luas_sawah    # Menyimpan luas sawah (Hektar)
        self.tarif_premi = 50000        # Premi Rp 50.000 per hektar (data riil)
    
    def hitung(self):
        """
        IMPLEMENTASI METHOD HITUNG UNTUK ASURANSI (POLYMORPHISM).
        Method ini memiliki NAMA yang SAMA dengan method hitung() di kelas induk,
        tetapi IMPLEMENTASinya BERBEDA (khusus untuk menghitung ASURANSI).
        Rumus: Premi Asuransi = Luas sawah x Tarif premi per hektar
        Contoh: 240 Ha x Rp 50.000 = Rp 12.000.000
        """
        return self.luas_sawah * self.tarif_premi  # Mengembalikan nilai premi asuransi


# ============================================================
# FUNGSI UNTUK MENUNJUKKAN POLYMORPHISM (SATU TOMBOL HITUNG)
# ============================================================

def jalankan_perhitungan(objek_biaya):
    """
    FUNGSI POLIMORFIK: Satu Tombol Hitung untuk Semua Jenis Perhitungan.
    
    Fungsi ini adalah INTI dari konsep POLYMORPHISM.
    Fungsi ini bisa menerima objek APA SAJA sebagai parameter, ASALKAN
    objek tersebut memiliki method bernama 'hitung()'.
    
    Parameter 'objek_biaya' bisa berupa:
    - Objek dari kelas PajakAir       -> akan menghitung PAJAK
    - Objek dari kelas DiskonIrigasi  -> akan menghitung DISKON
    - Objek dari kelas PremiAsuransi  -> akan menghitung ASURANSI
    
    Fungsi ini TIDAK PEDULI dengan tipe objek yang masuk.
    Yang penting objek tersebut memiliki method hitung().
    Inilah yang disebut POLYMORPHISM (banyak bentuk, satu antarmuka).
    """
    hasil = objek_biaya.hitung()  # Memanggil method hitung() dari objek yang masuk
    return hasil  # Mengembalikan hasil perhitungan ke pemanggil fungsi


# ============================================================
# IMPLEMENTASI DENGAN DATA RIIL (CONTOH PENGGUNAAN)
# ============================================================

# 1. INISIALISASI OBJEK DENGAN DATA RIIL
# Perbedaan CLASS vs OBJECT:
# - PajakAir adalah CLASS (cetak biru/blueprint)
# - pajak adalah OBJECT (wujud nyata dari class PajakAir)

pajak = PajakAir(120)          # Membuat objek pajak dengan debit 120 L/dtk (data riil)
diskon = DiskonIrigasi(5000000)  # Membuat objek diskon dengan biaya Rp 5.000.000 (data riil)
asuransi = PremiAsuransi(240)  # Membuat objek asuransi dengan luas 240 Hektar (data riil)

# 2. EKSEKUSI "SATU TOMBOL" UNTUK BERBAGAI OBJEK BERBEDA
print("=" * 50)  # Mencetak garis pemisah
print("      === HASIL PERHITUNGAN SM-IRIGASI ===")  # Mencetak judul program
print("=" * 50)  # Mencetak garis pemisah
print()  # Mencetak baris kosong

# Memanggil fungsi yang SAMA untuk objek yang BERBEDA
# Inilah POLYMORPHISM dalam aksi
hasil_pajak = jalankan_perhitungan(pajak)      # Menghitung PAJAK
hasil_diskon = jalankan_perhitungan(diskon)    # Menghitung DISKON
hasil_asuransi = jalankan_perhitungan(asuransi)  # Menghitung ASURANSI

# 3. MENAMPILKAN HASIL PERHITUNGAN
print(f"Total Pajak Air (120 L/dtk)      : Rp {hasil_pajak:,.0f}")
print(f"Total Potongan Diskon (15%)      : Rp {hasil_diskon:,.0f}")
print(f"Total Premi Asuransi (240 Ha)    : Rp {hasil_asuransi:,.0f}")

# ============================================================
# PENJELASAN SINGKAT TENTANG POLYMORPHISM
# ============================================================
# 
# APA ITU POLYMORPHISM?
# Polymorphism berasal dari bahasa Yunani:
# - Poly = banyak
# - Morph = bentuk
# Jadi POLYMORPHISM = BANYAK BENTUK.
# 
# BUKTI POLYMORPHISM DALAM KODE INI:
# 1. Tiga kelas berbeda (PajakAir, DiskonIrigasi, PremiAsuransi)
#    SEMUANYA memiliki method dengan NAMA yang SAMA yaitu 'hitung()'
# 
# 2. TAPI implementasi 'hitung()' di setiap kelas BERBEDA:
#    - PajakAir.hitung()      -> menghitung PAJAK (debit x tarif)
#    - DiskonIrigasi.hitung() -> menghitung DISKON (biaya x diskon)
#    - PremiAsuransi.hitung() -> menghitung ASURANSI (luas x premi)
# 
# 3. Fungsi 'jalankan_perhitungan()' BISA menerima objek dari
#    KETIGA kelas tersebut, selama objek memiliki method 'hitung()'
# 
# MANFAAT POLYMORPHISM:
# - Kode lebih fleksibel: satu fungsi bisa digunakan untuk berbagai tipe
# - Kode lebih mudah diperluas: menambah kelas baru tidak perlu mengubah fungsi lama
# - Kode lebih rapi: tidak perlu menggunakan if-else untuk mengecek tipe objek
# ============================================================
