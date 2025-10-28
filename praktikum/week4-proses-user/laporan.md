
# Laporan Praktikum Minggu [X]
Topik: Proses User

---

## Identitas
- **Nama**  : Nadya Pramudita
- **NIM**   : 250202956
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Menjelaskan konsep proses dan user dalam sistem operasi Linux.
2. Menampilkan daftar proses yang sedang berjalan dan statusnya.
3. Menggunakan perintah untuk membuat dan mengelola user.
4. Menghentikan atau mengontrol proses tertentu menggunakan PID.
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem.
---

## Dasar Teori
1. Proses User adalah program yang sedang dieksekusi di ruang pengguna (user space), berbeda dengan proses kernel yang berjalan di kernel space.
2. Setiap proses user memiliki ruang memori sendiri untuk mencegah gangguan antarproses dan menjaga keamanan sistem.
3. Proses user berinteraksi dengan perangkat keras atau layanan sistem melalui system call, yaitu permintaan layanan ke kernel.
4. Sistem operasi mengatur penjadwalan (scheduling) proses user agar CPU digunakan secara efisien dan adil antarproses.
5. Proses user dapat membuat proses baru (child process) menggunakan mekanisme seperti fork() dan berkomunikasi antarproses melalui IPC (Inter-Process Communication).

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
2. Jelaskan setiap output dan fungsinya.
3. Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.
4. Catat PID proses sleep.
5. Amati hierarki proses dan identifikasi proses induk (init/systemd).

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---
## Tugas dan Quiz
### Tugas
1. Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.  
2. Gambarkan hierarki proses dalam bentuk diagram pohon (`pstree`) di laporan.  
3. Jelaskan hubungan antara user management dan keamanan sistem Linux.
- Pengendalian akses:
User management menentukan siapa yang boleh mengakses sistem dan sumber daya tertentu. Dengan mengatur akun dan hak akses dengan tepat, hanya pengguna yang berwenang yang dapat menjalankan perintah atau mengakses file penting.
- Pembatasan hak istimewa:
Setiap user diberi izin (permission) sesuai kebutuhan. Prinsip “least privilege” diterapkan agar pengguna tidak memiliki hak lebih dari yang diperlukan, sehingga risiko penyalahgunaan atau kesalahan sistem dapat diminimalkan.
- Audit dan pelacakan aktivitas:
Setiap user memiliki identitas unik. Hal ini memungkinkan administrator untuk melacak aktivitas pengguna (melalui log), mendeteksi pelanggaran, atau mengidentifikasi sumber masalah keamanan.
- Perlindungan terhadap data dan file sistem:
Dengan manajemen user yang baik (misalnya pengaturan permission rwx pada file), data sensitif dapat dilindungi dari akses, perubahan, atau penghapusan oleh pengguna yang tidak berhak.
- Pencegahan akses tidak sah:
User management juga mencakup kebijakan kata sandi, penguncian akun, dan otentikasi yang kuat, yang membantu mencegah login ilegal atau serangan brute force.

4. Upload laporan ke repositori Git tepat waktu.

### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?
Proses init atau systemd adalah yang pertama dijalankan oleh kernel saat sistem dinyalakan. Ini seperti induk dari semua proses lain, bertugas menginisialisasi sistem dengan menjalankan layanan dan skrip startup, mengelola daemon seperti sshd atau cron, membersihkan proses zombie, serta menangani shutdown dan reboot agar sistem mati dengan aman. Tanpa systemd, sistem operasi ini tidak akan berjalan lancar—bayangkan saja kacau balau tanpa pengatur utama.


2. Apa perbedaan antara `kill` dan `killall`?
Perintah kill dan killall untuk menghentikan proses. Kill mengirim sinyal ke proses spesifik berdasarkan PID (Process ID), misalnya kill 1234 hanya berhenti proses dengan ID itu. Sedangkan killall lebih luas, mengirim sinyal ke semua proses dengan nama sama, seperti killall firefox yang menghentikan semua instance Firefox yang berjalan. Ini berguna kalau ada banyak proses serupa yang perlu dibersihkan sekaligus.


3. Mengapa user `root` memiliki hak istimewa di sistem Linux?
User root adalah akun administrator utama di Linux, dengan akses penuh ke seluruh sistem. Dia bisa instal software, ubah konfigurasi, tambah/hapus pengguna, atau modifikasi file penting tanpa batasan izin. Tapi, karena kendalinya total, gunakan dengan hati-hati satu kesalahan bisa merusak system.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
