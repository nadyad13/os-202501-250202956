# LAPORAN PRAKTIKUM SISTEM OPERASI
## Minggu 11 – Simulasi dan Deteksi Deadlock

### Nama  : Nadya Pramudita  
### NIM   : 250202956  
### Prodi : Ilmu Komputer  

---

## A. Tujuan Praktikum
Praktikum ini bertujuan untuk memahami mekanisme deteksi deadlock dalam sistem operasi melalui simulasi program sederhana berbasis terminal serta menganalisis hasil deteksi secara logis dan sistematis.

---

## B. Dasar Teori
Deadlock adalah kondisi kebuntuan ketika dua atau lebih proses saling menunggu sumber daya yang sedang dipegang proses lain sehingga tidak ada proses yang dapat berjalan.

Empat kondisi deadlock:
1. Mutual Exclusion  
2. Hold and Wait  
3. No Preemption  
4. Circular Wait  

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

## D. Implementasi Program
Program dibuat menggunakan bahasa Python dan berjalan di terminal.  
Algoritma bekerja dengan membentuk relasi tunggu antar proses berdasarkan alokasi dan permintaan sumber daya untuk mendeteksi circular wait.

---

## E. Hasil Eksekusi
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

## F. Analisis
Deadlock terjadi karena seluruh kondisi deadlock terpenuhi, khususnya circular wait.  
Program berhasil mendeteksi proses-proses yang saling menunggu sumber daya secara melingkar.

---

## G. Kesimpulan
Simulasi deteksi deadlock berhasil menunjukkan bahwa pendekatan deteksi diperlukan untuk sistem yang tidak menerapkan pencegahan atau penghindaran deadlock.

---

## Quiz

### 1. Perbedaan pencegahan, penghindaran, dan deteksi deadlock
- Pencegahan: mencegah salah satu kondisi deadlock terjadi.
- Penghindaran: menghindari deadlock dengan analisis keadaan aman.
- Deteksi: membiarkan deadlock terjadi lalu mendeteksinya.

### 2. Mengapa deteksi deadlock diperlukan?
Karena tidak semua sistem dapat menerapkan pencegahan atau penghindaran akibat keterbatasan sumber daya dan fleksibilitas sistem.

### 3. Kelebihan dan kekurangan deteksi deadlock
**Kelebihan:** lebih fleksibel dan efisien penggunaan sumber daya.  
**Kekurangan:** deadlock sudah terjadi sebelum ditangani.

---

## Referensi
Silberschatz, A., Galvin, P., Gagne, G. *Operating System Concepts*.  
Tanenbaum, A. *Modern Operating Systems*.  
OSTEP – Deadlock Detection.
