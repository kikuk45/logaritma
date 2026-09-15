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
# CUSTOM CSS AGRESIF - PAKSA TEMA KARTUN & LIGHT MODE
# -----------------------------------------------------------------------------
st.markdown("""

""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# HEADER APLIKASI
# -----------------------------------------------------------------------------
st.title("📐 Kalkulator & Learning Media Logaritma")
st.caption("Materi sesuai buku cetak Matematika Kelas X (Definisi & Sifat-Sifat Logaritma)")
st.divider()

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------------------------------------------------
st.sidebar.header("🎯 Navigasi Materi")

menu_options = {
    "Definisi Logaritma": "📘 Definisi Logaritma",
    "Sifat A": "🔹 Sifat a: Basis & Numerus Sama",
    "Sifat B": "🔹 Sifat b: Pangkat Numerus",
    "Sifat C": "🔹 Sifat c: Pangkat Basis & Numerus",
    "Sifat D": "🔹 Sifat d: Penjumlahan Logaritma",
    "Sifat E": "🔹 Sifat e: Pengurangan Logaritma",
    "Sifat F": "🔹 Sifat f: Perkalian Logaritma",
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
# KONTEN UTAMA (1 KOLOM KE BAWAH)
# -----------------------------------------------------------------------------
if selected_key == "Definisi Logaritma":
    st.header("📘 Definisi Logaritma")
    st.write("Bentuk umum logaritma adalah:")
    st.latex(r"^a\log x = n \iff a^n = x")

    st.write("**Keterangan:**")
    st.latex(r"a = \text{basis/bilangan pokok } (a > 0, a \neq 1)")
    st.latex(r"x = \text{numerus } (x > 0)")
    st.latex(r"n = \text{hasil logaritma}")
    st.divider()

    with st.container():
        st.subheader("A. Perpangkatan ➔ Logaritma")
        a_1 = st.number_input("Basis (a):", value=2, step=1, key="a_1")
        n_1 = st.number_input("Pangkat (n):", value=3, step=1, key="n_1")
        x_1 = int(math.pow(a_1, n_1)) if a_1 != 0 else 0
        st.divider()
        st.write("**Bentuk Pangkat:**"); st.latex(rf"{a_1}^{{{n_1}}} = {x_1}")
        st.write("**Bentuk Logaritma:**"); st.latex(rf"^{a_1}\log {x_1} = {n_1}")

    with st.container():
        st.subheader("B. Logaritma ➔ Perpangkatan")
        a_2 = st.number_input("Basis Log (a):", value=3, step=1, min_value=2, key="a_2")
        x_2 = st.number_input("Numerus (x):", value=81, step=1, min_value=1, key="x_2")
        try:
            n_2 = int(math.log(x_2, a_2))
            st.divider()
            st.write("**Bentuk Logaritma:**"); st.latex(rf"^{a_2}\log {x_2} = {n_2}")
            st.write("**Bentuk Pangkat:**"); st.latex(rf"{a_2}^{{{n_2}}} = {x_2}")
        except ValueError:
            st.error("Masukkan nilai numerus dan basis yang valid!")

elif selected_key == "Sifat A":
    st.markdown("### a. Syarat & Rumus Dasar:")
    st.latex(r"a > 0, \, a \neq 1")
    st.latex(r"^a\log 1 = 0 \quad \text{dan} \quad ^a\log a = 1")
    st.divider()
    a_val = st.number_input("Masukkan Nilai Basis (a):", value=5, step=1, min_value=2)
    with st.container():
        st.subheader("Sifat 1")
        st.latex(rf"^{a_val}\log 1 = 0")
    with st.container():
        st.subheader("Sifat 2")
        st.latex(rf"^{a_val}\log {a_val} = 1")

elif selected_key == "Sifat B":
    st.markdown("### b. Pangkat Numerus:")
    st.latex(r"^a\log x^n = n \cdot {}^a\log x")
    st.divider()
    a_s3 = st.number_input("Basis (a):", value=2, step=1, min_value=2, key="a_s3")
    x_base = st.number_input("Nilai dasar x:", value=2, step=1, min_value=1, key="x_s3")
    n_pangkat = st.number_input("Pangkat Numerus (n):", value=4, step=1, key="n_s3")
    numerus_total = int(math.pow(x_base, n_pangkat))
    st.divider()
    with st.container():
        st.subheader("📋 Langkah Penyelesaian:")
        val_base_log = int(math.log(x_base, a_s3))
        hasil_akhir = n_pangkat * val_base_log
        st.latex(rf"^{a_s3}\log ({x_base}^{{{n_pangkat}}}) = {n_pangkat} \cdot ^{a_s3}\log {x_base} = {hasil_akhir}")

elif selected_key == "Sifat C":
    st.markdown("### c. Pangkat Basis & Numerus:")
    st.latex(r"^{a^n}\log x^m = \frac{m}{n} \cdot {}^a\log x")
    st.divider()
    with st.container():
        a_base = st.number_input("Basis Utama (a):", value=2, step=1, min_value=2, key="a_base_s4")
        n_exp = st.number_input("Pangkat Basis (n):", value=2, step=1, min_value=1, key="n_exp_s4")
    with st.container():
        x_base = st.number_input("Numerus Utama (x):", value=2, step=1, min_value=1, key="x_base_s4")
        m_exp = st.number_input("Pangkat Numerus (m):", value=3, step=1, key="m_exp_s4")
    basis_total = int(math.pow(a_base, n_exp))
    numerus_total = int(math.pow(x_base, m_exp))
    st.divider()
    with st.container():
        st.subheader("📋 Langkah Penyelesaian:")
        base_log = int(math.log(x_base, a_base))
        pembagi_frac = Fraction(m_exp, n_exp) * base_log
        st.latex(rf"^{basis_total}\log {numerus_total} = \frac{{{m_exp}}}{{{n_exp}}} \cdot {base_log}")

elif selected_key == "Sifat D":
    st.markdown("### d. Penjumlahan Logaritma:")
    st.latex(r"^a\log x + {}^a\log y = {}^a\log(x \cdot y)")
    st.divider()
    a_d = st.number_input("Basis (a):", value=2, step=1, min_value=2, key="a_d")
    x_d = st.number_input("Numerus Pertama (x):", value=2, step=1, min_value=1, key="x_d")
    y_d = st.number_input("Numerus Kedua (y):", value=16, step=1, min_value=1, key="y_d")
    xy_prod = x_d * y_d
    st.divider()
    with st.container():
        st.subheader("📋 Langkah Penyelesaian:")
        st.latex(rf"^{a_d}\log {x_d} + ^{a_d}\log {y_d} = ^{a_d}\log ({x_d} \cdot {y_d}) = ^{a_d}\log {xy_prod}")

elif selected_key == "Sifat E":
    st.markdown("### e. Pengurangan Logaritma:")
    st.latex(r"^a\log x - {}^a\log y = {}^a\log\left(\frac{x}{y}\right)")
    st.divider()
    a_e = st.number_input("Basis (a):", value=2, step=1, min_value=2, key="a_e")
    x_e = st.number_input("Numerus Pertama (x):", value=32, step=1, min_value=1, key="x_e")
    y_e = st.number_input("Numerus Kedua (y):", value=2, step=1, min_value=1, key="y_e")
    st.divider()
    with st.container():
        st.subheader("📋 Langkah Penyelesaian:")
        st.latex(rf"^{a_e}\log {x_e} - ^{a_e}\log {y_e} = ^{a_e}\log \left(\frac{{{x_e}}}{{{y_e}}}\right)")

elif selected_key == "Sifat F":
    st.markdown("### f. Perkalian Logaritma Berantai:")
    st.latex(r"^a\log x \cdot {}^x\log y = {}^a\log y")
    st.divider()
    a_f = st.number_input("Basis Pertama (a):", value=2, step=1, min_value=2, key="a_f")
    x_f = st.number_input("Numerus 1 / Basis 2 (x):", value=3, step=1, min_value=2, key="x_f")
    y_f = st.number_input("Numerus Kedua (y):", value=16, step=1, min_value=1, key="y_f")
    st.divider()
    with st.container():
        st.subheader("📋 Langkah Penyelesaian:")
        st.latex(rf"^{a_f}\log {x_f} \cdot ^{x_f}\log {y_f} = ^{a_f}\log {y_f}")

elif selected_key == "Sifat G":
    st.markdown("### g. Mengubah Basis Logaritma:")
    st.latex(r"^a\log x = \frac{{}^b\log x}{{}^b\log a}")
    st.divider()
    with st.container():
        a_g = st.number_input("Basis Awal (a):", value=4, step=1, min_value=2, key="a_g")
        x_g = st.number_input("Numerus (x):", value=8, step=1, min_value=2, key="x_g")
        b_g = st.number_input("Basis Baru (b):", value=2, step=1, min_value=2, key="b_g")
        st.latex(rf"^{a_g}\log {x_g} = \frac{{^{b_g}\log {x_g}}}{{^{b_g}\log {a_g}}}")

elif selected_key == "Sifat H":
    st.markdown("### h. Eksponen Logaritma Basis Sama:")
    st.latex(r"a^{{}^a\log x} = x")
    st.divider()
    a_h = st.number_input("Basis (a):", value=2, step=1, min_value=2, key="a_h")
    x_h = st.number_input("Numerus (x):", value=7, step=1, min_value=1, key="x_h")
    st.divider()
    with st.container():
        st.latex(rf"{a_h}^{{^{a_h}\log {x_h}}} = {x_h}")

elif selected_key == "Sifat I":
    st.markdown("### i. Eksponen Logaritma Berkoefisien:")
    st.latex(r"a^{n \cdot {}^a\log x} = x^n")
    st.divider()
    a_i = st.number_input("Basis (a):", value=3, step=1, min_value=2, key="a_i")
    n_i = st.number_input("Koefisien (n):", value=2, step=1, key="n_i")
    x_i = st.number_input("Numerus (x):", value=5, step=1, min_value=1, key="x_i")
    hasil_i = int(math.pow(x_i, n_i))
    st.divider()
    with st.container():
        st.latex(rf"{a_i}^{{{n_i} \cdot ^{a_i}\log {x_i}}} = {x_i}^{{{n_i}}} = {hasil_i}")

# -----------------------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------------------
st.sidebar.divider()
st.sidebar.caption("Oleh : Mochammad Rifqi Al Khadziq")
