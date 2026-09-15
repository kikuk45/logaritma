from decimal import Decimal
from fractions import Fraction
import math
import streamlit as st

# -----------------------------------------------------------------------------
# KONFIGURASI HALAMAN
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Modul & Kalkulator Logaritma Interaktif",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# HEADER APLIKASI
# -----------------------------------------------------------------------------
st.title("📐 Learning Media & Kalkulator Logaritma")
st.caption("Materi Pembelajaran Matematika Kelas X — Definisi & Sifat-Sifat Logaritma")
st.divider()

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION (Dibuat Ringkas agar Tidak Berantakan)
# -----------------------------------------------------------------------------
st.sidebar.header("🎯 Navigasi Materi")

# Mapping label ringkas untuk sidebar -> judul lengkap materi
menu_options = {
    "Definisi Logaritma": "📘 Definisi Logaritma",
    "Sifat A": "🔹 Sifat a: Basis & Numerus Sama",
    "Sifat B": "🔹 Sifat b: Pangkat Numerus",
    "Sifat C": "🔹 Sifat c: Pangkat Basis & Numerus",
    "Sifat D": "🔹 Sifat d: Penjumlahan Logaritma",
    "Sifat E": "🔹 Sifat e: Pengurangan Logaritma",
    "Sifat F": "🔹 Sifat f: Perkalian Logaritma Berantai",
    "Sifat G": "🔹 Sifat g: Mengubah Basis Logaritma",
    "Sifat H": "🔹 Sifat h: Eksponen Logaritma Basis Sama",
    "Sifat I": "🔹 Sifat i: Eksponen Logaritma Berkoefisien",
}

selected_key = st.sidebar.radio(
    "Pilih Sub-materi / Sifat:",
    options=list(menu_options.keys()),
    format_func=lambda x: menu_options[x],
)

