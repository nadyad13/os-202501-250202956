
# Laporan Praktikum Minggu [2]
Topik: system call

---

## Identitas
- **Nama**  : Nadya Pramudita
- **NIM**   : 250202956
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  

1. Konsep dan Fungsi System Call dalam Sistem Operasi
System call adalah mekanisme yang menghubungkan program pengguna dengan kernel sistem operasi. Karena program di user mode tidak boleh langsung mengakses perangkat keras, system call berfungsi sebagai perantara yang aman.
Fungsinya meliputi: mengatur akses sumber daya, memungkinkan komunikasi antar proses, menjalankan operasi input/output, serta menjaga keamanan dan stabilitas sistem.

2. Jenis-jenis System Call dan Fungsinya :
- Manajemen Proses: untuk membuat, menjalankan, dan mengakhiri proses.
- Manajemen File: untuk membuka, membaca, menulis, dan menutup file.
- Manajemen Perangkat: untuk berinteraksi dengan perangkat keras melalui kernel.
- Manajemen Memori: untuk mengalokasikan dan membebaskan memori.
- Komunikasi Antar Proses: untuk bertukar data antar proses dalam sistem.

4. Alur Perpindahan Mode User ke Kernel
Saat system call dipanggil, program di user mode mengirim permintaan ke kernel melalui interrupt atau trap. CPU berpindah ke kernel mode, kernel mengeksekusi fungsi yang diminta, kemudian hasilnya dikembalikan ke program dan sistem kembali ke user mode.
Proses ini memastikan keamanan dan pengendalian penuh oleh sistem operasi.

5. Perintah Linux untuk Melihat System Call
Linux menyediakan perintah seperti strace atau ltrace untuk menampilkan aktivitas system call dan menganalisis interaksi program dengan kernel secara singkat.


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
1. Apa fungsi utama system call dalam sistem oprasi?
   System call berfungsi sebagai penghubung krusial antara aplikasi pengguna yang beroperasi di mode user dan inti sistem operasi di mode kernel. Lewat mekanisme ini, aplikasi bisa meminta bantuan OS untuk tugas-tugas esensial, seperti membuka file, memulai proses baru, atau berinteraksi dengan hardware, semuanya dalam kerangka yang aman dan terawasi ketat.

2. Sebutkan 4 kategori utama system call yang umum digunakan
- Manajemen Proses
Ini mencakup perintah untuk mengendalikan alur proses, seperti fork untuk duplikasi proses, exec untuk jalankan program baru, exit untuk akhiri proses, dan wait untuk pantau proses turunan.
- Manajemen File
Fokus pada operasi file, termasuk open untuk akses file, read untuk ambil data, write untuk simpan data, serta close untuk tutup file.
- Manajemen Perangkat (I/O)
Khusus untuk interaksi hardware, contohnya ioctl untuk perintah khusus perangkat, plus read dan write yang disesuaikan untuk input/output.
- Manajemen Memori
Menangani alokasi ruang memori, seperti mmap untuk petakan memori dan brk untuk sesuaikan ukuran heap.
  
3. Mengapa System Call tidak bisa dipanggil langsung oleh user program?
   Alasannya program di mode user sengaja dibatasi aksesnya agar tak bisa langsung sentuh hardware atau sumber daya vital OS—semua demi keamanan dan kestabilan sistem. kalau aplikasi bisa bebas campuri kernel; risikonya besar, mulai dari kerusakan total hingga penyalahgunaan yang merusak. Makanya, system call harus dipanggil via jalur khusus seperti interrupt atau trap, yang memastikan transisi ke kernel tetap terkendali dan diawasi. 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
