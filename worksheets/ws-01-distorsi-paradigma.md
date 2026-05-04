# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah kebohongan sengaja. Validitas mendeteksi kesalahan yang tidak sengaja.

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| Internal Validity | Apakah hubungan benar-benar ada? | Variabel lain ikut berpengaruh |
| External Validity | Apakah hasil bisa berlaku umum? | Data terlalu sempit |
| Construct Validity | Apakah yang diukur memang benar? | Metrik tidak cocok dengan klaim |

### Paradigma Riset

Kuliah ini pakai **Positivis** untuk mengukur secara objektif, dan **Design Science Research** untuk membuat artefak sebagai bagian dari riset.

### Mode Berpikir Peneliti

Curious → Critical → Systematic

- Curious: tanya dan cari bukti
- Critical: cek apakah bukti kuat
- Systematic: ikuti proses yang jelas

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | buat sistem yang bekerja | buat pengetahuan yang benar |
| Pertanyaan | "Bagaimana dibuat?" | "Apakah klaim benar?" |
| Ukuran sukses | sistem berfungsi | hipotesis terjawab |
| Kegagalan | dihindari | dilaporkan juga |

### Istilah Penting

- Research Mindset: cari bukti dan jangan terima mentah-mentah
- Research Ethics: jujur, terbuka, dan bisa dipertanggungjawabkan
- HARKing: bikin hipotesis setelah lihat hasil
- Falsifiability: hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Risky Dimas Nugroho
Tanggal          : 12 April 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Menurut saya, yang pertama harus dipertanyakan adalah dataset apa yang digunakan dan apakah data tersebut seimbang atau tidak.
   - Data yang dibutuhkan untuk verifikasi: Menurut saya, dibutuhkan dataset asli, metode evaluasi, confusion matrix, serta perbandingan dengan metode lain.

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [✓] Interpretivis  [ ] Design Science  [ ] Mixed
   - Alasan: Menurut saya, pendekatan yang digunakan lebih ke interpretivis karena penelitian ini banyak menggunakan studi literatur dan interpretasi terhadap data yang sudah ada.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Menurut saya, ada asumsi bahwa cloud computing selalu lebih baik dibanding infrastruktur tradisional.
   - Sumber bias potensial: Menurut saya, bias bisa muncul dari pemilihan literatur yang hanya mendukung keunggulan cloud computing.
   - Langkah mitigasi: Menurut saya, perlu menggunakan sumber yang beragam dan juga menyertakan data empiris atau eksperimen langsung.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Menurut saya, semua data hasil penelitian baik yang mendukung maupun tidak mendukung hipotesis harus tetap ditampilkan.
   - Batasan yang diakui sejak awal: Menurut saya, keterbatasan penelitian seperti hanya menggunakan studi literatur harus dijelaskan sejak awal.
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: Analisis Perbandingan antara Teknologi Cloud Computing dan Infrastruktur Komputer Tradisional dalam Konteks Bisnis
> Penulis (Tahun):Adi Prasetya dkk (2024)

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengumpulkan data dari wawancara, survei, dan studi literatur | Data bisa tidak representatif karena hanya dari sumber tertentu |
| Data → Processing | Menyeleksi literatur yang relevan | Bisa terjadi bias seleksi karena hanya memilih sumber yang mendukung |
| Processing → Analysis | Menganalisis kelebihan dan kekurangan kedua teknologi | Analisis bisa subjektif karena tidak ada eksperimen langsung |
| Analysis → Inference | Menarik kesimpulan bahwa cloud lebih fleksibel | Bisa terjadi generalisasi berlebihan |
| Inference → Knowledge | Memberikan rekomendasi penggunaan teknologi | Kesimpulan terlalu umum dan tidak spesifik pada kondisi tertentu |

**Distorsi paling besar di tahap:** Data → Processing

**Dua distorsi spesifik yang teridentifikasi:**
1. Adanya bias dalam pemilihan literatur (cherry-picking).
2. Kurangnya data empiris karena hanya menggunakan studi literatur.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Data outlier tidak boleh langsung dihapus tanpa alasan yang jelas |
| Transparansi | Peneliti harus menampilkan hasil dengan dan tanpa outlier. |
| Peer review | Reviewer akan mempertanyakan jika data dihapus tanpa penjelasan |

**Keputusan akhir dan justifikasi:**
> Menurut saya, sebaiknya kedua hasil tetap ditampilkan, baik dengan outlier maupun tanpa outlier. Jika outlier dihapus, harus ada alasan yang kuat seperti kesalahan pengukuran. Jika tidak dijelaskan, maka termasuk manipulasi data dan melanggar etika penelitian.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Perbandingan cloud computing dan infrastruktur komputer tradisional dalam bisnis

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian | 3 | 4 | 2 |
| Jenis data | Berupa data sekunder dan hasil penelitian lain | berupa wawancara dan interpretasi | tidak ada artefak yang diuji |
| Limitasi | tidak ada eksperimen langsung | cenderung subjektif | tidak relevan dengan penelitian ini |

**Paradigma yang dipilih:** Interpretivis
**Alasan:** Penelitian ini lebih fokus pada pemahaman dan interpretasi dari berbagai sumber literatur dibandingkan dengan eksperimen langsung atau pembangunan sistem baru.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**> Menurut saya, sebelum mempelajari materi ini, saya cenderung langsung percaya dengan klaim seperti “akurasi 95%” tanpa mempertanyakan lebih dalam.
>
> Setelah memahami adanya tahapan distorsi dalam penelitian, menurut saya penting untuk lebih kritis. Sekarang saya akan mempertanyakan hal-hal seperti dataset yang digunakan, metode pengujian, kemungkinan bias, dan apakah hasilnya bisa digeneralisasi atau tidak.

