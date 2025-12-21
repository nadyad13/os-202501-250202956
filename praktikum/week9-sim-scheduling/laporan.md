
# Laporan Praktikum Minggu [9]
Topik: simulasi scheduling 

---

## Identitas
- **Nama**  : Nadya Pramudita
- **NIM**   : 250202956
- **Kelas** : 1IKRA

---

## Tujuan
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.  
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.  
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.  
4. Menjelaskan hasil simulasi secara tertulis.  
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
- Manajemen Proses Sistem Operasi
Scheduling merupakan bagian dari manajemen proses yang bertujuan mengatur urutan eksekusi proses pada CPU agar sumber daya digunakan secara optimal.

- Model Waktu dan Status Proses
Simulasi scheduling didasarkan pada model waktu (arrival time, burst time) serta perubahan status proses (ready, running, waiting, terminated).

- Algoritma Penjadwalan CPU
Berbagai algoritma seperti FCFS, SJF, Priority, dan Round Robin memiliki aturan berbeda yang memengaruhi performa sistem dan perlu diuji melalui simulasi.

- Parameter Kinerja Sistem
Simulasi digunakan untuk menghitung dan membandingkan metrik kinerja seperti waiting time, turnaround time, response time, dan throughput.

- Pendekatan Eksperimental
Simulasi memungkinkan pengujian perilaku algoritma dalam berbagai skenario tanpa harus mengimplementasikannya langsung pada sistem nyata.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**

   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```
---

## Hasil Eksekusi
<img width="1365" height="767" alt="Screenshot 2025-12-21 191751" src="https://github.com/user-attachments/assets/a463ad05-15c2-4aab-95c6-e2ec874a03c8" />

<img width="1365" height="767" alt="Screenshot 2025-12-21 191939" src="https://github.com/user-attachments/assets/6e51169b-5217-4e37-a111-8613acb0f181" />


---s

## Analisis

1. Alur Program FCFS Scheduling

Program ini mensimulasikan algoritma penjadwalan FCFS (First Come First Served), yaitu proses dieksekusi berdasarkan urutan kedatangan.

a. Inisialisasi Data

```processes``` → daftar nama proses (P1–P4)

```arrival_time ```→ waktu kedatangan setiap proses

```burst_time``` → lama eksekusi CPU tiap proses

n → jumlah proses

Array ```start_time, finish_time, waiting_time, dan turnaround_time``` disiapkan untuk menyimpan hasil perhitungan.

b. Proses Simulasi FCFS

Perulangan for i in range(n) mengeksekusi proses satu per satu:

Menentukan Start Time

Proses pertama (i == 0) langsung dimulai saat waktu kedatangannya.

Proses berikutnya dimulai saat:

CPU sudah selesai menjalankan proses sebelumnya atau

proses sudah tiba
→ menggunakan ```max(finish_time[i-1], arrival_time[i]).```
Menghitung Finish Time
```
finish_time = start_time + burst_time
```

Menghitung Waiting Time
```
waiting_time = start_time − arrival_time
```

Menghitung Turnaround Time
```
turnaround_time = finish_time − arrival_time
```
c. Perhitungan Rata-rata

Rata-rata Waiting Time

Rata-rata Turnaround Time
Dihitung dengan menjumlahkan seluruh nilai lalu dibagi jumlah proses.

d. Menampilkan Output

Program mencetak tabel berisi:

Proses

```Arrival Time

Burst Time

Start Time

Finish Time

