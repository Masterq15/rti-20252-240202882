# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database**: IEEE Xplore, ACM DL, Scopus, Google Scholar
2. **Boolean query** yang terdokumentasi eksplisit
3. **Snowballing**: backward (telusuri referensi) + forward (cari yang mengutip)
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Perbandingan Efektivitas dan Efisiensi Platform Web vs Mobile untuk Pembelajaran
Database   : Google Scholar, IEEE Xplore, UNNES Repository
Query      : "web vs mobile learning", "e-learning platform comparison", "mobile application education"
Tahun      : 2015-2025
Hasil awal : 5 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| Alfita et al. (Elena UNNES) | 2024 | Survei Kuesioner | 50 mahasiswa OS | Elena 79.4%, YouTube 78.3%, E-Book 75% | Hanya 3 platform, 1 mata kuliah |
| Tri Wahyudi (SLR Apps) | 2022 | Systematic Literature Review | 15 artikel (2015-2022) | Sektor pendidikan dominan (6 artikel) | Fokus pada rancang bangun, bukan perbandingan |
| Dalimunthe et al. (E-Learning Efficiency) | 2025 | Survei Kuantitatif | 90 mahasiswa | Sig > 0.05 (tidak berbeda signifikan) | Sample kecil, satu institusi |
| Ridho et al. (PWA vs Mobile Web) | 2025 | Technical Testing | Halaman optimal/sedang/berat | PWA unggul untuk file besar | Pengujian terbatas pada performa teknis |
| Prasetyaningsih et al. (Shopee UX) | 2023 | UEQ + FGD | 30 responden + 9 FGD | Keduanya punya kekuatan-kelemahan | Hanya e-commerce, tidak generalisir |

Pola yang ditemukan:
  Metode dominan     : Survei kuantitatif + UX questionnaire (UEQ), fokus pada persepsi pengguna
  Dataset umum       : Mahasiswa Indonesia, konteks pendidikan
  Limitasi berulang  : Sample kecil, single-context (satu institusi/mata kuliah/platform), belum ada ablation study untuk fitur spesifik

GAP IDENTIFICATION

Gap 1: [Jenis: method]
  Deskripsi    : Belum ada integrated methodology yang menggabungkan technical metrics (response time, memory, storage) + user perception (UEQ) + learning outcome secara bersamaan
  Bukti        : Papers 1-5 fokus terpisah: Paper 1 (UEQ satisfaction), Paper 4 (technical performance), belum ada yang mengintegrasikan
  Signifikansi : Penting untuk mata kuliah praktik-heavy dimana technical limitation bisa mempengaruhi learning effectiveness

Gap 2: [Jenis: context]
  Deskripsi    : Belum ada studi pada konteks pembelajaran dengan mata kuliah praktik-heavy (seperti Sistem Operasi) yang memerlukan hands-on experience
  Bukti        : Papers 1,3,5 dalam konteks general e-learning, belum spesifik untuk mata kuliah dengan praktikum intensif
  Signifikansi : Platform yang efektif untuk teori mungkin tidak sama untuk praktik yang memerlukan resources besar

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
| Platform Web Tradisional (Elena UNNES berbasis Moodle) | Sudah digunakan di institusi pendidikan, umum untuk pembelajaran online | Digunakan di 35 dari 50 responden (70%), merepresentasikan platform e-learning LMS | Paper 1 (Alfita et al., 2024) |
| Aplikasi Mobile Pembelajaran (YouTube + aplikasi dedicated) | Mobile learning semakin popular, fleksibel diakses, multifungsi | YouTube digunakan 12 dari 50 responden (24%), merepresentasikan trend mobile learning | Paper 1 (Alfita et al., 2024) + Paper 2 (Tri Wahyudi, 2022) |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan Google Scholar atau database lain.

**Topik riset:** Perbandingan Efektivitas dan Efisiensi Platform Web vs Mobile untuk Pembelajaran
**Query pencarian:** "web vs mobile learning", "e-learning platform comparison", "mobile application education"
**Database:** Google Scholar, IEEE Xplore, UNNES Repository (2015-2025)

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Alfita et al. (Elena UNNES) | 2024 | Survei Kuesioner | 50 mahasiswa OS | Elena 79.4%, YouTube 78.3%, E-Book 75% | Hanya 3 platform, 1 mata kuliah |
| 2 | Tri Wahyudi (SLR Apps) | 2022 | Systematic Literature Review | 15 artikel (2015-2022) | Sektor pendidikan dominan (6 artikel) | Fokus pada rancang bangun, bukan perbandingan |
| 3 | Dalimunthe et al. (E-Learning Efficiency) | 2025 | Survei Kuantitatif | 90 mahasiswa | Sig > 0.05 (tidak berbeda signifikan) | Sample kecil, satu institusi |
| 4 | Ridho et al. (PWA vs Mobile Web) | 2018 | Technical Testing | Halaman optimal/sedang/berat | PWA unggul untuk file besar | Pengujian terbatas pada performa teknis |
| 5 | Prasetyaningsih et al. (Shopee UX) | 2023 | UEQ + FGD | 30 responden + 9 FGD | Keduanya punya kekuatan-kelemahan | Hanya e-commerce, tidak generalisir |

