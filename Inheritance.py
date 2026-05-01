# ============================================================
# TUGAS UTS PEMROGRAMAN BERORIENTASI OBJEK (PBO)
# SISTEM MONITORING IRIGASI SAWAH (SM IRIGASI)
# ============================================================
# KONSEP: INHERITANCE (Pewarisan Sifat)
# Tema: Kelas anak mewarisi atribut dari kelas induk tanpa mengulang kode
# Data riil: Saluran Induk Ngidul (Primer) & Saluran Petak 12 (Tersier)
# ============================================================

# ============================================================
# IMPLEMENTASI KONSEP INHERITANCE - SISTEM MONITORING IRIGASI
# ============================================================

# ---------- MENDEFINISIKAN KELAS INDUK (PARENT CLASS) ----------
class Irigasi:  # Membuat kelas induk bernama Irigasi
    """
    Kelas Irigasi menampung atribut dan method dasar yang dimiliki 
    oleh semua jenis saluran irigasi.
    Kelas ini berperan sebagai BLUEPRINT / CETAK BIRU untuk semua jenis irigasi.
    """
    
    def __init__(self, nama, debit, panjang):
        """
        CONSTRUCTOR: Method ini dipanggil OTOMATIS saat objek dibuat.
        Parameter:
        - nama   : Nama saluran irigasi (string)
        - debit  : Debit air dalam Liter per detik (float)
        - panjang: Panjang saluran dalam meter (int)
        """
        self.nama = nama            # Atribut umum: Menyimpan nama saluran
        self.debit = debit          # Atribut umum: Menyimpan debit air (L/dtk)
        self.panjang = panjang      # Atribut umum: Menyimpan panjang saluran (meter)

    def tampilkan_info_dasar(self):
        """
        METHOD DASAR: Method ini akan DIWARISKAN ke semua kelas anak.
        Menampilkan informasi dasar saluran irigasi.
        """
        print(f"Nama Saluran    : {self.nama}")      # Mencetak nama saluran
        print(f"Debit Air       : {self.debit} L/dtk")  # Mencetak debit air
        print(f"Panjang Saluran : {self.panjang} meter")  # Mencetak panjang saluran


# ---------- MENDEFINISIKAN KELAS ANAK (CHILD CLASS) 1: IRIGASI PRIMER ----------
class IrigasiPrimer(Irigasi):  # Tanda kurung (Irigasi) = MEWARISI dari kelas Irigasi
    """
    KELAS ANAK (CHILD CLASS): IrigasiPrimer
    Kelas ini MEWARISI semua atribut dan method dari kelas Irigasi.
    BUKTI: Tidak perlu menulis ulang atribut nama, debit, panjang!
    """
    
    def __init__(self, nama, debit, panjang, jumlah_pintu):
        """
        CONSTRUCTOR untuk IrigasiPrimer.
        Parameter tambahan: jumlah_pintu (spesifik untuk irigasi primer)
        """
        # INI KUNCI INHERITANCE
        # super() = memanggil constructor kelas INDUK (Irigasi)
        # Kita TIDAK perlu menulis ulang: self.nama = nama
        # Cukup satu baris ini, semua atribut induk diwariskan!
        super().__init__(nama, debit, panjang)  # Mewarisi nama, debit, panjang dari induk
        
        # Atribut KHUSUS untuk IrigasiPrimer (TIDAK ADA di kelas induk)
        self.jumlah_pintu = jumlah_pintu  # Menyimpan jumlah pintu air utama

    def monitoring_pintu(self):
        """
        METHOD TAMBAHAN: Method ini hanya ada di kelas IrigasiPrimer.
        Method ini TIDAK DIWARISKAN ke kelas lain karena spesifik untuk primer.
        """
        print(f"Status          : Monitoring {self.jumlah_pintu} pintu air utama.")


