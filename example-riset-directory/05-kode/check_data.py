import pandas as pd
import numpy as np
import os


def validate_survey_data(filepath):
    print(f"=== Memulai Validasi Data: {filepath} ===")

    # 1. Cek apakah file ada
    if not os.path.exists(filepath):
        print(f"[ERROR] File {filepath} tidak ditemukan. Pastikan data dari Google Form sudah diunduh.")
        return

    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        print(f"[ERROR] Gagal membaca CSV. Pastikan format benar. Detail: {e}")
        return

    # 2. Cek Completeness (Missing Value)
    total_rows = len(df)
    print(f"\n[INFO] Total responden tercatat: {total_rows}")

    missing_data = df.isnull().sum()
    if missing_data.any():
        print("[WARNING] Ditemukan missing values (data tidak lengkap):")
        print(missing_data[missing_data > 0])
        print("-> Tindakan: Jika missing <= 10% per responden, gunakan mean imputation per subdimensi.")
        print("             Jika missing > 10% per responden, gunakan df.dropna() untuk listwise deletion.")
    else:
        print("[OK] Tidak ada data missing. Completeness 100%.")

    # 3. Cek Duplikat
    duplicates = df.duplicated(subset=['responden_id'])
    if duplicates.any():
        print(f"\n[WARNING] Ditemukan {duplicates.sum()} baris duplikat berdasarkan responden_id.")
        print("-> Tindakan: Hapus submisi kedua, pertahankan yang pertama.")
        df = df.drop_duplicates(subset=['responden_id'], keep='first')
        print(f"[OK] Duplikat sudah dihapus. Total responden setelah cleaning: {len(df)}")
    else:
        print("\n[OK] Tidak ada duplikat ditemukan.")

    # 4. Range & Logic Check untuk SUS (harus 0-100)
    if 'sus_total' in df.columns:
        out_of_bounds = df[(df['sus_total'] < 0) | (df['sus_total'] > 100)]
        if not out_of_bounds.empty:
            print(f"\n[WARNING] Anomali pada kolom sus_total! Ada nilai di luar 0-100:")
            print(out_of_bounds[['responden_id', 'sus_total']])
            print("-> Tindakan: Investigasi responden ini. Kemungkinan salah input atau salah paham instruksi SUS.")
        else:
            print(f"\n[OK] Range validasi sus_total aman (0-100). Semua nilai valid.")
    else:
        print("\n[INFO] Kolom sus_total tidak ditemukan. Pastikan header CSV sesuai.")

    # 5. Range & Logic Check untuk CSUQ (harus 1-7)
    csuq_cols = ['csuq_sysuse', 'csuq_infoqual', 'csuq_interqual', 'csuq_total']
    for col in csuq_cols:
        if col in df.columns:
            out_of_bounds = df[(df[col] < 1) | (df[col] > 7)]
            if not out_of_bounds.empty:
                print(f"\n[WARNING] Anomali pada kolom {col}! Ada nilai di luar 1-7:")
                print(out_of_bounds[['responden_id', col]])
            else:
                print(f"[OK] Range validasi {col} aman (1-7).")

    # 6. Outlier Check menggunakan IQR untuk SUS
    if 'sus_total' in df.columns:
        Q1 = df['sus_total'].quantile(0.25)
        Q3 = df['sus_total'].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[(df['sus_total'] < lower_bound) | (df['sus_total'] > upper_bound)]
        if not outliers.empty:
            print(f"\n[INFO] Terdeteksi outlier statistik (IQR) pada sus_total:")
            print(outliers[['responden_id', 'sus_total']])
            print(f"       Batas bawah: {lower_bound:.2f} | Batas atas: {upper_bound:.2f}")
            print("-> Catatan: Outlier statistik tidak wajib dihapus jika masih dalam range 0-100.")
            print("            Investigasi ke responden terkait sebelum memutuskan.")
        else:
            print(f"\n[OK] Tidak ada outlier statistik pada sus_total (IQR: {lower_bound:.2f} - {upper_bound:.2f}).")

    # 7. Statistik Deskriptif Singkat
    print("\n=== Statistik Deskriptif Awal ===")
    if 'sus_total' in df.columns:
        print(f"SUS Total  | Mean: {df['sus_total'].mean():.2f} | SD: {df['sus_total'].std():.2f} | n: {len(df)}")
    if 'csuq_total' in df.columns:
        print(f"CSUQ Total | Mean: {df['csuq_total'].mean():.2f} | SD: {df['csuq_total'].std():.2f} | n: {len(df)}")

    print("\n=== Validasi Selesai ===")
    return df


if __name__ == "__main__":
    print("Menjalankan skrip validasi data...\n")
    print("=" * 50)
    print("KELOMPOK WEB (Elena UNNES)")
    print("=" * 50)
    df_web = validate_survey_data('../04-data/kuesioner-web.csv')

    print("\n")
    print("=" * 50)
    print("KELOMPOK MOBILE")
    print("=" * 50)
    df_mobile = validate_survey_data('../04-data/kuesioner-mobile.csv')
