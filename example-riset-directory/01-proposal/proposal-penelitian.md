# Proposal Penelitian

**Nama**  : Risky Dimas Nugroho  
**NIM**   : 240202882  
**Kelas** : 4 IKRB  

---

## A. JUDUL

**Perbandingan Kepuasan Pengguna dan Performa Teknis Platform Web dan Mobile pada Pembelajaran Mata Kuliah Sistem Operasi**

---

## B. RINGKASAN

Mahasiswa Mata Kuliah Sistem Operasi saat ini menggunakan dua jenis platform e-learning secara bersamaan — platform berbasis web yang diakses melalui browser dan aplikasi mobile yang diinstal pada perangkat pintar — namun belum tersedia data empiris yang membandingkan keduanya secara objektif. Ketiadaan data ini menyulitkan pengelola akademik dan pengembang platform dalam mengambil keputusan berbasis bukti mengenai platform mana yang lebih efektif untuk konteks pembelajaran ini.

Penelitian ini membandingkan kepuasan pengguna dan performa teknis kedua jenis platform dalam konteks pembelajaran Mata Kuliah Sistem Operasi. Kepuasan pengguna diukur menggunakan System Usability Scale (SUS) dan Computer System Usability Questionnaire (CSUQ), sementara performa teknis diukur melalui response time, loading speed, dan error rate menggunakan Browser DevTools dan Google Lighthouse.

Penelitian menggunakan desain kuantitatif komparatif dengan responden mahasiswa aktif yang menggunakan kedua platform pada semester berjalan. Analisis dilakukan dengan Independent Samples t-test atau Mann-Whitney U, bergantung pada distribusi data. Luaran yang diharapkan adalah profil keunggulan komparatif per dimensi dari masing-masing platform, beserta rekomendasi berbasis data untuk pengembangan dan pemilihan platform pembelajaran Sistem Operasi.

---

## C. KATA KUNCI

platform e-learning; kepuasan pengguna; performa teknis; aplikasi mobile; web; Sistem Operasi

---

## D. PENDAHULUAN

### D.1. Latar Belakang dan Rumusan Masalah

Mata Kuliah Sistem Operasi merupakan salah satu mata kuliah inti di program studi Ilmu Komputer dan Sistem Informasi yang memadukan pemahaman teori dengan kemampuan praktik. Dalam penyelenggaraannya, mahasiswa sering kali menggunakan dua jenis platform e-learning secara bersamaan: platform berbasis web yang diakses melalui browser, dan aplikasi mobile yang diinstal pada perangkat pintar. Alfita dkk. (2024) menemukan bahwa mahasiswa Ilmu Komputer Universitas Negeri Semarang memanfaatkan Elena (e-learning berbasis MOODLE), YouTube, dan E-book sebagai platform utama pada mata kuliah ini, dengan skor rata-rata keefektifan sebesar 78,62% untuk Elena, 75,14% untuk YouTube, dan 63,3% untuk E-book. Namun, penelitian tersebut tidak mengukur perbedaan performa teknis antara akses web dan mobile secara eksplisit.

Beberapa penelitian sebelumnya telah menyentuh persoalan ini dari sudut yang berbeda-beda. Dalimunthe dkk. (2025) membandingkan efisiensi e-learning berbasis website dan aplikasi mobile menggunakan survei terhadap 90 responden mahasiswa dengan Independent Samples t-test pada sembilan indikator persepsi; seluruh indikator menunjukkan nilai Sig. (2-tailed) > 0,05 sehingga tidak ditemukan perbedaan yang signifikan secara statistik. Namun, penelitian ini tidak melakukan pengukuran performa teknis secara objektif dan tidak terikat pada konteks mata kuliah tertentu. Ridho dkk. (2018) mengukur performa teknis Progressive Web Apps versus Mobile Web secara laboratoris dan menemukan bahwa waktu respons sangat dipengaruhi ukuran berkas dan frekuensi akses, namun pengukuran kepuasan pengguna tidak dilakukan. Prasetyaningsih dan Muchtar (2023) membandingkan user experience platform web dan mobile Shopee menggunakan User Experience Questionnaire (UEQ) dan menemukan bahwa masing-masing platform unggul pada dimensi yang berbeda, namun konteksnya adalah e-commerce, bukan e-learning.

