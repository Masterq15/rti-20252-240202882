# Laporan Penelitian

**Judul:** Perbandingan Kepuasan Pengguna dan Performa Teknis Platform Web dan Mobile pada Pembelajaran Mata Kuliah Sistem Operasi

**Peneliti:** Risky Dimas Nugroho (240202882)  
**Target Publikasi:** Jurnal nasional terakreditasi SINTA  
**Status Penelitian:** Tahap 0 (proposal + WS-01 s.d. WS-16) selesai; Tahap 1–5 belum dimulai

---

## 1. Ringkasan Eksekutif

Penelitian ini membandingkan kepuasan pengguna dan performa teknis antara platform e-learning berbasis web (Elena UNNES/MOODLE diakses via browser) dan platform mobile (aplikasi mobile) dalam konteks pembelajaran Mata Kuliah Sistem Operasi. Kepuasan pengguna diukur menggunakan SUS (System Usability Scale) dan CSUQ (Computer System Usability Questionnaire), sedangkan performa teknis diukur menggunakan Google Lighthouse (response time, loading speed, error rate).

Penelitian menggunakan desain kuantitatif komparatif between-subject dengan minimal 60 mahasiswa aktif Mata Kuliah Sistem Operasi sebagai responden. Analisis statistik akan dilakukan menggunakan Independent Samples T-Test atau Mann-Whitney U bergantung pada distribusi data, disertai pelaporan Cohen's d untuk mengukur kekuatan praktis perbedaan yang ditemukan.

**Status saat ini:** Proposal final sudah disusun dan semua WS-01 s.d. WS-16 sudah diselesaikan. Pengumpulan data belum dimulai — menunggu koordinasi dengan dosen pengampu Mata Kuliah Sistem Operasi.

---

## 2. Latar Belakang dan Rumusan Masalah

### 2.1 Latar Belakang

Mahasiswa Mata Kuliah Sistem Operasi saat ini menggunakan dua jenis platform e-learning secara bersamaan: platform berbasis web yang diakses melalui browser, dan aplikasi mobile yang diinstal pada perangkat smartphone. Alfita dkk. (2024) menemukan bahwa mahasiswa Ilmu Komputer UNNES memanfaatkan Elena, YouTube, dan E-book dengan skor keefektifan masing-masing 78.62%, 75.14%, dan 63.3%. Namun, penelitian tersebut tidak mengukur performa teknis antar platform secara eksplisit.

Penelitian sebelumnya oleh Dalimunthe dkk. (2025) membandingkan website dan aplikasi mobile pada 90 responden dan tidak menemukan perbedaan signifikan (Sig > 0.05), namun tanpa pengukuran teknis objektif. Ridho dkk. (2018) mengukur performa teknis PWA vs Mobile Web secara laboratoris namun tanpa kepuasan pengguna. Prasetyaningsih & Muchtar (2023) membandingkan UX web dan mobile Shopee namun dalam konteks e-commerce.

Dari kondisi ini muncul masalah konkret: belum ada data empiris terintegrasi yang membandingkan kepuasan pengguna dan performa teknis antara platform web dan mobile dalam konteks Mata Kuliah Sistem Operasi.

### 2.2 Rumusan Masalah

1. Apakah terdapat perbedaan signifikan antara kepuasan pengguna platform web dan mobile pada pembelajaran Mata Kuliah Sistem Operasi?
2. Apakah terdapat perbedaan signifikan antara performa teknis (response time, loading speed, error rate) platform web dan mobile dalam konteks yang sama?
3. Pada dimensi apa saja masing-masing platform menunjukkan keunggulan relatif?

### 2.3 Tujuan Penelitian

Detail lengkap: [../01-proposal/proposal-penelitian.md](../01-proposal/proposal-penelitian.md) bagian D.2.

---

## 3. Metodologi dan Rencana Pelaksanaan

Penelitian dilaksanakan dalam 5 tahap. Bagian ini merangkum rencana setiap tahap; detail teknis ada pada dokumen `09-docs/`.

### 3.1 Tahap 1 — Persiapan Instrumen dan Konfigurasi

**Status: Belum dimulai.**  
Rencana: menyusun Google Form kuesioner SUS (10 item) + CSUQ (19 item), melakukan pilot test ke 5–10 mahasiswa, mengonfigurasi Lighthouse (lighthouse-config.json, simulated 4G), dan mengurus izin pengumpulan data.

