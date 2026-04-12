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
   - Pertanyaan pertama saya: Akurat untuk data apa dan apakah sudah diuji pada data baru?
   - Data yang dibutuhkan untuk verifikasi: dataset lengkap, metode evaluasi, dan catatan apakah ada data yang dibuang.

2. Posisi paradigma:
   - Pendekatan: [x] Positivis  [ ] Interpretivis  [ ] Design Science  [ ] Mixed
   - Alasan: klaim akurat bisa diuji lewat angka dan data.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: hasil berlaku untuk semua kondisi.
   - Sumber bias potensial: pilih data yang sesuai, buang hasil yang jelek.
   - Langkah mitigasi: cek ulang data, laporkan prosesnya, bandingkan dengan studi lain.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: hasil asli, outlier, dan data tes.
   - Batasan yang diakui sejak awal: fokus pada konteks dan data yang digunakan.
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: Paradigma Kritis dalam Penelitian Sistem Informasi di Indonesia: Perlukah?
> Penulis (Tahun): Agung Darono (2013)

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Kumpulkan studi tentang paradigma riset SI di Indonesia, dengan fokus bahwa artefak SI juga bagian dari interaksi sosial dan politik | Pilih literatur yang hanya mendukung kritik terhadap pendekatan positivis |
| Data → Processing | Mengklasifikasi argumen, tema, dan bukti dari berbagai jurnal sistem informasi | Proses seleksi literatur dapat menyingkirkan penelitian yang bertentangan atau relevansi konteks lokal |
| Processing → Analysis | Bandingkan cara tiap paradigma melihat artefak SI dan kontribusi sosialnya | Penulis bisa menekankan bukti yang mendukung paradigma kritis lebih dari bukti lain |
| Analysis → Inference | Simpulkan bahwa paradigma kritis perlu dipertimbangkan dalam penelitian SI Indonesia | Kesimpulan bisa terlalu umum jika hanya berdasar beberapa studi atau area tertentu |
| Inference → Knowledge | Klaim bahwa paradigma kritis relevan untuk riset SI Indonesia | Tidak semua topik SI cocok dengan pendekatan ini |

**Distorsi paling besar di tahap:** Inference → Knowledge

**Dua distorsi spesifik yang teridentifikasi:**
1. Pilih literatur yang mendukung paradigma kritis saja.
2. Tarik kesimpulan bahwa paradigma kritis wajib dipakai tanpa bukti empiris lengkap.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Tulis hasil dengan dan tanpa outlier, lalu jelaskan alasan penghapusan. |
| Transparansi | Jelaskan proses pembersihan data secara jelas. |
| Peer review | Reviewer bisa menilai apakah penghapusan wajar atau hanya untuk memperbaiki angka. |

**Keputusan akhir dan justifikasi:**
> Hapus outlier hanya jika jelas salah data atau ada alasan metode yang kuat. Jika tidak, laporkan kedua hasilnya.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Pengaruh Design Science Research pada kualitas artefak sistem informasi di Indonesia.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian | 3 | 2 | 5 |
| Jenis data | angka kinerja artefak | pengalaman perancang | artefak dan uji lapangan |
| Limitasi | kurang lihat konteks sosial | sulit digeneralisasi | sulit nilai kontribusi secara baku |

**Paradigma yang dipilih:** Design Science Research
**Alasan:** Topiknya tentang bikin dan uji artefak. DSR paling pas, sementara positivis bisa dipakai untuk mengukur hasil.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**> Sebelum membaca materi ini, klaim "95% akurat" cenderung diterima begitu saja sebagai bukti bahwa metode tersebut memang unggul, tanpa mempertanyakan konteks atau proses di baliknya.
>
> Setelah memahami rantai distorsi dalam Research Trust Model, pertanyaan yang sekarang akan diajukan antara lain: Akurat pada dataset seperti apa dan seberapa representatif dataset itu terhadap kondisi nyata? Apakah ada data yang dibuang sebelum angka ini dihitung? Apakah hipotesis dirumuskan sebelum atau sesudah melihat data (HARKing)? Metrik apa yang digunakan dan apakah metrik itu benar-benar mengukur hal yang diklaim (construct validity)? Apakah hasil ini sudah direplikasi oleh peneliti independen?