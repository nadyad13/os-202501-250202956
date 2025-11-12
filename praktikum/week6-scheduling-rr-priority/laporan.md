
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
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  

   | Proses |   CT   | Arivaal| TAT(ct-at) |	WT(TAT-bt) |
   | :----: | :----: | :----: | :--------: | :--------: |
   |   P1   |	 14   |    0   |	14-0=14   |	14-5=9     |
   |   P2   |   6 	|    1	|  6-1=5	    | 5-3=2      |
   |   P3	|   22   |	  2   |	22-2=20   |	20-8=12    |
   |   P4	|   20   |    3	|  20-3=17   |	17-6=11    |
Rata rata TAT:14
Rata rata WT :8,5

   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
     0    3    6    9   12   14   17   20   22
     ```
   - Catat sisa *burst time* tiap putaran.
   
   | waktu | Brust | sisa waktu|
   |:-----:|:-----:|:---------:|
   | 0-3   | 5-3=0 | P1 sisa 2 |
   | 3-6   | 3-3=0 | 2 selesai |
   | 6-9   | 8-3=5 | P3 sisa 5 |
   | 9-12  | 6-3=3 | P4 sisa 3 |
   | 12-14 | 2 < 3 | P1 selesai|
   | 14-17 | 5-3=0 | P3 sisa 2 |
   | 17-20 | 3-3=0 | P4 selesai|
   | 20-22 | 2 < 3 | P3 selesai|
   

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]o
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

|Proses|	BT | AT |PRIO|	ST |	WT(ST-AT)	|TAT(WT+BT)|
|:----:|:--:|:--:|:--:|:--:|:------------:|:--------:|
|  P1  |	 5 | 0  |  2 |	0  |	   0        | 	  5     |
|  P2  |	 3 | 1  |  1 |	5  | 	   4        |	  7     |
|  P4  |	 6 | 3  |  3 |	8  |	   5        |	  11    |
|  P3  |	 8 | 2  |  4 |	14 |     12       |    20    |

Rata rata WT  :5,25
Rata rata TAT :10,75

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  

Quantum 2
|Proses|	CT | AT |BT | TAT | WT |
|:----:|:--:|:--:|:-:|:---:|:--:|
|  P1  |	18 |  0 | 5 |	18 |  13|
|  P2  |	13 |	1 | 3 |	12 |	9 |
|  P3  |	24 |	2 | 8 |	22 |	14|
|  P4  |	22 |  3 | 6 |	19 |	13|
|Rata-rata  |    |   ||17.75|12.25|

Quantum 5
|Proses|	CT | AT |BT | TAT | WT |
|:----:|:--:|:--:|:-:|:---:|:--:|
|  P1  |	5  |  0 | 5 |	5  |  0 |
|  P2  |	8  |	1 | 3 |	7  |	4 |
|  P3  |	21 |	2 | 8 |	19 |	11|
|  P4  |	22 |  3 | 6 |	19 |	13|
|Rata-rata  |    |  || 12.5|  7 |




   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | 8,5 | 14 | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | 5,25 | 10,75 | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```
   
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
Perbandingan kinerja

Dalam dataset ini Priority (non-preemptive) menghasilkan avg waiting dan avg turnaround terendah. Itu karena urutan eksekusi berdasarkan prioritas (angka prioritas kecil = dieksekusi lebih dulu), sehingga proses penting (dengan prioritas lebih tinggi) segera terselesaikan.

Round Robin memberikan fairness tetapi rata-rata metrik lebih tinggi dibanding Priority pada contoh ini (karena RR membagi waktu merata tanpa memandang prioritas proses).

Pengaruh ukuran time quantum pada RR

Terlihat tren: q kecil → metrik rata-rata lebih besar, q besar → metrik rata-rata lebih kecil (dalam rentang q yang dicoba: 2 → 3 → 5).

Penjelasan:

Quantum kecil (q=2): banyak context switching → overhead teoretis lebih besar dan fragmentasi eksekusi → menambah waiting time keseluruhan.

Quantum besar (q=5): lebih sedikit switching, setiap proses menyelesaikan lebih banyak pekerjaan tiap giliran → mirip FCFS untuk proses yang tiba awal, sehingga rata-rata waiting turun.

Tapi peringatan: kalau quantum terlalu besar, RR kehilangan tujuan time-sharing (respon buruk terhadap proses interaktif) dan perilaku mendekati FCFS sehingga fairness terhadap proses singkat berkurang.

Fairness vs Efisiensi

RR: lebih adil (setiap proses mendapat giliran secara bergiliran), cocok sistem interaktif. Namun efisiensi (waktu tunggu rata-rata) bergantung kuat pada pemilihan q.

Priority: efisien untuk proses penting, tetapi potensi starvation pada proses berprioritas rendah (terutama pada varian preemptive). Pada implementasi non-preemptive contoh ini tidak mengalami starvation tetapi menunggu lebih lama.

Starvation & Mitigasi

Priority scheduling dapat menyebabkan starvation. Solusi umum: aging — secara bertahap menaikkan prioritas proses yang menunggu lama sehingga pada akhirnya juga mendapat CPU.

Catatan tentang dataset & generalisasi

Hasil ini bergantung pada arrival times, burst times, dan nilai prioritas pada contoh. Untuk dataset lain urutan relatif dan nilai rata-rata bisa berbeda.

Dalam praktek, pemilihan algoritma bergantung tujuan: throughput maksimum? latensi rendah untuk proses interaktif? fairness?

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
- Apa bagian yang paling menantang minggu ini?  kurang memahami perbedaan rr dan priority
- Bagaimana cara Anda mengatasinya?  bertanya pada teman yang sudah memahami tentang rr dan priority

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
