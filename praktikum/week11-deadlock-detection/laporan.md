
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

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
