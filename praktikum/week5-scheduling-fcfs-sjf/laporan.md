
# Laporan Praktikum Minggu [X]
Topik: scheduling fcfs dan sjf

---

## Identitas
- **Nama**  : Nadya Pramudita
- **NIM**   : 250202956 
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Menghitung waiting time dan turnaround time untuk algoritma FCFS dan SJF.
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.


---

## Dasar Teori
1. FCFS (First Come First Served)

- Proses dijalankan sesuai urutan kedatangan (siapa datang lebih dulu, dijalankan lebih dulu).

- Bersifat non-preemptive, proses tidak bisa dihentikan sebelum selesai.

- Implementasinya mudah karena menggunakan antrian FIFO (First In First Out).

- Dapat menyebabkan efek konvoi, yaitu proses pendek menunggu proses panjang selesai.

- Kurang efisien untuk sistem interaktif karena waktu tunggu bisa lama.

2. SJF (Shortest Job First)

- Proses dengan waktu eksekusi (burst time) paling pendek dijalankan terlebih dahulu.

- Dapat bersifat non-preemptive atau preemptive (SRTF).

- Memberikan waktu tunggu rata-rata paling rendah dibanding algoritma lain.

- Membutuhkan perkiraan akurat burst time untuk menentukan prioritas.

- Efisien untuk sistem dengan beban kerja yang dapat diprediksi durasinya.
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Siapkan Data Proses**
   Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):
   | Proses | Burst Time | Arrival Time |
   |:--:|:--:|:--:|
   | P1 | 6 | 0 |
   | P2 | 8 | 1 |
   | P3 | 7 | 2 |
   | P4 | 3 | 3 |

2. **Eksperimen 1 – FCFS (First Come First Served)**
   - Urutkan proses berdasarkan *Arrival Time*.  
   - Hitung nilai berikut untuk tiap proses:
     ```
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
     ```
   - Hitung rata-rata Waiting Time dan Turnaround Time.  
   - Buat Gantt Chart sederhana:  
     ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
     ```

| Proses | Burst Time | Arrival Time | Star Time | Finis Time |WT | TAT|
   |:--:|:--:|:--:|:--:|:--:|:--:|:--:|
   | P1 | 6 | 0 | 0 | 6 | 0 | 6 |
   | P2 | 8 | 1 | 6 | 14 | 5 | 13 |
   | P3 | 7 | 2 | 14 | 21 | 12 | 19 |
   | P4 | 3 | 3 | 21 | 24 | 18 | 21 |

   rata-rata Waiting Time (WT) = 8,75

   rata-rata Turnaround Time (TAT) = 14,75

   Gantt Chart:

    | P1 | P2 | P3 | P4 |
     0    6    14   21   24

3. **Eksperimen 2 – SJF (Shortest Job First)**
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).  
   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.  

| Proses | Burst Time | Arrival Time | Star Time | Finis Time |WT | TAT|
   |:--:|:--:|:--:|:--:|:--:|:--:|:--:|
   | P4 | 3 | 3 | 3 | 6 | 0 | 3 |
   | P1 | 6 | 0 | 6  | 12  | 6  |  12 |
   | P3 | 7 | 2 | 12 | 19 | 10 | 17 |
   | P2 | 8 | 1 | 19  | 27 | 18  | 26 |
   
   rata-rata Waiting Time (WT) = 8,5

   rata-rata Turnaround Time (TAT) = 14,5

Gantt Chart:

    | P1 | P2 | P3 | P4 |
     0    6    12   19   27

   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS | 8,75 | 14,75 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF | 8,5 | 14,5 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |



4. **Eksperimen 3 – Visualisasi Spreadsheet (Opsional)**
   - Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
     - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
     - Gunakan formula dasar penjumlahan/subtraksi.
   - Screenshot hasil perhitungan dan simpan di:
     ```
     praktikum/week5-scheduling-fcfs-sjf/screenshots/
     ```

5. **Analisis**
   - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
   - Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
   - Tambahkan kesimpulan singkat di akhir laporan. 

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
   git push origin main
   ```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
1. Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF. 
2. Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya. 
3. Tambahkan kesimpulan singkat di akhir laporan.

**jawaban**
1. Rata rata FCFS
- rata-rata Waiting Time (WT) = 8,75
- rata-rata Turnaround Time (TAT) = 14,75

Rata rata FJS
- rata-rata Waiting Time (WT) = 8,5
- rata-rata Turnaround Time (TAT) = 14,5

2. - SJF lebih unggul dari FCFS ketika:

