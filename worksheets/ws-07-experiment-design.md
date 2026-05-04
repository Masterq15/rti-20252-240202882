# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : Apakah platform web (Elena UNNES) menghasilkan kepuasan pengguna dan efektivitas pembelajaran yang signifikan berbeda dengan platform mobile (YouTube + dedicated app) pada mata kuliah Sistem Operasi?
Hypothesis        : H₀: Tidak ada perbedaan signifikan dalam kepuasan pengguna dan efektivitas pembelajaran antara platform web dan mobile; H₁: Ada perbedaan signifikan
Tipe Eksperimen   : [✓] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Mahasiswa yang primarily menggunakan Elena UNNES untuk belajar | Platform: Web (Elena) | Mata kuliah: Sistem Operasi, Semester: genap 2026, Duration: 4 minggu |
| Treatment | Mahasiswa yang primarily menggunakan YouTube/mobile app untuk belajar | Platform: Mobile (YouTube + app) | Sama dengan Control |

Fairness Checklist:
  [✓] Dataset identik untuk semua kondisi
  [✓] Preprocessing setara
  [✓] Tuning effort setara
  [✓] Environment identik
  [✓] Metrik evaluasi sama

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Platform selection bias: tech-savvy students prefer mobile | Stratified sampling by GPA, ANCOVA control |
| External | Generalization limited ke UNNES Sistem Operasi | State limitations, recommend multi-context studies |
| Construct | UEQ conflate dengan interface familiarity | Measure familiarity separately, include new users |
| Conclusion | Small sample size reduce statistical power | Power analysis, report effect sizes, CIs |

Statistical Plan:
  Uji statistik   : Independent t-test untuk comparison, ANCOVA untuk control confounding
  Justifikasi      : Standard parametric tests untuk interval/ratio data dengan normal distribution
  Alpha            : 0.05
  Effect size min  : 0.5 (medium effect, detectable dengan n=50)
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Apakah platform web (Elena UNNES) menghasilkan kepuasan pengguna dan efektivitas pembelajaran yang signifikan berbeda dengan platform mobile (YouTube + dedicated app) pada mata kuliah Sistem Operasi?
**Tipe eksperimen:** [✓] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Group 1: Web User | Mahasiswa yang primarily menggunakan Elena UNNES untuk belajar | Platform: Web (Elena) | Mata kuliah: Sistem Operasi, Semester: genap 2026, Duration: 4 minggu, Instruction: standard, no intervention |
| Group 2: Mobile User | Mahasiswa yang primarily menggunakan YouTube/mobile app untuk belajar | Platform: Mobile (YouTube + app) | Sama dengan Group 1 |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✓ | Semua mahasiswa ambil mata kuliah Sistem Operasi yang sama |
| Preprocessing setara | ✓ | Kuesioner UEQ dan SUS sama untuk semua; technical monitoring dengan tool yang sama |
| Tuning effort setara | ✓ | User tidak di-force prefer platform tertentu; mereka choose naturally |
| Environment identik | ✓ | Semester sama, instruktur sama, jadwal kuliah sama; hanya platform yang berbeda |
| Metrik evaluasi sama | ✓ | Semua group diukur dengan metrik yang identik (UEQ, SUS, response time, memory) |

**Ada yang tidak fair?** [ ] Ya / [✓] Tidak
> Jika ya, bagaimana cara memperbaikinya? Design ini fair karena kedua group mendapat treatment yang equal dalam semua aspek kecuali platform choice (yang merupakan IV yang ingin diukur)

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Platform selection bias: tech-savvy students prefer mobile, less experienced prefer web. Confounding dengan learning ability. | Stratified random sampling by prior GPA/performance. Use ANCOVA to statistically control learning ability as covariate. |
| Internal | History effect: during 4-week period, major course events (exam, assignment deadline) bisa affect satisfaction differently for each group | Document all major events. Use repeated measures (survey setiap minggu) to capture time trends. |
| External | Generalization limited ke context specific (mata kuliah Sistem Operasi, UNNES). Bisa tidak applicable untuk mata kuliah lain atau institusi lain | Clearly state limitations. Recommend future study di multiple contexts. Discuss generalizability constraints. |
| External | Selection of participant: hanya mahasiswa yang already chose platform. Self-selection bias might not represent full population | Use intentional stratified sampling. Survey non-respondents untuk check representativeness. Report demographics. |
| Construct | UEQ satisfaction score bisa conflate dengan interface familiarity (mahasiswa sudah terbiasa Elena, bukan benar-benar lebih baik) | Measure familiarity separately, control statistically. Include new users cohort. |
| Construct | Response time measurements bisa affected by network conditions, not platform per se | Standardize environment (lab WiFi), measure multiple times, report variance. |
| Conclusion | Small sample size (50 students) might reduce power untuk detect effect | Power analysis sebelumnya (G*Power). Report effect sizes, confidence intervals. |
| Conclusion | Multiple comparisons without correction: jika compare 5 DV metrics tanpa Bonferroni, inflated Type I error | Pre-register primary metric (UEQ satisfaction score). Secondary metrics exploratory. Use alpha correction if doing multiple t-tests. |

**Ancaman mana yang paling sulit dimitigasi?** Internal validity threats (confounding variables, self-selection bias)
**Mengapa?**
> Karena design adalah quasi-experimental (observational), bukan true experimental. User already chose platform before study. Cannot ethically force platform assignment. Best mitigation adalah strong statistical controls, tapi will never fully eliminate internal validity concerns unlike true RCT

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. **Apakah baseline fair dan representatif terhadap state-of-the-art?** Paper 1: Elena 79.4% vs YouTube 78.3% vs E-book 75%. Tapi kenapa hanya 3 platform? Kenapa tidak PWA atau mLearning apps lain? Bisa straw man jika baseline dipilih bias. Paper 2 (SLR) lebih baik: kriteria inklusi/eksklusi eksplisit, multiple databases, transparent screening.

2. **Apakah sample size cukup dan representatif terhadap populasi?** Paper 3: 90 responden dari 1 institusi. Apakah applicable ke universitas lain? Gender-balanced? Semua semesters atau 1 cohort? Sudah power analysis? Sample kecil = power rendah = risiko Type II error. Paper 4 test 1 phone model saja → generalization limited.

3. **Apa yang diukur sebagai "sukses" dan apakah metrik benar-benar mengukur claim?** Paper 1: Satisfaction via UEQ, tapi TIDAK measure learning outcome atau test scores. Ini construct validity issue: satisfaction ≠ learning effectiveness. User satisfied tapi tidak learn. Paper 5 Shopee juga hanya UX metrics. Demand: learning outcome measurement (quiz results, concept mastery, skill test), actual usage duration, atau retention metrics. Jangan hanya survey satisfaction.
