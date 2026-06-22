import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Buat direktori output jika belum ada
os.makedirs('../06-output/tables', exist_ok=True)
os.makedirs('../06-output/figures', exist_ok=True)


# ============================================================
# 1. BACA DAN GABUNGKAN DATA
# ============================================================
df_web = pd.read_csv('../04-data/kuesioner-web.csv')
df_mobile = pd.read_csv('../04-data/kuesioner-mobile.csv')
df = pd.concat([df_web, df_mobile], ignore_index=True)

# Pisahkan per kelompok
web_sus = df[df['platform'] == 'web']['sus_total']
mobile_sus = df[df['platform'] == 'mobile']['sus_total']
web_csuq = df[df['platform'] == 'web']['csuq_total']
mobile_csuq = df[df['platform'] == 'mobile']['csuq_total']


# ============================================================
# 2. STATISTIK DESKRIPTIF
# ============================================================
n_web, n_mobile = len(web_sus), len(mobile_sus)
m_web_sus, m_mobile_sus = np.mean(web_sus), np.mean(mobile_sus)
std_web_sus, std_mobile_sus = np.std(web_sus, ddof=1), np.std(mobile_sus, ddof=1)
m_web_csuq, m_mobile_csuq = np.mean(web_csuq), np.mean(mobile_csuq)
std_web_csuq, std_mobile_csuq = np.std(web_csuq, ddof=1), np.std(mobile_csuq, ddof=1)

desc_stats = pd.DataFrame({
    'Platform': ['Web (Elena UNNES)', 'Mobile'],
    'SUS_Mean': [round(m_web_sus, 2), round(m_mobile_sus, 2)],
    'SUS_SD': [round(std_web_sus, 2), round(std_mobile_sus, 2)],
    'CSUQ_Mean': [round(m_web_csuq, 2), round(m_mobile_csuq, 2)],
    'CSUQ_SD': [round(std_web_csuq, 2), round(std_mobile_csuq, 2)],
    'n': [n_web, n_mobile]
})

desc_stats.to_csv('../06-output/tables/descriptive_stats.csv', index=False)
print("[OK] descriptive_stats.csv berhasil dibuat.")


# ============================================================
# 3. UJI T-TEST MANUAL (tanpa scipy untuk portabilitas)
# ============================================================
def independent_t_test(group1, group2):
    n1, n2 = len(group1), len(group2)
    m1, m2 = np.mean(group1), np.mean(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    dof = n1 + n2 - 2
    sp = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / dof)
    t_stat = (m1 - m2) / (sp * np.sqrt(1 / n1 + 1 / n2))
    cohens_d = (m1 - m2) / sp
    # Estimasi p-value (gunakan library scipy untuk nilai exak)
    p_approx = "< 0.001" if abs(t_stat) > 3.3 else "> 0.05 (tidak signifikan)" if abs(t_stat) < 2.0 else "0.001 - 0.05"
    return round(t_stat, 3), dof, p_approx, round(cohens_d, 3)

t_sus, dof_sus, p_sus, d_sus = independent_t_test(web_sus, mobile_sus)
t_csuq, dof_csuq, p_csuq, d_csuq = independent_t_test(web_csuq, mobile_csuq)

t_test_results = pd.DataFrame({
    'Metrik': ['SUS Score', 'CSUQ Score'],
    't_statistic': [t_sus, t_csuq],
    'Degrees_of_Freedom': [dof_sus, dof_csuq],
    'p_value_approx': [p_sus, p_csuq],
    'Cohens_d': [d_sus, d_csuq]
})

t_test_results.to_csv('../06-output/tables/t_test_results.csv', index=False)
print("[OK] t_test_results.csv berhasil dibuat.")


# ============================================================
# 4. VISUALISASI 1: Grouped Bar Chart SUS + CSUQ
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# SUS Chart
bars1 = axes[0].bar(
    ['Web (Elena)', 'Mobile'],
    [m_web_sus, m_mobile_sus],
    yerr=[std_web_sus, std_mobile_sus],
    capsize=8,
    color=['#4C72B0', '#DD8452'],
    width=0.5
)
axes[0].axhline(y=68, color='red', linestyle='--', linewidth=1.5, label='Batas Kelayakan (68)')
axes[0].set_ylabel('Rata-rata Skor SUS')
axes[0].set_title('Perbandingan SUS Score')
axes[0].set_ylim(0, 100)
axes[0].legend()
for bar in bars1:
    axes[0].text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 8,
                 f'{bar.get_height():.1f}', ha='center', va='bottom',
                 color='white', fontweight='bold')

