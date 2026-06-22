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

Research Question: Apakah terdapat perbedaan signifikan antara platform web dan mobile dalam hal kepuasan pengguna dan performa teknis pada pembelajaran Mata Kuliah Sistem Operasi?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
| Platform (Web/Mobile) | IV | Jenis platform e-learning yang digunakan | Categorical: Web (Elena UNNES) vs Mobile (aplikasi mobile) | Nominal | - | Penugasan atau observasi pilihan platform mahasiswa | Berdasarkan penggunaan aktual mahasiswa (Alfita 2024) |
| Kepuasan Pengguna — SUS | DV | Tingkat usability dan kepuasan keseluruhan platform | SUS score (10 item) | Interval | 0–100 | Kuesioner SUS post-usage | Instrumen tervalidasi luas untuk usability, interpretasi standar (>68 = above average) |
| Kepuasan Pengguna — CSUQ | DV | Kepuasan multidimensi: system quality, info quality, interface quality | CSUQ score (19 item, 3 subdimensi) | Interval | 1–7 | Kuesioner CSUQ post-usage | Lebih terperinci dari SUS, cocok untuk konteks e-learning (Dalimunthe 2025) |
| Response Time | DV | Kecepatan platform merespons aksi pengguna | Waktu respons halaman/konten | Ratio | ms | Google Lighthouse / Chrome DevTools | Technical metric langsung terkait perceived performance (Ridho 2018) |
| Loading Speed | DV | Kecepatan total konten dimuat hingga bisa diakses | First Contentful Paint / Time to Interactive | Ratio | ms | Google Lighthouse Performance Score | Indikator performa teknis utama yang mempengaruhi user experience |
| Error Rate | DV | Persentase aksi yang menghasilkan kegagalan sistem | Jumlah error / total aksi × 100 | Ratio | % | Log sistem + observasi sesi terstruktur | Indikator reliabilitas platform selama penggunaan |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [✓] Setiap langkah terdokumentasi
  [✓] Tidak ada "lompatan logis"
  [✓] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah terdapat perbedaan signifikan antara platform web dan mobile dalam hal kepuasan pengguna dan performa teknis pada pembelajaran Mata Kuliah Sistem Operasi?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Platform (Web/Mobile) | IV | Jenis platform e-learning yang digunakan | Categorical: Web (Elena UNNES) vs Mobile (aplikasi mobile) | Nominal | - |
| Kepuasan Pengguna — SUS | DV | Tingkat usability dan kepuasan keseluruhan | SUS score (10 item) | Interval | 0–100 |
| Kepuasan Pengguna — CSUQ | DV | Kepuasan multidimensi: system quality, info quality, interface quality | CSUQ score (19 item, 3 subdimensi) | Interval | 1–7 |
| Response Time | DV (Technical) | Kecepatan platform merespons aksi pengguna | Waktu respons halaman/konten | Ratio | ms |
| Loading Speed | DV (Technical) | Kecepatan total konten dimuat hingga bisa diakses | First Contentful Paint (FCP) / Time to Interactive (TTI) | Ratio | ms |
| Error Rate | DV (Technical) | Persentase aksi yang menghasilkan kegagalan sistem | Jumlah error / total aksi x 100 | Ratio | % |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [✓] Tidak
> Rantai logis: Kepuasan pengguna adalah outcome dari pengalaman menggunakan platform → diukur via SUS (overall) dan CSUQ (per dimensi) yang keduanya tervalidasi. Performa teknis adalah karakteristik objektif platform → diukur via Lighthouse dan DevTools yang reproducible.

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | SUS dan CSUQ adalah instrumen standar tervalidasi untuk usability dan kepuasan sistem. Lighthouse adalah tool resmi Google untuk performa teknis. Semua metrik mewakili konsep yang diteliti dengan baik |
| Sensitive | 5 | SUS skala 0–100 dan CSUQ skala 1–7 cukup granular. Response time dan loading speed dalam ms sangat sensitif mendeteksi perbedaan performa. Ceiling effect minimal |
| Feasible | 5 | Kuesioner via Google Forms mudah didistribusikan. Lighthouse dan DevTools gratis dan built-in di Chrome. Tidak butuh infrastruktur tambahan |

**Apakah perlu secondary metric?** [✓] Ya / [ ] Tidak
> Performance Score dari Lighthouse (0–100) sebagai secondary metric untuk memberikan gambaran performa keseluruhan platform secara agregat, selain metrik individual response time dan loading speed.

**Contoh kasus ceiling effect untuk metrik ini:**
> Jika mahasiswa sudah sangat terbiasa dengan Elena UNNES (misal semester 4 ke atas), SUS score bisa tinggi bukan karena platformnya bagus tapi karena habituation. Ini sebabnya frekuensi penggunaan sebelumnya dicatat sebagai variabel kontrol.

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