- Beban kerja terdiri dari proses-proses pendek. SJF memprioritaskan proses dengan waktu eksekusi singkat, sehingga rata-rata waktu tunggu dan waktu selesai menjadi lebih cepat.

- Tujuan sistem adalah efisiensi waktu (throughput tinggi). Karena proses singkat diselesaikan dulu, lebih banyak proses selesai dalam waktu tertentu.

- Tujuan sistem adalah efisiensi waktu (throughput tinggi). Karena proses singkat diselesaikan dulu, lebih banyak proses selesai dalam waktu tertentu.

- FCFS lebih unggul dari SJF ketika:

- Lingkungan bersifat interaktif atau waktu proses tidak bisa diprediksi. FCFS tidak perlu tahu waktu eksekusi, cukup melayani berdasarkan urutan kedatangan.

- Menuntut keadilan (fairness) antar proses. FCFS memastikan setiap proses dilayani secara adil, tanpa ada yang terus tertunda.

- Variasi waktu proses kecil (semua proses hampir sama panjang). Dalam kondisi ini, keunggulan SJF tidak terlalu terasa, dan FCFS lebih sederhana diterapkan.

---

## Kesimpulan
1.	FCFS (First Come First Served) menjadwalkan proses berdasarkan urutan kedatangan, sehingga sederhana namun dapat menyebabkan waktu tunggu tinggi bila ada proses berdurasi panjang yang datang lebih dulu (efek convoy).
2.	SJF (Shortest Job First) memberikan prioritas pada proses dengan waktu eksekusi terpendek, sehingga mampu menghasilkan rata-rata waktu tunggu dan waktu penyelesaian yang lebih rendah dibanding FCFS.


---

## D. Tugas & Quiz
### Tugas
1. Hitung *waiting time* dan *turnaround time* dari minimal 2 skenario FCFS dan SJF.  
2. Sajikan hasil perhitungan dalam tabel perbandingan (FCFS vs SJF).  
3. Analisis kelebihan dan kelemahan tiap algoritma.  
4. Simpan seluruh hasil dan analisis ke `laporan.md`.  

**JAWABAN**
1. FCFS (First Come First Served)

Kelebihan:

- Sederhana dan mudah diterapkan, karena proses dijalankan sesuai urutan kedatangan.

- Adil secara urutan waktu, setiap proses mendapatkan giliran tanpa prioritas khusus.

- Cocok untuk sistem batch di mana semua proses memiliki ukuran pekerjaan relatif sama.

Kelemahan:

- Waktu tunggu rata-rata bisa tinggi, terutama jika proses pertama memakan waktu lama (efek “convoy”).

- Tidak efisien untuk sistem interaktif, karena proses pendek bisa menunggu terlalu lama.

- Tidak mempertimbangkan lama waktu eksekusi, sehingga bisa menurunkan throughput sistem.

2. SJF (Shortest Job First)

Kelebihan:

- Meminimalkan waktu tunggu rata-rata — proses pendek dieksekusi lebih dulu, meningkatkan efisiensi.

- Meningkatkan throughput (jumlah proses selesai per satuan waktu).

- Cocok untuk sistem batch processing dengan waktu eksekusi yang diketahui sebelumnya.

Kelemahan:

- Sulit diterapkan secara praktis, karena waktu eksekusi proses sulit diprediksi.

- Tidak adil untuk proses panjang — bisa tertunda lama (starvation).

- Kurang cocok untuk sistem interaktif atau real-time, karena proses baru pendek bisa terus mendahului proses lama.

### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa perbedaan utama antara FCFS dan SJF?  
2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?  
3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?  

**JAWABAN** 
1.	Perbedaan utama antara FCFS dan SJF
FCFS (First Come First Served) menjadwalkan proses berdasarkan urutan kedatangan, sedangkan SJF (Shortest Job First) memilih proses dengan waktu eksekusi terpendek terlebih dahulu.
2.	Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum
Karena proses dengan waktu eksekusi yang lebih pendek dijalankan lebih dulu, sehingga proses-proses kecil tidak perlu menunggu proses besar selesai. Hal ini meminimalkan total waktu tunggu semua proses.
3.	Kelemahan SJF jika diterapkan pada sistem interaktif
SJF sulit diterapkan karena sistem tidak selalu mengetahui waktu eksekusi proses sebelumnya, dan proses yang lama bisa tertunda terus (starvation) jika selalu ada proses pendek yang datang lebih dulu.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  langkah perhitungan dan waktu rata-rata.
- Bagaimana cara Anda mengatasinya?  mencari dan memahami materi.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
