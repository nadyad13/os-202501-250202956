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


## Analisis
2. Jelaskan setiap output dan fungsinya(whoami, id, groups)

   
- Perintah whoami
Fungsi:
Menampilkan nama user (pengguna) yang sedang aktif login di sistem saat ini.
Penjelasan output:
Output nadya berarti user yang sedang menjalankan terminal saat ini bernama nadya.
Perintah ini berguna untuk memastikan kamu sedang berada sebagai user siapa (terutama jika sering berpindah ke root dengan sudo).

- Perintah id
Fungsi:
Menampilkan informasi identitas lengkap user, termasuk UID (User ID), GID (Group ID), Daftar grup yang diikuti user
Penjelasan output:
uid=1000(nadya) → ID unik user nadya adalah 1000
gid=1000(nadya) → ID grup utama user nadya adalah 1000
groups=1000(nadya),27(sudo) → User nadya termasuk dalam dua grup: nadya (utama) dan sudo (grup dengan hak admin)

- Perintah groups
Fungsi:
Menampilkan grup-grup yang diikuti oleh user saat ini.
Penjelasan output:
Menunjukkan bahwa user nadya tergabung dalam dua grup:
nadya (grup utama)
sudo (grup tambahan yang memberikan akses administrasi)








3. Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.
   
- PID (Process ID)
Fungsi: Menunjukkan nomor unik yang diberikan sistem untuk setiap proses yang sedang berjalan.
- USER
Fungsi: Menunjukkan nama user (pengguna) yang menjalankan proses tersebut.
- %CPU
Fungsi: Menunjukkan persentase penggunaan CPU oleh proses tersebut.
- %MEM
Fungsi: Menunjukkan persentase penggunaan memori (RAM) oleh proses.
- COMMAND
Fungsi: Menampilkan nama atau perintah yang digunakan untuk menjalankan proses.


4. Catat PID proses sleep.




5. Amati hierarki proses dan identifikasi proses induk (init/systemd).

---

## Kesimpulan
1.	Manajemen Proses: memungkinkan pengguna menggunakan ps, top, kill, dan nice untuk pantau, kontrol, dan prioritaskan proses, agar sumber daya sistem lebih efisien.
2.	Manajemen User dan Group: berperan penting untukpengguna melalui perintah useradd, passwd, dan groups bantu tetapkan hak akses dan izin file untuk jaga keamanan sistem.
3.	Multitasking dan Multiuser: memungkinkan banyak proses dan pengguna jalan bersamaan tanpa gangguan, bikin sistem stabil dan efektif untuk digunakan Bersama.


---



## Tugas dan Quiz

### Tugas
1. Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.
- whoami
Perintah whoami digunakan untuk mengetahui nama user yang sedang aktif di terminal. Hasil menunjukkan bahwa user yang sedang login adalah nadya.
- id
Perintah id menampilkan identitas lengkap user, termasuk UID, GID, dan grup yang diikuti. Hasil menunjukkan user nadya memiliki UID 1000 dan tergabung dalam beberapa grup penting seperti sudo dan adm.
- groups
Perintah groups digunakan untuk melihat daftar grup tempat user tergabung. Output menunjukkan nadya termasuk dalam grup adm, sudo, dan users, yang memberi hak akses administratif.
- sudo adduser praktikan
Perintah ini berhasil menambahkan user baru bernama praktikan, lengkap dengan home directory dan password. User ini juga otomatis dimasukkan ke dalam grup users.
- sudo passwd praktikan
Perintah passwd berfungsi untuk mengatur atau mengubah password user. Hasil menunjukkan password untuk user praktikan berhasil diperbarui dengan sukses.
- ps aux | head -10
Perintah ini menampilkan daftar proses yang sedang berjalan di sistem beserta informasi penting seperti PID, CPU, dan memori. Hasil menunjukkan proses sistem utama yang dijalankan oleh user root dan systemd.
- top -n 1
Perintah top memberikan tampilan dinamis kondisi sistem, termasuk beban CPU, penggunaan memori, dan proses aktif. Opsi -n 1 menampilkan data satu kali saja. Hasil menunjukkan sistem dalam keadaan ringan (load rendah).
- sleep 1000 &
Perintah ini menjalankan proses sleep selama 1000 detik di background, memungkinkan terminal tetap digunakan untuk perintah lain. PID proses sleep adalah 586.
- ps aux | grep sleep
Perintah ini digunakan untuk mengecek apakah proses sleep sedang berjalan. Output menunjukkan proses sleep dengan PID 586 aktif di background sebelum dihentikan.
- kill 586
Perintah kill mengirim sinyal untuk menghentikan proses tertentu berdasarkan PID. Proses sleep 1000 berhasil dihentikan, terbukti dari pesan “Terminated”.
- pstree -p | head -20
Perintah ini menampilkan hierarki proses dalam bentuk pohon dengan PID-nya. Hasil menunjukkan hubungan antara proses utama systemd(1) dan proses turunannya seperti cron, dbus-daemon, serta bash.

2. Gambarkan hierarki proses dalam bentuk diagram pohon (`pstree`) di laporan.

<img width="4002" height="1072" alt="diagrampohon" src="https://github.com/user-attachments/assets/b0dc47c1-a374-4486-ab0d-7bd831207969" />

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
