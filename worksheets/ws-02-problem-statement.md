# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Teknologi Informasi (E-Learning)
  Konteks  : Penggunaan platform e-learning dalam pembelajaran Mata Kuliah Sistem Operasi antara platform berbasis web dan aplikasi mobile

System Context
  Input       : Mahasiswa aktif Mata Kuliah Sistem Operasi, materi perkuliahan, aksi pengguna di platform
  Process     : Penggunaan platform web (Elena UNNES via browser) atau platform mobile (aplikasi mobile/mobile browser) untuk mengakses materi dan berinteraksi
  Output      : Sesi pembelajaran yang berjalan (akses materi, kuis, diskusi)
  Outcome     : Kepuasan pengguna dan efektivitas pembelajaran mahasiswa
  Constraints : Koneksi internet, jenis perangkat yang digunakan, ketersediaan fitur platform
  Stakeholders: Mahasiswa, dosen pengampu, pengelola program studi, pengembang platform

Fenomena → Problem
  Fenomena yang diamati             : Mahasiswa Mata Kuliah Sistem Operasi menggunakan platform web (Elena) dan mobile (YouTube/app) secara bersamaan
  Gejala (symptom) yang terukur     : Belum ada data yang menunjukkan platform mana yang lebih efektif dan memuaskan untuk konteks ini
  Masalah yang didiagnosis          : Ketiadaan data empiris terintegrasi yang membandingkan kepuasan pengguna dan performa teknis kedua jenis platform
  Masalah riset (researchable)      : Belum diketahui apakah terdapat perbedaan signifikan antara platform web dan mobile dalam hal kepuasan pengguna dan performa teknis pada pembelajaran Sistem Operasi
  Variabel yang terukur             : Kepuasan pengguna (SUS score, CSUQ score), performa teknis (response time, loading speed, error rate)

Problem Quality Check
  [✓] Clarity — Apakah satu orang membaca akan paham?
  [✓] Measurability — Apakah ada metrik kuantitatif?
  [✓] Relevance — Apakah penting untuk domain?
  [✓] Testability — Apakah bisa gagal?
  [✓] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
  Mahasiswa Mata Kuliah Sistem Operasi saat ini menggunakan dua jenis platform e-learning secara bersamaan — platform berbasis web yang diakses melalui browser dan aplikasi mobile — namun belum tersedia data empiris yang membandingkan keduanya secara objektif dari sisi kepuasan pengguna maupun performa teknis. Ketiadaan data ini menyulitkan pengelola akademik dan pengembang platform dalam mengambil keputusan berbasis bukti mengenai platform mana yang lebih efektif untuk konteks pembelajaran ini.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Perbandingan platform web dan mobile untuk pembelajaran Mata Kuliah Sistem Operasi

| Tahap | Hasil |
|-------|-------|
| Reality | Mahasiswa Sistem Operasi menggunakan platform e-learning untuk belajar |
| Observed Issue (Symptom) | Mahasiswa menggunakan dua jenis platform (web dan mobile) secara bersamaan tanpa tahu mana yang lebih efektif |
| Diagnosed Problem (Root Cause) | Belum ada data empiris yang membandingkan kepuasan pengguna dan performa teknis kedua platform secara terintegrasi |
| Researchable Problem | Belum diketahui apakah ada perbedaan signifikan antara platform web dan mobile dari sisi kepuasan pengguna dan performa teknis pada Mata Kuliah Sistem Operasi |
| Measurable Variable | Kepuasan pengguna (SUS score, CSUQ score), performa teknis (response time ms, loading speed ms, error rate %) |

**Apakah terjebak solution-first thinking?** [ ] Ya / [✓] Tidak
> Tidak, karena fokusnya pada mengidentifikasi apakah ada perbedaan, bukan langsung merekomendasikan satu platform tertentu.

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Mahasiswa aktif Mata Kuliah Sistem Operasi, materi kuliah, aksi pengguna di platform |
| Process | Penggunaan platform web (Elena UNNES via browser) atau platform mobile (aplikasi/mobile browser) untuk mengakses materi dan berinteraksi |
| Output | Sesi pembelajaran yang berjalan: akses materi, kuis, diskusi |
| Outcome | Kepuasan pengguna dan efektivitas pembelajaran mahasiswa |
| Constraints | Koneksi internet, jenis perangkat, ketersediaan fitur platform, familiar-tidaknya mahasiswa dengan platform |
| Stakeholders | Mahasiswa, dosen pengampu, pengelola program studi, pengembang platform Elena |

**Komponen mana yang paling relevan dengan masalah riset?**
Process dan Outcome, karena berkaitan langsung dengan perbandingan pengalaman menggunakan kedua platform dan dampaknya terhadap kepuasan pengguna.
---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Problem statement jelas menyebut siapa (mahasiswa Sistem Operasi), apa (belum ada data perbandingan kepuasan + performa teknis), dan dampaknya (kesulitan pengambilan keputusan institusi) |
| Measurability | 5 | Metrik terukur eksplisit: SUS score (0-100), CSUQ score (1-7), response time (ms), loading speed (ms), error rate (%) |
| Relevance | 5 | Sangat relevan — e-learning adalah topik aktif di riset TI pendidikan, dan perbandingan web vs mobile belum terintegrasi |
| Testability | 5 | Bisa gagal: jika p-value > 0.05 pada semua metrik, berarti tidak ada perbedaan signifikan dan H0 tidak ditolak |
| Impact | 5 | Hasilnya langsung bisa jadi rekomendasi berbasis data untuk pengelola akademik dalam memilih platform |

**Skor total:** 25 / 25

**Problem statement versi final (1 paragraf):**
> Mahasiswa Mata Kuliah Sistem Operasi saat ini menggunakan platform e-learning berbasis web (Elena UNNES) dan aplikasi mobile secara bersamaan, namun belum tersedia data empiris yang membandingkan keduanya secara objektif dari sisi kepuasan pengguna maupun performa teknis. Ketiadaan data ini menyulitkan pengelola akademik dalam memilih dan mengoptimalkan platform yang paling sesuai untuk konteks pembelajaran ini. Oleh karena itu, diperlukan penelitian yang mengukur dan membandingkan kepuasan pengguna (SUS, CSUQ) dan performa teknis (response time, loading speed, error rate) dari kedua platform secara terintegrasi.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Masalah saat coding biasanya langsung terlihat — ada error, ada output yang salah, dan solusinya adalah debug dan fix. Fokusnya ke "ini rusak, perbaiki."
>
> Masalah riset berbeda: tidak ada yang "rusak", tapi ada yang "belum diketahui." Di penelitian ini, platform web dan mobile keduanya berfungsi, tapi belum diketahui mana yang lebih memuaskan dan lebih optimal secara teknis. Cara mendefinisikan masalah riset harus lebih ketat: harus ada gap yang terdokumentasi dari literatur, metrik yang terukur, dan hipotesis yang bisa salah.
