# LAPORAN PRAKTIKUM SISTEM OPERASI
## Minggu 11 – Simulasi dan Deteksi Deadlock

# Laporan Praktikum Minggu [11]
Topik: deadlock detection

---

## Identitas
- **Nama**  : Nadya Pramudita
- **NIM**   : 250202956
- **Kelas** : 1IKRA

---

## Tujuan
1. Membuat program sederhana untuk mendeteksi deadlock.  
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.  
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.  
4. Memberikan interpretasi hasil uji secara logis dan sistematis.  
5. Menyusun laporan praktikum sesuai format yang ditentukan.

---

## Dasar Teori
1. Konsep Deadlock
Deadlock adalah kondisi ketika beberapa proses saling menunggu sumber daya yang sedang digunakan proses lain sehingga sistem tidak dapat berjalan.

2. Syarat Terjadinya Deadlock
Deadlock terjadi jika empat kondisi terpenuhi bersamaan, yaitu mutual exclusion, hold and wait, no preemption, dan circular wait.

3. Resource Allocation Graph (RAG)
RAG digunakan untuk memodelkan hubungan proses dan sumber daya, di mana siklus pada graf menunjukkan kemungkinan deadlock.

4. Algoritma Deadlock Detection
Algoritma ini memeriksa status alokasi dan permintaan sumber daya untuk menentukan apakah terdapat proses yang terjebak deadlock.

5. Tujuan Deadlock Detection
Deadlock detection bertujuan mendeteksi deadlock agar sistem dapat melakukan pemulihan dan mencegah berhentinya proses.

---

## C. Dataset Uji
Dataset berisi informasi alokasi dan permintaan sumber daya oleh proses.

| Proses | Alokasi | Permintaan |
|------|--------|-----------|
| P1 | R1 | R2 |
| P2 | R2 | R3 |
| P3 | R3 | R1 |
| P4 | R4 | - |

---

## Implementasi Program
Program dibuat menggunakan bahasa Python dan berjalan di terminal.  
Algoritma bekerja dengan membentuk relasi tunggu antar proses berdasarkan alokasi dan permintaan sumber daya untuk mendeteksi circular wait.

---

## Hasil Eksekusi
Berdasarkan hasil eksekusi program:
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/f6c287f4-f7f0-4770-8f78-54cb3742ed20" />


| Proses | Status |
|------|--------|
| P1 | Deadlock |
| P2 | Deadlock |
| P3 | Deadlock |
| P4 | Aman |

Proses P1, P2, dan P3 mengalami deadlock karena membentuk siklus permintaan sumber daya, sedangkan P4 tidak terlibat karena tidak meminta sumber daya lain.

---

## Analisis
Deadlock terjadi karena seluruh kondisi deadlock terpenuhi, khususnya circular wait.  
Program berhasil mendeteksi proses-proses yang saling menunggu sumber daya secara melingkar.

---

## Kesimpulan
Simulasi deteksi deadlock berhasil menunjukkan bahwa pendekatan deteksi diperlukan untuk sistem yang tidak menerapkan pencegahan atau penghindaran deadlock.

---


## E. Tugas & Quiz
### Tugas
1. Buat program simulasi deteksi deadlock.  
2. Jalankan program dengan dataset uji.  
3. Sajikan hasil analisis dalam tabel dan narasi.  
4. Tulis laporan praktikum pada `laporan.md`.

### Quiz
1. Apa perbedaan antara *deadlock prevention*, *avoidance*, dan *detection*?  
2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?  
3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?

**Jawaban:**  
1. Perbedaan deadlock prevention, avoidance, dan detection

   Deadlock prevention mencegah deadlock dengan menghilangkan satu atau lebih syarat deadlock sejak awal.

   Deadlock avoidance menghindari deadlock dengan mengatur alokasi sumber daya agar sistem selalu berada pada keadaan aman.

   Deadlock detection membiarkan deadlock terjadi, lalu mendeteksinya dan melakukan pemulihan.
   
2. Alasan deteksi deadlock tetap diperlukan

   Deteksi deadlock diperlukan karena pencegahan dan penghindaran deadlock sering membatasi kinerja sistem. Dengan deteksi, sistem dapat berjalan lebih fleksibel dan efisien meskipun berisiko deadlock.

3. Kelebihan dan kekurangan deteksi deadlock

- Kelebihan:

   1. Pemanfaatan sumber daya lebih optimal

   2. Lebih fleksibel untuk sistem kompleks

- Kekurangan:

   1. Membutuhkan overhead untuk proses deteksi

   2. Memerlukan mekanisme pemulihan yang dapat berdampak pada proses lain
=======
## Quiz

1. Perbedaan deadlock prevention, avoidance, dan detection

   Deadlock prevention mencegah deadlock dengan menghilangkan satu atau lebih syarat deadlock sejak awal.

   Deadlock avoidance menghindari deadlock dengan mengatur alokasi sumber daya agar sistem selalu berada pada keadaan aman.

   Deadlock detection membiarkan deadlock terjadi, lalu mendeteksinya dan melakukan pemulihan.
   
2. Alasan deteksi deadlock tetap diperlukan

   Deteksi deadlock diperlukan karena pencegahan dan penghindaran deadlock sering membatasi kinerja sistem. Dengan deteksi, sistem dapat berjalan lebih fleksibel dan efisien meskipun berisiko deadlock.

3. Kelebihan dan kekurangan deteksi deadlock

- Kelebihan:

   1. Pemanfaatan sumber daya lebih optimal

   2. Lebih fleksibel untuk sistem kompleks

- Kekurangan:

   1. Membutuhkan overhead untuk proses deteksi

   2. Memerlukan mekanisme pemulihan yang dapat berdampak pada proses lain
---

## Referensi
Silberschatz, A., Galvin, P., Gagne, G. *Operating System Concepts*.  
Tanenbaum, A. *Modern Operating Systems*.  
OSTEP – Deadlock Detection.