Dari kondisi ini muncul masalah konkret: mahasiswa Mata Kuliah Sistem Operasi menggunakan dua jenis platform secara bersamaan, tetapi tidak ada data empiris yang menunjukkan platform mana yang lebih memuaskan dan lebih optimal secara teknis dalam konteks tersebut. Masalah inti penelitian ini adalah **ketiadaan data empiris terintegrasi yang membandingkan kepuasan pengguna dan performa teknis antara platform web dan mobile pada pembelajaran Mata Kuliah Sistem Operasi**.

**Rumusan masalah:** Apakah terdapat perbedaan yang signifikan antara platform web dan mobile dalam hal kepuasan pengguna dan performa teknis pada pembelajaran Mata Kuliah Sistem Operasi?

---

### D.2. Pendekatan Pemecahan Masalah

Penelitian ini menggunakan pendekatan komparatif kuantitatif untuk mengisi celah data empiris mengenai perbandingan kepuasan pengguna dan performa teknis platform web dan mobile dalam konteks pembelajaran Mata Kuliah Sistem Operasi.

**Tujuan Penelitian:**

1. Mengukur dan membandingkan kepuasan pengguna platform e-learning berbasis web dan mobile pada Mata Kuliah Sistem Operasi.
2. Mengukur dan membandingkan performa teknis (response time, loading speed, error rate) platform web dan mobile.
3. Mengidentifikasi dimensi kepuasan dan performa teknis yang secara relatif lebih unggul pada masing-masing platform.
4. Menyusun rekomendasi berbasis data untuk pengembangan dan pemilihan platform pembelajaran.

**Research Question (RQ):**

- **RQ1:** Apakah terdapat perbedaan yang signifikan antara kepuasan pengguna platform web dan mobile pada pembelajaran Mata Kuliah Sistem Operasi?
- **RQ2:** Apakah terdapat perbedaan yang signifikan antara performa teknis (response time, loading speed, error rate) platform web dan mobile dalam konteks yang sama?
- **RQ3:** Pada dimensi apa saja masing-masing platform menunjukkan keunggulan relatif?

**Hipotesis:**

- **H0:** Tidak terdapat perbedaan yang signifikan antara kepuasan pengguna dan performa teknis platform web dan mobile pada pembelajaran Mata Kuliah Sistem Operasi.
- **Ha:** Terdapat perbedaan yang signifikan pada salah satu atau lebih dimensi kepuasan pengguna dan/atau performa teknis antara platform web dan mobile.

Intervensi penelitian berupa penugasan mahasiswa untuk menggunakan kedua jenis platform secara bergantian pada sesi pembelajaran dengan konten dan tugas yang setara (same task, different platform). Baseline penelitian adalah kondisi penggunaan platform e-learning yang sudah berjalan di program studi tanpa intervensi teknis tambahan.

---

### D.3. State of the Art dan Kebaruan

Penelitian yang ada telah mendekati persoalan ini dari tiga arah utama, namun masing-masing terbatas pada sebagian dimensi. Alfita dkk. (2024) mengevaluasi keefektifan platform web dan mobile pada Mata Kuliah Sistem Operasi melalui kuesioner dengan 50 responden; evaluasi hanya bersifat perseptual dan tidak membedakan secara eksplisit antara akses web dan mobile. Dalimunthe dkk. (2025) membandingkan efisiensi website dan aplikasi mobile menggunakan kuesioner terhadap 90 responden dan tidak menemukan perbedaan signifikan; pengukuran performa teknis secara objektif tidak dilakukan dan penelitian tidak terikat pada konteks mata kuliah spesifik. Ridho dkk. (2018) mengukur performa teknis PWA versus Mobile Web secara laboratoris — menyediakan dasar metodologis untuk pengukuran response time, penggunaan memori, dan media penyimpanan — tetapi tidak mengukur kepuasan pengguna dan tidak berada dalam konteks pembelajaran formal. Prasetyaningsih dan Muchtar (2023) memberikan bukti menggunakan UEQ bahwa platform web dan mobile memiliki profil keunggulan yang berbeda per dimensi, namun konteksnya adalah aplikasi e-commerce, bukan e-learning.

Dari pemetaan ini, tiga celah penelitian tampak konsisten:

1. Belum ada penelitian yang secara simultan mengukur kepuasan pengguna dan performa teknis pada kedua jenis platform dalam konteks Mata Kuliah Sistem Operasi.
2. Pengukuran performa teknis yang ada bersifat laboratoris dan tidak dihubungkan dengan persepsi kepuasan pengguna akhir.
3. Belum ada penelitian yang menggunakan instrumen terstandar (SUS/CSUQ) dalam konteks e-learning Sistem Operasi di perguruan tinggi Indonesia.

