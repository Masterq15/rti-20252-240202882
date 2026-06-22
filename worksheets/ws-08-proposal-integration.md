# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment). Setiap section menjawab pertanyaan yang diangkat section sebelumnya dan memunculkan pertanyaan baru.
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

**Operasionalisasi Red Thread** (benang merah):
```
Bab 2 (Problem) → | memperkenalkan masalah X + evidensi |
                          ↓ menimbulkan pertanyaan: "apa akar gap-nya?"
Bab 3 (Gap)     → | menjawab pertanyaan tadi + membuka "lalu apa yang perlu diteliti?" |
                          ↓
Bab 4 (RQ/H)    → | menjawab gap dengan pertanyaan spesifik + prediksi terukur |
                          ↓
Bab 5-7 (Method)→ | menjawab RQ melalui desain eksperimen yang tepat |
```
Jika ada lompatan (section B tidak menjawab pertanyaan section A), red thread putus.

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [✓] Problem → Gap: masalah terdokumentasi di literatur
  [✓] Gap → RQ: pertanyaan menjawab gap spesifik
  [✓] RQ → Hypothesis: hipotesis memprediksi jawaban
  [✓] Hypothesis → Metric: metrik mengukur variabel dalam hipotesis
  [✓] Metric → System: komponen sistem menghasilkan/mengukur metrik
  [✓] System → Experiment: desain eksperimen menggunakan sistem

Koneksi Horizontal (Konsistensi):
  [✓] Istilah sama di semua bagian
  [✓] Variabel di RQ = variabel di hipotesis = metrik di desain
  [✓] Scope tidak berubah dari masalah ke eksperimen

Cognitive Trap Checklist:
  [✓] Tidak ada paragraf "promosi" di pendahuluan (hanya data & gap)
  [✓] Metodologi disesuaikan ke RQ, bukan copy-paste textbook
  [✓] Timeline sudah ditambah buffer 30-50% dari estimasi awal
  [✓] Proposal mengakui kemungkinan H0 tidak ditolak (honest uncertainty)
  [✓] Tidak ada klaim "pasti berhasil" atau "meningkatkan signifikan"

Rubrik Self-Assessment:
| Kriteria     | 1 (Lemah)                                        | 2 (Cukup)                                     | 3 (Baik)                                           | Skor |
|------------- |--------------------------------------------------|-----------------------------------------------|----------------------------------------------------|------|
| Koherensi    | >2 koneksi vertikal terputus                     | 1-2 koneksi lemah, argumen masih bisa diikuti | Semua 6 koneksi terhubung, red thread jelas        | 3    |
| Specificity  | Variabel/metrik masih abstrak, tidak ada angka   | Sebagian metrik terdefinisi numerik           | Semua metrik + threshold + unit pengukuran jelas   | 3    |
| Feasibility  | Timeline >6 bulan tanpa memperhitungkan sumber   | Timeline 3-6 bulan dengan asumsi tertentu     | Timeline 1-3 bulan realistis dengan rencana detail | 2    |
| Rigor        | Baseline tidak jelas atau straw man              | 1-2 baseline dengan justifikasi partial       | 2+ baseline SOTA + justifikasi pemilihan lengkap   | 2    |
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| Problem Statement | WS-02 | Mahasiswa Mata Kuliah Sistem Operasi menggunakan platform web (Elena UNNES) dan mobile (YouTube/app) secara bersamaan, tetapi belum ada data empiris yang membandingkan kepuasan pengguna dan performa teknis keduanya secara terintegrasi. Ketiadaan data ini menyulitkan pengelola akademik dalam memilih platform yang tepat untuk konteks pembelajaran ini. |
| Gap | WS-03 | Penelitian sebelumnya mengukur kepuasan (Alfita 2024, Dalimunthe 2025) atau performa teknis (Ridho 2018) secara terpisah, belum ada yang mengintegrasikan keduanya sekaligus dalam konteks mata kuliah Sistem Operasi di perguruan tinggi Indonesia. |
| RQ | WS-04 | Apakah terdapat perbedaan yang signifikan antara platform web dan mobile dalam hal kepuasan pengguna (SUS + CSUQ) dan performa teknis (response time, loading speed, error rate) pada pembelajaran Mata Kuliah Sistem Operasi? |
| Hipotesis | WS-04 | H0: Tidak terdapat perbedaan signifikan antara kepuasan pengguna dan performa teknis platform web dan mobile pada pembelajaran Sistem Operasi. Ha: Terdapat perbedaan signifikan pada salah satu atau lebih dimensi kepuasan dan/atau performa teknis antara kedua platform. |
| Variabel & Metrik | WS-05 | IV = jenis platform (Web/Elena vs Mobile/app); DV = skor SUS (0–100), skor CSUQ (1–7), response time (ms), loading speed (ms), error rate (%). Semua metrik ditentukan sebelum pengumpulan data. |
| Sistem | WS-06 | Platform web: Elena UNNES via browser Chrome/Firefox di laptop. Platform mobile: aplikasi mobile atau mobile browser di smartphone. Instrumen: Google Form SUS+CSUQ, Google Lighthouse, Browser DevTools, log observasi error rate. |
| Desain Eksperimen | WS-07 | Desain kuantitatif komparatif non-eksperimental. Responden minimal 30 per kelompok platform (between-subject) atau 30–50 untuk within-subject. Uji statistik: Independent t-test atau Mann-Whitney U bergantung normalitas. Ancaman validitas dikontrol via variabel kontrol (jenis perangkat, koneksi internet, frekuensi penggunaan sebelumnya). |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| Problem → Gap | ✅ | Gap muncul dari 4 paper (Alfita 2024, Dalimunthe 2025, Ridho 2018, Prasetyaningsih 2023) yang masing-masing hanya mengukur sebagian dimensi — tidak ada yang mengintegrasikan kepuasan + performa teknis di konteks Sistem Operasi |
| Gap → RQ | ✅ | RQ1 langsung menanyakan perbedaan kepuasan, RQ2 menanyakan perbedaan performa teknis — keduanya menjawab gap integrasi yang teridentifikasi |
| RQ → Hypothesis | ✅ | H0 menyatakan tidak ada perbedaan signifikan, Ha menyatakan ada perbedaan pada salah satu atau lebih dimensi — langsung mengikuti arah RQ1 dan RQ2 |
| Hypothesis → Metric | ✅ | Kepuasan di hipotesis → diukur via SUS (0–100) + CSUQ (1–7); Performa teknis → diukur via response time (ms), loading speed (ms), error rate (%) |
| Metric → System | ✅ | SUS+CSUQ → Google Form; response time+loading speed → Google Lighthouse + Chrome DevTools; error rate → log observasi terstruktur. Semua metrik punya jalur pengukuran yang nyata |
| System → Experiment | ✅ | Desain komparatif menggunakan sistem existing (Elena web vs mobile app) sebagai kondisi A dan B; instrumen pengukuran terintegrasi langsung dalam prosedur eksperimen |

