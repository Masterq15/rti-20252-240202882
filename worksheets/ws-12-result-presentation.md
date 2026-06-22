# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

```
RESULT PRESENTATION PLAN

Research Question : Apakah terdapat perbedaan signifikan antara platform web dan mobile dalam hal kepuasan pengguna dan performa teknis pada pembelajaran Mata Kuliah Sistem Operasi?
Metrik Utama      : SUS Score (0–100), CSUQ Score (1–7), Response Time (ms), Loading Speed (ms), Error Rate (%)

Tabel Hasil:
| Platform | SUS Score (mean ± std) | CSUQ Score (mean ± std) | Response Time (mean ± std ms) | Loading Speed (mean ± std ms) | Error Rate (mean ± std %) | n |
|----------|----------------------|------------------------|-------------------------------|-------------------------------|--------------------------|---|
| Web (Elena UNNES) | 72.3 ± 8.4 | 5.1 ± 0.9 | 423 ± 54 | 1840 ± 210 | 2.1 ± 1.3 | 28 |
| Mobile (App) | 68.7 ± 10.2 | 4.8 ± 1.1 | 387 ± 71 | 1520 ± 185 | 3.4 ± 1.8 | 27 |

Visualisasi yang Direncanakan:
| # | Jenis Grafik | Pesan Utama | Metrik |
|---|-------------|-------------|--------|
| 1 | Grouped bar chart + error bar | Perbandingan kepuasan pengguna (SUS + CSUQ) antara kedua platform | Mean SUS ± std, Mean CSUQ ± std |
| 2 | Grouped bar chart + error bar | Perbandingan performa teknis (response time + loading speed) | Mean response time ± std, Mean loading speed ± std |
| 3 | Radar/spider chart | Profil keunggulan per subdimensi CSUQ untuk Web vs Mobile | Mean skor per subdimensi CSUQ |

Bias Check:
  [✓] Y-axis mulai dari 0 (atau dijustifikasi)
  [✓] Error bar/CI ditampilkan
  [✓] Semua data disertakan (tidak cherry-picked)
  [✓] Tidak menggunakan 3D tanpa alasan
```

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

**Tabel 1. Kepuasan Pengguna — SUS Score per Platform (simulasi)**

| Platform | SUS Score (mean ± std) | CSUQ Score (mean ± std) | n |
|----------|----------------------|------------------------|---|
| Web (Elena UNNES) | 72.3 ± 8.4 | 5.1 ± 0.9 | 28 |
| Mobile (App) | 68.7 ± 10.2 | 4.8 ± 1.1 | 27 |

**Tabel 2. Performa Teknis per Platform (simulasi)**

| Platform | Response Time — mean ± std (ms) | Loading Speed — mean ± std (ms) | Error Rate — mean ± std (%) | n |
|----------|--------------------------------|--------------------------------|-----------------------------|---|
| Web (Elena UNNES) | 423 ± 54 | 1840 ± 210 | 2.1 ± 1.3 | 3 runs |
| Mobile (App) | 387 ± 71 | 1520 ± 185 | 3.4 ± 1.8 | 3 runs |

**Checklist tabel:**
- [✓] Self-contained (judul jelas, satuan ada, N tercantum)
- [✓] Mean ± std (bukan single number)
- [✓] Diurutkan berdasarkan metrik utama (SUS score)
- [✓] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|-------------|-------|---------------------|
| 1 | Grouped bar chart + error bar | Perbandingan SUS Score dan CSUQ Score antara platform web dan mobile | Mean SUS ± std, Mean CSUQ ± std untuk kedua platform |
| 2 | Grouped bar chart + error bar | Perbandingan performa teknis (response time dan loading speed) antara kedua platform | Mean response time ± std, Mean loading speed ± std |
| 3 | Radar/spider chart | Profil keunggulan per dimensi CSUQ (kepuasan sistem, kemanfaatan informasi, kualitas antarmuka) untuk masing-masing platform | Mean skor per subdimensi CSUQ untuk Web vs Mobile |

---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Platform Web SUS = 72.3, Platform Mobile SUS = 68.7. Bar chart dengan Y-axis mulai dari 65.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan? | Ya — Web terlihat jauh lebih tinggi dari Mobile padahal selisihnya hanya 3.6 poin. Y-axis harus mulai dari 0 atau minimal diberi catatan mengapa dipotong. |
| Apakah error bar ditampilkan? | Belum — harus ditambahkan karena std cukup besar (8.4 dan 10.2). Tanpa error bar, perbedaan terlihat lebih pasti dari yang sebenarnya. |
| Apakah semua kondisi ditampilkan? | Ya — kedua platform ditampilkan |
| Apa solusinya? | Mulai Y-axis dari 0, tambahkan error bar ± std, dan tambahkan catatan n per kelompok di bawah grafik |

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [ ] Semua bias check lulus
- [✓] Ada yang perlu diperbaiki: Y-axis bar chart di Latihan 2 harus mulai dari 0, dan semua grafik harus menyertakan error bar untuk menampilkan variabilitas data.

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

> Tabel diperlukan untuk angka presisi — reviewer yang ingin tahu nilai exak, standar deviasi, atau n bisa langsung membacanya tanpa harus estimasi dari grafik. Grafik diperlukan untuk pola — melihat sekilas mana yang lebih tinggi, seberapa besar variasinya, dan apakah ada tren. Kalau hanya pakai tabel, susah melihat pola; kalau hanya grafik, angka persisnya tidak jelas.
>
> Pernah, waktu presentasi tugas saya buat bar chart perbandingan dua metode dengan Y-axis mulai dari 80%. Hasilnya terlihat dramatis padahal selisihnya cuma 3%. Reviewer langsung tanya "emang beda segitu?" dan saya baru sadar grafik saya menyesatkan tanpa saya sadari.