**Kebaruan penelitian** ini terletak pada desain integratif yang menggabungkan pengukuran kepuasan pengguna multidimensi (SUS + CSUQ) dengan pengukuran performa teknis objektif (response time, loading speed, error rate) secara bersamaan, dalam konteks spesifik Mata Kuliah Sistem Operasi.

---

### D.4. Peta Jalan Penelitian

**Tahap yang telah dicapai (pra-penelitian):**

1. Studi literatur awal mengenai perbandingan platform web dan mobile dalam e-learning.
2. Identifikasi instrumen kepuasan pengguna yang relevan (SUS, CSUQ, UEQ).
3. Identifikasi metode pengukuran performa teknis yang dapat diterapkan tanpa lingkungan laboratorium (Lighthouse, DevTools).

**Tahap yang dikerjakan pada usulan ini:**

1. Penyusunan instrumen pengukuran kepuasan pengguna dan protokol pengukuran performa teknis.
2. Pengumpulan data pada sampel mahasiswa yang menggunakan platform web dan mobile pada Mata Kuliah Sistem Operasi.
3. Analisis komparatif dan interpretasi hasil.

**Tahap lanjutan yang direncanakan:**

1. Pengembangan rekomendasi desain platform berdasarkan hasil penelitian.
2. Publikasi hasil pada jurnal nasional terakreditasi SINTA.
3. Kemungkinan perluasan kajian ke mata kuliah lain dengan karakteristik serupa (teori + praktik).

---

## E. METODE

### E.1. Desain Penelitian dan Unit Analisis

Penelitian ini menggunakan desain kuantitatif komparatif dengan pendekatan survei dan pengukuran teknis langsung. Jenis penelitian adalah non-eksperimental komparatif karena variabel independen (jenis platform) tidak dimanipulasi, melainkan dibandingkan dalam kondisi yang berlangsung secara alami.

**Hipotesis Operasional:**

- **H0:** Tidak terdapat perbedaan yang signifikan antara kepuasan pengguna dan performa teknis platform web dan mobile pada pembelajaran Mata Kuliah Sistem Operasi.
- **Ha:** Terdapat perbedaan yang signifikan pada salah satu atau lebih dimensi kepuasan pengguna dan/atau performa teknis antara kedua platform.

Unit analisis adalah mahasiswa aktif yang mengambil Mata Kuliah Sistem Operasi pada semester berjalan dan menggunakan platform e-learning berbasis web maupun mobile secara reguler, pada program studi Ilmu Komputer atau Sistem Informasi yang menjalankan setidaknya dua platform secara bersamaan.

**Kondisi yang dibandingkan:**
- **Kondisi A:** Penggunaan platform berbasis web (Elena/MOODLE melalui browser)
- **Kondisi B:** Penggunaan aplikasi mobile yang setara atau platform mobile yang digunakan secara reguler

---

### E.2. Variabel, Metric, Instrumen, dan Data

**Variabel Independen (IV):**

Jenis platform e-learning yang digunakan mahasiswa pada Mata Kuliah Sistem Operasi, terdiri dari dua kondisi: (1) platform berbasis web yang diakses melalui browser pada perangkat desktop/laptop, dan (2) platform berbasis mobile yang diakses melalui aplikasi pada perangkat smartphone.

**Variabel Dependen (DV):**

1. **Kepuasan Pengguna**, dioperasionalkan sebagai skor gabungan dari:
   - Skor System Usability Scale (SUS) — skala 0–100
   - Skor Computer System Usability Questionnaire (CSUQ) — skala 1–7, pada tiga subdimensi: kepuasan sistem, kemanfaatan informasi, dan kualitas antarmuka.

2. **Performa Teknis**, dioperasionalkan sebagai:
   - Response time (ms): waktu yang dibutuhkan platform untuk merespons aksi pengguna
   - Loading speed (ms): waktu total halaman/konten dimuat hingga dapat diakses penuh
   - Error rate (%): persentase aksi yang menghasilkan error atau kegagalan sistem selama sesi penggunaan

**Variabel Kontrol:**
- Jenis perangkat yang digunakan mahasiswa saat mengakses platform
- Kualitas koneksi internet responden (cepat/sedang/lambat)
- Frekuensi penggunaan platform sebelumnya

