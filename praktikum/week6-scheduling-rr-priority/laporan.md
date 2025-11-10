
# Laporan Praktikum Minggu [6]
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling

---

## Identitas
- **Nama**  : Nadya Pramudita
- **NIM**   : 250202956
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
1. Menghitung *waiting time* dan *turnaround time* pada algoritma RR dan Priority.  
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.  
3. Membandingkan performa algoritma RR dan Priority.  
4. Menjelaskan pengaruh *time quantum* dan prioritas terhadap keadilan eksekusi proses.  
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.  


---

## Dasar Teori
Round Robin (RR)
1. Berdasarkan konsep time-sharing, di mana setiap proses mendapat jatah waktu CPU secara bergiliran.

2. Menggunakan time quantum tetap untuk membatasi lama eksekusi tiap proses sebelum digantikan proses lain.

3. Jika proses belum selesai dalam jatah waktunya, proses tersebut dimasukkan kembali ke antrian siap (ready queue).

4. Menjamin keadilan bagi semua proses, karena setiap proses mendapat kesempatan yang sama.

5. Efisiensi dan respons sistem sangat dipengaruhi oleh ukuran time quantum yang digunakan.

Priority Scheduling

1. Menjadwalkan proses berdasarkan tingkat prioritas yang ditetapkan — prioritas tinggi dijalankan lebih dahulu.

2. Dapat bersifat preemptive (menghentikan proses yang sedang berjalan) atau non-preemptive (menunggu proses selesai).

3. Cocok untuk sistem yang membutuhkan pengaturan tingkat kepentingan proses.

4. Dapat menimbulkan starvation jika proses prioritas rendah terus tertunda.

5. Dapat diatasi dengan aging, yaitu menaikkan prioritas proses yang menunggu terlalu lama.

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

## Kesimpulan
Round Robin (RR)
- Setiap proses mendapat giliran waktu yang sama (time quantum), sehingga sistem lebih adil dan responsif.

- Cocok untuk sistem interaktif atau time-sharing, karena semua proses mendapat kesempatan berjalan.

- Kinerja sistem sangat dipengaruhi oleh besar-kecilnya time quantum — terlalu kecil menyebabkan overhead, terlalu besar menurunkan respons.

Priority Scheduling

- Proses dijalankan berdasarkan tingkat prioritas, sehingga proses penting selesai lebih cepat.

- Dapat menyebabkan starvation bagi proses berprioritas rendah jika tidak diatur dengan baik.

- Dapat diperbaiki dengan teknik aging untuk meningkatkan prioritas proses yang menunggu terlalu lama.

---

## Quiz
1. Perbedaan utama antara Round Robin dan Priority Scheduling

   **Jawaban:** 

- Round Robin (RR) menggunakan pembagian waktu yang sama untuk setiap proses. Setiap proses mendapat giliran menjalankan CPU selama waktu tertentu yang disebut time quantum, lalu digantikan oleh proses lain. Tujuannya agar semua proses diperlakukan adil dan sistem tetap responsif, terutama pada sistem interaktif.

- Priority Scheduling menentukan urutan eksekusi berdasarkan tingkat prioritas. Proses dengan prioritas tertinggi dijalankan terlebih dahulu. Sistem ini cocok jika ada proses yang harus diselesaikan lebih cepat daripada yang lain, tetapi bisa menimbulkan ketidakadilan bagi proses berprioritas rendah.

2. Pengaruh besar/kecilnya time quantum terhadap performa sistem

   **Jawaban:**  

Time quantum terlalu kecil
- Terjadi terlalu sering context switching, menyebabkan:
- Overhead CPU tinggi
- Performa sistem menurun
- Respons cepat, tapi efisiensi buruk

Time quantum terlalu besar
- Proses panjang bisa mendominasi CPU, menyebabkan:
- Sistem jadi mirip FCFS
- Respons terhadap proses lain menjadi lambat
- Waktu tunggu meningkat

3. Mengapa algoritma Priority dapat menyebabkan starvation

   **Jawaban:**  

Algoritma Priority dapat menyebabkan starvation karena proses dengan prioritas rendah terus tertunda, sementara proses prioritas tinggi selalu didahulukan, sehingga yang prioritas rendah mungkin tidak pernah dieksekusi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
