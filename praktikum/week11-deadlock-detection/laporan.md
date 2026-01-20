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

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```

---

## Kode / Perintah
```
import csv

def read_dataset(filename):
    processes = []
    allocation = {}
    request = {}

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = row['Process']
            processes.append(p)
            allocation[p] = row['Allocation']
            request[p] = row['Request']

    return processes, allocation, request


def detect_deadlock(processes, allocation, request):
    graph = {}

    for p in processes:
        if request[p] != "-" and request[p] != "":
            graph[p] = request[p]
        else:
            graph[p] = None

    deadlock_processes = []

    for p in processes:
        visited = set()
        current = p

        while current and current not in visited:
            visited.add(current)
            req = graph.get(current)

            if req:
                holder = None
                for proc, alloc in allocation.items():
                    if alloc == req:
                        holder = proc
                        break
                current = holder
            else:
                current = None

        if current in visited:
            deadlock_processes.extend(list(visited))
```

---

## Hasil Eksekusi
Berdasarkan hasil eksekusi program:
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/f6c287f4-f7f0-4770-8f78-54cb3742ed20" />

---

## Analisis
1. Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).
2. Jelaskan mengapa deadlock terjadi atau tidak terjadi.
3. Kaitkan hasil dengan teori deadlock (empat kondisi).

1.Penyajian Hasil Deteksi dalam Bentuk Tabel

Program membaca file dataset_deadlock.csv, lalu menandai setiap proses apakah DEADLOCK atau AMAN.
Hasil akhirnya secara konsep dapat disajikan dalam tabel berikut:
| No | Proses | Status          |
| -- | ------ | --------------- |
| 1  | P1     | DEADLOCK / AMAN |
| 2  | P2     | DEADLOCK / AMAN |
| 3  | P3     | DEADLOCK / AMAN |
| 4  | P4     | DEADLOCK / AMAN |

2.Penjelasan Mengapa Deadlock Terjadi / Tidak Terjadi
Proses yang Mengalami Deadlock
Deadlock terjadi ketika:
- Suatu proses meminta resource yang sedang dialokasikan ke proses lain
- Proses lain tersebut juga menunggu resource yang dipegang proses sebelumnya
- Terbentuk siklus tunggu (cycle)

Contoh alur:
P1 menunggu R2 → R2 dipegang P2
P2 menunggu R1 → R1 dipegang P1

3.Kaitan dengan Teori Deadlock (Empat Kondisi Coffman)

Deadlock hanya terjadi jika keempat kondisi berikut terpenuhi secara bersamaan:

1. Mutual Exclusion

- Resource hanya bisa digunakan satu proses dalam satu waktu
- Terlihat dari satu resource hanya dialokasikan ke satu proses.

2. Hold and Wait

- Proses menahan resource sambil menunggu resource lain
- Di dataset: proses memiliki Allocation dan Request sekaligus.

3. No Preemption

- Resource tidak bisa diambil paksa
- Program tidak memiliki mekanisme pelepasan paksa resource.

4. Circular Wait

- Terjadi siklus menunggu antar proses
- Inilah yang dideteksi oleh algoritma pada fungsi detect_deadlock().

---

## Kesimpulan
1. Program simulasi yang dibuat berhasil mendeteksi kondisi deadlock dengan mengidentifikasi adanya circular wait antar proses berdasarkan alokasi dan permintaan sumber daya.

2. Pendekatan deteksi deadlock memungkinkan sistem tetap berjalan secara fleksibel tanpa pembatasan ketat, namun memerlukan mekanisme pemulihan yang tepat agar tidak mengganggu proses lain.

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

## Referensi
Silberschatz, A., Galvin, P., Gagne, G. *Operating System Concepts*.  
Tanenbaum, A. *Modern Operating Systems*.  
OSTEP – Deadlock Detection.
