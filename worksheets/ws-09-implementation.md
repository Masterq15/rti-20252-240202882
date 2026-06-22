# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

> **Mengapa reproducibility penting?** Sains dibangun di atas prinsip verifikasi — temuan harus bisa dikonfirmasi oleh peneliti lain. _Replicability crisis_ yang terjadi di banyak paper riset ML/AI disebabkan oleh environment tidak terdokumentasi: orang lain tidak bisa reproduksi, hasil diragukan, kepercayaan terhadap temuan hilang. Prinsip: **dokumentasi environment = snapshot kredibilitas riset Anda.**

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
   - **Docker** = teknologi container yang "membungkus" aplikasi beserta seluruh dependency-nya dalam satu unit terisolasi. Hasilnya: kode berjalan identik di laptop, server, maupun reviewer lain. Intro singkat: `docker run -v $(pwd):/workspace environment-image python run_experiment.py`
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Dependency Locking

Mengandalkan "install library terbaru" berbahaya: versi berbeda = perilaku berbeda = hasil tidak reproducible. Praktik:
- **Python**: buat `requirements.txt` dengan versi eksplisit: `scikit-learn==1.3.2`, lalu kunci dengan `pip freeze > requirements.txt`
- **Conda**: gunakan `conda env export > environment.yml` untuk snapshot lengkap
- **Node.js/R/Julia**: gunakan `package-lock.json` / `renv.lock` / `Project.toml` — semua fungsi serupa: lock versi + hash

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : Intel Core i5-13420H (8 Core, 4P + 4E, up to 4.6GHz)
  RAM     : 16 GB DDR5 4800MHz
  GPU     : NVIDIA GeForce RTX 3050 6GB GDDR6
  Storage : 512 GB NVMe SSD

Software:
  OS        : Windows 11 Home 64-bit
  Runtime   : Google Chrome 124.x (Lighthouse + DevTools), Google Forms (web)
  Framework : Google Lighthouse v11 (built-in Chrome DevTools), Jamovi 0.9.x

Dependencies:
| Library        | Version     | Sumber              | Hash/Checksum         |
|----------------|-------------|---------------------|-----------------------|
| Google Chrome  | 124.x       | google.com/chrome   | N/A (official release)|
| Google Lighthouse | 11.x     | built-in DevTools   | N/A (bundled)         |
| Jamovi         | 0.9.x       | jamovi.org          | N/A (official release)|
| Speedtest CLI  | latest (web)| speedtest.net       | N/A                   |
| Google Forms   | latest (web)| forms.google.com    | N/A                   |

Konfigurasi:
  Config file     : lighthouse-config.json (throttling: simulated 4G, kategori: Performance)
  Random seed     : Tidak berlaku untuk pengukuran teknis; Google Forms shuffle untuk urutan kuesioner
  Hyperparameters : Lighthouse throttling = simulated 4G; device = Desktop (web) / Mobile (mobile); audit runs = 3x per platform

Reproducibility Check:
  [✓] Dependency terdokumentasi (versi Chrome dan Lighthouse dicatat per sesi pengukuran)
  [✓] Seed ditetapkan di semua level (tidak berlaku — bukan ML; urutan kuesioner di-shuffle via Google Forms)
  [✓] Config di version control (lighthouse-config.json disimpan di repo)
  [✓] README instruksi reproduksi lengkap (lihat Latihan 3 — README Eksperimen)
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | Intel Core i5-13420H, 8 Core (4P + 4E) |
| RAM | 16 GB DDR5 |
| GPU | NVIDIA GeForce RTX 3050 6GB GDDR6 |
| Storage | 512 GB NVMe SSD |
| OS | Windows 11 Home 64-bit |
| Runtime | Browser: Google Chrome 124.x (untuk Lighthouse & DevTools); Google Forms untuk kuesioner |
| Framework | Google Lighthouse v11 (built-in Chrome DevTools), Android Studio (opsional untuk profiling mobile) |
| Random Seed | Tidak berlaku untuk pengukuran teknis; urutan pengisian kuesioner dirandomisasi via Google Forms |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| Google Chrome | 124.x | Menjalankan Lighthouse dan DevTools untuk pengukuran performa teknis |
| Google Lighthouse | 11.x (built-in) | Mengukur Performance Score, FCP, TTI, TBT, Loading Speed |
| Google Forms | Latest (web) | Distribusi dan pengumpulan kuesioner SUS + CSUQ |
| SPSS / Jamovi | 29.x / 0.9.x | Uji normalitas, Independent t-test, Mann-Whitney U, effect size |
| Speedtest.net | Latest (web) | Dokumentasi kecepatan jaringan saat pengukuran performa teknis |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | N/A (Lighthouse run pertama, jaringan terdokumentasi) | Response Time (ms) | — |
| 2 | N/A (Lighthouse run kedua, kondisi jaringan sama) | Response Time (ms) | [ ] Ya / [✓] Tidak (variasi wajar ±50ms) |
| 3 | N/A (Lighthouse run ketiga, kondisi jaringan sama) | Response Time (ms) | [ ] Ya / [✓] Tidak (variasi wajar ±50ms) |