**Tabel 1. Definisi Variabel, Metric, dan Instrumen Penelitian**

| Variabel | Jenis | Skala | Definisi Operasional | Instrumen / Cara Ukur |
|----------|-------|-------|---------------------|----------------------|
| Platform (Web/Mobile) | Independen | Nominal | Jenis platform e-learning yang digunakan: berbasis website atau aplikasi mobile | Penugasan platform oleh peneliti |
| Kepuasan Pengguna | Dependen | Interval (skor) | Tingkat kepuasan mahasiswa saat menggunakan platform dalam pembelajaran Sistem Operasi | Kuesioner SUS (0–100) dan CSUQ (1–7) |
| Response Time | Dependen | Rasio (ms) | Waktu yang dibutuhkan platform merespons aksi pengguna (loading halaman, akses materi) | Browser DevTools & Google Lighthouse |
| Loading Speed | Dependen | Rasio (ms) | Waktu total halaman/konten dimuat hingga dapat diakses penuh | Lighthouse Performance Score & Waktu Muat Data |
| Error Rate | Dependen | Rasio (%) | Persentase aksi yang menghasilkan error atau kegagalan sistem selama sesi penggunaan | Log sistem dan observasi sesi pengguna |
| Jenis Perangkat | Kontrol | Nominal | Jenis perangkat yang digunakan mahasiswa saat mengakses platform | Dicatat pada lembar demografis |
| Koneksi Internet | Kontrol | Ordinal | Kualitas koneksi internet responden (cepat/sedang/lambat) | Self-report pada kuesioner |

**Responden dan Ukuran Sampel:**

Populasi adalah mahasiswa aktif yang mengambil Mata Kuliah Sistem Operasi pada semester berjalan dan menggunakan platform e-learning berbasis web maupun mobile secara reguler. Teknik sampling menggunakan purposive sampling dengan kriteria: (1) aktif menggunakan platform e-learning Sistem Operasi minimal empat pertemuan; (2) memiliki akses terhadap kedua jenis platform. Estimasi ukuran sampel minimal 30 responden per kelompok platform, atau total 60 responden bila menggunakan desain between-subject.

**Justifikasi Instrumen:**

SUS dipilih karena merupakan instrumen standar yang telah divalidasi secara luas untuk mengukur usability perangkat lunak dengan 10 item dan skor 0–100. CSUQ digunakan sebagai instrumen pelengkap yang lebih terperinci pada dimensi kepuasan sistem, kemanfaatan informasi, dan kualitas antarmuka. Google Lighthouse dan Browser DevTools dipilih sebagai alat ukur performa teknis karena bebas biaya, replikabel, dan menghasilkan data objektif yang dapat dibandingkan lintas platform.

---

### E.3. Skenario dan Prosedur Pengujian

Prosedur pengujian dirancang untuk menjamin kesetaraan perbandingan antara kondisi platform web dan mobile dengan mengontrol faktor konten, tugas, dan kondisi jaringan sejauh mungkin.

**Langkah Prosedur:**

1. Identifikasi platform web dan mobile yang digunakan secara reguler pada Mata Kuliah Sistem Operasi di lokasi penelitian.
2. Penyusunan skenario tugas standar: mahasiswa mengakses materi kuliah, mengunduh bahan ajar, mengikuti kuis online, dan berinteraksi dengan fitur diskusi pada kedua platform.
3. Kelompok web mengakses platform melalui browser desktop/laptop; kelompok mobile mengakses melalui aplikasi mobile pada smartphone.
4. Setelah sesi penggunaan (minimal 30 menit aktif), responden mengisi kuesioner SUS dan CSUQ.
5. Pengukuran performa teknis dilakukan secara terpisah oleh peneliti menggunakan Google Lighthouse pada simulasi kondisi jaringan rata-rata (4G/WiFi umum).
6. Error rate dicatat melalui observasi langsung dan/atau log sistem selama sesi penggunaan.
7. Data dikumpulkan, diperiksa kelengkapannya, lalu dianalisis.

**Faktor yang Dijaga Tetap (kontrol):**

1. Konten materi yang sama antara platform web dan mobile.
2. Skenario tugas yang sama untuk kedua kelompok.
3. Kualitas koneksi internet dicatat sebagai variabel kontrol.
4. Jenis perangkat dicatat dan dijadikan kovariat bila diperlukan.

---

