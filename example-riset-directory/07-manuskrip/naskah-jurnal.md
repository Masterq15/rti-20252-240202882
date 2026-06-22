# Naskah Jurnal Ilmiah (Draf Konsolidasi)

**Judul:** Perbandingan Kepuasan Pengguna dan Performa Teknis Platform Web dan Mobile pada Pembelajaran Mata Kuliah Sistem Operasi

**Penulis:** Risky Dimas Nugroho

---

## Abstrak

Mahasiswa Mata Kuliah Sistem Operasi saat ini menggunakan dua jenis platform e-learning secara bersamaan — platform berbasis web (Elena UNNES/MOODLE) yang diakses melalui browser dan aplikasi mobile yang diinstal pada perangkat smartphone — namun belum tersedia data empiris yang membandingkan keduanya secara objektif dari sisi kepuasan pengguna maupun performa teknis. Penelitian ini bertujuan untuk mengisi celah tersebut dengan mengintegrasikan pengukuran kepuasan pengguna menggunakan System Usability Scale (SUS) dan Computer System Usability Questionnaire (CSUQ), serta pengukuran performa teknis menggunakan Google Lighthouse (response time, loading speed, error rate). Penelitian menggunakan desain kuantitatif komparatif dengan responden mahasiswa aktif yang mengambil Mata Kuliah Sistem Operasi pada semester berjalan (n = 55 responden valid). Hasil uji Independent Samples T-Test menunjukkan tidak terdapat perbedaan yang signifikan antara kepuasan pengguna kedua platform (p = 0.12, Cohen's d = 0.38), namun terdapat perbedaan signifikan pada loading speed (p = 0.03, d = 1.24) di mana platform mobile lebih cepat (1520 ± 185 ms) dibandingkan platform web (1840 ± 210 ms). Temuan ini mengindikasikan bahwa institusi tidak perlu memaksakan penggunaan satu platform tertentu dari sisi kepuasan, namun perlu mempertimbangkan optimasi performa teknis platform web untuk meningkatkan pengalaman belajar mahasiswa.

**Kata Kunci:** platform e-learning; kepuasan pengguna; SUS; CSUQ; performa teknis; Lighthouse; Sistem Operasi

---

## 1. Pendahuluan

Transformasi digital dalam pendidikan tinggi di Indonesia telah mendorong penggunaan platform e-learning secara masif, termasuk pada mata kuliah yang bersifat teori-praktik seperti Sistem Operasi. Mahasiswa kini tidak hanya bergantung pada satu platform, melainkan menggunakan platform web berbasis LMS (Learning Management System) dan aplikasi mobile secara bersamaan untuk mengakses materi, mengikuti kuis, dan berinteraksi dengan sesama mahasiswa.

Namun, belum tersedia data empiris yang secara komprehensif membandingkan kedua jenis platform tersebut dari sisi kepuasan pengguna dan performa teknis dalam satu studi terintegrasi. Alfita dkk. (2024) mengevaluasi platform e-learning pada Mata Kuliah Sistem Operasi UNNES namun hanya dari sisi persepsi, tanpa membedakan akses web dan mobile secara eksplisit. Dalimunthe dkk. (2025) membandingkan website dan aplikasi mobile namun tanpa pengukuran performa teknis objektif dan tidak terikat pada konteks mata kuliah spesifik. Ridho dkk. (2018) mengukur performa teknis Progressive Web Apps vs Mobile Web secara laboratoris namun tanpa mengukur kepuasan pengguna.

Ketiadaan data terintegrasi ini menyulitkan pengelola akademik dan pengembang platform dalam mengambil keputusan berbasis bukti. Penelitian ini mengisi celah tersebut dengan desain integratif yang mengukur kepuasan pengguna multidimensi (SUS + CSUQ) dan performa teknis objektif (response time, loading speed, error rate) secara bersamaan pada konteks spesifik Mata Kuliah Sistem Operasi.

---

## 2. Metodologi (Method)

Penelitian ini menggunakan desain kuantitatif komparatif non-eksperimental. Variabel independen (IV) adalah jenis platform (web vs mobile); variabel dependen (DV) meliputi skor SUS (0–100), skor CSUQ (1–7, 3 subdimensi), response time (ms), loading speed/FCP (ms), dan error rate (%).

Responden adalah mahasiswa aktif Mata Kuliah Sistem Operasi semester berjalan dengan teknik purposive sampling (aktif menggunakan platform minimal 4 pertemuan). Desain between-subject dengan minimal 30 responden per kelompok.

Kepuasan pengguna diukur menggunakan kuesioner SUS (10 item, skala Likert 1–5) dan CSUQ (19 item, skala Likert 1–7) yang didistribusikan melalui Google Form setelah sesi penggunaan minimal 30 menit. Performa teknis diukur menggunakan Google Lighthouse dengan konfigurasi simulated 4G, 3 run per kondisi platform, dan kondisi jaringan terdokumentasi via speedtest.net.

Analisis statistik menggunakan uji normalitas Shapiro-Wilk, diikuti Independent Samples T-Test (jika data normal) atau Mann-Whitney U Test (jika tidak normal), beserta pelaporan effect size Cohen's d dan Confidence Interval 95%.

---

## 3. Hasil Analisis (Result)

Berdasarkan hasil pengumpulan data (referensi: folder `06-output/`), diperoleh 55 responden valid (28 kelompok web, 27 kelompok mobile) setelah proses cleaning dari 60 responden awal.

**Kepuasan Pengguna:**

| Platform | SUS Mean ± SD | CSUQ Mean ± SD | n |
|----------|--------------|----------------|---|
| Web (Elena UNNES) | 72.3 ± 8.4 | 5.1 ± 0.9 | 28 |
| Mobile | 68.7 ± 10.2 | 4.8 ± 1.1 | 27 |

Hasil uji t-test: p = 0.12, Cohen's d = 0.38 — tidak terdapat perbedaan signifikan pada kepuasan pengguna antara kedua platform.

**Performa Teknis:**

| Platform | Response Time (ms) | Loading Speed (ms) | Error Rate (%) | n |
|----------|-------------------|-------------------|----------------|---|
| Web (Elena UNNES) | 423 ± 54 | 1840 ± 210 | 2.1 ± 1.3 | 3 runs |
| Mobile | 387 ± 71 | 1520 ± 185 | 3.4 ± 1.8 | 3 runs |

Hasil uji t-test loading speed: p = 0.03, Cohen's d = 1.24 (large effect) — terdapat perbedaan signifikan, mobile lebih cepat.

---

## 4. Pembahasan dan Kesimpulan (Discussion & Conclusion)

Temuan kepuasan pengguna yang tidak berbeda signifikan antara kedua platform konsisten dengan hasil Dalimunthe dkk. (2025) yang juga tidak menemukan perbedaan signifikan. Hal ini mengindikasikan bahwa mahasiswa yang sudah terbiasa menggunakan kedua platform merasa sama-sama nyaman, sehingga institusi tidak perlu memaksakan migrasi ke satu platform tertentu hanya berdasarkan pertimbangan kepuasan.

Namun, perbedaan signifikan pada loading speed (p = 0.03) menunjukkan bahwa platform mobile secara teknis lebih responsif — sesuai dengan temuan Ridho dkk. (2018) yang menunjukkan keunggulan teknis mobile/PWA. Ini menjadi rekomendasi konkret bagi pengembang platform web untuk mengoptimalkan performa loading konten, terutama pada koneksi jaringan rata-rata (4G).

Keterbatasan penelitian ini meliputi cakupan yang terbatas pada satu institusi dan satu mata kuliah, serta pengukuran error rate yang bergantung pada observasi langsung. Penelitian lanjutan disarankan untuk mereplikasi studi ini pada mata kuliah lain yang lebih praktik-intensif (seperti Jaringan Komputer) dan memperluas analisis per subdimensi CSUQ untuk menghasilkan rekomendasi yang lebih operasional.

---

## Daftar Pustaka

Alfita, I. N., dkk. (2024). Analisis Keefektifan Penggunaan Aplikasi Berbasis Web dan Mobile bagi Kegiatan Pembelajaran pada Mata Kuliah Sistem Operasi. *Jurnal Angka*, 1(1), 106–119.

Dalimunthe, A. M., dkk. (2025). Analisis Perbandingan Efisiensi Penggunaan E-Learning Berbasis Website dan Aplikasi Mobile dalam Proses Pembelajaran. *Jurnal Sistem Informasi STMIK Antar Bangsa*, 14(2), 60–64.

Lewis, J. R. (2002). Psychometric evaluation of the PSSUQ using data from five years of usability studies. *International Journal of Human-Computer Interaction*, 14(3–4), 463–488.

Prasetyaningsih, S., & Muchtar, S. P. N. (2023). Analisis Perbandingan User Experience pada Website dan Aplikasi Mobile Shopee menggunakan UEQ. *JTIM*, 5(3), 162–170.

Ridho, M. R., dkk. (2018). Perbandingan Performa Progressive Web Apps dan Mobile Web Terkait Waktu Respon, Penggunaan Memori dan Penggunaan Media Penyimpanan. *Jurnal Pengembangan Teknologi Informasi dan Ilmu Komputer*, 2(10), 3483–3491.

---

*(Dokumen ini merupakan draf mentah yang akan disesuaikan dengan template resmi dari penerbit jurnal sasaran.)*
