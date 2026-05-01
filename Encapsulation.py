# ============================================================
# TUGAS UTS PEMROGRAMAN BERORIENTASI OBJEK (PBO)
# SISTEM MONITORING IRIGASI SAWAH (SM IRIGASI)
# ============================================================
# KONSEP: ENCAPSULATION (Enkapsulasi)
# Tema: Perlindungan data rahasia (PIN, Harga Pokok, Diagnosis) dari akses langsung
# ============================================================
# IMPLEMENTASI KONSEP ENCAPSULATION - SISTEM MONITORING IRIGASI
# ============================================================

# Mendefinisikan kelas SensorIrigasi untuk menerapkan konsep enkapsulasi
class SensorIrigasi:
    """
    KELAS: SensorIrigasi
    Kelas ini mendemonstrasikan konsep ENCAPSULATION dengan menyembunyikan
    data-data sensitif (PIN, harga pokok, diagnosis) dari akses langsung.
    Data hanya bisa diakses melalui method GETTER dan SETTER dengan validasi PIN.
    """
    
    def __init__(self, nama, pin_awal):
        """
        CONSTRUCTOR: Method ini dipanggil OTOMATIS saat objek dibuat.
        Parameter:
        - nama: nama sensor (contoh: "Sensor Debit Saluran Induk")
        - pin_awal: PIN untuk mengakses data rahasia (contoh: "123456")
        """
        
        # ATRIBUT PUBLIK - Bisa diakses langsung dari luar kelas
        # Contoh: print(sensor_utama.nama) -> Berhasil
        self.nama = nama  # Menyimpan nama sensor (informasi publik)
        
        # ========== DATA RAHASIA (PRIVATE) ==========
        # Menggunakan double underscore (__) di depan nama atribut
        # Ini membuat atribut menjadi PRIVATE / TERSEMBUNYI
        # Tidak bisa diakses langsung dari luar kelas!
        
        # DATA RAHASIA A: PIN Akses Kalibrasi
        # Private karena PIN adalah kredensial rahasia teknisi
        self.__pin_kalibrasi = pin_awal  # PIN untuk validasi akses data rahasia
        
        # DATA RAHASIA B: Harga Pokok Pembelian Sensor
        # Private karena harga pokok adalah informasi internal perusahaan
        self.__harga_pokok = 1850000  # Harga beli sensor dalam Rupiah (data riil)
        
        # DATA RAHASIA C: Diagnosis Kerusakan Sensor
        # Private karena diagnosis hanya boleh diketahui oleh teknisi berwenang
        self.__diagnosis = "Sensor Normal"  # Status awal diagnosis sensor

    # ========== GETTER METHOD ==========
    # Getter berfungsi untuk MEMBACA / MENGAMBIL data rahasia
    # Dengan validasi PIN, hanya pihak berwenang yang bisa mengakses
    
    def get_info_rahasia(self, input_pin):
        """
        GETTER METHOD: Mengambil/membaca data rahasia sensor.
        Parameter: input_pin (PIN yang dimasukkan oleh pengguna)
        Output: Menampilkan data rahasia jika PIN cocok, menolak jika PIN salah.
        
        Method ini menerapkan validasi sebagai bentuk keamanan data.
        Hanya PIN yang benar yang diizinkan untuk melihat data internal.
        """
        
        # VALIDASI PIN: Memeriksa apakah PIN yang dimasukkan cocok
        # Ini adalah KUNCI UTAMA dari konsep ENCAPSULATION
        if input_pin == self.__pin_kalibrasi:
            # PIN cocok -> Berikan akses ke data rahasia
            print(f"\n[AKSES BERHASIL] Mengambil data rahasia {self.nama}:")
            # Mencetak harga pokok dengan format ribuan (1,850,000)
            print(f"- Harga Pokok Beli : Rp {self.__harga_pokok:,}")
            # Mencetak diagnosis terbaru sensor
            print(f"- Hasil Diagnosis  : {self.__diagnosis}")
        else:
            # PIN salah -> TOLAK akses (enkapsulasi melindungi data!)
            print(f"\n[AKSES DITOLAK] PIN '{input_pin}' salah! Anda tidak berhak melihat data internal.")

    # ========== SETTER METHOD ==========
    # Setter berfungsi untuk MENGUBAH / MEMPERBARUI data rahasia
    # Dengan validasi PIN, hanya pihak berwenang yang bisa mengubah data
    
    def set_diagnosis_kerusakan(self, input_pin, diagnosis_baru):
        """
        SETTER METHOD: Mengubah/memperbarui diagnosis kerusakan sensor.
        Parameter:
        - input_pin: PIN untuk validasi akses
        - diagnosis_baru: diagnosis terbaru dari teknisi
        
        Method ini memastikan bahwa hanya teknisi dengan PIN benar
        yang dapat mengubah data diagnosis sensor.
        """
        
        # VALIDASI PIN sebelum mengizinkan perubahan data
        # Setter juga dilengkapi validasi untuk keamanan
        if input_pin == self.__pin_kalibrasi:
            # PIN cocok -> Izinkan perubahan data
            self.__diagnosis = diagnosis_baru  # Mengubah nilai diagnosis
            print(f"\n[UPDATE BERHASIL] Diagnosis {self.nama} telah diperbarui.")
        else:
            # PIN salah -> TOLAK perubahan data
            print(f"\n[UPDATE GAGAL] PIN '{input_pin}' salah! Perubahan data ditolak.")


