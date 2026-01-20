
# Laporan Praktikum Minggu [13]
Topik: Docker Resource Limit

---

## Identitas
- **Nama**  : Nadya Pramudita
- **NIM**   : 250202956
- **Kelas** : 1IKRA

---

## Tujuan
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan **CPU** dan **memori**.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.

---

## Dasar Teori
1. Isolasi Sumber Daya dengan Cgroups
Docker memanfaatkan Control Groups (cgroups) pada sistem operasi Linux untuk membatasi dan mengatur penggunaan sumber daya seperti CPU dan memori pada setiap container agar tidak saling mengganggu.

2. Pembatasan CPU Container
Docker memungkinkan pengaturan batas CPU, baik dalam bentuk persentase, jumlah core, maupun CPU shares, sehingga container hanya menggunakan jatah CPU yang telah ditentukan dan menjaga performa sistem tetap stabil.

3. Pembatasan Memori Container
Dengan fitur memory limit, Docker dapat membatasi penggunaan RAM oleh container. Jika penggunaan melebihi batas, container dapat dihentikan (out of memory) untuk mencegah kerusakan sistem host.

4. Efisiensi dan Stabilitas Sistem
Resource limit membantu menjalankan banyak container secara bersamaan dengan lebih efisien, memastikan tidak ada satu container yang memonopoli CPU atau memori, serta meningkatkan keamanan dan keandalan aplikasi.

---

## Langkah Praktikum
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```

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
1. Buat Dockerfile sederhana dan program uji di folder `code/`.
2. Build image dan jalankan container **tanpa limit**.
3. Jalankan container dengan limit **CPU** dan **memori**.
4. Sajikan hasil pengamatan dalam tabel/uraian singkat di `laporan.md`.

### Quiz
1. Mengapa container perlu dibatasi CPU dan memori?
2. Apa perbedaan VM dan container dalam konteks isolasi resource?
3. Apa dampak limit memori terhadap aplikasi yang boros memori?

**Jawaban:**  
1. Pembatasan CPU dan memori diperlukan agar satu container tidak menggunakan sumber daya secara berlebihan. Tanpa batasan, container yang bermasalah atau boros resource dapat mengganggu kinerja container lain dan bahkan menyebabkan sistem host menjadi lambat atau tidak stabil.

2. Virtual Machine (VM) memiliki isolasi resource yang lebih kuat karena setiap VM menjalankan sistem operasi sendiri dengan alokasi CPU dan memori yang tetap. Sebaliknya, container berbagi kernel sistem operasi host sehingga isolasinya lebih ringan dan efisien, namun pengaturan resource dilakukan secara dinamis melalui mekanisme seperti cgroups.

3. Jika aplikasi dalam container menggunakan memori melebihi batas yang ditentukan, container dapat mengalami Out of Memory (OOM) dan dihentikan secara otomatis. Hal ini melindungi sistem host, tetapi aplikasi harus dirancang agar efisien dalam penggunaan memori atau mampu menangani restart.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
