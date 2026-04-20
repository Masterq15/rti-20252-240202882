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
  Domain   : Teknologi Informasi (Cloud Computing)
  Konteks  : Penggunaan infrastruktur IT dalam bisnis antara cloud computing dan infrastruktur tradisional

System Context
  Input       : Data kebutuhan bisnis, permintaan layanan IT, dan resource komputasi
  Process     : Pengolahan data menggunakan sistem cloud atau infrastruktur tradisional
  Output      : Layanan IT yang berjalan (aplikasi, penyimpanan, dll)
  Outcome     : Efisiensi operasional dan pertumbuhan bisnis
  Constraints : Koneksi internet, biaya, keamanan data
  Stakeholders: Perusahaan, pengguna, penyedia layanan cloud

Fenomena → Problem
  Fenomena yang diamati             : Banyak perusahaan mulai beralih ke cloud computing
  Gejala (symptom) yang terukur     : Adanya peningkatan penggunaan cloud karena fleksibilitas dan skalabilitas
  Masalah yang didiagnosis          : Belum jelas perbandingan efektivitas cloud dan infrastruktur tradisional secara spesifik
  Masalah riset (researchable)      : Belum ada analisis yang terukur mengenai perbandingan manfaat dan dampak kedua teknologi dalam konteks bisnis
  Variabel yang terukur             : fleksibilitas, biaya, keamanan data, dan efisiensi operasional

Problem Quality Check
  [✓] Clarity — Apakah satu orang membaca akan paham?
  [✓] Measurability — Apakah ada metrik kuantitatif?
  [✓] Relevance — Apakah penting untuk domain?
  [✓] Testability — Apakah bisa gagal?
  [✓] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
 Dalam konteks bisnis modern, banyak perusahaan dihadapkan pada pilihan antara cloud computing dan infrastruktur komputer tradisional, namun belum ada analisis yang benar-benar jelas dan terukur mengenai perbandingan manfaat, efisiensi, dan dampak dari kedua teknologi tersebut. Hal ini menyebabkan kesulitan dalam menentukan teknologi yang paling sesuai dengan kebutuhan bisnis. Oleh karena itu, diperlukan penelitian yang dapat mengukur dan membandingkan aspek seperti fleksibilitas, biaya, keamanan data, dan efisiensi operasional agar dapat memberikan dasar pengambilan keputusan yang lebih tepat.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Perbandingan cloud computing dan infrastruktur tradisional

| Tahap | Hasil |
|-------|-------|
| Reality | Perusahaan menggunakan sistem IT untuk operasional bisnis |
| Observed Issue (Symptom) | banyak perusahaan beralih ke cloud computing |
| Diagnosed Problem (Root Cause) | belum ada perbandingan yang jelas dan terukur antara kedua teknologi |
| Researchable Problem | belum diketahui secara pasti dampak penggunaan cloud dibandingkan infrastruktur tradisional dalam bisnis |
| Measurable Variable | biaya, fleksibilitas, keamanan, dan efisiensi |

**Apakah terjebak solution-first thinking?** [ ] Ya / [✓] Tidak
> tidak, karena fokusnya masih pada masalah, bukan langsung ke solusi.

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Data bisnis dan kebutuhan sistem IT |
| Process | Pengolahan menggunakan cloud atau sistem tradisional |
| Output | layanan IT seperti aplikasi dan penyimpanan |
| Outcome | Efisiensi dan peningkatan kinerja bisnis |
| Constraints | Biaya, keamanan, dan koneksi internet |
| Stakeholders | Perusahaan, pengguna, dan penyedia layanan |

**Komponen mana yang paling relevan dengan masalah riset?** 
Process dan Outcome, karena berkaitan langsung dengan perbandingan kinerja kedua teknologi.
---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 4| Sudah cukup jelas tapi masih bisa dipersempit |
| Measurability |4 | Bisa diukur dengan beberapa variabel |
| Relevance | 5 | Sangat penting di bidang IT |
| Testability | 4| Bisa diuji dengan data |
| Impact | 5 | Hasilnya bisa membantu perusahaan |

**Skor total:** 22 / 25

**Problem statement versi final (1 paragraf):**
> perusahaan saat ini dihadapkan pada pilihan antara cloud computing dan infrastruktur tradisional, namun belum ada perbandingan yang jelas dan terukur mengenai efektivitas keduanya dalam mendukung bisnis. Oleh karena itu, penelitian diperlukan untuk membandingkan aspek biaya, fleksibilitas, keamanan, dan efisiensi agar dapat membantu pengambilan keputusan yang lebih tepat.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Masalah saat coding biasanya langsung terlihat seperti error atau bug dan fokusnya untuk diperbaiki.

>Sedangkan masalah riset lebih ke mencari penyebab dan membuktikan sesuatu, jadi harus lebih terstruktur dan tidak langsung ke solusi.
