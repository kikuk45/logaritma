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
)

st.title("📐 Kalkulator & Learning Media Logaritma")
st.caption("Materi sesuai buku cetak Matematika Kelas X (Definisi & Sifat-Sifat Logaritma)")

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------------------------------------------------
st.sidebar.header("🎯 Pilih Materi/Sifat")
menu = st.sidebar.radio(
    "Navigasi Modul:",
    [
        "1. Definisi Logaritma",
        "a. Untuk a > 0 dan a ≠ 1, berlaku:",
        "b. Untuk a > 0, a ≠ 1, x > 0 dan a, n, x ∈ R, berlaku:",
        "c. Untuk a > 0, a ≠ 1, x > 0 dan a, m, n, x ∈ R, berlaku:",
    ],
)

# -----------------------------------------------------------------------------
# MENU 1: DEFINISI LOGARITMA
# -----------------------------------------------------------------------------
if menu == "1. Definisi Logaritma":
    st.header("1. Definisi Logaritma")
    st.write("Bentuk umum logaritma adalah:")

    st.latex(r"^a\log x = n \iff a^n = x")

    st.write("**Keterangan:**")
    st.latex(r"a = \text{basis/bilangan pokok } (a > 0, a \neq 1)")
    st.latex(r"x = \text{numerus } (x > 0)")
    st.latex(r"n = \text{hasil logaritma}")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("A. Perpangkatan ➔ Logaritma")
        st.caption("Ubah bentuk perpangkatan menjadi logaritma")

        a_1 = st.number_input("Basis (a):", value=2, step=1, key="a_1")
        n_1 = st.number_input("Pangkat (n):", value=3, step=1, key="n_1")

        x_1 = int(math.pow(a_1, n_1)) if a_1 != 0 else 0

        st.divider()
        st.write("**Bentuk Pangkat:**")
        st.latex(rf"{a_1}^{{{n_1}}} = {x_1}")
        
        st.write("**Bentuk Logaritma:**")
        st.latex(rf"^{{{a_1}}}\log({{{x_1}}}) = {n_1}")

    with col2:
        st.subheader("B. Logaritma ➔ Perpangkatan")
        st.caption("Ubah bentuk logaritma menjadi perpangkatan")

        a_2 = st.number_input("Basis Log (a):", value=3, step=1, min_value=2, key="a_2")
        x_2 = st.number_input("Numerus (x):", value=81, step=1, min_value=1, key="x_2")

        try:
            n_2 = int(math.log(x_2, a_2))
            st.divider()
            st.write("**Bentuk Logaritma:**")
            st.latex(rf"^{{{a_2}}}\log({{{x_2}}}) = {n_2}")
            
            st.write("**Bentuk Pangkat:**")
            st.latex(rf"{a_2}^{{{n_2}}} = {x_2}")
        except ValueError:
            st.error("Masukkan nilai numerus dan basis yang valid!")

# -----------------------------------------------------------------------------
# MENU 2: SIFAT DASAR (POIN A)
# -----------------------------------------------------------------------------
elif menu == "a. Untuk a > 0 dan a ≠ 1, berlaku:":
    st.header("a. Untuk a > 0 dan a ≠ 1, berlaku:")

    st.latex(r"^a\log 1 = 0 \quad \text{dan} \quad ^a\log a = 1")

    st.divider()
    a_val = st.number_input("Masukkan Nilai Basis (a):", value=5, step=1, min_value=2)

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("Sifat 1")
            st.latex(rf"^{{{a_val}}}\log 1 = 0")
            st.caption(f"Bukti: {a_val}⁰ = 1")

    with col2:
        with st.container(border=True):
            st.subheader("Sifat 2")
            st.latex(rf"^{{{a_val}}}\log {a_val} = 1")
            st.caption(f"Bukti: {a_val}¹ = {a_val}")

