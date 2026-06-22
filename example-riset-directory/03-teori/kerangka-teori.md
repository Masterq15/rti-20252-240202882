# Kerangka Teori

**Penelitian:** Perbandingan Kepuasan Pengguna dan Performa Teknis Platform Web dan Mobile pada Pembelajaran Mata Kuliah Sistem Operasi

---

## 1. Platform E-Learning

E-learning adalah sistem pembelajaran yang memanfaatkan teknologi informasi dan komunikasi untuk mendukung proses belajar-mengajar. Dalam penelitian ini, dua jenis platform dibandingkan:

- **Platform Web:** Diakses melalui browser (Chrome/Firefox) pada perangkat desktop/laptop. Contoh: Elena UNNES (berbasis MOODLE).
- **Platform Mobile:** Diakses melalui aplikasi yang diinstal pada smartphone. Fitur, UI/UX, dan performa teknis bisa berbeda dengan versi web meskipun menyajikan konten yang sama.

---

## 2. System Usability Scale (SUS)

SUS adalah instrumen pengukuran usability yang dikembangkan oleh John Brooke (1986) dan telah divalidasi secara luas. Terdiri dari 10 item dengan skala Likert 1–5 (sangat tidak setuju sampai sangat setuju). Skor akhir dihitung menggunakan formula standar dan menghasilkan nilai 0–100.

| Rentang Skor | Interpretasi |
|-------------|-------------|
| ≥ 90 | Excellent |
| 80–89 | Good |
| 68–79 | Above Average (Acceptable) |
| 51–67 | Below Average |
| ≤ 50 | Poor |

Skor > 68 dianggap **above average** dan diterima sebagai usable.

---

## 3. Computer System Usability Questionnaire (CSUQ)

CSUQ dikembangkan oleh Lewis (1995) di IBM. Terdiri dari 19 item dengan skala Likert 1–7, dibagi menjadi 3 subdimensi plus 1 item kepuasan keseluruhan:

| Subdimensi | Item | Fokus |
|------------|------|-------|
| System Usefulness (SYSUSE) | Item 1–8 | Kemudahan penggunaan, efisiensi sistem |
| Information Quality (INFOQUAL) | Item 9–15 | Kejelasan informasi, pesan error, dokumentasi |
| Interface Quality (INTERQUAL) | Item 16–18 | Kenyamanan antarmuka |
| Overall | Item 19 | Kepuasan keseluruhan terhadap sistem |

Skala 1–7 di mana **1 = sangat tidak setuju** dan **7 = sangat setuju/sangat puas**. Skor yang **lebih tinggi menunjukkan kepuasan yang lebih tinggi**. Skor agregat dihitung sebagai mean dari seluruh item yang relevan per subdimensi.

---

## 4. Google Lighthouse

Google Lighthouse adalah tool audit performa web open-source yang terintegrasi dalam Chrome DevTools. Menghasilkan skor 0–100 untuk beberapa kategori, termasuk Performance.

**Metrik utama yang digunakan dalam penelitian ini:**

| Metrik | Singkatan | Definisi | Satuan |
|--------|-----------|----------|--------|
| First Contentful Paint | FCP | Waktu hingga konten pertama muncul di layar | ms |
| Time to Interactive | TTI | Waktu hingga halaman sepenuhnya interaktif | ms |
| Total Blocking Time | TBT | Total waktu blocking thread utama | ms |
| Speed Index | SI | Seberapa cepat konten terisi secara visual | ms |

**Konfigurasi pengukuran:**
- Throttling: Simulated 4G (jaringan representatif)
- Device: Desktop (untuk platform web) / Mobile (untuk platform mobile)
- Runs: 3 run per platform untuk mengurangi variabilitas

---

## 5. Hubungan Antar Konsep

```
Platform (Web vs Mobile) — IV
        ↓
Kepuasan Pengguna — DV
  ├── SUS Score (usability keseluruhan)
  └── CSUQ Score (3 subdimensi)

Performa Teknis — DV
  ├── Response Time (ms)
  ├── Loading Speed / FCP (ms)
  └── Error Rate (%)
```

Hipotesis yang diuji: apakah perbedaan jenis platform (IV) menghasilkan perbedaan signifikan pada kepuasan pengguna dan performa teknis (DV).

---

## 6. Kerangka Konseptual Penelitian

```
┌─────────────────────────────────────────────────────────┐
│                  VARIABEL INDEPENDEN (IV)                │
│         Jenis Platform: Web (Elena) vs Mobile (App)      │
└────────────────────────┬────────────────────────────────┘
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
┌─────────────────┐          ┌──────────────────────┐
│  KEPUASAN       │          │  PERFORMA TEKNIS     │
│  PENGGUNA       │          │                      │
│  (DV1)          │          │  (DV2)               │
│                 │          │                      │
│  • SUS Score    │          │  • Response Time (ms)│
│    (0–100)      │          │  • Loading Speed (ms)│
│  • CSUQ Score   │          │  • Error Rate (%)    │
│    (1–7)        │          │                      │
└─────────────────┘          └──────────────────────┘
          │                             │
          └──────────────┬──────────────┘
                         ▼
              ┌─────────────────────┐
              │  VARIABEL KONTROL   │
              │  • Jenis perangkat  │
              │  • Koneksi internet │
              │  • Prior experience │
              └─────────────────────┘
```