# CSUQ Chart
bars2 = axes[1].bar(
    ['Web (Elena)', 'Mobile'],
    [m_web_csuq, m_mobile_csuq],
    yerr=[std_web_csuq, std_mobile_csuq],
    capsize=8,
    color=['#4C72B0', '#DD8452'],
    width=0.5
)
axes[1].set_ylabel('Rata-rata Skor CSUQ')
axes[1].set_title('Perbandingan CSUQ Score')
axes[1].set_ylim(1, 7)
for bar in bars2:
    axes[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 0.4,
                 f'{bar.get_height():.2f}', ha='center', va='bottom',
                 color='white', fontweight='bold')

plt.suptitle('Perbandingan Kepuasan Pengguna: Platform Web vs Mobile\n(Mata Kuliah Sistem Operasi)',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('../06-output/figures/fig1_sus_csuq_comparison.png', dpi=300)
plt.close()
print("[OK] fig1_sus_csuq_comparison.png berhasil dibuat.")


# ============================================================
# 5. VISUALISASI 2: Box Plot Distribusi
# ============================================================
fig2, ax2 = plt.subplots(figsize=(8, 6))
bp = ax2.boxplot(
    [web_sus, mobile_sus],
    patch_artist=True,
    labels=['Web (Elena)', 'Mobile']
)
colors = ['#4C72B0', '#DD8452']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax2.axhline(y=68, color='red', linestyle='--', linewidth=1.5, label='Batas Kelayakan (68)')
ax2.set_ylabel('Skor SUS')
ax2.set_title('Distribusi Skor SUS per Platform')
ax2.legend()
plt.tight_layout()
plt.savefig('../06-output/figures/fig2_sus_distribution.png', dpi=300)
plt.close()
print("[OK] fig2_sus_distribution.png berhasil dibuat.")


# ============================================================
# 6. VISUALISASI 3: Radar Chart Subdimensi CSUQ
# ============================================================
categories = ['System\nUsefulness', 'Information\nQuality', 'Interface\nQuality']
web_vals = [
    df[df['platform'] == 'web']['csuq_sysuse'].mean(),
    df[df['platform'] == 'web']['csuq_infoqual'].mean(),
    df[df['platform'] == 'web']['csuq_interqual'].mean()
]
mobile_vals = [
    df[df['platform'] == 'mobile']['csuq_sysuse'].mean(),
    df[df['platform'] == 'mobile']['csuq_infoqual'].mean(),
    df[df['platform'] == 'mobile']['csuq_interqual'].mean()
]

N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
web_vals_plot = web_vals + [web_vals[0]]
mobile_vals_plot = mobile_vals + [mobile_vals[0]]
angles_plot = angles + [angles[0]]
categories_plot = categories + [categories[0]]

fig3, ax3 = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
ax3.plot(angles_plot, web_vals_plot, 'o-', linewidth=2, label='Web (Elena)', color='#4C72B0')
ax3.fill(angles_plot, web_vals_plot, alpha=0.25, color='#4C72B0')
ax3.plot(angles_plot, mobile_vals_plot, 's-', linewidth=2, label='Mobile', color='#DD8452')
ax3.fill(angles_plot, mobile_vals_plot, alpha=0.25, color='#DD8452')
ax3.set_thetagrids(np.degrees(angles), categories)
ax3.set_ylim(1, 7)
ax3.set_title('Profil Subdimensi CSUQ: Web vs Mobile', fontweight='bold', pad=20)
ax3.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.savefig('../06-output/figures/fig3_csuq_radar.png', dpi=300)
plt.close()
print("[OK] fig3_csuq_radar.png berhasil dibuat.")

print("\n=== Semua output berhasil dibuat di folder 06-output/ ===")
print(f"\nRingkasan Hasil:")
print(f"  SUS  | Web: {m_web_sus:.2f} ± {std_web_sus:.2f} | Mobile: {m_mobile_sus:.2f} ± {std_mobile_sus:.2f} | t={t_sus}, {p_sus}")
print(f"  CSUQ | Web: {m_web_csuq:.2f} ± {std_web_csuq:.2f} | Mobile: {m_mobile_csuq:.2f} ± {std_mobile_csuq:.2f} | t={t_csuq}, {p_csuq}")
