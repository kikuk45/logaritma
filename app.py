import streamlit as st
import math

# Konfigurasi Halaman
st.set_page_config(
    page_title="Kalkulator & Belajar Logaritma",
    page_icon="📐",
    layout="wide"
)

st.title("📐 Media Pembelajaran & Kalkulator Logaritma")
st.write("Aplikasi bantu untuk memahami konsep dasar, konversi bentuk, dan sifat-sifat logaritma.")

# Sidebar Navigation
menu = st.sidebar.selectbox(
    "Pilih Menu:",
    ["1. Konversi Forms (Pangkat ↔ Logaritma)", 
     "2. Sifat Dasar ($a > 0, a \\neq 1$)", 
     "3. Sifat Eksponen ($^a\\log x^n$)"]
)

# -----------------------------------------------------------------------------
# MENU 1: KONVERSI BENTUK
# -----------------------------------------------------------------------------
if menu == "1. Konversi Forms (Pangkat ↔ Logaritma)":
    st.header("🔄 Konversi Bentuk Perpangkatan & Logaritma")
    st.latex(r"a^b = c \iff {}^a\log c = b")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Bentuk Pangkat ke Logaritma")
        a_pangkat = st.number_input("Masukkan Basis (a):", value=2.0, key="a_p")
        b_pangkat = st.number_input("Masukkan Eksponen (b):", value=3.0, key="b_p")
        c_pangkat = a_pangkat ** b_pangkat
        
        st.info(f"**Bentuk Pangkat:** ${a_pangkat}^{{{b_pangkat}}} = {c_pangkat}$")
        st.success(f"**Bentuk Logaritma:** ${{{a_pangkat}}}\\log({{{c_pangkat}}}) = {b_pangkat}$")

    with col2:
        st.subheader("Bentuk Logaritma ke Pangkat")
        a_log = st.number_input("Masukkan Basis Log (a):", value=2.0, min_value=0.0001, key="a_l")
        c_log = st.number_input("Masukkan Numerus (c):", value=8.0, min_value=0.0001, key="c_l")
        
        if a_log == 1:
            st.error("Basis (a) tidak boleh sama dengan 1!")
        else:
            b_log = math.log(c_log, a_log)
            st.info(f"**Bentuk Logaritma:** ${{{a_log}}}\\log({{{c_log}}}) = {b_log:.4f}$")
            st.success(f"**Bentuk Pangkat:** ${a_log}^{{{b_log:.4f}}} = {c_log}$")

# -----------------------------------------------------------------------------
# MENU 2: SIFAT DASAR LOGARITMA
# -----------------------------------------------------------------------------
elif menu == "2. Sifat Dasar ($a > 0, a \\neq 1$)":
    st.header("📌 Sifat Dasar Logaritma")
    st.caption("Syarat: $a > 0$ dan $a \\neq 1$")
    
    a = st.number_input("Masukkan Nilai Basis (a):", value=5.0, min_value=0.0001, key="sifat1_a")
    
    if a == 1:
        st.error("Basis (a) tidak boleh bernilai 1.")
    else:
        st.subheader("1. $^a\\log a = 1$")
        res1 = math.log(a, a)
        st.write(f"Hitung: ${{{a}}}\\log({{{a}}}) = {int(res1)}$")
        
        st.subheader("2. $^a\\log 1 = 0$")
        res2 = math.log(1, a)
        st.write(f"Hitung: ${{{a}}}\\log(1) = {int(res2)}$")

# -----------------------------------------------------------------------------
# MENU 3: SIFAT EKSPONEN NUMERUS
# -----------------------------------------------------------------------------
elif menu == "3. Sifat Eksponen ($^a\\log x^n$)":
    st.header("📌 Sifat Eksponen Logaritma")
    st.caption("Syarat: $a > 0, a \\neq 1, x > 0$ dan $a, n, x \\in \\mathbb{R}$")
    st.latex(r"^a\log(x^n) = n \cdot {}^a\log x")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        a_s3 = st.number_input("Basis (a):", value=2.0, min_value=0.0001, key="a_s3")
    with col2:
        x_s3 = st.number_input("Nilai (x):", value=4.0, min_value=0.0001, key="x_s3")
    with col3:
        n_s3 = st.number_input("Pangkat Numerus (n):", value=3.0, key="n_s3")
        
    if a_s3 == 1:
        st.error("Basis (a) tidak boleh bernilai 1.")
    else:
        # Perhitungan ruas kiri & kanan
        ruas_kiri = math.log(x_s3 ** n_s3, a_s3)
        log_x = math.log(x_s3, a_s3)
        ruas_kanan = n_s3 * log_x
        
        st.markdown("---")
        st.subheader("Langkah Perhitungan:")
        st.write(f"**Bentuk:** ${{{a_s3}}}\\log({{{x_s3}}}^{{{n_s3}}})$")
        st.write(f"**Sifat:** $n \\cdot {{{a_s3}}}\\log({{{x_s3}}}) = {n_s3} \\cdot {log_x:.4f}$")
        
        st.success(f"**Hasil Akhir:** {ruas_kanan:.4f}")