# -----------------------------------------------------------------------------
# MENU 3: SIFAT PANGKAT NUMERUS (POIN B)
# -----------------------------------------------------------------------------
elif menu == "b. Untuk a > 0, a ≠ 1, x > 0 dan a, n, x ∈ R, berlaku:":
    st.header("b. Untuk a > 0, a ≠ 1, x > 0 dan a, n, x ∈ R, berlaku:")

    st.latex(r"^a\log x^n = n \cdot {}^a\log x")

    st.divider()
    col1, col2, col3 = st.columns(3)

    with col1:
        a_s3 = st.number_input("Basis (a):", value=2, step=1, min_value=2, key="a_s3")
    with col2:
        x_base = st.number_input("Nilai dasar x:", value=2, step=1, min_value=1, key="x_s3")
    with col3:
        n_pangkat = st.number_input("Pangkat Numerus (n):", value=4, step=1, key="n_s3")

    numerus_total = int(math.pow(x_base, n_pangkat))

    st.divider()
    st.subheader("📋 Langkah Penyelesaian:")

    val_base_log = int(math.log(x_base, a_s3))
    hasil_akhir = n_pangkat * val_base_log

    st.write("1. Bentuk Soal Sesuai Sifat:")
    st.latex(rf"^{{{a_s3}}}\log({x_base}^{{{n_pangkat}}}) = {n_pangkat} \cdot ^{{{a_s3}}}\log({x_base})")
    
    st.write("2. Substitusi Hasil:")
    st.latex(rf"= {n_pangkat} \cdot {val_base_log}")

    st.write("3. Hasil Akhir:")
    st.latex(rf"^{{{a_s3}}}\log({numerus_total}) = {hasil_akhir}")

# -----------------------------------------------------------------------------
# MENU 4: SIFAT PANGKAT BASIS & NUMERUS (POIN C)
# -----------------------------------------------------------------------------
elif menu == "c. Untuk a > 0, a ≠ 1, x > 0 dan a, m, n, x ∈ R, berlaku:":
    st.header("c. Untuk a > 0, a ≠ 1, x > 0 dan a, m, n, x ∈ R, berlaku:")

    st.latex(r"^{a^n}\log x^m = \frac{m}{n} \cdot {}^a\log x")

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Input Basis (\(a^n\))")
        a_base = st.number_input("Basis Utama (a):", value=2, step=1, min_value=2, key="a_base_s4")
        n_exp = st.number_input("Pangkat Basis (n):", value=2, step=1, min_value=1, key="n_exp_s4")

    with col2:
        st.subheader("Input Numerus (\(x^m\))")
        x_base = st.number_input("Numerus Utama (x):", value=2, step=1, min_value=1, key="x_base_s4")
        m_exp = st.number_input("Pangkat Numerus (m):", value=3, step=1, key="m_exp_s4")

    basis_total = int(math.pow(a_base, n_exp))
    numerus_total = int(math.pow(x_base, m_exp))

    st.divider()
    st.subheader("📋 Langkah Penyelesaian:")

    base_log = int(math.log(x_base, a_base))
    pembagi_frac = Fraction(m_exp, n_exp) * base_log

    if pembagi_frac.denominator == 1:
        hasil_latex = f"{pembagi_frac.numerator}"
    else:
        hasil_latex = f"\\frac{{{pembagi_frac.numerator}}}{{{pembagi_frac.denominator}}}"

    st.write("1. Bentuk Soal Disederhanakan:")
    st.latex(rf"^{{{basis_total}}}\log({numerus_total}) \implies ^{{{a_base}^{{{n_exp}}}}}\log({x_base}^{{{m_exp}}})")
    
    st.write("2. Gunakan Rumus Sifat:")
    st.latex(rf"\frac{{{m_exp}}}{{{n_exp}}} \cdot ^{{{a_base}}}\log({x_base}) = \frac{{{m_exp}}}{{{n_exp}}} \cdot {base_log}")

    st.write("3. Hasil Akhir:")
    st.latex(rf"^{{{basis_total}}}\log({numerus_total}) = {hasil_latex}")

# -----------------------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------------------
st.sidebar.divider()
st.sidebar.caption("Oleh : Mochammad Rifqi Al Khadziq")
