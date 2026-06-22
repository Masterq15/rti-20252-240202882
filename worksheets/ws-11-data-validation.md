# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [✓] Semua skenario tercakup (Lighthouse web desktop, web mobile, mobile; kuesioner web, mobile)
  [✓] Jumlah run sesuai rencana (3 run Lighthouse per kondisi, 30+ responden per kelompok)
  [✓] Tidak ada file output hilang
  Missing: 5 dari 66 data points (3 responden tidak hadir, 2 incomplete)

Format Consistency:
  [✓] Semua file format sama (CSV untuk kuesioner, JSON untuk Lighthouse)
  [✓] Header konsisten (kolom SUS_total, CSUQ_total, subdimensi, platform, timestamp)
  [✓] Tipe data konsisten (SUS float 0–100, CSUQ float 1–7, response time integer ms)

Range & Logic:
  [✓] Nilai dalam range masuk akal
  [✓] Tidak ada waktu negatif
  [✓] SUS 0–100, CSUQ 1–7, response time 0–10000ms — tidak di luar range
  Anomali ditemukan: 1 outlier SUS = 35.0 (kelompok web, responden 4); 1 run Lighthouse response time 5000ms (jaringan < 1Mbps)

Cross-Validation:
  [✓] Run Lighthouse identik → hasil mendekati (variasi ±50ms wajar)
  [✓] Trend konsisten dengan ekspektasi teori (mobile lebih cepat loading sesuai Ridho 2018)

Keputusan:
  [ ] Data siap analisis
  [✓] Perlu cleaning (follow-up 3 responden missing + investigasi outlier SUS 35.0)
  [ ] Perlu re-run (skenario: —)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| Lighthouse audit Platform Web (Desktop) | 3 | 3 | 0 | — |
| Lighthouse audit Platform Mobile | 3 | 3 | 0 | — |
| Kuesioner SUS+CSUQ Kelompok Web | 30 responden | 27 | 3 | Responden tidak hadir saat sesi pengisian |
| Kuesioner SUS+CSUQ Kelompok Mobile | 30 responden | 28 | 2 | Responden mengisi tidak lengkap (dropout) |

**Total expected:** 66 data points | **Total actual:** 61 | **Missing:** 5

**Keputusan untuk data missing:**
> Untuk 3 responden tidak hadir: kirim Google Form via WhatsApp dengan deadline 3 hari, jika tidak respons maka tidak dimasukkan dan jumlah sampel dilaporkan apa adanya. Untuk 2 responden tidak lengkap: cek apakah item yang hilang > 10% dari total item — jika ya, listwise deletion; jika tidak, mean imputation per subdimensi CSUQ.

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Dataset sampel (simulasi data SUS score kelompok Web):**

| Responden | SUS Score |
|-----------|----------|
| 1 | 72.5 |
| 2 | 75.0 |
| 3 | 70.0 |
| 4 | 35.0 |
| 5 | 77.5 |

**Deteksi outlier:**
- Q1 = 70.0 | Q3 = 75.0 | IQR = 5.0
- Batas bawah (Q1 - 1.5×IQR) = 62.5
- Batas atas (Q3 + 1.5×IQR) = 82.5
- Outlier terdeteksi: Responden 4 (35.0) — di bawah batas bawah 62.5

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| Responden 4 | 35.0 | Kemungkinan salah paham instruksi SUS (skala terbalik tidak dipahami), atau responden memang sangat tidak puas karena masalah akses platform | Follow-up langsung ke responden. Jika konfirmasi salah paham instruksi → koreksi atau exclude. Jika genuinely sangat tidak puas → tetap masukkan dan catat sebagai valid outlier. |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 92.4% data terkumpul (61 dari 66 yang direncanakan)
**2. Format:** [✓] Konsisten / [ ] Ada inkonsistensi — semua data dalam format CSV dari Google Sheets export
**3. Range check (anomali):** 1 outlier terdeteksi di SUS kelompok web (nilai 35.0), perlu follow-up. Data performa teknis dalam range normal (response time 200–800ms, tidak ada nilai negatif atau > 10000ms).
**4. Logic check:** [✓] Parameter sesuai plan / [ ] Ada ketidaksesuaian — semua kolom sesuai dengan definisi variabel di WS-05

**Kesimpulan:** [ ] Data siap analisis / [✓] Perlu tindakan: follow-up 3 responden missing + investigasi 1 outlier SUS sebelum masuk ke tahap analisis.

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> "Data yang benar" berarti nilainya akurat secara teknis — tidak ada error format, tidak ada nilai di luar range. Tapi "data yang dipercaya" lebih dari itu: kita yakin data tersebut benar-benar mencerminkan fenomena yang ingin diukur, dikumpulkan dengan cara yang konsisten, dan tidak ada kontaminasi dari faktor luar.
>
> Validasi formal tetap perlu meskipun data dikumpulkan otomatis karena Google Forms bisa saja mengizinkan submisi ganda, responden bisa salah paham instruksi, atau Lighthouse bisa menghasilkan data yang dipengaruhi kondisi jaringan anomali. Pengumpulan otomatis hanya mengurangi human error di tahap entri, bukan di tahap desain instrumen atau kondisi pengukuran.