Waiting Time 
```

Turnaround Time
serta nilai rata-ratanya.

  - Bandingkan hasil simulasi dengan perhitungan manual. 

2. Perbandingan Simulasi dengan Perhitungan Manual
a. Hasil Perhitungan Manual

| Proses | Arrival | Burst | Start | Finish | Waiting | Turnaround |
| ------ | ------- | ----- | ----- | ------ | ------- | ---------- |
| P1     | 0       | 6     | 0     | 6      | 0       | 6          |
| P2     | 1       | 8     | 6     | 14     | 5       | 13         |
| P3     | 2       | 7     | 14    | 21     | 12      | 19         |
| P4     | 3       | 3     | 21    | 24     | 18      | 21         |


Rata-rata Waiting Time
= (0 + 5 + 12 + 18) / 4 = 8.75

Rata-rata Turnaround Time
= (6 + 13 + 19 + 21) / 4 = 14.75

b. Hasil Simulasi Program

Output program menghasilkan nilai yang sama persis dengan perhitungan manual.

c. Kesimpulan Perbandingan

Simulasi FCFS pada program valid dan akurat

Program berhasil merepresentasikan konsep FCFS secara matematis

Simulasi mempermudah perhitungan tanpa risiko kesalahan hitung manual
 
   - Jelaskan kelebihan dan keterbatasan simulasi.

a. Kelebihan Simulasi

Cepat dan efisien untuk jumlah proses yang besar

Mengurangi kesalahan manusia dalam perhitungan

Mudah dimodifikasi untuk algoritma lain (SJF, Priority, Round Robin)

Membantu visualisasi dan analisis performa CPU

Cocok untuk eksperimen dan pembelajaran

b. Keterbatasan Simulasi

Tidak merepresentasikan kondisi sistem nyata sepenuhnya
(misalnya I/O, interupsi, context switching)

Bergantung pada asumsi yang disederhanakan

Tidak mencerminkan overhead sistem operasi

Hanya menunjukkan hasil numerik, bukan kondisi real-time sebenarnya



---

## Kesimpulan
1. Praktikum ini berhasil mengimplementasikan simulasi algoritma penjadwalan First Come First Served (FCFS) untuk menghitung waiting time dan turnaround time berdasarkan data arrival time dan burst time.

2. Hasil simulasi menunjukkan kesesuaian dengan perhitungan manual, sehingga membuktikan bahwa program yang dibuat valid dan mampu merepresentasikan konsep penjadwalan CPU secara benar.

3. Simulasi scheduling mempermudah analisis kinerja algoritma penjadwalan, terutama untuk jumlah proses yang besar, meskipun masih memiliki keterbatasan dalam merepresentasikan kondisi sistem operasi secara nyata.

---

## Tugas & Quiz
### Tugas
1. Buat program simulasi FCFS atau SJF.  
2. Jalankan program dengan dataset uji.  
3. Sajikan output dalam tabel atau grafik.  
4. Tulis laporan praktikum pada `laporan.md`.


### Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?  
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?  
3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.

**Jawaban:**  
1. Simulasi diperlukan karena algoritma scheduling bekerja dalam lingkungan yang dinamis dan kompleks. Melalui simulasi, kita dapat meniru kondisi nyata sistem (misalnya waktu kedatangan proses, burst time, prioritas, dan context switching) tanpa harus menjalankannya pada sistem operasi sebenarnya. Simulasi juga memungkinkan pengujian berbagai skenario, membandingkan kinerja beberapa algoritma (seperti waiting time, turnaround time, dan throughput), serta mengamati dampak perubahan parameter secara aman dan efisien.

2. Pada dataset kecil, hasil simulasi dan perhitungan manual biasanya sama. Namun, ketika dataset besar:

- Perhitungan manual menjadi tidak praktis, rawan kesalahan, dan memakan waktu lama.

- Simulasi dapat memproses data dalam jumlah besar dengan cepat dan konsisten, serta menghasilkan statistik yang lebih lengkap dan akurat.

Perbedaannya terletak pada efisiensi dan keandalan, bukan pada konsep perhitungannya. Simulasi lebih unggul untuk skala besar dan analisis mendalam.

3. Algoritma yang paling mudah diimplementasikan adalah First Come First Served (FCFS). Alasannya:

- Logikanya sederhana: proses dieksekusi sesuai urutan kedatangan.

- Tidak memerlukan perhitungan prioritas atau pembagian time quantum.

- Struktur datanya cukup menggunakan antrian (queue) biasa.

Sebaliknya, algoritma seperti Shortest Job First (SJF), Priority Scheduling, atau Round Robin lebih kompleks karena memerlukan perhitungan tambahan, pengurutan proses, atau mekanisme time slicing.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
