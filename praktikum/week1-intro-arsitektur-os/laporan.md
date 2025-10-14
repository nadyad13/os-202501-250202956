
# Laporan Praktikum Minggu [1]
Topik: Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : Nadya Pramudita
- **NIM**   : 250202956 
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1 Sistem Operasi
Sistem operasi (Operating System / OS) adalah perangkat lunak utama yang mengatur seluruh sumber daya komputer — baik perangkat keras (hardware) maupun perangkat lunak (software) — agar dapat bekerja secara efisien dan saling berkomunikasi.
Fungsi utamanya mencakup:
1.	Manajemen Proses (Process Management)
o	Mengatur pembuatan, penjadwalan, dan penghentian proses.
o	Menentukan proses mana yang dijalankan oleh CPU pada waktu tertentu (CPU scheduling).
2.	Manajemen Memori (Memory Management)
o	Mengalokasikan dan membebaskan memori untuk proses yang sedang berjalan.
o	Menjaga agar proses tidak saling mengganggu area memori satu sama lain.
3.	Manajemen Berkas (File Management)
o	Mengatur pembuatan, penyimpanan, pembacaan, dan penghapusan file.
o	Menyediakan struktur direktori agar data mudah diakses.
4.	Manajemen Perangkat I/O (Input/Output Management)
o	Mengontrol perangkat keras seperti keyboard, printer, dan disk.
o	Menyediakan antarmuka agar aplikasi dapat menggunakan perangkat tanpa harus tahu detail teknisnya.
5.	Manajemen Penyimpanan Sekunder (Storage Management)
o	Mengatur ruang disk dan sistem file (file system).
o	Mengoptimalkan akses ke data yang tersimpan.
6.	Manajemen Keamanan dan Proteksi (Security & Protection)
o	Menyediakan mekanisme autentikasi, otorisasi, dan kontrol akses.
o	Melindungi sistem dari gangguan atau akses tidak sah.
7.	User Interface (Antarmuka Pengguna)
o	Bisa berupa Command-Line Interface (CLI) seperti terminal, atau Graphical User Interface (GUI) seperti Windows dan macOS.

2. Peran Kernel
Kernel adalah inti dari sistem operasi — bagian yang paling dekat dengan perangkat keras.
Semua interaksi antara aplikasi dan hardware harus melalui kernel.
Fungsi utama kernel:
•	Mengelola sumber daya sistem (CPU, memori, perangkat I/O).
•	Mengatur eksekusi proses dan multitasking.
•	Menangani interupsi dari perangkat keras.
•	Menyediakan abstraksi perangkat keras agar program tidak perlu mengakses hardware secara langsung.
Tipe kernel (secara umum):
•	Monolithic Kernel → Semua layanan berjalan di dalam kernel (contoh: Linux, Unix).
•	Microkernel → Hanya fungsi dasar di dalam kernel; layanan lain berjalan di ruang pengguna (contoh: Minix, QNX).
•	Hybrid Kernel → Gabungan keduanya (contoh: Windows NT, macOS).

3. Peran System Call
System call adalah antarmuka (interface) antara program aplikasi dengan kernel.
Ketika sebuah program butuh melakukan operasi yang melibatkan hardware (misalnya membaca file, membuat proses baru, atau mengirim data ke jaringan), ia tidak bisa langsung mengakses hardware.
Sebaliknya, ia meminta layanan ke kernel melalui system call.
Contoh system call:
•	read() dan write() untuk operasi file.
•	fork() untuk membuat proses baru.
•	exec() untuk menjalankan program lain.
•	open() dan close() untuk membuka/menutup file.
•	malloc() (melalui library) untuk meminta alokasi memori.

---

## Dasar Teori
1.	Sistem operasi (Operating System / OS) adalah perangkat lunak sistem yang berfungsi sebagai penghubung antara pengguna dan perangkat keras komputer, serta bertugas mengelola sumber daya sistem seperti CPU, memori, dan perangkat I/O.
2.	Kernel merupakan inti dari sistem operasi yang beroperasi di level terendah dan bertanggung jawab langsung terhadap pengendalian dan pengelolaan perangkat keras. Kernel menyediakan layanan dasar yang dibutuhkan oleh seluruh sistem.
3.	System call adalah mekanisme yang digunakan oleh program aplikasi untuk meminta layanan dari kernel, seperti operasi pada file, memori, atau proses. Dengan system call, aplikasi dapat berinteraksi dengan hardware secara aman dan terkontrol.
4.	Hubungan antara aplikasi, system call, dan kernel membentuk arsitektur berlapis: aplikasi berada di user space, kernel di kernel space, dan system call menjadi jembatan komunikasi di antara keduanya.
5.	Tujuan utama percobaan adalah memahami bagaimana sistem operasi bekerja dalam mengatur interaksi antara perangkat lunak dan perangkat keras melalui kernel dan system call.

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
1. Sebutkan tiga fungsi utama sistem operasi.
   1.	Manajemen Proses
Sistem operasi mengatur jalannya proses, mulai dari membuat, menghentikan, hingga menjadwalkan eksekusinya dan menghubungkan antar proses.
   2.	Manajemen Memori
Sistem membagi dan mengelola penggunaan RAM agar proses berjalan tanpa gangguan dan memori bisa digunakan efisien.
   3.	Manajemen I/O
Sistem mengatur komunikasi antara perangkat keras (seperti keyboard dan printer) dengan komputer, termasuk pengelolaan driver dan buffer.
 
2. Jelaskan perbedaan antara kernel mode dan user mode. 
   Kernel mode memberi akses penuh ke perangkat keras dan semua sumber daya sistem. Hanya bagian inti sistem operasi yang berjalan di mode ini.
   User mode memiliki akses terbatas dan digunakan oleh aplikasi. Jika butuh akses ke sistem, aplikasi harus meminta lewat system call. Crash di user mode tidak memengaruhi sistem secara keseluruhan.

3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel. 
   •	Arsitektur Monolithic:
o	Linux
o	MS-DOS
o	Unix (versi awal)
   •	Arsitektur Microkernel:
o	Minix
o	QNX
o	seL4
o	GNU Hurd


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini = Membuat akun git
- Bagaimana cara Anda mengatasinya = Saya melakukan pengecekan username, nim, mencari cara diinternet, dan bertanya kepada teman yang sudah paham.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
