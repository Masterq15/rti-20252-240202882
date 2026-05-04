# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: Apakah platform web (Elena UNNES) menghasilkan kepuasan pengguna yang signifikan berbeda dengan platform mobile (YouTube + dedicated app) pada mata kuliah Sistem Operasi?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
| Platform/Jenis Media | IV | Pendekatan penyampaian pembelajaran | Categorical: Web (Elena) vs Mobile (YouTube) | Nominal | - | Survey response pada baseline selection | Berdasarkan penggunaan aktual mahasiswa (Paper 1) |
| Learning Satisfaction | DV | Kepuasan pengguna terhadap pengalaman belajar | UEQ score (6 dimensi) | Interval | 1-7 | Kuesioner UEQ post-usage | Standard tool untuk UX measurement (Papers 1,5) |
| Ease of Use | DV | Kemudahan dalam menggunakan platform | SUS score | Interval | 0-100 | Kuesioner SUS post-usage | Validated usability scale (Paper 1) |
| Response Time | DV | Kecepatan sistem merespons tindakan pengguna | Waktu loading halaman/API | Ratio | ms | Chrome DevTools Network tab | Technical metric untuk performance (Paper 4) |
| Memory Usage | DV | Efisiensi penggunaan memory system | Ukuran memory runtime | Ratio | kB | Android Studio Profiler / Chrome DevTools | Critical untuk mobile platform limitation (Paper 4) |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [✓] Setiap langkah terdokumentasi
  [✓] Tidak ada "lompatan logis"
  [✓] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah platform web (Elena UNNES) menghasilkan kepuasan pengguna yang signifikan berbeda dengan platform mobile (YouTube + dedicated app) pada mata kuliah Sistem Operasi?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Platform/Jenis Media | IV | Pendekatan penyampaian pembelajaran | Categorical: Web (Elena) vs Mobile (YouTube) | Nominal | - |
| Learning Satisfaction | DV | Kepuasan pengguna terhadap pengalaman belajar | UEQ score (Attractiveness, Perspicuity, Efficiency, Dependability, Stimulation, Novelty) | Interval | 1-7 skala |
| Ease of Use | DV | Kemudahan dalam menggunakan platform | SUS (System Usability Scale) score | Interval | 0-100 |
| Response Time | DV (Technical) | Kecepatan sistem merespons tindakan pengguna | Waktu loading halaman / API response | Ratio | milliseconds (ms) |
| Memory Usage | DV (Technical) | Efisiensi penggunaan memory system | Ukuran memory yang dikonsumsi saat runtime | Ratio | kilobytes (kB) |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [✓] Tidak
> Jika ya, di mana? Rantai logis: Learning Satisfaction adalah dampak langsung dari pengalaman pengguna → diukur via UEQ yang valid. Technical metrics adalah karakteristik platform yang mempengaruhi satisfaction."

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | UEQ adalah instrumen standar untuk user experience evaluation, mencakup 6 dimensi komprehensif. Sudah terbukti valid di e-learning (Paper 5) |
| Sensitive | 4 | UEQ menggunakan skala 1-7 cukup granular. Technical metrics sangat sensitif terhadap perbedaan platform. Kemungkinan ceiling effect minimal |
| Feasible | 5 | Kuesioner online efisien. Technical metrics via Chrome DevTools (web) dan Android Profiler (mobile) tanpa cost |

**Apakah perlu secondary metric?** [✓] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? Learning Outcome (score praktikum) sebagai secondary metric untuk memvalidasi apakah kepuasan berkorelasi dengan pencapaian pembelajaran aktual

**Contoh kasus ceiling effect untuk metrik ini:**
> Jika Elena UNNES sudah sangat familiar bagi mahasiswa, skor satisfaction bisa tinggi bahkan meski ada improvement → perlu perbandingan dengan platform baru untuk mendeteksi perbedaan"

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | *Apakah semua data point terkumpul?* | Semua 50 responden diharapkan submit kuesioner, tapi kemungkinan 10-15% dropout | Pengingat berkala via email/WhatsApp, insentif partisipasi, follow-up untuk non-responden |
| Consistency | *Apakah ada kontradiksi internal?* | Kemungkinan ada responden dengan rating satisfaction tinggi tapi ease of use rendah | Review data mentah, cek outliers, wawancara follow-up untuk cases tidak konsisten |
| Validity | *Apakah benar-benar mengukur yang dimaksud?* | UEQ sudah valid instrument, tapi perlu memastikan pemahaman responden | Pilot test dengan 5-10 mahasiswa, revisi pertanyaan yang membingungkan |
| Representativeness | *Apakah sampel mewakili populasi target?* | 50 dari ~200 mahasiswa (25%) yang ambil OS → representative jika random sampling | Random sampling, stratifikasi berdasarkan semester, pastikan web vs mobile user balanced |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> **P-hacking (cherry-picking metrik)**: Lihat data hasil → pilih hanya metrik yang "significant". Contoh buruk: Paper 3 melakukan t-test pada 9 indikator, jika semua non-significant tapi kemudian "post-hoc" lihat sub-grup tertentu (misal: hanya pengguna usia < 20) dan report "dalam sub-grup ini perbedaan signifikan" TANPA pre-register → p-hacking. Probability menemukan spurious significant result by chance naik drastis dengan multiple tests.
>
> **Eksplorasi data seyogyanya**: (1) Pre-register PRIMARY metric SEBELUM collect data. (2) Setelah eksperimen, boleh explore SECONDARY metrics dan label "exploratory". (3) Adjust p-value dengan Bonferroni: α=0.05/9 untuk 9 tests. (4) Jelaskan kenapa explore metrik tambahan. Paper 4 (PWA vs Mobile Web) do this well: report semua metrics (response time, memory, storage) dengan clear hypothesis, tidak cherry-pick.