**Koneksi mana yang paling lemah?** Metric → System untuk error rate
**Bagaimana cara memperkuatnya?**
> Error rate bergantung pada log sistem yang tidak selalu tersedia dan observasi langsung yang bisa subjektif. Perlu protokol observasi terstruktur yang lebih ketat dan kalau bisa tambahkan screen recording untuk validasi.

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [✓] Ya / [ ] Tidak
> Istilah "platform web" dan "platform mobile" konsisten dari problem statement sampai desain eksperimen. Metrik di RQ = metrik di hipotesis = metrik di instrumen.

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| Koherensi | 3 | Semua 6 koneksi vertikal terhubung. Red thread jelas: mahasiswa pakai dua platform → tidak ada data perbandingan empiris → gap integrasi → RQ komparatif → metrik terukur → instrumen siap pakai |
| Specificity | 3 | Semua metrik terdefinisi numerik: SUS (0–100), CSUQ (1–7), response time (ms), loading speed (ms), error rate (%). Instrumen pengukuran juga spesifik: Lighthouse, DevTools, Google Form |
| Feasibility | 2 | Timeline 6 bulan cukup realistis. Sedikit risiko di pengumpulan data (perlu koordinasi dengan dosen pengampu dan kesediaan mahasiswa). Buffer sudah ada tapi bisa lebih ketat di bulan 1-2 |
| Rigor | 2 | Baseline dari literatur yang relevan (Alfita 2024, Dalimunthe 2025). Uji statistik sudah direncanakan dengan alternatif (t-test atau Mann-Whitney). Ancaman validitas teridentifikasi. Tapi jumlah paper baseline bisa ditambah untuk memperkuat posisi riset |

**Skor total:** 10 / 12

**Apakah proposal siap untuk fase eksekusi?** [✓] Ya / [ ] Belum
> Proposal sudah cukup bagus dan metrik sudah operasional. Yang perlu disiapkan sebelum eksekusi: protokol observasi error rate yang lebih ketat, koordinasi akses ke mahasiswa Sistem Operasi semester berjalan, dan pilot test instrumen SUS+CSUQ minimal ke 5 responden dulu.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** WS-02 Problem Statement — karena fenomenanya sudah jelas terlihat di kehidupan sehari-hari. Mahasiswa memang benar-benar pakai dua platform sekaligus dan tidak ada yang pernah bandingin secara ilmiah, jadi gampang ngidentifikasi masalahnya.

**Bagian tersulit:** WS-03 Literature Gap — susah banget nemuin gap yang beneran valid bukan sekadar "belum ada yang neliti ini". Harus baca paper satu-satu, cari pola limitasinya, terus jelasin kenapa gap-nya penting. Awalnya saya sempat nulis gap yang terlalu general.

**Yang akan dilakukan berbeda:**
> Kalau mulai ulang dari awal, saya akan fix topik lebih spesifik sejak WS-01 supaya pas nyari literatur di WS-03 tidak terlalu lebar. Saya juga akan langsung dokumentasikan search query dari awal biar tidak lupa mana paper yang sudah dibaca dan mana yang belum. Dan yang paling penting, saya tidak akan langsung loncat ke solusi sebelum problem statement benar-benar solid.
