
# Laporan Praktikum Minggu [3]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : Nadya Pramudita
- **NIM**   : 250202956 
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Fungsi Perintah Chmod
  Perintah chmod memungkinkan pengguna mengubah izin akses pada file atau direktori di sistem operasi Linux atau Unix. Dengan perintah ini, bisa secara tepat menentukan hak-hak spesifik, seperti siapa yang boleh membaca, menulis, atau menjalankan file tersebut, sehingga membantu mengamankan dan mengelola akses data dengan lebih efektif.
2. Arti dari kode permission rwxr-xr--
  Kode tersebut menunjukkan hak akses sebuah file: 
rwx : memberikan pemilik file hak penuh untuk membaca, menulis, dan menjalankannya.
r-x : membatasi anggota grup agar hanya bisa membaca dan menjalankan file, tanpa izin menulis.
r-- : menyimpan akses pengguna lain hanya untuk membaca saja, tanpa kemampuan menulis atau menjalankan.
Pemilik mendapat kendali penuh, grup menikmati akses terbatas, dan pengguna lain dibatasi pada fungsi dasar pembacaan.
3. Perbedaan Antara Chown dan Chmod
   Chmod secara khusus digunakan untuk mengatur atau mengubah izin akses pada file atau direktori, sehingga menentukan tindakan apa yang diizinkan.
Chown berfungsi untuk mengubah pemilik dan grup dari file atau direktori tersebut, yang berfokus pada siapa yang bertanggung jawab atasnya.
Singkatnya chmod mengendalikan "apa yang boleh dilakukan", sedangkan chown menangani "siapa yang memilikinya", membuat keduanya saling melengkapi dalam pengelolaan file di Linux atau Unix.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