# ---------- MENDEFINISIKAN KELAS ANAK (CHILD CLASS) 2: IRIGASI TERSIER ----------
class IrigasiTersier(Irigasi):  # Mewarisi atribut dari kelas Irigasi
    """
    KELAS ANAK (CHILD CLASS): IrigasiTersier
    Juga mewarisi dari kelas Irigasi (sama seperti IrigasiPrimer).
    Sekali lagi: TIDAK perlu mengulang kode dari kelas induk!
    """
    
    def __init__(self, nama, debit, panjang, luas_cakupan):
        """
        CONSTRUCTOR untuk IrigasiTersier.
        Parameter tambahan: luas_cakupan (spesifik untuk irigasi tersier)
        """
        # EKALI LAGI BUKTI INHERITANCE
        # Memanggil constructor induk untuk mewarisi nama, debit, panjang
        super().__init__(nama, debit, panjang)  # Mewarisi dari kelas induk
        
        # Atribut KHUSUS untuk IrigasiTersier (TIDAK ADA di kelas induk)
        self.luas_cakupan = luas_cakupan  # Menyimpan luas area yang diairi (Hektar)

    def info_layanan(self):
        """
        METHOD TAMBAHAN: Method ini hanya ada di kelas IrigasiTersier.
        Menampilkan informasi cakupan area irigasi.
        """
        print(f"Cakupan Area    : Mengairi {self.luas_cakupan} hektar sawah.")


# ============================================================
# IMPLEMENTASI DENGAN DATA RIIL (CONTOH PENGGUNAAN)
# ============================================================

print("=" * 50)  # Mencetak garis pemisah
print("=== SISTEM MONITORING SM-IRIGASI (DATA REAL) ===")  # Judul program
print("=" * 50)  # Mencetak garis pemisah
print()  # Mencetak baris kosong

# ---------- MEMBUAT OBJEK 1: IRIGASI PRIMER ----------
# Perbedaan CLASS vs OBJECT:
# - IrigasiPrimer adalah CLASS (cetak biru/blueprint)
# - saluran_utama adalah OBJECT (wujud nyata dari class IrigasiPrimer)

# Data: Saluran Induk Ngidul, debit 120.5 L/dtk, panjang 5000m, 8 pintu
saluran_utama = IrigasiPrimer("Saluran Induk Ngidul", 120.5, 5000, 8)
# Baris di atas membuat objek bernama 'saluran_utama' dari class IrigasiPrimer

# BUKTI PEWARISAN 1: Memanggil method dari kelas INDUK
# Method 'tampilkan_info_dasar()' TIDAK ADA di class IrigasiPrimer
# Method ini DIWARISIN dari kelas Irigasi!
saluran_utama.tampilkan_info_dasar()  # Memanggil method warisan dari induk

# BUKTI PEWARISAN 2: Memanggil method dari kelas ANAK sendiri
# Method 'monitoring_pintu()' adalah method KHUSUS milik IrigasiPrimer
saluran_utama.monitoring_pintu()  # Memanggil method spesifik kelas anak

print("-" * 40)  # Mencetak garis pemisah

# ---------- MEMBUAT OBJEK 2: IRIGASI TERSIER ----------
# Data: Saluran Petak 12, debit 9.3 L/dtk, panjang 800m, 240 Hektar
saluran_sawah = IrigasiTersier("Saluran Petak 12", 9.3, 800, 240)
# Baris di atas membuat objek 'saluran_sawah' dari class IrigasiTersier

# BUKTI PEWARISAN 3: Method yang SAMA bisa dipanggil oleh objek berbeda
# Method 'tampilkan_info_dasar()' digunakan oleh IrigasiPrimer DAN IrigasiTersier
# Kode method ini ditulis SEKALI di kelas induk, dipakai berkali-kali!
saluran_sawah.tampilkan_info_dasar()  # Memanggil method warisan dari induk

# Memanggil method KHUSUS milik IrigasiTersier
saluran_sawah.info_layanan()  # Memanggil method spesifik kelas anak

# ============================================================
# PENJELASAN SINGKAT TENTANG INHERITANCE
# ============================================================
# 
# 1. KELAS INDUK: Irigasi (memiliki atribut: nama, debit, panjang)
# 2. KELAS ANAK: IrigasiPrimer dan IrigasiTersier
# 
# BUKTI KELAS ANAK TIDAK MENGULANG KODE:
# - Di IrigasiPrimer, kita TIDAK menulis: self.nama = nama
# - Di IrigasiTersier, kita TIDAK menulis: self.debit = debit
# - Cukup panggil super().__init__(nama, debit, panjang) SEKALI!
# 
# ATRIBUT YANG DIWARISKAN: nama, debit, panjang
# METHOD YANG DIWARISKAN: tampilkan_info_dasar()
# 
# ATRIBUT YANG DITAMBAHKAN DI KELAS ANAK:
# - IrigasiPrimer: jumlah_pintu
# - IrigasiTersier: luas_cakupan
# 
# METHOD YANG DITAMBAHKAN DI KELAS ANAK:
# - IrigasiPrimer: monitoring_pintu()
# - IrigasiTersier: info_layanan()
# ============================================================
