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

1. Ketika membaca klaim "platform X lebih memuaskan pengguna":
   - Pertanyaan pertama saya: Instrumen apa yang dipakai untuk mengukur kepuasan? Berapa responden dan apakah sampelnya representatif?
   - Data yang dibutuhkan untuk verifikasi: Kuesioner asli (SUS/CSUQ/UEQ), jumlah responden, karakteristik sampel, hasil uji statistik, dan apakah ada pengukuran performa teknis yang mendukung klaim tersebut.

2. Posisi paradigma:
   - Pendekatan: [✓] Positivis  [ ] Interpretivis  [ ] Design Science  [ ] Mixed
   - Alasan: Penelitian ini menggunakan pendekatan positivis karena mengukur kepuasan pengguna dan performa teknis secara objektif dan kuantitatif. Ada hipotesis yang bisa diuji (H0/Ha), metrik terukur (SUS score, response time), dan uji statistik yang hasilnya bisa diverifikasi oleh peneliti lain.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Ada asumsi bahwa mahasiswa menggunakan kedua platform dengan intensitas yang sama, padahal bisa jadi kelompok web lebih sering pakai Elena karena diwajibkan dosen.
   - Sumber bias potensial: Bias bisa muncul dari self-selection — mahasiswa yang memilih mobile mungkin lebih tech-savvy dan cenderung menilai lebih positif terhadap teknologi baru.
   - Langkah mitigasi: Catat frekuensi penggunaan sebelumnya sebagai variabel kontrol, gunakan stratified sampling, dan kontrol secara statistik menggunakan ANCOVA jika diperlukan.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Semua hasil uji statistik dilaporkan apa adanya, termasuk jika p-value > 0.05 (H0 tidak ditolak). Tidak akan memilih metrik setelah melihat data (p-hacking).
   - Batasan yang diakui sejak awal: Penelitian terbatas pada satu institusi (UNNES) dan satu mata kuliah (Sistem Operasi), sehingga generalisasi ke konteks lain memerlukan replikasi.
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: Analisis Perbandingan Efisiensi Penggunaan E-Learning Berbasis Website dan Aplikasi Mobile dalam Proses Pembelajaran
> Penulis (Tahun): Dalimunthe dkk. (2025)

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengumpulkan data persepsi dari 90 mahasiswa via survei kuesioner | Sampel dari 1 institusi saja — bisa tidak representatif untuk konteks lain |
| Data → Processing | Menseleksi 9 indikator persepsi untuk dibandingkan antar platform | Indikator dipilih peneliti — bisa ada bias dalam pemilihan dimensi yang diukur |
| Processing → Analysis | Uji Independent Samples t-test pada 9 indikator | Tidak ada pengukuran performa teknis objektif, hanya persepsi subyektif |
| Analysis → Inference | Menyimpulkan tidak ada perbedaan signifikan (Sig > 0.05) | Kesimpulan "setara" bisa misleading jika power test rendah (sampel kecil) |
| Inference → Knowledge | Memberikan rekomendasi pemilihan platform berdasarkan efisiensi | Rekomendasi terlalu luas karena tidak terikat konteks mata kuliah spesifik |

**Distorsi paling besar di tahap:** Data → Processing

**Dua distorsi spesifik yang teridentifikasi:**
1. Tidak ada pengukuran performa teknis objektif — hanya persepsi pengguna yang diukur, sehingga klaim "efisiensi" tidak didukung data teknis.
2. Konteks mata kuliah tidak spesifik — hasil tidak bisa digeneralisasi ke mata kuliah praktik-heavy seperti Sistem Operasi.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Data outlier tidak boleh langsung dihapus tanpa alasan yang jelas |
| Transparansi | Peneliti harus menampilkan hasil dengan dan tanpa outlier |
| Peer review | Reviewer akan mempertanyakan jika data dihapus tanpa penjelasan |

**Keputusan akhir dan justifikasi:**
> Kedua hasil harus tetap ditampilkan, baik dengan outlier maupun tanpa outlier. Jika outlier dihapus, harus ada alasan yang kuat seperti kesalahan pengukuran atau kondisi jaringan anomali yang terdokumentasi. Di penelitian saya sendiri, outlier response time yang disebabkan jaringan < 1Mbps di-exclude tapi tetap dilaporkan dengan alasan yang jelas.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Perbandingan platform web dan mobile untuk pembelajaran Mata Kuliah Sistem Operasi

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian | 5 | 2 | 1 |
| Jenis data | Data kuantitatif terukur: SUS score, CSUQ score, response time, loading speed, error rate | Interpretasi pengalaman pengguna secara kualitatif | Tidak ada artefak baru yang dibangun |
| Limitasi | Tidak bisa menangkap nuansa pengalaman subjektif secara mendalam | Sulit diverifikasi dan direplikasi, terlalu subjektif | Tidak relevan — penelitian tidak membangun sistem baru |

**Paradigma yang dipilih:** Positivis
**Alasan:** Penelitian ini mengukur kepuasan pengguna dan performa teknis secara kuantitatif dengan instrumen tervalidasi (SUS, CSUQ, Lighthouse). Ada hipotesis yang bisa diuji secara statistik, metrik yang terdefinisi numerik, dan prosedur yang bisa direplikasi. Ini sesuai ciri paradigma positivis: objektif, terukur, dan dapat diverifikasi.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelum mempelajari materi ini, saya cenderung langsung percaya klaim seperti "platform X lebih memuaskan pengguna" tanpa cek lebih lanjut.
>
> Setelah memahami rantai distorsi, sekarang saya akan tanya: instrumen apa yang dipakai? Berapa sampelnya? Apakah hanya mengukur persepsi atau ada data teknis juga? Apakah konteksnya spesifik atau terlalu general? Ini persis gap yang saya isi di penelitian sendiri — paper sebelumnya tidak mengintegrasikan kepuasan dan performa teknis sekaligus.
