# SM Irigasi - Sistem Monitoring Irigasi Sawah

Proyek ini adalah prototipe sistem pemantauan irigasi berbasis Pemrograman Berorientasi Objek (OOP). Kode ini mendemonstrasikan implementasi tiga pilar utama PBO: **Inheritance**, **Polymorphism**, dan **Encapsulation** menggunakan bahasa pemrograman Python.

---

## Implementasi Konsep PBO

### 1. Inheritance (Pewarisan Sifat)
Konsep ini digunakan untuk membangun hirarki saluran irigasi tanpa menulis ulang kode yang sama berkali-kali (*Code Reuse*).

* **Parent Class (`Irigasi`):** Menampung atribut dasar seperti nama saluran, debit air, dan panjang saluran.
* **Child Classes (`IrigasiPrimer` & `IrigasiTersier`):** Mewarisi atribut induk dan menambahkan fitur spesifik (seperti jumlah pintu air atau luas cakupan sawah).
* **Key Feature:** Penggunaan `super().__init__()` untuk menghubungkan logika kelas anak dengan kelas induk secara efisien.



[Image of Inheritance in object-oriented programming]


### 2. Polymorphism (Polimorfisme)
Konsep ini memungkinkan sistem memiliki satu antarmuka (nama fungsi) yang sama, namun menghasilkan perilaku yang berbeda sesuai jenis objeknya.

* **Method Overriding:** Menggunakan satu method bernama `hitung()` di berbagai kelas (Pajak, Diskon, dan Asuransi).
* **Polymorphic Function:** Fungsi `jalankan_perhitungan()` dapat menerima objek apapun (Pajak/Diskon/Asuransi) dan menjalankan perhitungan yang tepat secara otomatis.
* **Benefit:** Mempermudah penambahan komponen biaya baru di masa depan tanpa mengubah struktur fungsi utama.



[Image of polymorphism in object-oriented programming]


### 3. Encapsulation (Enkapsulasi)
Konsep ini digunakan untuk melindungi data sensitif dan menjamin keamanan informasi sensor.

* **Private Attributes:** Data seperti `__pin_kalibrasi`, `__harga_pokok`, dan `__diagnosis` disembunyikan menggunakan *double underscore* agar tidak bisa diakses secara ilegal dari luar kelas.
* **Access Control:** Data hanya dapat dibaca melalui **Getter** (`get_info_rahasia`) dan diubah melalui **Setter** (`set_diagnosis_kerusakan`) yang keduanya memerlukan validasi PIN teknisi.
* **Security:** Mencegah manipulasi data sensor oleh pihak yang tidak berwenang.



---

## Cara Menjalankan Kode

1. Pastikan Anda memiliki Python terinstal di komputer Anda.
2. Salin kode ke dalam file berekstensi `.py` (misal: `irigasi_oop.py`).
3. Jalankan melalui terminal:
   ```bash
   python irigasi_oop.py
