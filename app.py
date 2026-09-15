import base64
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
# BACKGROUND IMAGE (bg_siswa.png)
# -----------------------------------------------------------------------------
def set_background(image_file: str):
    """Menjadikan gambar lokal sebagai background aplikasi Streamlit."""
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{b64_encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* Lapisan semi-transparan agar teks tetap terbaca di atas foto */
        .stApp::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.85);
            z-index: -1;
        }}

        /* Membuat sidebar sedikit transparan juga agar serasi */
        section[data-testid="stSidebar"] {{
            background-color: rgba(255, 255, 255, 0.9);
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Panggil fungsi background sebelum konten lain dirender.
# Pastikan file bg_siswa.png berada satu folder dengan app.py (sudah sesuai di repo kamu).
set_background("bg_siswa.png")

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
# MENU 1: DEFINISI LOGARITMA
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
        st.latex(rf"^{a_1}\log {x_1} = {n_1}")

    with col2:
        st.subheader("B. Logaritma ➔ Perpangkatan")
        st.caption("Ubah bentuk logaritma menjadi perpangkatan")

        a_2 = st.number_input("Basis Log (a):", value=3, step=1, min_value=2, key="a_2")
        x_2 = st.number_input("Numerus (x):", value=81, step=1, min_value=1, key="x_2")

        try:
            n_2 = int(math.log(x_2, a_2))
            st.divider()
            st.write("**Bentuk Logaritma:**")
            st.latex(rf"^{a_2}\log {x_2} = {n_2}")

            st.write("**Bentuk Pangkat:**")
            st.latex(rf"{a_2}^{{{n_2}}} = {x_2}")
        except ValueError:
            st.error("Masukkan nilai numerus dan basis yang valid!")

# -----------------------------------------------------------------------------
# MENU 2: SIFAT DASAR (POIN A)
# -----------------------------------------------------------------------------
elif selected_key == "Sifat A":
    st.markdown("### a. Syarat & Rumus Dasar:")
    st.latex(r"a > 0, \, a \neq 1")
    st.latex(r"^a\log 1 = 0 \quad \text{dan} \quad ^a\log a = 1")

    st.divider()
    a_val = st.number_input("Masukkan Nilai Basis (a):", value=5, step=1, min_value=2)

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("Sifat 1")
            st.latex(rf"^{a_val}\log 1 = 0")
            st.caption(f"Bukti: {a_val}⁰ = 1")

    with col2:
        with st.container(border=True):
            st.subheader("Sifat 2")
            st.latex(rf"^{a_val}\log {a_val} = 1")
            st.caption(f"Bukti: {a_val}¹ = {a_val}")

# -----------------------------------------------------------------------------
# MENU 3: SIFAT PANGKAT NUMERUS (POIN B)
# -----------------------------------------------------------------------------
elif selected_key == "Sifat B":
    st.markdown("### b. Pangkat Numerus:")
    st.latex(r"a > 0, \, a \neq 1, \, x > 0 \quad (a, n, x \in \mathbb{R})")
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
    st.latex(rf"^{a_s3}\log ({x_base}^{{{n_pangkat}}}) = {n_pangkat} \cdot ^{a_s3}\log {x_base}")

    st.write("2. Substitusi Hasil:")
    st.latex(rf"= {n_pangkat} \cdot {val_base_log}")

    st.write("3. Hasil Akhir:")
    st.latex(rf"^{a_s3}\log {numerus_total} = {hasil_akhir}")

# -----------------------------------------------------------------------------
# MENU 4: SIFAT PANGKAT BASIS & NUMERUS (POIN C)
# -----------------------------------------------------------------------------
elif selected_key == "Sifat C":
    st.markdown("### c. Pangkat Basis & Numerus:")
    st.latex(r"a > 0, \, a \neq 1, \, x > 0 \quad (a, m, n, x \in \mathbb{R})")
    st.latex(r"^{a^n}\log x^m = \frac{m}{n} \cdot {}^a\log x")

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Input Basis (aⁿ)")
        a_base = st.number_input("Basis Utama (a):", value=2, step=1, min_value=2, key="a_base_s4")
        n_exp = st.number_input("Pangkat Basis (n):", value=2, step=1, min_value=1, key="n_exp_s4")

    with col2:
        st.subheader("Input Numerus (xᵐ)")
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
    st.latex(rf"^{basis_total}\log {numerus_total} \implies ^{{{a_base}^{{{n_exp}}}}}\log ({x_base}^{{{m_exp}}})")

    st.write("2. Gunakan Rumus Sifat:")
    st.latex(rf"\frac{{{m_exp}}}{{{n_exp}}} \cdot ^{a_base}\log {x_base} = \frac{{{m_exp}}}{{{n_exp}}} \cdot {base_log}")

    st.write("3. Hasil Akhir:")
    st.latex(rf"^{basis_total}\log {numerus_total} = {hasil_latex}")

# -----------------------------------------------------------------------------
# MENU 5: PENJUMLAHAN LOGARITMA (POIN D)
# -----------------------------------------------------------------------------
elif selected_key == "Sifat D":
    st.markdown("### d. Penjumlahan Logaritma:")
    st.latex(r"a > 0, \, a \neq 1, \, x > 0, \, y > 0 \quad (a, x, y \in \mathbb{R})")
    st.latex(r"^a\log x + {}^a\log y = {}^a\log(x \cdot y)")

    st.divider()
    col1, col2, col3 = st.columns(3)

    with col1:
        a_d = st.number_input("Basis (a):", value=2, step=1, min_value=2, key="a_d")
    with col2:
        x_d = st.number_input("Numerus Pertama (x):", value=2, step=1, min_value=1, key="x_d")
    with col3:
        y_d = st.number_input("Numerus Kedua (y):", value=16, step=1, min_value=1, key="y_d")

    xy_prod = x_d * y_d

    st.divider()
    st.subheader("📋 Langkah Penyelesaian:")

    st.write("1. Gabungkan Numerus (Perkalian):")
    st.latex(rf"^{a_d}\log {x_d} + ^{a_d}\log {y_d} = ^{a_d}\log ({x_d} \cdot {y_d})")

    st.write("2. Hasil Perkalian Numerus:")
    st.latex(rf"= ^{a_d}\log {xy_prod}")

    try:
        val_res = math.log(xy_prod, a_d)
        if val_res.is_integer():
            st.write("3. Hasil Akhir:")
            st.latex(rf"= {int(val_res)}")
    except ValueError:
        pass

# -----------------------------------------------------------------------------
# MENU 6: PENGURANGAN LOGARITMA (POIN E)
# -----------------------------------------------------------------------------
elif selected_key == "Sifat E":
    st.markdown("### e. Pengurangan Logaritma:")
    st.latex(r"a > 0, \, a \neq 1, \, x > 0, \, y > 0 \quad (a, x, y \in \mathbb{R})")
    st.latex(r"^a\log x - {}^a\log y = {}^a\log\left(\frac{x}{y}\right)")

    st.divider()
    col1, col2, col3 = st.columns(3)

    with col1:
        a_e = st.number_input("Basis (a):", value=2, step=1, min_value=2, key="a_e")
    with col2:
        x_e = st.number_input("Numerus Pertama (x):", value=32, step=1, min_value=1, key="x_e")
    with col3:
        y_e = st.number_input("Numerus Kedua (y):", value=2, step=1, min_value=1, key="y_e")

    st.divider()
    st.subheader("📋 Langkah Penyelesaian:")

    st.write("1. Gabungkan Numerus (Pembagian):")
    st.latex(rf"^{a_e}\log {x_e} - ^{a_e}\log {y_e} = ^{a_e}\log \left(\frac{{{x_e}}}{{{y_e}}}\right)")

    div_frac = Fraction(x_e, y_e)
    if div_frac.denominator == 1:
        xy_div_str = f"{div_frac.numerator}"
    else:
        xy_div_str = f"\\frac{{{div_frac.numerator}}}{{{div_frac.denominator}}}"

    st.write("2. Hasil Pembagian Numerus:")
    st.latex(rf"= ^{a_e}\log \left({xy_div_str}\right)")

    try:
        val_res = math.log(x_e / y_e, a_e)
        if val_res.is_integer():
            st.write("3. Hasil Akhir:")
            st.latex(rf"= {int(val_res)}")
    except ValueError:
        pass

# -----------------------------------------------------------------------------
# MENU 7: PERKALIAN LOGARITMA (POIN F)
# -----------------------------------------------------------------------------
elif selected_key == "Sifat F":
    st.markdown("### f. Perkalian Logaritma Berantai:")
    st.latex(r"a > 0, \, a \neq 1, \, x > 0, \, y > 0 \quad (a, x, y \in \mathbb{R})")
    st.latex(r"^a\log x \cdot {}^x\log y = {}^a\log y")

    st.divider()
    col1, col2, col3 = st.columns(3)

    with col1:
        a_f = st.number_input("Basis Pertama (a):", value=2, step=1, min_value=2, key="a_f")
    with col2:
        x_f = st.number_input("Numerus 1 / Basis 2 (x):", value=3, step=1, min_value=2, key="x_f")
    with col3:
        y_f = st.number_input("Numerus Kedua (y):", value=16, step=1, min_value=1, key="y_f")

    st.divider()
    st.subheader("📋 Langkah Penyelesaian:")

    st.write("1. Bentuk Perkalian Logaritma Berantai:")
    st.latex(rf"^{a_f}\log {x_f} \cdot ^{x_f}\log {y_f}")

    st.write("2. Penyederhanaan (Menghilangkan Basis & Numerus x yang Sama):")
    st.latex(rf"= ^{a_f}\log {y_f}")

    try:
        val_res = math.log(y_f, a_f)
        if val_res.is_integer():
            st.write("3. Hasil Akhir:")
            st.latex(rf"= {int(val_res)}")
    except ValueError:
        pass

# -----------------------------------------------------------------------------
# MENU 8: MENGUBAH BASIS LOGARITMA (POIN G)
# -----------------------------------------------------------------------------
elif selected_key == "Sifat G":
    st.markdown("### g. Mengubah Basis Logaritma:")
    st.latex(r"a > 0, \, a \neq 1, \, b > 0, \, b \neq 1, \, x > 0 \quad (a, b, x \in \mathbb{R})")
    st.latex(r"^a\log x = \frac{{}^b\log x}{{}^b\log a} = \frac{1}{{}^x\log a}")

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("A. Mengubah Basis ke-b")
        a_g = st.number_input("Basis Awal (a):", value=4, step=1, min_value=2, key="a_g")
        x_g = st.number_input("Numerus (x):", value=8, step=1, min_value=2, key="x_g")
        b_g = st.number_input("Basis Baru (b):", value=2, step=1, min_value=2, key="b_g")

        st.write("**Proses Ubah Basis:**")
        st.latex(rf"^{a_g}\log {x_g} = \frac{{^{b_g}\log {x_g}}}{{^{b_g}\log {a_g}}}")

        try:
            log_bx = math.log(x_g, b_g)
            log_ba = math.log(a_g, b_g)
            frac_res = Fraction(Decimal(str(log_bx / log_ba))).limit_denominator() if not (log_bx/log_ba).is_integer() else int(log_bx/log_ba)

            if isinstance(frac_res, Fraction):
                res_str = f"\\frac{{{frac_res.numerator}}}{{{frac_res.denominator}}}"
            else:
                res_str = f"{frac_res}"

            st.write("**Hasil Akhir:**")
            st.latex(rf"= \frac{{{int(log_bx) if log_bx.is_integer() else round(log_bx, 2)}}}{{{int(log_ba) if log_ba.is_integer() else round(log_ba, 2)}}} = {res_str}")
        except Exception:
            pass

    with col2:
        st.subheader("B. Kebalikan Basis & Numerus")
        st.write("**Bentuk Sifat:**")
        st.latex(rf"^{a_g}\log {x_g} = \frac{{1}}{{^{x_g}\log {a_g}}}")

# -----------------------------------------------------------------------------
# MENU 9: PANGKAT DENGAN EKSPLISIT LOGARITMA (POIN H)
# -----------------------------------------------------------------------------
elif selected_key == "Sifat H":
    st.markdown("### h. Eksponen Logaritma Basis Sama:")
    st.latex(r"a > 0, \, a \neq 1, \, x > 0 \quad (a, x \in \mathbb{R})")
    st.latex(r"a^{{}^a\log x} = x")

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        a_h = st.number_input("Basis Utama / Basis Logaritma (a):", value=2, step=1, min_value=2, key="a_h")
    with col2:
        x_h = st.number_input("Numerus / Hasil (x):", value=7, step=1, min_value=1, key="x_h")

    st.divider()
    st.subheader("📋 Langkah Penyelesaian:")

    st.write("1. Bentuk Pangkat Logaritma:")
    st.latex(rf"{a_h}^{{^{a_h}\log {x_h}}}")

    st.write("2. Berdasarkan Sifat (Basis Pangkat == Basis Logaritma):")
    st.latex(rf"= {x_h}")

# -----------------------------------------------------------------------------
# MENU 10: PANGKAT DENGAN KOEFISIEN LOGARITMA (POIN I)
# -----------------------------------------------------------------------------
elif selected_key == "Sifat I":
    st.markdown("### i. Eksponen Logaritma Berkoefisien:")
    st.latex(r"a > 0, \, a \neq 1, \, x > 0 \quad (a, x, n \in \mathbb{R})")
    st.latex(r"a^{n \cdot {}^a\log x} = x^n")

    st.divider()
    col1, col2, col3 = st.columns(3)

    with col1:
        a_i = st.number_input("Basis Utama / Basis Log (a):", value=3, step=1, min_value=2, key="a_i")
    with col2:
        n_i = st.number_input("Koefisien Pangkat (n):", value=2, step=1, key="n_i")
    with col3:
        x_i = st.number_input("Numerus Logaritma (x):", value=5, step=1, min_value=1, key="x_i")

    hasil_i = int(math.pow(x_i, n_i))

    st.divider()
    st.subheader("📋 Langkah Penyelesaian:")

    st.write("1. Bentuk Soal Sesuai Sifat:")
    st.latex(rf"{a_i}^{{{n_i} \cdot ^{a_i}\log {x_i}}}")

    st.write("2. Pindahkan Koefisien Menjadi Pangkat Numerus:")
    st.latex(rf"= {a_i}^{{^{a_i}\log ({x_i}^{{{n_i}}})}}")

    st.write("3. Hasil Akhir:")
    st.latex(rf"= {x_i}^{{{n_i}}} = {hasil_i}")

# -----------------------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------------------
st.sidebar.divider()
st.sidebar.caption("Oleh : Mochammad Rifqi Al Khadziq")