# ============================================================
# IMPLEMENTASI PENGGUNAAN (CONTOH EKSEKUSI PROGRAM)
# ============================================================

print("=" * 55)  # Mencetak garis pemisah
print("   SM IRIGASI - DEMONSTRASI ENCAPSULATION")
print("   Perlindungan Data Rahasia Sensor")
print("=" * 55)  # Mencetak garis pemisah
print()  # Mencetak baris kosong

# 1. INISIALISASI OBJEK SENSOR
# Membuat objek 'sensor_utama' dari class SensorIrigasi
# Parameter: (nama_sensor, PIN_awal)
sensor_utama = SensorIrigasi("Sensor Debit Saluran Induk", "123456")

# Menampilkan nama sensor (atribut publik, bisa diakses langsung)
print(f"--- SISTEM MONITORING {sensor_utama.nama} ---")
print()  # Mencetak baris kosong

# 2. PERCOBAAN AKSES LANGSUNG KE DATA RAHASIA (AKAN GAGAL)
# Ini adalah BUKTI bahwa enkapsulasi BERHASIL melindungi data!
# Python akan menyembunyikan atribut yang diawali dengan double underscore
print("PERCOBAAN 1: Akses Langsung ke Data Rahasia")
print("-" * 40)  # Mencetak garis pemisah

try:
    # Mencoba mengakses atribut private __harga_pokok secara langsung
    # Baris ini akan menyebabkan AttributeError karena atribut bersifat private
    print(sensor_utama.__harga_pokok)
except AttributeError:
    # Blok ini dieksekusi ketika terjadi AttributeError
    # Membuktikan bahwa akses langsung TIDAK DIPERBOLEHKAN
    print("\n[KEAMANAN SISTEM] Gagal! Atribut '__harga_pokok' bersifat PRIVATE")
    print("dan tidak bisa diakses langsung dari luar kelas.")
print()  # Mencetak baris kosong

# 3. PERCOBAAN AKSES DATA DENGAN PIN SALAH (via GETTER)
print("PERCOBAAN 2: Akses via Getter dengan PIN SALAH")
print("-" * 40)  # Mencetak garis pemisah
print("Memasukkan PIN: 000000 (salah)")  # Menampilkan PIN yang dimasukkan

