# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Method Gap + Context Gap: Belum ada studi yang mengintegrasikan pengukuran kepuasan pengguna (SUS, CSUQ) + performa teknis (response time, loading speed, error rate) secara bersamaan untuk platform web vs mobile pada pembelajaran Mata Kuliah Sistem Operasi.

Research Question:
  Tipe         : [✓] Comparison  [ ] Improvement  [ ] Exploratory
  Formulasi    : Apakah terdapat perbedaan signifikan antara platform web (Elena UNNES) dan platform mobile dalam hal kepuasan pengguna dan performa teknis pada pembelajaran Mata Kuliah Sistem Operasi?
  Variabel IV  : Jenis platform (Web/Elena UNNES vs Mobile/aplikasi mobile)
  Variabel DV  : Kepuasan Pengguna (SUS score, CSUQ score), Performa Teknis (response time ms, loading speed ms, error rate %)
  Metrik       : SUS score (0–100), CSUQ score (1–7, 3 subdimensi), Response Time (ms), Loading Speed/FCP (ms), Error Rate (%)
  Dataset      : Minimal 30 mahasiswa per kelompok (60 total), Mata Kuliah Sistem Operasi semester berjalan
  Baseline     : Elena UNNES (web, LMS-based) sebagai platform yang sudah established dan aktif digunakan

Quality Check RQ:
  [✓] Variabel spesifik
  [✓] Metrik jelas
  [✓] Baseline ada
  [✓] Konteks disebutkan
  [✓] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Integrated comparison technical + pedagogical metrics untuk mata kuliah praktik-heavy
  Jenis kontribusi        : [✓] Comparison  [ ] Improvement  [ ] Novel approach
  Gap yang diisi          : Method Gap + Context Gap: Belum ada integrated methodology untuk web vs mobile di pembelajaran praktik

Hypothesis Pair:
  H₀ : Tidak ada perbedaan signifikan dalam kepuasan pengguna dan efektivitas pembelajaran antara platform web dan mobile
  H₁ : Ada perbedaan signifikan dalam kepuasan pengguna dan efektivitas pembelajaran antara platform web dan mobile
  Threshold              : α = 0.05; p-value < 0.05 maka H₀ ditolak
  Justifikasi threshold  : α = 0.05 adalah standar dalam penelitian sosial dan teknologi pendidikan, memberikan confidence level 95%
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Method Gap + Context Gap: Belum ada integrated methodology yang menggabungkan technical metrics (response time, memory, storage) + pedagogical effectiveness (learning satisfaction, information retention) untuk mata kuliah praktik-heavy seperti Sistem Operasi di platform web vs mobile.

**RQ versi pertama (tulis bebas):**
> Platform mana (web vs mobile) yang lebih efektif untuk pembelajaran Sistem Operasi jika diukur dari segi teknis dan pedagogis?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | Ya | Web platform (Elena UNNES) vs Mobile applications (YouTube/dedicated app) |
| Metrik terukur | Ya | Technical: response time, memory usage, storage; Pedagogical: learning satisfaction (UEQ score), perceived ease of learning |
| Baseline | Ya | Elena UNNES (web, LMS-based) sebagai baseline platform yang sudah established |
| Dataset/konteks | Ya | Mahasiswa Sistem Informasi, mata kuliah Sistem Operasi (praktik-heavy), institusi pendidikan |

**Tipe RQ:** [✓] Comparison / [ ] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah platform web (Elena UNNES) menghasilkan kepuasan pengguna dan efektivitas pembelajaran yang signifikan berbeda dengan platform mobile (YouTube + dedicated app) pada mata kuliah Sistem Operasi, ditinjau dari metrik teknis (response time, memory usage) dan metrik pedagogis (learning satisfaction, ease of use)?"

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Tidak ada perbedaan signifikan antara kepuasan pengguna dan performa teknis platform web (Elena UNNES) dan platform mobile pada pembelajaran Mata Kuliah Sistem Operasi |
| H₁ | Ada perbedaan signifikan pada salah satu atau lebih dimensi kepuasan pengguna dan/atau performa teknis antara platform web dan mobile |
| Metrik | Kepuasan: SUS score (0–100), CSUQ score (1–7, 3 subdimensi); Performa teknis: Response Time (ms), Loading Speed (ms), Error Rate (%) |
| Threshold | α = 0.05; p-value < 0.05 maka H₀ ditolak |
| Justifikasi threshold | α = 0.05 adalah standar dalam penelitian sosial dan teknologi pendidikan, memberikan confidence level 95% — konsisten dengan Dalimunthe dkk. (2025) |

**Apakah hipotesis ini falsifiable?** [✓] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Dengan uji t-test: jika semua metrik menghasilkan p-value > 0.05, maka tidak ada bukti perbedaan signifikan dan H₀ tidak ditolak."

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Apakah terdapat perbedaan signifikan antara platform web (Elena UNNES) dan platform mobile dalam hal kepuasan pengguna dan performa teknis pada pembelajaran Mata Kuliah Sistem Operasi? |
| Variable (IV) | Jenis platform: Web (Elena UNNES via browser) vs Mobile (aplikasi mobile/mobile browser) |
| Variable (DV) | Kepuasan Pengguna: SUS score (0–100), CSUQ score (1–7, 3 subdimensi); Performa Teknis: Response Time (ms), Loading Speed (ms), Error Rate (%) |
| Metric | SUS (0–100), CSUQ (1–7), Response Time (ms), Loading Speed/FCP (ms), Error Rate (%) |
| Data source | Kuesioner SUS+CSUQ via Google Forms (60+ mahasiswa), pengukuran teknis via Google Lighthouse + Chrome DevTools |
| Analysis method | Shapiro-Wilk → Independent Samples t-test (normal) atau Mann-Whitney U (tidak normal) + Cohen's d |

**Apakah rantai lengkap?** [✓] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? Rantai sudah lengkap dari RQ → IV/DV → Metrik → Data → Analysis

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Perbandingan Efisiensi Penggunaan E-Learning Berbasis Website dan Aplikasi Mobile dalam Proses Pembelajaran (Dalimunthe et al., 2025) — Paper 3

**RQ yang diekstrak:** Apakah ada perbedaan signifikan dalam persepsi pengguna terhadap efisiensi platform e-learning antara website dan aplikasi mobile?

**Komponen yang hilang:** 
- **METODE SPESIFIK**: RQ terlalu general (\"e-learning\"), tidak menyebut platform konkret. Lebih baik seperti Paper 1: "Elena UNNES vs YouTube"
- **BASELINE**: Tidak ada referensi ke performa diketahui atau best practice. Hanya "platform yang sering digunakan" (vague)
- **METRIK JELAS**: Disebutkan "efisiensi" tapi tidak jelas: response time? satisfaction? learning outcome? Semua?
- **Konteks sudah ada** (90 mahasiswa STMIK, tapi mata kuliah apa? kompetensi awal responden?)
>> **Pelajaran utama**: RQ yang matang harus nama platform spesifik + metrik terukur konkret + baseline reference, bukan generic generic terms.
