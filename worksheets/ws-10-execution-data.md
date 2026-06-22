# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| 1     | Lighthouse audit — Platform Web (Elena), Desktop | N/A | Throttling: 4G, kategori: Performance | Planned | ~5 menit | lighthouse_web_desktop_run1.json |
| 2     | Lighthouse audit — Platform Web (Elena), Mobile emu | N/A | Throttling: 4G, device: mobile | Planned | ~5 menit | lighthouse_web_mobile_run1.json |
| 3     | Lighthouse audit — Platform Mobile (app/mobile browser) | N/A | Throttling: 4G, device: mobile | Planned | ~5 menit | lighthouse_mobile_run1.json |
| 4     | Kuesioner SUS+CSUQ — Kelompok Web (30 responden) | N/A | Google Forms shuffle aktif | Planned | 1 sesi | kuesioner_web.csv |
| 5     | Kuesioner SUS+CSUQ — Kelompok Mobile (30 responden) | N/A | Google Forms shuffle aktif | Planned | 1 sesi | kuesioner_mobile.csv |

Jumlah runs per skenario : 3 run Lighthouse per kondisi platform; 1 sesi kuesioner per kelompok
Total runs               : 6 run Lighthouse + 2 sesi kuesioner (60+ responden total)

DATA LOG (per run):
  Run ID    : lighthouse-web-desktop-run1
  Timestamp : 2026-03-15T09:30:00
  Skenario  : Platform Web (Elena UNNES), kondisi Desktop
  Input     : URL Elena UNNES, throttling simulated 4G, Chrome 124.x
  Output    : response_time=423ms, FCP=1840ms, TTI=2100ms, error_rate=2.1%
  Anomali   : Tidak ada
  Catatan   : Speedtest sebelum run: 15.2 Mbps download / 8.4 Mbps upload
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| 1 | Lighthouse audit — Platform Web (Elena UNNES), kondisi Desktop | N/A | Throttling: simulated 4G, kategori: Performance | Planned |
| 2 | Lighthouse audit — Platform Web (Elena UNNES), kondisi Mobile | N/A | Throttling: simulated 4G, device: mobile emulation | Planned |
| 3 | Lighthouse audit — Platform Mobile (versi mobile browser/app), kondisi Mobile | N/A | Throttling: simulated 4G, device: mobile emulation | Planned |
| 4 | Kuesioner SUS + CSUQ — Kelompok Web (30 responden) | N/A | Google Forms, urutan item diacak, setelah 30 menit sesi | Planned |
| 5 | Kuesioner SUS + CSUQ — Kelompok Mobile (30 responden) | N/A | Google Forms, urutan item diacak, setelah 30 menit sesi | Planned |

**Total skenario:** 2 (Performa Teknis + Kepuasan Pengguna)
**Run per skenario:** 3 run Lighthouse per kondisi platform; 1 sesi kuesioner per kelompok
**Total run keseluruhan:** 6 run Lighthouse + 2 sesi kuesioner (60+ responden total)

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | lighthouse-web-desktop-run1 |
| Timestamp | 2026-03-15T09:30:00 |
| Platform | Web / Mobile |
| Kondisi Perangkat | Desktop / Mobile Emulation |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Jaringan (Speedtest) | 15.2 Mbps download / 8.4 Mbps upload |
| Lighthouse throttling | Simulated 4G |
| Versi Chrome | 124.0.6367.82 |
| URL yang diuji | https://elena.unnes.ac.id/course/... |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| Response Time (ms) | float | 0 – 10000 ms |
| Loading Speed / FCP (ms) | float | 0 – 10000 ms |
| Error Rate (%) | float | 0.0 – 100.0 |
| SUS Score | float | 0 – 100 |
| CSUQ Score (total + 3 subdimensi) | float | 1.0 – 7.0 |

**Format output:** [✓] CSV / [ ] JSON / [ ] Database / [ ] Lainnya: ____

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | Lighthouse error / halaman tidak bisa diakses saat audit | Dokumentasi penyebab (server down? jaringan putus?), tunggu 15 menit, re-run dengan kondisi yang sama. Catat di log. |
| Hasil ekstrem | Response time 8000ms padahal run lain ~400ms | Cek kondisi jaringan saat itu via speedtest, cek apakah server Elena sedang down atau maintenance. Re-run setelah kondisi stabil. Jangan hapus data, tandai sebagai suspect. |
| Waktu eksekusi anomali | Lighthouse audit selesai dalam 5 detik (terlalu cepat) | Kemungkinan hasil dari cache. Hard refresh dulu (Ctrl+Shift+R), bersihkan cache browser, re-run. |
| Inkonsistensi dengan run lain | SUS score responden = 0 atau 100 (terlalu ekstrem) | Follow-up dengan responden, cek apakah salah paham instruksi. Kalau tidak bisa diklarifikasi, tandai sebagai outlier dan laporkan di validasi data. |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Pernah, waktu tugas praktikum jaringan saya cuma tes ping sekali terus langsung tulis hasilnya di laporan. Ternyata pas dicek ulang hasilnya berbeda karena kondisi jaringan kampus lagi ramai.

**Yang akan dilakukan berbeda:**
> Sekarang saya akan selalu ambil minimal 3 run untuk data teknis dan hitung rata-ratanya. Untuk kuesioner, saya akan cek distribusi responsnya dulu sebelum langsung analisis supaya tahu ada outlier atau tidak sebelum terlambat.