### E.4. Artifact, Setup, dan Kesiapan Implementasi

Penelitian ini tidak mengembangkan artifact baru, melainkan menggunakan platform e-learning yang telah berjalan. Setup pengukuran meliputi:

1. **Platform web:** Elena UNNES (berbasis MOODLE) atau platform setara yang diakses melalui browser Google Chrome/Firefox pada laptop/komputer.
2. **Platform mobile:** Aplikasi mobile atau versi mobile browser dari platform yang sama, diakses pada smartphone Android/iOS.
3. **Instrumen kepuasan:** Kuesioner SUS (10 item, skala Likert 1–5) dan CSUQ (19 item, skala Likert 1–7) dalam format Google Form.
4. **Alat ukur performa teknis:** Google Lighthouse (dijalankan pada Chrome DevTools) untuk mengukur Performance Score, First Contentful Paint (FCP), Time to Interactive (TTI), dan Total Blocking Time (TBT).
5. **Log pengamatan:** Lembar observasi terstruktur untuk mencatat error rate selama sesi penggunaan.

Seluruh pengukuran performa teknis dilakukan oleh peneliti pada kondisi jaringan yang terdokumentasi — kecepatan unduh dan unggah dicatat menggunakan speedtest.net untuk memastikan replikabilitas.

---

### E.5. Batasan dan Asumsi Penelitian

**Batasan Penelitian:**

1. Penelitian ini terbatas pada konteks Mata Kuliah Sistem Operasi di program studi Ilmu Komputer dan Sistem Informasi, sehingga hasilnya mungkin tidak dapat digeneralisasi ke mata kuliah lain dengan karakteristik berbeda.
2. Pengukuran performa teknis dilakukan pada kondisi jaringan yang representatif tetapi tidak mencakup seluruh skenario kondisi jaringan ekstrem.
3. Penelitian menggunakan platform e-learning yang sudah berjalan (Elena/MOODLE) dan tidak mengembangkan platform baru.
4. Sampel terbatas pada mahasiswa yang memiliki akses terhadap kedua jenis platform dan bersedia berpartisipasi dalam penelitian.
5. Pengukuran error rate bergantung pada log sistem yang tersedia dan observasi langsung.

**Asumsi Penelitian:**

1. Kedua platform menyajikan konten yang setara dan dapat diakses oleh seluruh responden.
2. Pengukuran performa teknis dilakukan pada kondisi jaringan yang representatif dan terdokumentasi.
3. Responden mengisi kuesioner dengan jujur dan sesuai dengan pengalaman mereka menggunakan platform.
4. Tidak ada intervensi teknis dari pengelola platform selama periode pengumpulan data.
5. Perbedaan tingkat kebiasaan penggunaan sebelumnya dapat dikontrol melalui pencatatan frekuensi penggunaan pada kuesioner demografis.

---

### E.6. Teknik Analisis, Asumsi Statistik, dan Validitas

**Teknik Analisis:**