**Pola yang terlihat — Metode dominan:** Survei kuantitatif + UX questionnaire (UEQ), fokus pada persepsi pengguna
**Limitasi yang berulang:** Sample kecil, single-context (satu institusi/mata kuliah/platform), belum ada ablation study untuk fitur spesifik

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [✓] Ya / [ ] Tidak | Penelitian menunjukkan kedua platform setara (Sig > 0.05), tapi belum diketahui pada mata kuliah/domain berbeda apakah perbedaan akan signifikan |
| Method Gap | [✓] Ya / [ ] Tidak | Belum ada integrated methodology yang menggabungkan technical metrics (PWA vs Mobile Web) + user perception (UEQ) + learning outcome secara bersamaan |
| Data Gap | [✓] Ya / [ ] Tidak | Data terbatas pada konteks Indonesia (UNNES, Shopee), belum ada cross-domain comparison (pembelajaran vs e-commerce vs layanan publik) |
| Context Gap | [✓] Ya / [ ] Tidak | Belum ada studi pada konteks pembelajaran dengan mata kuliah praktik-heavy (seperti Sistem Operasi, Jaringan Komputer) yang memerlukan hands-on experience |

**Gap utama yang dipilih:** Method Gap + Context Gap (integrated approach untuk pembelajaran praktik-heavy)
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Penelitian sebelumnya tidak mengintegrasikan technical performance (response time, memory, storage) dengan pedagogical effectiveness (learning outcomes, satisfaction). Untuk mata kuliah praktik seperti Sistem Operasi, belum diketahui apakah mobile platform dengan keterbatasan memory/storage masih efektif untuk learning, atau apakah diperlukan web platform dengan resources lebih besar. Gap ini penting karena hasil akan membantu institusi memilih platform yang tepat untuk tipe mata kuliah berbeda.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | Platform Web Tradisional (Elena UNNES berbasis Moodle) | Sudah digunakan di institusi pendidikan, umum untuk pembelajaran online | Digunakan di 35 dari 50 responden (70%), merepresentasikan platform e-learning LMS | Bukan SOTA tapi common practice di akademik | Paper 1 (Alfita et al., 2024) |
| 2 | Aplikasi Mobile Pembelajaran (YouTube + aplikasi dedicated) | Mobile learning semakin popular, fleksibel diakses, multifungsi | YouTube digunakan 12 dari 50 responden (24%), merepresentasikan trend mobile learning | Bukan SOTA tapi high adoption | Paper 1 (Alfita et al., 2024) + Paper 2 (SLR) |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [✓] Ya / [ ] Tidak
> Justifikasi: Sebelumnya Papers tidak membandingkan dengan SOTA seperti Progressive Web Apps (PWA) yang more advanced. Perlu ditambahkan PWA sebagai kontrol tambahan untuk menghindari straw man, agar perbandingan tidak hanya "web lama vs mobile" tapi juga "teknologi yang lebih modern". Namun, untuk MA ini akan fokus pada perbandingan yang sudah terbukti digunakan di institusi (Elena + YouTube) sebagai baseline utama yang representative.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> **Klaim tanpa bukti**: Hanya mengatakan "belum ada" tanpa pencarian sistematis. Contoh: "belum ada yang membandingkan web vs mobile untuk pembelajaran" padahal Papers 1, 3, 5 sudah membandingkan, hanya dengan fokus berbeda.
>
> **Gap yang valid**: Harus didukung bukti pencarian sistematis (SLR dengan query dokumentasi, screening process, backward/forward snowballing). Papers 1-5 semuanya membandingkan platform, TAPI tidak ada yang mengintegrasikan technical metrics (Paper 4: response time, memory) + pedagogical effectiveness (Paper 1: UEQ satisfaction score) + learning outcome secara bersamaan untuk mata kuliah praktik-heavy. INILAH gap yang valid. Cara membuktikan: (1) Dokumentasikan query pencarian di multiple databases, (2) Tunjukkan screening: berapa paper awal → berapa final, (3) Eksplikasikan pola limitation yang berulang di papers (sample kecil, single context, missing learning outcome), (4) Jelaskan mengapa research sebelumnya belum sufficient untuk menjawab problem spesifik.
