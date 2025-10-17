
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
1.	System call berfungsi sebagai jembatan penting antara program aplikasi di ruang pengguna (user space) dan kernel di ruang kernel (kernel space). 
Program dapat meminta layanan esensial dari sistem operasi, seperti mengakses file, mengelola proses, atau menangani komunikasi antarproses.
2.	Kernel menjalankan system call dalam mode khusus yang disebut kernel mode.
Pendekatan ini melindungi sistem dari risiko akses langsung yang berbahaya oleh program pengguna terhadap perangkat keras atau memori.
3.	Implementasi system call biasanya melibatkan mekanisme interrupt atau trap. Saat sebuah aplikasi memanggil system call, prosesor segera beralih dari user mode ke kernel mode melalui interrupt, sehingga kernel bisa menangani permintaan secara efektif.
4.	Jenis system call meliputi manajemen proses (misalnya, fungsi fork dan exec), manajemen file (seperti open, read, write, dan close), komunikasi antarproses, serta pengelolaan memori (seperti mmap dan brk).
5.	Setiap sistem operasi memiliki tabel system call yang unik. Misalnya, Linux menggunakan tabel dengan nomor unik untuk setiap fungsi, sementara Windows mengadopsi API yang berbeda tapi tetap mengikuti mekanisme serupa. 

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
strace ls
strace -e trace=open,read,write,close cat /etc/passwd
dmesg | tail -n 10
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
<img width="1352" height="696" alt="Screenshot 2025-10-16 194124" src="https://github.com/user-attachments/assets/72aeeb2c-1f9d-432c-a655-e8def914c2b3" />


---

## Analisis
- Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel.
- Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?

- 1. Membuka File
open("/etc/passwd", O_RDONLY) = 3
Perintah open() adalah system call yang digunakan program untuk meminta kernel membuka file /etc/passwd. 
Parameter O_RDONLY artinya file dibuka dalam mode read-only.
Kernel mengembalikan file descriptor bernomor 3 — ini adalah “penanda” yang digunakan proses untuk mengakses file tersebut.
Makna:
Kernel memeriksa izin akses, mencari lokasi file di sistem berkas (melalui inode), lalu mempersiapkan struktur data internal untuk operasi selanjutnya.

2. Membaca Isi File
read(3, "root:x:0:0:root:/root:/bin/bash\n"..., 131072) = 1424

read() meminta kernel membaca isi file dari descriptor 3 (yakni /etc/passwd).

Kernel menyalin data dari file di disk ke memori user space sebanyak 1424 byte.

Nilai 1424 menunjukkan banyaknya byte yang berhasil dibaca.

Makna:
Kernel bertugas melakukan I/O operation — mengambil data dari media penyimpanan dan mengirimkannya ke proses user (cat) agar bisa ditampilkan.

3. Menampilkan ke Layar
write(1, "root:x:0:0:root:/root:/bin/bash\n"..., 1424)
write() digunakan untuk menulis data ke file descriptor 1, yaitu stdout (layar terminal).
Data hasil read() tadi dikirimkan ke terminal melalui kernel.

Makna:
Kernel menyalurkan data dari memori user menuju perangkat output (layar) menggunakan mekanisme file descriptor.

4. Menutup File
close(3) = 0
Setelah selesai membaca, program menutup file descriptor 3 menggunakan close().
Kernel kemudian melepaskan sumber daya yang digunakan untuk file itu (misalnya buffer dan inode reference).

Makna:
Kernel memastikan bahwa file tidak lagi digunakan, mencegah kebocoran sumber daya (resource leak).

5. Menutup Output dan Error Stream
close(1) = 0
close(2) = 0
close(1) dan close(2) menutup stdout dan stderr setelah program cat selesai berjalan.


| Aspek               | Log Kernel (`dmesg`)                                                            | Program Biasa (mis. `cat`, `ls`, `echo`)                                 |
| ------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Sumber pesan**    | Dari **kernel Linux**                                                           | Dari **program user** di user space                                      |
| **Isi pesan**       | Aktivitas sistem (driver, modul, hardware, virtualisasi, error internal kernel) | Hasil operasi spesifik program (menampilkan file, teks, direktori, dll.) |
| **Level kerja**     | Level **kernel space**                                                          | Level **user space**                                                     |
| **Tujuan utama**    | Diagnostik, debugging, status perangkat                                         | Memberi hasil langsung ke pengguna                                       |
| **Dihasilkan oleh** | Kernel dan modulnya                                                             | Proses atau aplikasi biasa                                               |


---

## Kesimpulan
1.	System call berperan sebagai jembatan penting antara program aplikasi dan kernel
Memungkinkan program untuk meminta layanan dari sistem operasi seperti pengelolaan file, memori, dan proses tanpa perlu berinteraksi langsung dengan perangkat keras.
2.	Kernel kemudian menangani eksekusi system call ini dengan cara yang aman dan efisien.
Saat program melakukan system call kendali sementara beralih dari mode pengguna ke mode kernel untuk menjalankan instruksi, sebelum kembali ke mode pengguna setelah tugas selesai.
3. Perbedaan antar sistem operasi dapat memengaruhi cara system call diimplementasikan.
Misalnya, Linux menggunakan fungsi seperti fork() untuk membuat proses baru, sementara Windows menggunakan CreateProcess() untuk fungsi serupa, meskipun keduanya pada dasarnya melakukan tugas yang sama.

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
- Apa bagian yang paling menantang minggu ini = Susah dalam mengerjakan system call (dll)
- Bagaimana cara Anda mengatasinya = Bertanya kepada teman yang sudah paham

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
