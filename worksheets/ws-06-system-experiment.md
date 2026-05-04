# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: Apakah platform web (Elena UNNES) menghasilkan kepuasan pengguna yang signifikan berbeda dengan platform mobile pada mata kuliah Sistem Operasi?

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
| Platform Type (Web vs Mobile) | IV | Elena UNNES (LMS web) vs YouTube app + mobile app | User choice observasi (quasi-experimental design) |
| Learning Satisfaction (UEQ) | DV | UI/UX, content delivery, interactivity features | Questionnaire post-usage 4 minggu |
| Ease of Use (SUS) | DV | Navigation, menu organization, accessibility | Questionnaire integrated atau external survey |
| Response Time | DV | Server backend, network infrastructure, client rendering | Automated monitoring Chrome DevTools / Android Profiler |
| Memory Usage | DV | Application runtime, caching, resource allocation | Memory profiling tools during typical 1-hour session |
| Learning Context | CV | Sistem Operasi, praktik-heavy course | Tetap konsisten untuk semua responden |
| Semester | CV | Semester genap, tahun akademik sama | Tetap konsisten untuk semua responden |

4 Prinsip Desain:
  [✓] Traceability — Setiap komponen bisa ditelusuri ke variabel
  [✓] Variable Isolation — IV bisa diubah tanpa mengubah CV
  [✓] Measurement Integration — Pengukuran DV built-in
  [✓] Reproducibility — Setup bisa direkonstruksi

Experimental Setup:
  Input data     : User demographics, course materials, baseline platform usage
  Parameter      : Platform assignment (observational), survey timing, profiling duration
  Output format  : CSV questionnaire responses, JSON performance logs, statistical analysis reports
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Apakah platform web (Elena UNNES) menghasilkan kepuasan pengguna yang signifikan berbeda dengan platform mobile pada mata kuliah Sistem Operasi?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| Platform Type (Web vs Mobile) | IV | Elena UNNES (LMS web) vs YouTube app + mobile app | User choice observasi (quasi-experimental design) |
| Learning Satisfaction (UEQ) | DV | UI/UX, content delivery, interactivity features | Questionnaire post-usage 4 minggu |
| Ease of Use (SUS) | DV | Navigation, menu organization, accessibility | Questionnaire integrated atau external survey |
| Response Time | DV | Server backend, network infrastructure, client rendering | Automated monitoring Chrome DevTools / Android Profiler |
| Memory Usage | DV | Application runtime, caching, resource allocation | Memory profiling tools during typical 1-hour session |
| Learning Context | CV | Sistem Operasi, praktik-heavy course | Tetap konsisten untuk semua responden |
| Semester | CV | Semester genap, tahun akademik sama | Tetap konsisten untuk semua responden |

**Apakah semua variabel bisa di-map?** [✓] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? Semua variabel ter-map dengan jelas

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Traceability | ✓ | Setiap komponen (Elena, YouTube) mapped ke IV; DV metrics clearly defined |
| Modularity | ✓ | Platforms independent, metrics independent, bisa analyzed separately |
| Controllability | ⚠ | User choice uncontrollable, tapi semester/context tetap terkontrol |
| Measurability | ✓ | Semua DV measurable: UEQ (1-7), SUS (0-100), response time (ms), memory (kB) |

**Prinsip mana yang paling sulit dipenuhi?** Controllability (user choice)
**Strategi untuk mengatasinya:**
> Gunakan stratified random sampling atau matching berdasarkan demographics. Gunakan statistical controls (ANCOVA) untuk reduce confounding effects dari unobserved variables

---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki 3 komponen utama, rencanakan ablation study.

| Kondisi | Platform Web | Platform Mobile | Fitur Interaktif | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| Full | ✓ Elena complete | ✓ YouTube complete | ✓ Discussion, quiz | Baseline: satisfaction optimal |
| – Web UI | ❌ (simplified) | ✓ | ✓ | Impact UI complexity pada satisfaction |
| – Mobile Responsiveness | ✓ | ❌ (non-optimized) | ✓ | Impact mobile optimization pada ease of use |
| – Interactivity | ✓ | ✓ | ❌ (read-only) | Impact interactive features pada satisfaction |

**Komponen mana yang diprediksi paling berkontribusi?** Platform optimization untuk device-nya (web for desktop, mobile for smartphone)
**Mengapa?**
> Papers 1-4 show technical performance significantly impacts satisfaction. Mobile optimization directly affects response time → perceived usability → satisfaction. More critical than UI complexity for platform satisfaction

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> **Risiko monolitik**: Jika Elena UNNES dibangun dengan semua fitur built-in tanpa isolasi, tidak bisa tahu: apakah satisfaction naik karena UI design bagus, atau karena video features, atau notification system? Tidak bisa ablation study. Paper 1 report Elena 79.4%, tapi kontributor utamanya apa? Tidak tahu karena tidak ada ablation. Gejala: masalah performance mendadak → tidak bisa isolate apakah dari server backend, network latency, atau client rendering?
>
> **Mengapa modular penting**: Paper 4 (PWA vs Mobile Web) implicit show ini → bisa isolate technical aspects (response time, memory, storage) terpisah dari pedagogical aspects (satisfaction). Modular design memungkinkan: (1) **Variable isolation**: Ubah 1 komponen (notification on/off), lihat dampaknya tanpa affect lain. (2) **Troubleshooting**: Learning outcome turun? Cek mana component culprit (cache strategy? API latency?). (3) **Replicability**: Orang lain reconstruct eksperimen dengan config file, bukan re-engineer sistem. Paper 2 (SLR) menunjukkan aplikasi profesional dibangun modular (separate backend PHP/MySQL, frontend Android/web) untuk support evolution dan testing. Implication: untuk riset, demand sistem yang configurable (YAML/JSON config) bukan hardcoded logic."