# Memanggil getter dengan PIN yang SALAH ("000000")
# Seharusnya akses ditolak karena PIN tidak cocok
sensor_utama.get_info_rahasia("000000")
print()  # Mencetak baris kosong

# 4. PERCOBAAN AKSES DATA DENGAN PIN BENAR (via GETTER)
print("PERCOBAAN 3: Akses via Getter dengan PIN BENAR")
print("-" * 40)  # Mencetak garis pemisah
print("Memasukkan PIN: 123456 (benar)")  # Menampilkan PIN yang dimasukkan

# Memanggil getter dengan PIN yang BENAR ("123456")
# Seharusnya akses berhasil dan data rahasia ditampilkan
sensor_utama.get_info_rahasia("123456")
print()  # Mencetak baris kosong

# 5. PERCOBAAN MENGUBAH DATA DENGAN PIN BENAR (via SETTER)
print("PERCOBAAN 4: Mengubah Data via Setter dengan PIN BENAR")
print("-" * 40)  # Mencetak garis pemisah

# Memanggil setter untuk mengubah diagnosis
# Parameter: (PIN_benar, diagnosis_baru)
sensor_utama.set_diagnosis_kerusakan("123456", "Debit turun drastis - Perlu Pembersihan")
print()  # Mencetak baris kosong

# 6. VERIFIKASI PERUBAHAN DATA (Membaca setelah diubah)
print("PERCOBAAN 5: Verifikasi Perubahan Data")
print("-" * 40)  # Mencetak garis pemisah

# Memanggil getter lagi untuk memastikan data diagnosis sudah berubah
# Seharusnya diagnosis berubah dari "Sensor Normal" menjadi "Debit turun drastis"
sensor_utama.get_info_rahasia("123456")

# ============================================================
# PENJELASAN SINGKAT TENTANG ENCAPSULATION
# ============================================================
# 
# APA ITU ENCAPSULATION?
# Enkapsulasi adalah konsep OOP yang menyembunyikan data internal suatu kelas
# dari akses langsung dari luar kelas. Data hanya bisa diakses melalui
# method-method publik (GETTER dan SETTER) yang disediakan.
# 
# BUKTI ENCAPSULATION DALAM KODE INI:
# 
# 1. TIGA DATA RAHASIA yang dilindungi:
#    A. __pin_kalibrasi    - PIN akses untuk kalibrasi sensor
#    B. __harga_pokok      - Harga beli sensor (Rp 1.850.000)
#    C. __diagnosis        - Status diagnosis kerusakan sensor
# 
# 2. DATA TIDAK BISA DIAKSES LANGSUNG:
#    - Percobaan print(sensor_utama.__harga_pokok) menghasilkan ERROR
#    - Ini membuktikan atribut private tidak bisa diakses dari luar kelas
# 
# 3. AKSES HANYA MELALUI GETTER dengan validasi:
#    - get_info_rahasia(input_pin) memvalidasi PIN terlebih dahulu
#    - PIN salah -> akses ditolak, data tidak ditampilkan
#    - PIN benar -> akses diizinkan, data ditampilkan
# 
# 4. PERUBAHAN HANYA MELALUI SETTER dengan validasi:
#    - set_diagnosis_kerusakan(input_pin, diagnosis_baru) juga memvalidasi PIN
#    - Hanya PIN benar yang diizinkan mengubah diagnosis
# 
# MANFAAT ENCAPSULATION:
# - Keamanan data: data sensitif tidak bisa diakses sembarangan
# - Kontrol akses: pengembang bisa menentukan siapa yang boleh mengakses data
# - Integritas data: data hanya bisa diubah melalui method yang sudah divalidasi
# - Perawatan kode: perubahan internal tidak mempengaruhi kode di luar kelas
# ============================================================

print()  # Mencetak baris kosong
print("=" * 55)  # Mencetak garis pemisah
print(" DEMONSTRASI ENCAPSULATION SELESAI")
print("=" * 55)  # Mencetak garis pemisah