1. Statistik deskriptif (mean, median, standar deviasi) untuk menggambarkan sebaran skor kepuasan dan data performa teknis pada masing-masing platform.
2. Uji normalitas (Shapiro-Wilk atau Kolmogorov-Smirnov) untuk menentukan uji statistik yang tepat.
3. Independent Samples t-test bila asumsi normalitas terpenuhi, atau Mann-Whitney U Test sebagai alternatif non-parametrik bila asumsi tidak terpenuhi.
4. Effect size (Cohen's d atau r) untuk menginterpretasikan kekuatan praktis dari perbedaan yang ditemukan, tidak hanya signifikansi statistik.
5. Analisis per dimensi SUS dan CSUQ untuk mengidentifikasi dimensi spesifik yang menunjukkan perbedaan paling relevan.

**Asumsi Statistik:**

- Data berdistribusi normal atau mendekati normal untuk uji parametrik.
- Varians antara kedua kelompok homogen (uji Levene).
- Data bersifat independen antar kelompok.

**Ancaman Validitas:**

- **Validitas internal:** Perbedaan tingkat kebiasaan penggunaan sebelumnya dapat memengaruhi skor kepuasan melalui novelty effect. Dikontrol dengan mencatat frekuensi penggunaan sebelumnya pada kuesioner demografis.
- **Validitas eksternal:** Hasil yang spesifik pada Mata Kuliah Sistem Operasi mungkin tidak langsung dapat digeneralisasi ke mata kuliah lain.
- **Validitas konstruk:** Penggunaan dua instrumen kepuasan secara paralel (SUS + CSUQ) meningkatkan ketepatan pengukuran konstruk kepuasan pengguna.

---

## F. HASIL YANG DIHARAPKAN

Penelitian ini diharapkan menghasilkan lima luaran utama:

1. **Data empiris** skor kepuasan pengguna (SUS dan CSUQ) pada platform web dan mobile beserta hasil uji beda yang menyatakan apakah perbedaan tersebut signifikan secara statistik.
2. **Data objektif** performa teknis (response time, loading speed, error rate) pada kedua platform dalam kondisi penggunaan yang representatif.
3. **Profil keunggulan relatif** masing-masing platform per dimensi — dimensi mana yang secara konsisten lebih baik pada platform web dan mana yang lebih baik pada mobile.
4. **Rekomendasi berbasis data** yang dapat digunakan oleh pengelola akademik dan pengembang platform dalam memilih, mengoptimalkan, atau mengintegrasikan fitur dari kedua jenis platform untuk Mata Kuliah Sistem Operasi.
5. **Artikel ilmiah** yang dipublikasikan pada jurnal nasional terakreditasi SINTA.

---

## G. JADWAL PENELITIAN

**Tabel 2. Jadwal Pelaksanaan Penelitian (6 Bulan)**

| Kegiatan | Bln 1 | Bln 2 | Bln 3 | Bln 4 | Bln 5 | Bln 6 |
|----------|-------|-------|-------|-------|-------|-------|
| 1. Identifikasi masalah, studi literatur, dan penyusunan instrumen | ✓ | ✓ | | | | |
| 2. Pengumpulan data kepuasan pengguna (SUS & CSUQ) pada kedua platform | ✓ | ✓ | ✓ | | | |
| 3. Pengukuran performa teknis (response time, loading speed, error rate) | | ✓ | ✓ | ✓ | | |
| 4. Pengolahan dan analisis data statistik (uji komparatif) | | | | ✓ | ✓ | |
| 5. Interpretasi hasil dan penyusunan laporan penelitian | | | | | ✓ | ✓ |
| 6. Revisi, finalisasi, dan publikasi hasil penelitian | | | | | | ✓ |

---

## H. DAFTAR PUSTAKA

Alfita, I. N., Sari, A. K. I., Iskandar, A. G. A., Calysta, A. D., Waliwalidaiya, H. B. A., Pramitha, C., Utomo, Y. T., Maulidina, S., & Saputra, A. R. D. (2024). Analisis Keefektifan Penggunaan Aplikasi Berbasis Web dan Mobile bagi Kegiatan Pembelajaran pada Mata Kuliah Sistem Operasi untuk Mahasiswa Ilmu Komputer Universitas Negeri Semarang. *Jurnal Angka*, 1(1), 106–119.

Dalimunthe, A. M., Apriyani, K., Saifullah, M., & Musyarofah, A. (2025). Analisis Perbandingan Efisiensi Penggunaan E-Learning Berbasis Website dan Aplikasi Mobile dalam Proses Pembelajaran. *Jurnal Sistem Informasi STMIK Antar Bangsa*, 14(2), 60–64.

Lowell, D., Riadi, S., Manalu, D. F., Ibrahim, S. A., & Mulyati. (2025). Analisis Komparatif Metodologi Perencanaan Strategis Sistem Informasi di Indonesia: Systematic Literature Review. *Impression: Jurnal Teknologi dan Informasi*, 4(3), 316–327.

Prasetyaningsih, S., & Muchtar, S. P. N. (2023). Analisis Perbandingan User Experience pada Website dan Aplikasi Mobile Shopee menggunakan UEQ. *JTIM: Jurnal Teknologi Informasi dan Multimedia*, 5(3), 162–170. https://doi.org/10.35746/jtim.v5i3.326

Ridho, M. R., Pinandito, A., & Dewi, R. K. (2018). Perbandingan Performa Progressive Web Apps dan Mobile Web Terkait Waktu Respon, Penggunaan Memori dan Penggunaan Media Penyimpanan. *Jurnal Pengembangan Teknologi Informasi dan Ilmu Komputer*, 2(10), 3483–3491.

Wahyudi, T. (2022). Pengembangan Aplikasi Berbasis Web dan Android Sebagai Penunjang Kerja di Indonesia: Systematic Literature Review. *Indonesian Journal Computer Science*, 1(2), 96–102.