Detail: [../09-docs/tahap-1-persiapan-instrumen.md](../09-docs/tahap-1-persiapan-instrumen.md)

### 3.2 Tahap 2 — Pengumpulan Data Kuesioner

**Status: Belum dimulai.**  
Rencana: mendistribusikan Google Form ke minimal 30 mahasiswa per kelompok (web dan mobile) setelah sesi penggunaan platform minimal 30 menit. Data disimpan di `04-data/kuesioner-web.csv` dan `04-data/kuesioner-mobile.csv`.

### 3.3 Tahap 3 — Pengukuran Performa Teknis Lighthouse

**Status: Belum dimulai.**  
Rencana: menjalankan audit Lighthouse sebanyak 3 run per kondisi platform (web desktop, web mobile emulation, mobile app), mendokumentasikan kondisi jaringan via speedtest.net sebelum setiap run. Data disimpan sebagai JSON di `04-data/`.

Detail: [../09-docs/tahap-3-pengukuran-lighthouse.md](../09-docs/tahap-3-pengukuran-lighthouse.md)

### 3.4 Tahap 4 — Preprocessing, Validasi, dan Analisis Statistik

**Status: Belum dimulai.**  
Rencana: cleaning data (missing values, duplikat, outlier), menghitung skor total SUS dan rata-rata subdimensi CSUQ, menjalankan Shapiro-Wilk → t-test atau Mann-Whitney U + Cohen's d menggunakan Jamovi. Output: tabel statistik dan grafik di `06-output/`.

Detail: [../09-docs/tahap-4-analisis-data.md](../09-docs/tahap-4-analisis-data.md)

### 3.5 Tahap 5 — Penulisan Manuskrip dan Publikasi

**Status: Belum dimulai.**  
Rencana: menulis naskah jurnal format IMRAD berdasarkan hasil analisis Tahap 4, menyesuaikan dengan template jurnal sasaran, dan melakukan submission.

Detail: [../09-docs/tahap-5-penulisan-manuskrip.md](../09-docs/tahap-5-penulisan-manuskrip.md)

---

## 4. Hasil Penelitian

*(Belum tersedia — akan diisi setelah pengumpulan dan analisis data selesai)*

### 4.1 Kepuasan Pengguna (SUS + CSUQ)

| Platform | SUS Mean ± SD | CSUQ Mean ± SD | n |
|----------|--------------|----------------|---|
| Web (Elena UNNES) | — | — | — |
| Mobile | — | — | — |

### 4.2 Performa Teknis (Lighthouse)

| Platform | Response Time (ms) | Loading Speed (ms) | Error Rate (%) | n |
|----------|-------------------|-------------------|----------------|---|
| Web (Elena UNNES) | — | — | — | — |
| Mobile | — | — | — | — |

### 4.3 Hasil Uji Statistik

| Metrik | p-value | Cohen's d | Kesimpulan |
|--------|---------|-----------|-----------|
| SUS Score | — | — | Menunggu data |
| CSUQ Score | — | — | Menunggu data |
| Response Time | — | — | Menunggu data |
| Loading Speed | — | — | Menunggu data |

---

## 5. Kendala dan Catatan

*(Akan diisi seiring pelaksanaan penelitian)*

---

## 6. Kesimpulan dan Saran

*(Akan diisi setelah analisis data selesai)*

---

## 7. Lampiran — Peta Artefak Penelitian

| Folder | Isi | Status |
|--------|-----|--------|
| [01-proposal/](../01-proposal/) | Proposal penelitian final | Selesai |
| [02-literatur/](../02-literatur/) | Matriks literatur 5 paper + daftar pustaka APA | Selesai |
| [03-teori/](../03-teori/) | Landasan teori SUS, CSUQ, Lighthouse, statistik | Selesai |
| [04-data/](../04-data/) | Data kuesioner CSV + hasil Lighthouse JSON | Belum ada (simulasi tersedia) |
| [05-kode/](../05-kode/) | Skrip Python: validasi data + analisis + visualisasi | Tersedia (siap dijalankan) |
| [06-output/](../06-output/) | Tabel statistik + grafik hasil analisis | Belum ada |
| [07-manuskrip/](../07-manuskrip/) | Draf naskah jurnal format IMRAD | Draf awal tersedia |
| [08-laporan/](../08-laporan/) | Laporan penelitian (dokumen ini) | Dalam pengerjaan |
| [09-docs/](../09-docs/) | Rencana dan protokol per tahap | Sebagian tersedia |