**Jika hasil berbeda, kemungkinan penyebab:**
> Variasi response time antar run adalah normal karena dipengaruhi kondisi jaringan real-time, caching browser, dan beban server saat itu. Solusinya: ambil rata-rata dari 3 run dan dokumentasikan kondisi jaringan (speedtest) di setiap run.

**Checklist kontrol yang sudah diterapkan:**
- [✓] Random seed di-set di semua level (tidak berlaku, tapi urutan kuesioner dirandomisasi)
- [✓] Tidak ada background process yang mengganggu (tutup tab lain saat Lighthouse berjalan)
- [✓] Cache dibersihkan antar-run (hard refresh Ctrl+Shift+R sebelum tiap pengukuran)
- [✓] Config file yang sama untuk semua run (kondisi jaringan dicatat, simulasi 4G di Lighthouse)

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Judul Eksperimen: Perbandingan Kepuasan Pengguna dan Performa Teknis Platform Web dan Mobile pada Pembelajaran Mata Kuliah Sistem Operasi

## 1. Environment
- OS: Windows 11 Home 64-bit
- Browser: Google Chrome 124.x
- Tools: Google Lighthouse v11, Chrome DevTools, Speedtest.net
- Analisis: Jamovi 0.9.x / SPSS 29.x
- Kuesioner: Google Forms (SUS 10 item + CSUQ 19 item)

## 2. Installation
- Install Google Chrome (terbaru)
- Lighthouse sudah built-in di Chrome DevTools (F12 → Lighthouse tab)
- Install Jamovi dari https://www.jamovi.org untuk analisis statistik
- Siapkan Google Form kuesioner SUS dan CSUQ

## 3. Data
- Sumber: Mahasiswa aktif Mata Kuliah Sistem Operasi semester berjalan
- Format kuesioner: Google Sheets export (CSV), min 30 responden per kelompok
- Format performa teknis: JSON export Lighthouse, dicatat manual ke spreadsheet
- Ukuran: estimasi 60-100 baris per metrik

## 4. Execution
- Performa teknis web: Buka Chrome DevTools → Lighthouse → Run audit (simulasi 4G)
- Performa teknis mobile: Gunakan Chrome DevTools device emulation atau tes di perangkat nyata
- Kuesioner: Bagikan Google Form link ke responden setelah sesi penggunaan 30 menit

## 5. Configuration
- Lighthouse: Kategori = Performance, Device = Mobile/Desktop, Throttling = Simulated 4G
- Jaringan: Dokumentasikan kecepatan via speedtest.net sebelum setiap sesi pengukuran
- Kuesioner: Randomisasi urutan item via Google Forms shuffle

## 6. Expected Output
- File CSV: data_kuesioner_web.csv, data_kuesioner_mobile.csv (kolom: responden_id, SUS_total, CSUQ_total, CSUQ_sub1, CSUQ_sub2, CSUQ_sub3)
- File spreadsheet: data_performa_teknis.xlsx (kolom: platform, run_id, response_time_ms, loading_speed_ms, error_rate_pct, jaringan_mbps)
- Output analisis: tabel deskriptif + hasil uji t-test/Mann-Whitney + effect size Cohen's d
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [✓] Repeatability / [ ] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> Protokol observasi error rate yang terstruktur belum dibuat secara detail. Juga belum ada instruksi eksplisit untuk mengontrol kondisi perangkat responden (versi OS smartphone, versi aplikasi mobile yang dipakai). Kalau orang lain mau replikasi, mereka butuh lembar observasi error rate yang lebih spesifik dan panduan versi aplikasi yang dipakai saat pengujian.