# -----------------------------------------------------------------------------
# MENU 1: DEFINISI LOGARITMA
# -----------------------------------------------------------------------------
if selected_key == "Definisi Logaritma":
    st.header("📘 Definisi Logaritma")
    
    st.info("**Bentuk Umum Logaritma:**\n\n" r"
$$^a\log x = n \iff a^n = x$$")with st.expander("📌 Keterangan Komponen Logaritma", expanded=True):
    col_k1, col_k2, col_k3 = st.columns(3)
    col_k1.markdown("**\(a\)** = Basis / Bilangan Pokok (\(a > 0, a \\neq 1\))")
    col_k2.markdown("**\(x\)** = Numerus (\(x > 0\))")
    col_k3.markdown("**\(n\)** = Hasil Logaritma")

st.subheader("⚡ Kalkulator Konversi Interaktif")
col1, col2 = st.columns(2, gap="large")

with col1:
    with st.container(border=True):
        st.markdown("#### A. Perpangkatan ➔ Logaritma")
        st.caption("Ubah bentuk perpangkatan menjadi logaritma")
        a_1 = st.number_input("Basis (\(a\)):", value=2, step=1, key="a_1")
        n_1 = st.number_input("Pangkat (\(n\)):", value=3, step=1, key="n_1")
        x_1 = int(math.pow(a_1, n_1)) if a_1 != 0 else 0

        st.divider()
        st.success(f"**Bentuk Pangkat:** \({a_1}^{{{n_1}}} = {x_1}\)\n\n"
                   f"**Bentuk Logaritma:** \(^{{{a_1}}}\\log({{{x_1}}}) = {n_1}\)")

with col2:
    with st.container(border=True):
        st.markdown("#### B. Logaritma ➔ Perpangkatan")
        st.caption("Ubah bentuk logaritma menjadi perpangkatan")
        a_2 = st.number_input("Basis Log (\(a\)):", value=3, step=1, min_value=2, key="a_2")
        x_2 = st.number_input("Numerus (\(x\)):", value=81, step=1, min_value=1, key="x_2")

        try:
            n_2 = int(math.log(x_2, a_2))
            st.divider()
            st.success(f"**Bentuk Logaritma:** \(^{{{a_2}}}\\log({{{x_2}}}) = {n_2}\)\n\n"
                       f"**Bentuk Pangkat:** \({a_2}^{{{n_2}}} = {x_2}\)")
        except ValueError:
            st.error("Masukkan nilai numerus dan basis yang valid!")
-----------------------------------------------------------------------------MENU 2: SIFAT DASAR (POIN A)-----------------------------------------------------------------------------elif selected_key == "Sifat A":st.header("a. Untuk $a > 0$ dan $a \neq 1$, berlaku:")st.info(r"$$^a\log 1 = 0 \quad \text{dan} \quad ^a\log a = 1$$")a_val = st.number_input("Masukkan Nilai Basis (\(a\)):", value=5, step=1, min_value=2)
col1, col2 = st.columns(2, gap="large")

with col1:
    with st.container(border=True):
        st.markdown("### Sifat 1")
        st.latex(rf"^{{{a_val}}}\log 1 = 0")
        st.caption(f"💡 Bukti Eksponensial: {a_val}⁰ = 1")

with col2:
    with st.container(border=True):
        st.markdown("### Sifat 2")
        st.latex(rf"^{{{a_val}}}\log {a_val} = 1")
        st.caption(f"💡 Bukti Eksponensial: {a_val}¹ = {a_val}")
-----------------------------------------------------------------------------MENU 3: SIFAT PANGKAT NUMERUS (POIN B)-----------------------------------------------------------------------------elif selected_key == "Sifat B":st.header("b. Untuk $a > 0, a \neq 1, x > 0$ dan $a, n, x \in \mathbb{R}$, berlaku:")st.info(r"$$^a\log x^n = n \cdot {}^a\log x$$")with st.container(border=True):
    st.markdown("#### 🧮 Input Parameter")
    col1, col2, col3 = st.columns(3)
    with col1:
        a_s3 = st.number_input("Basis (\(a\)):", value=2, step=1, min_value=2, key="a_s3")
    with col2:
        x_base = st.number_input("Nilai Dasar (\(x\)):", value=2, step=1, min_value=1, key="x_s3")
    with col3:
        n_pangkat = st.number_input("Pangkat Numerus (\(n\)):", value=4, step=1, key="n_s3")

numerus_total = int(math.pow(x_base, n_pangkat))
val_base_log = int(math.log(x_base, a_s3))
hasil_akhir = n_pangkat * val_base_log

with st.container(border=True):
    st.markdown("#### 📋 Langkah Penyelesaian:")
    st.write("1. Bentuk Soal Sesuai Sifat:")
    st.latex(rf"^{{{a_s3}}}\log({x_base}^{{{n_pangkat}}}) = {n_pangkat} \cdot ^{{{a_s3}}}\log({x_base})")
    st.write("2. Substitusi Hasil Logaritma Dasar:")
    st.latex(rf"= {n_pangkat} \cdot {val_base_log}")
    st.write("3. Hasil Akhir:")
    st.success(rf"
$$^{{{a_s3}}}\log({numerus_total}) = {hasil_akhir}$$")-----------------------------------------------------------------------------MENU 4: SIFAT PANGKAT BASIS & NUMERUS (POIN C)-----------------------------------------------------------------------------elif selected_key == "Sifat C":st.header("c. Untuk $a > 0, a \neq 1, x > 0$ dan $a, m, n, x \in \mathbb{R}$, berlaku:")st.info(r"$$^{a^n}\log x^m = \frac{m}{n} \cdot {}^a\log x$$")with st.container(border=True):
    st.markdown("#### 🧮 Input Parameter")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Basis (\(a^n\))**")
        a_base = st.number_input("Basis Utama (\(a\)):", value=2, step=1, min_value=2, key="a_base_s4")
        n_exp = st.number_input("Pangkat Basis (\(n\)):", value=2, step=1, min_value=1, key="n_exp_s4")
    with col2:
        st.markdown("**Numerus (\(x^m\))**")
        x_base = st.number_input("Numerus Utama (\(x\)):", value=2, step=1, min_value=1, key="x_base_s4")
        m_exp = st.number_input("Pangkat Numerus (\(m\)):", value=3, step=1, key="m_exp_s4")

basis_total = int(math.pow(a_base, n_exp))
numerus_total = int(math.pow(x_base, m_exp))
base_log = int(math.log(x_base, a_base))
pembagi_frac = Fraction(m_exp, n_exp) * base_log

hasil_latex = f"{pembagi_frac.numerator}" if pembagi_frac.denominator == 1 else f"\\frac{{{pembagi_frac.numerator}}}{{{pembagi_frac.denominator}}}"

with st.container(border=True):
    st.markdown("#### 📋 Langkah Penyelesaian:")
    st.write("1. Bentuk Soal Disederhanakan:")
    st.latex(rf"^{{{basis_total}}}\log({numerus_total}) \implies ^{{{a_base}^{{{n_exp}}}}}\log({x_base}^{{{m_exp}}})")
    st.write("2. Gunakan Rumus Sifat:")
    st.latex(rf"\frac{{{m_exp}}}{{{n_exp}}} \cdot ^{{{a_base}}}\log({x_base}) = \frac{{{m_exp}}}{{{n_exp}}} \cdot {base_log}")
    st.write("3. Hasil Akhir:")
    st.success(rf"
$$^{{{basis_total}}}\log({numerus_total}) = {hasil_latex}$$")-----------------------------------------------------------------------------MENU 5: PENJUMLAHAN LOGARITMA (POIN D)-----------------------------------------------------------------------------elif selected_key == "Sifat D":st.header("d. Untuk $a > 0, a \neq 1, x > 0, y > 0$ dan $a, x, y \in \mathbb{R}$, berlaku:")st.info(r"$$^a\log x + {}^a\log y = {}^a\log(x \cdot y)$$")with st.container(border=True):
    st.markdown("#### 🧮 Input Parameter")
    col1, col2, col3 = st.columns(3)
    with col1:
        a_d = st.number_input("Basis (\(a\)):", value=2, step=1, min_value=2, key="a_d")
    with col2:
        x_d = st.number_input("Numerus Pertama (\(x\)):", value=2, step=1, min_value=1, key="x_d")
    with col3:
        y_d = st.number_input("Numerus Kedua (\(y\)):", value=16, step=1, min_value=1, key="y_d")

xy_prod = x_d * y_d

with st.container(border=True):
    st.markdown("#### 📋 Langkah Penyelesaian:")
    st.write("1. Gabungkan Numerus (Perkalian):")
    st.latex(rf"^{{{a_d}}}\log({x_d}) + ^{{{a_d}}}\log({y_d}) = ^{{{a_d}}}\log({x_d} \cdot {y_d})")
    st.write("2. Hasil Perkalian Numerus:")
    st.latex(rf"= ^{{{a_d}}}\log({xy_prod})")

    try:
        val_res = math.log(xy_prod, a_d)
        if val_res.is_integer():
            st.write("3. Hasil Akhir:")
            st.success(rf"
$$= {int(val_res)}$$")except ValueError:pass-----------------------------------------------------------------------------MENU 6: PENGURANGAN LOGARITMA (POIN E)-----------------------------------------------------------------------------elif selected_key == "Sifat E":st.header("e. Untuk $a > 0, a \neq 1, x > 0, y > 0$ dan $a, x, y \in \mathbb{R}$, berlaku:")st.info(r"$$^a\log x - {}^a\log y = {}^a\log\left(\frac{x}{y}\right)$$")with st.container(border=True):
    st.markdown("#### 🧮 Input Parameter")
    col1, col2, col3 = st.columns(3)
    with col1:
        a_e = st.number_input("Basis (\(a\)):", value=2, step=1, min_value=2, key="a_e")
    with col2:
        x_e = st.number_input("Numerus Pertama (\(x\)):", value=32, step=1, min_value=1, key="x_e")
    with col3:
        y_e = st.number_input("Numerus Kedua (\(y\)):", value=2, step=1, min_value=1, key="y_e")

div_frac = Fraction(x_e, y_e)
xy_div_str = f"{div_frac.numerator}" if div_frac.denominator == 1 else f"\\frac{{{div_frac.numerator}}}{{{div_frac.denominator}}}"

with st.container(border=True):
    st.markdown("#### 📋 Langkah Penyelesaian:")
    st.write("1. Gabungkan Numerus (Pembagian):")
    st.latex(rf"^{{{a_e}}}\log({x_e}) - ^{{{a_e}}}\log({y_e}) = ^{{{a_e}}}\log\left(\frac{{{x_e}}}{{{y_e}}}\right)")
    st.write("2. Hasil Pembagian Numerus:")
    st.latex(rf"= ^{{{a_e}}}\log\left({xy_div_str}\right)")

    try:
        val_res = math.log(x_e / y_e, a_e)
        if val_res.is_integer():
            st.write("3. Hasil Akhir:")
            st.success(rf"
$$= {int(val_res)}$$")except ValueError:pass-----------------------------------------------------------------------------MENU 7: PERKALIAN LOGARITMA (POIN F)-----------------------------------------------------------------------------elif selected_key == "Sifat F":st.header("f. Untuk $a > 0, a \neq 1, x > 0, y > 0$ dan $a, x, y \in \mathbb{R}$, berlaku:")st.info(r"$$^a\log x \cdot {}^x\log y = {}^a\log y$$")with st.container(border=True):
    st.markdown("#### 🧮 Input Parameter")
    col1, col2, col3 = st.columns(3)
    with col1:
        a_f = st.number_input("Basis Pertama (\(a\)):", value=2, step=1, min_value=2, key="a_f")
    with col2:
        x_f = st.number_input("Numerus 1 / Basis 2 (\(x\)):", value=3, step=1, min_value=2, key="x_f")
    with col3:
        y_f = st.number_input("Numerus Kedua (\(y\)):", value=16, step=1, min_value=1, key="y_f")

with st.container(border=True):
    st.markdown("#### 📋 Langkah Penyelesaian:")
    st.write("1. Bentuk Perkalian Logaritma Berantai:")
    st.latex(rf"^{{{a_f}}}\log({x_f}) \cdot ^{{{x_f}}}\log({y_f})")
    st.write("2. Penyederhanaan (Saling Menghilangkan \(x\)):")
    st.latex(rf"= ^{{{a_f}}}\log({y_f})")

    try:
        val_res = math.log(y_f, a_f)
        if val_res.is_integer():
            st.write("3. Hasil Akhir:")
            st.success(rf"
$$= {int(val_res)}$$")except ValueError:pass-----------------------------------------------------------------------------MENU 8: MENGUBAH BASIS LOGARITMA (POIN G)-----------------------------------------------------------------------------elif selected_key == "Sifat G":st.header("g. Untuk $a > 0, a \neq 1, b > 0, b \neq 1, x > 0$ dan $a, b, x \in \mathbb{R}$, berlaku:")st.info(r"$$^a\log x = \frac{{}^b\log x}{{}^b\log a} = \frac{1}{{}^x\log a}$$")col1, col2 = st.columns(2, gap="large")

with col1:
    with st.container(border=True):
        st.markdown("#### A. Mengubah Basis ke-\(b\)")
        a_g = st.number_input("Basis Awal (\(a\)):", value=4, step=1, min_value=2, key="a_g")
        x_g = st.number_input("Numerus (\(x\)):", value=8, step=1, min_value=2, key="x_g")
        b_g = st.number_input("Basis Baru (\(b\)):", value=2, step=1, min_value=2, key="b_g")

        st.write("**Proses Ubah Basis:**")
        st.latex(rf"^{{{a_g}}}\log({x_g}) = \frac{{^{{{b_g}}}\log({x_g})}}{{^{{{b_g}}}\log({a_g})}}")

        try:
            log_bx = math.log(x_g, b_g)
            log_ba = math.log(a_g, b_g)
            frac_res = Fraction(Decimal(str(log_bx / log_ba))).limit_denominator() if not (log_bx/log_ba).is_integer() else int(log_bx/log_ba)
            
            res_str = f"\\frac{{{frac_res.numerator}}}{{{frac_res.denominator}}}" if isinstance(frac_res, Fraction) else f"{frac_res}"

            st.success(rf"**Hasil Akhir:** = \(\frac{{{int(log_bx) if log_bx.is_integer() else round(log_bx, 2)}}}{{{int(log_ba) if log_ba.is_integer() else round(log_ba, 2)}}} = {res_str}\)")
        except Exception:
            pass

with col2:
    with st.container(border=True):
        st.markdown("#### B. Kebalikan Basis & Numerus")
        a_g2 = st.number_input("Basis Awal (\(a\)):", value=2, step=1, min_value=2, key="a_g2")
        x_g2 = st.number_input("Numerus (\(x\)):", value=8, step=1, min_value=2, key="x_g2")

        st.write("**Bentuk Kebalikan:**")
        st.latex(rf"^{{{a_g2}}}\log({x_g2}) = \frac{{1}}{{^{{{x_g2}}}\log({a_g2})}}")
-----------------------------------------------------------------------------MENU 9: PANGKAT EKSPLISIT LOGARITMA (POIN H)-----------------------------------------------------------------------------elif selected_key == "Sifat H":st.header("h. Untuk $a > 0, a \neq 1, x > 0$ dan $a, x \in \mathbb{R}$, berlaku:")st.info(r"$$a^{{}^a\log x} = x$$")with st.container(border=True):
    st.markdown("#### 🧮 Input Parameter")
    col1, col2 = st.columns(2)
    with col1:
        a_h = st.number_input("Basis Utama / Basis Log (\(a\)):", value=2, step=1, min_value=2, key="a_h")
    with col2:
        x_h = st.number_input("Numerus (\(x\)):", value=7, step=1, min_value=1, key="x_h")

with st.container(border=True):
    st.markdown("#### 📋 Langkah Penyelesaian:")
    st.write("1. Bentuk Pangkat Logaritma:")
    st.latex(rf"{a_h}^{{^{{{a_h}}}\log({x_h})}}")
    st.write("2. Berdasarkan Sifat (Basis Pangkat == Basis Logaritma):")
    st.success(rf"
$$= {x_h}$$")-----------------------------------------------------------------------------MENU 10: PANGKAT KOEFISIEN LOGARITMA (POIN I)-----------------------------------------------------------------------------elif selected_key == "Sifat I":st.header("i. Untuk $a > 0, a \neq 1, x > 0$ dan $a, x, n \in \mathbb{R}$, berlaku:")st.info(r"$$a^{n \cdot {}^a\log x} = x^n$$")with st.container(border=True):
    st.markdown("#### 🧮 Input Parameter")
    col1, col2, col3 = st.columns(3)
    with col1:
        a_i = st.number_input("Basis Utama / Basis Log (\(a\)):", value=3, step=1, min_value=2, key="a_i")
    with col2:
        n_i = st.number_input("Koefisien Pangkat (\(n\)):", value=2, step=1, key="n_i")
    with col3:
        x_i = st.number_input("Numerus Logaritma (\(x\)):", value=5, step=1, min_value=1, key="x_i")

hasil_i = int(math.pow(x_i, n_i))

with st.container(border=True):
    st.markdown("#### 📋 Langkah Penyelesaian:")
    st.write("1. Bentuk Soal Sesuai Sifat:")
    st.latex(rf"{a_i}^{{{n_i} \cdot ^{{{a_i}}}\log({x_i})}}")
    st.write("2. Pindahkan Koefisien Menjadi Pangkat Numerus:")
    st.latex(rf"= {a_i}^{{^{{{a_i}}}\log({x_i}^{{{n_i}}})}}")
    st.write("3. Hasil Akhir:")
    st.success(rf"
$$= {x_i}^{{{n_i}}} = {hasil_i}$$")-----------------------------------------------------------------------------FOOTER-----------------------------------------------------------------------------st.sidebar.divider()st.sidebar.caption("👨‍🏫 Pengembang Modul:\nMochammad Rifqi Al Khadziq")
