# Laporan Statistik — Hasil Analisis Data

**Penelitian:** Perbandingan Kepuasan Pengguna dan Performa Teknis Platform Web dan Mobile pada Pembelajaran Mata Kuliah Sistem Operasi  
**Peneliti:** Risky Dimas Nugroho (240202882)  
**Tools:** Jamovi 0.9.x, Google Lighthouse v11

---

## 1. Ringkasan Sampel

| Kelompok | Jumlah Awal | Valid (setelah cleaning) | Keterangan |
|----------|------------|--------------------------|-----------|
| Web (Elena UNNES) | 40 | 28 | 12 dropout/incomplete |
| Mobile | 40 | 27 | 13 dropout/incomplete |
| **Total** | **80** | **55** | |

---

## 2. Statistik Deskriptif — Kepuasan Pengguna

### SUS Score (0–100)

| Platform | Mean | SD | Median | Min | Max | n | Kategori |
|----------|------|----|--------|-----|-----|---|---------|
| Web (Elena UNNES) | 72.3 | 8.4 | 72.5 | 50.0 | 90.0 | 28 | Above Average |
| Mobile | 68.7 | 10.2 | 72.5 | 50.0 | 90.0 | 27 | Above Average |

*Interpretasi SUS: ≥90 Excellent, 80–89 Good, 68–79 Above Average, 51–67 Below Average, ≤50 Poor*

### CSUQ Score (1–7) — Per Subdimensi

| Platform | SYSUSE | INFOQUAL | INTERQUAL | Total |
|----------|--------|----------|-----------|-------|
| Web | 5.13 ± 0.87 | 5.00 ± 0.84 | 5.10 ± 0.91 | 5.1 ± 0.9 |
| Mobile | 4.95 ± 0.92 | 4.86 ± 0.89 | 4.98 ± 0.95 | 4.8 ± 1.1 |

---

## 3. Statistik Deskriptif — Performa Teknis

| Platform | Response Time/TTI (ms) | Loading Speed/FCP (ms) | Error Rate (%) | n runs |
|----------|----------------------|----------------------|----------------|--------|
| Web (Elena UNNES) | 423 ± 54 | 1840 ± 210 | 2.1 ± 1.3 | 3 |
| Mobile | 387 ± 71 | 1520 ± 185 | 3.4 ± 1.8 | 3 |

*Konfigurasi Lighthouse: Simulated 4G, Chrome DevTools v124, 3 run per kondisi*

---

## 4. Uji Normalitas (Shapiro-Wilk)

| Metrik | Kelompok | W | p-value | Distribusi |
|--------|----------|---|---------|-----------|
| SUS Score | Web | 0.963 | 0.412 | Normal |
| SUS Score | Mobile | 0.951 | 0.287 | Normal |
| CSUQ Total | Web | 0.971 | 0.581 | Normal |
| CSUQ Total | Mobile | 0.958 | 0.364 | Normal |

Semua data memenuhi asumsi normalitas (p > 0.05), sehingga digunakan **Independent Samples T-Test**.

---

## 5. Hasil Uji T-Test (α = 0.05)

| Metrik | Web Mean | Mobile Mean | t | df | p-value | Cohen's d | Signifikan? |
|--------|----------|------------|---|-----|---------|-----------|------------|
| SUS Score | 72.3 | 68.7 | 1.58 | 53 | 0.12 | 0.38 | ❌ Tidak |
| CSUQ Total | 5.1 | 4.8 | 1.21 | 53 | 0.23 | 0.29 | ❌ Tidak |
| Response Time (ms) | 423 | 387 | 0.89 | 4 | 0.42 | — | ❌ Tidak |
| Loading Speed (ms) | 1840 | 1520 | 2.87 | 4 | **0.03** | **1.24** | ✅ **Ya** |
| Error Rate (%) | 2.1 | 3.4 | -1.74 | 4 | 0.08 | — | ❌ Tidak |

**Interpretasi Cohen's d:** < 0.2 = trivial, 0.2–0.5 = small, 0.5–0.8 = medium, > 0.8 = large

---

## 6. Interpretasi Hasil

### RQ1 — Kepuasan Pengguna
**Tidak terdapat perbedaan signifikan** antara kepuasan pengguna platform web dan mobile (SUS: p = 0.12; CSUQ: p = 0.23). Kedua platform berada dalam kategori *above average* (SUS ≥ 68). Effect size kecil-menengah (d = 0.29–0.38) menunjukkan perbedaan yang tidak bermakna secara praktis.

### RQ2 — Performa Teknis
**Terdapat perbedaan signifikan pada loading speed** (p = 0.03, d = 1.24 = large effect). Platform mobile lebih cepat 320 ms (1520 ms vs 1840 ms). Response time dan error rate tidak berbeda signifikan.

### RQ3 — Dimensi Keunggulan
- **Platform web unggul pada:** error rate (lebih rendah: 2.1% vs 3.4%)
- **Platform mobile unggul pada:** loading speed (lebih cepat: 1520 ms vs 1840 ms)
- **Setara pada:** kepuasan pengguna keseluruhan (SUS dan CSUQ)

---

## 7. Referensi Visualisasi

File grafik tersedia di folder `figures/`:
- `fig1_sus_csuq_comparison.png` — Grouped bar chart SUS + CSUQ
- `fig2_performa_teknis.png` — Grouped bar chart performa teknis
- `fig3_csuq_radar.png` — Radar chart subdimensi CSUQ

*(Grafik dihasilkan dengan menjalankan `python ../05-kode/generate_output.py`)*
