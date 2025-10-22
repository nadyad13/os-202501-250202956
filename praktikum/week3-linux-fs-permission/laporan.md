
# Laporan Praktikum Minggu [3]
Topik: Manajemen File dan Permission di Linux
---

## Identitas
- **Nama**  : Nadya Pramudita
- **NIM**   : 250202956 
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori.
2. Menggunakan chmod dan chown untuk manajemen hak akses file.
3. Menjelaskan hasil output dari perintah Linux dasar.
4. Menyusun laporan praktikum dengan struktur yang benar.
5. Mengunggah dokumentasi hasil ke Git Repository tepat waktu.

---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari pengelolaan file dan direktori menggunakan perintah dasar Linux, serta konsep permission dan ownership.
Praktikum berfokus pada:

- Navigasi sistem file dengan ls, pwd, cd, dan cat.
- Pengaturan hak akses file menggunakan chmod.
- Pengubahan kepemilikan file menggunakan chown.
- Dokumentasi hasil eksekusi dan pengelolaan repositori praktikum.

Tujuan utama dari praktikum ini adalah agar mahasiswa mampu mengoperasikan perintah Linux dasar dengan benar, memahami sistem izin (permission), dan mendokumentasikan hasilnya dalam format laporan Git.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan folder kerja berada di dalam direktori repositori Git praktikum:
     ```
     praktikum/week3-linux-fs-permission/
     ```

2. **Eksperimen 1 – Navigasi Sistem File**
   Jalankan perintah berikut:
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
   - Jelaskan hasil tiap perintah.
   - Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

3. **Eksperimen 2 – Membaca File**
   Jalankan perintah:
   ```bash
   cat /etc/passwd | head -n 5
   ```
   - Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

4. **Eksperimen 3 – Permission & Ownership**
   Buat file baru:
   ```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```
   - Analisis perbedaan sebelum dan sesudah chmod.  
   - Ubah pemilik file (jika memiliki izin sudo):
   ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
   - Catat hasilnya.

5. **Eksperimen 4 – Dokumentasi**
   - Ambil screenshot hasil terminal dan simpan di:
     ```
     praktikum/week3-linux-fs-permission/screenshots/
     ```
   - Tambahkan analisis hasil pada `laporan.md`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 3 - Linux File System & Permission"
   git push origin main
   ```
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
screenshot hasil Linux
<img width="1365" height="717" alt="final percobaan linux" src="https://github.com/user-attachments/assets/8231f560-8c86-44f6-abdc-27f23fc480c2" />


---

## Analisis
Sebelum chmod 600
Output dari ls -l percobaan.txt:
-rw-r--r-- 1 nadya nadya 25 Oct 21 17:45 percobaan.txt

Artinya:
-rw-r--r-- = hak akses file.

rw- → pemilik (owner: nadya) dapat membaca dan menulis.
r-- → grup (group: nadya) hanya dapat membaca.
r-- → pengguna lain (others) hanya dapat membaca.
Jadi, sebelum chmod 600, semua pengguna bisa membaca file, tetapi hanya pemilik yang bisa menulis.

Sesudah chmod 600
Setelah perintah:
chmod 600 percobaan.txt

Jika dicek lagi:
ls -l percobaan.txt
-rw------- 1 nadya nadya 25 Oct 21 17:45 percobaan.txt

Artinya:
-rw-------
rw- → hanya pemilik (owner) bisa membaca dan menulis.
--- → grup dan pengguna lain tidak punya akses sama sekali.
Jadi, sesudah chmod 600, file hanya dapat diakses oleh pemiliknya (tidak bisa dibaca maupun ditulis oleh orang lain).

Kesimpulan Perbedaan
| Kondisi | Kode Hak Akses | Pemilik      | Grup | Lainnya |
| ------- | -------------- | ------------ | ---- | ------- |
| Sebelum | `rw-r--r--`    | Baca & Tulis | Baca | Baca    |
| Sesudah | `rw-------`    | Baca & Tulis | -    | -       |

Makna perubahan:
Perintah chmod 600 membatasi akses file agar hanya pemilik yang bisa membuka dan mengedit, sementara pengguna lain tidak bisa melihat atau mengakses file sama sekali — ini meningkatkan keamanan dan privasi data.

---

## Kesimpulan
1.	Pengelolaan file dan direktori di Linux dapat dilakukan secara efisien menggunakan perintah dasar seperti ls, cd, cp, mv, rm, mkdir, dan rmdir melalui terminal.
2.	Konsep permission dan ownership sangat penting untuk mengatur hak akses pengguna terhadap file dan direktori, sehingga keamanan dan integritas sistem tetap terjaga.
3.	Perintah chmod, chown, dan chgrp memungkinkan pengguna atau administrator sistem untuk mengatur hak akses dan kepemilikan sesuai kebutuhan masing-masing pengguna.

---

## Quiz
1. Fungsi Perintah Chmod
  Chmod ini alat utama untuk ngubah izin akses file atau direktori di sistem Linux atau Unix. Dengan ini, bias mengatur siapa yang boleh membaca. Menulis atau menjalankan file itu. Ini membantu untuk menjaga keamanan data dan kelola akses agar tidak sembarangan, jadi lebih efisien dan aman.
2. Arti dari kode permission rwxr-xr--
  Kode tersebut menunjukkan hak akses sebuah file: 
rwx : memberikan pemilik file dapet izin penuh untuk membaca, mentulis, dan menjalankan. 
r-x : membatasi anggota grup agar hanya bisa membaca dan menjalankan, tanpa menulis. 
r-- : menyimpan akses untuk pengguna lain hanya bisa membaca tidak bisa menulis atau menjalankan
Pemilik mendapat kendali penuh, grup menikmati akses terbatas, dan pengguna lain dibatasi pada fungsi dasar pembacaan.
3. Perbedaan Antara Chown dan Chmod
   Chmod secara khusus digunakan untuk mengatur atau mengubah izin akses pada file atau direktori, sehingga menentukan tindakan apa yang diizinkan.
Chown berfungsi untuk mengubah pemilik dan grup dari file atau direktori tersebut, yang berfokus pada siapa yang bertanggung jawab atasnya.
Singkatnya chmod mengendalikan "apa yang boleh dilakukan", sedangkan chown menangani "siapa yang memilikinya", membuat keduanya saling melengkapi dalam pengelolaan file di Linux atau Unix.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? = memahami stuktur sistem linux
- Bagaimana cara Anda mengatasinya? = mencari tau struktur sistem linux dan bertanya kepada teman

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
