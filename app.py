import base64
import math
from fractions import Fraction

import streamlit as st


# =============================================================================
# KONFIGURASI HALAMAN
# =============================================================================
st.set_page_config(
    page_title="Modul & Kalkulator Logaritma Interaktif",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =============================================================================
# STYLE & BACKGROUND
# Fokus utama: teks dan materi, bukan gambar latar.
# =============================================================================
def set_background(image_file: str) -> None:
    """Memasang background dengan opacity rendah agar teks tetap dominan."""
    try:
        with open(image_file, "rb") as file:
            image_data = base64.b64encode(file.read()).decode()
    except FileNotFoundError:
        return

    st.markdown(
        f"""
        <style>
        /* -----------------------------------------------------------------
           BACKGROUND
           Gambar dibuat sangat lembut dengan overlay putih.
           ----------------------------------------------------------------- */
        .stApp {{
            background-image: url("data:image/png;base64,{image_data}");
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
            background-attachment: fixed;
        }}

        .stApp::before {{
            content: "";
            position: fixed;
            inset: 0;
            background: rgba(255, 255, 255, 0.86);
            z-index: 0;
            pointer-events: none;
        }}

        /* -----------------------------------------------------------------
           AREA UTAMA
           Panel putih dibuat cukup solid agar tulisan menjadi fokus utama.
           ----------------------------------------------------------------- */
        [data-testid="stAppViewContainer"] {{
            position: relative;
            z-index: 1;
        }}

        .block-container {{
            max-width: 1400px;
            padding-top: 2rem;
            padding-bottom: 3rem;
            background: rgba(255, 255, 255, 0.94);
            border-radius: 18px;
            box-shadow: 0 8px 30px rgba(20, 33, 61, 0.08);
        }}

        [data-testid="stHeader"] {{
            background: transparent !important;
        }}

        /* -----------------------------------------------------------------
           TIPOGRAFI
           ----------------------------------------------------------------- */
        [data-testid="stAppViewContainer"] * {{
            color: #14213d;
        }}

        h1, h2, h3, h4 {{
            color: #14213d !important;
            font-weight: 700 !important;
        }}

        p, li, label, .stCaption {{
            color: #243b5a !important;
        }}

        /* -----------------------------------------------------------------
           SIDEBAR
           ----------------------------------------------------------------- */
        section[data-testid="stSidebar"] {{
            background: rgba(255, 255, 255, 0.98) !important;
            border-right: 1px solid rgba(20, 33, 61, 0.10);
        }}

        section[data-testid="stSidebar"] * {{
            color: #14213d !important;
        }}

        /* Radio navigation lebih rapi dan mudah dibaca. */
        section[data-testid="stSidebar"] [role="radiogroup"] {{
            gap: 0.15rem;
        }}

        /* -----------------------------------------------------------------
           INPUT & CONTAINER
           ----------------------------------------------------------------- */
        [data-testid="stNumberInput"] input {{
            background: #ffffff !important;
            color: #14213d !important;
            border: 1px solid #c9d4e3 !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
        }}

        [data-testid="stNumberInput"] button {{
            background: #f4f7fb !important;
        }}

        [data-testid="stVerticalBlockBorderWrapper"] {{
            background: rgba(255, 255, 255, 0.96) !important;
            border: 1px solid #dbe3ee !important;
            border-radius: 14px !important;
        }}

        /* Rumus lebih menonjol daripada elemen dekoratif. */
        [data-testid="stLatex"] {{
            background: rgba(248, 250, 253, 0.92);
            border-radius: 10px;
            padding: 0.45rem 0.7rem;
            margin: 0.35rem 0;
        }}

        hr {{
            border-color: #dbe3ee !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


set_background("bg_siswa.png")


# =============================================================================
# FUNGSI BANTU
# =============================================================================
def format_number(value: float) -> str:
    """Membuat hasil matematika lebih rapi."""
    if abs(value - round(value)) < 1e-10:
        return str(int(round(value)))
    return f"{value:.4f}".rstrip("0").rstrip(".")


def format_fraction(value: Fraction) -> str:
    """Mengubah Fraction menjadi format LaTeX."""
    if value.denominator == 1:
        return str(value.numerator)
    return rf"\frac{{{value.numerator}}}{{{value.denominator}}}"


def safe_log(x: float, base: float) -> float:
    """Menghitung logaritma dengan validasi sederhana."""
    if x <= 0:
        raise ValueError("Numerus harus lebih besar dari 0.")
    if base <= 0 or base == 1:
        raise ValueError("Basis harus lebih besar dari 0 dan tidak sama dengan 1.")
    return math.log(x, base)


def show_steps_title() -> None:
    st.divider()
    st.subheader("📋 Langkah Penyelesaian:")


# =============================================================================
# HEADER
# =============================================================================
st.title("📐 Kalkulator & Learning Media Logaritma")
st.caption(
    "Materi sesuai buku cetak Matematika Kelas X "
    "(Definisi & Sifat-Sifat Logaritma)"
)
st.divider()


# =============================================================================
# SIDEBAR NAVIGATION
# =============================================================================
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
    format_func=lambda key: menu_options[key],
)


# =============================================================================
# MENU 1 — DEFINISI LOGARITMA
# =============================================================================
if selected_key == "Definisi Logaritma":
    st.header("📘 Definisi Logaritma")
    st.write("Bentuk umum logaritma adalah:")
    st.latex(r"{{}}^a\log x = n \iff a^n = x")

    st.write("**Keterangan:**")
    st.latex(r"a = \text{basis/bilangan pokok } (a > 0, a \neq 1)")
    st.latex(r"x = \text{numerus } (x > 0)")
    st.latex(r"n = \text{hasil logaritma}")

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("A. Perpangkatan ➔ Logaritma")
        st.caption("Ubah bentuk perpangkatan menjadi logaritma")

        a_1 = st.number_input(
            "Basis (a):", value=2, step=1, min_value=2, key="a_1"
        )
        n_1 = st.number_input(
            "Pangkat (n):", value=3, step=1, key="n_1"
        )

        x_1 = int(math.pow(a_1, n_1))

        st.write("**Bentuk Pangkat:**")
        st.latex(rf"{a_1}^{{{n_1}}} = {x_1}")

        st.write("**Bentuk Logaritma:**")
        st.latex(rf"{{}}^{a_1}\log {x_1} = {n_1}")

    with col2:
        st.subheader("B. Logaritma ➔ Perpangkatan")
        st.caption("Ubah bentuk logaritma menjadi perpangkatan")

        a_2 = st.number_input(
            "Basis Log (a):", value=3, step=1, min_value=2, key="a_2"
        )
        x_2 = st.number_input(
            "Numerus (x):", value=81, step=1, min_value=1, key="x_2"
        )

        try:
            n_2 = safe_log(x_2, a_2)

            st.write("**Bentuk Logaritma:**")
            st.latex(rf"{{}}^{a_2}\log {x_2} = {format_number(n_2)}")

            st.write("**Bentuk Pangkat:**")
            st.latex(rf"{a_2}^{{{format_number(n_2)}}} = {x_2}")
        except ValueError as error:
            st.error(str(error))


# =============================================================================
# MENU 2 — SIFAT A
# =============================================================================
elif selected_key == "Sifat A":
    st.markdown("### a. Syarat & Rumus Dasar:")
    st.latex(r"a > 0, \, a \neq 1")
    st.latex(r"{{}}^a\log 1 = 0 \quad \text{dan} \quad {{}}^a\log a = 1")

    st.divider()
    a_val = st.number_input(
        "Masukkan Nilai Basis (a):",
        value=5,
        step=1,
        min_value=2,
    )

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("Sifat 1")
            st.latex(rf"{{}}^{a_val}\log 1 = 0")
            st.caption(f"Bukti: {a_val}⁰ = 1")

    with col2:
        with st.container(border=True):
            st.subheader("Sifat 2")
            st.latex(rf"{{}}^{a_val}\log {a_val} = 1")
            st.caption(f"Bukti: {a_val}¹ = {a_val}")


# =============================================================================
# MENU 3 — SIFAT B: PANGKAT NUMERUS
# =============================================================================
elif selected_key == "Sifat B":
    st.markdown("### b. Pangkat Numerus:")
    st.latex(r"a > 0, \, a \neq 1, \, x > 0 \quad (a, n, x \in \mathbb{R})")
    st.latex(r"{{}}^a\log x^n = n \cdot {{}}^a\log x")

    st.divider()
    col1, col2, col3 = st.columns(3)

    with col1:
        a_s3 = st.number_input(
            "Basis (a):", value=2, step=1, min_value=2, key="a_s3"
        )

    with col2:
        x_s3 = st.number_input(
            "Nilai dasar x:", value=2, step=1, min_value=1, key="x_s3"
        )

    with col3:
        n_pangkat = st.number_input(
            "Pangkat Numerus (n):", value=4, step=1, key="n_s3"
        )

    numerus_total = int(math.pow(x_s3, n_pangkat))

    show_steps_title()

    try:
        val_base_log = safe_log(x_s3, a_s3)
        hasil_akhir = n_pangkat * val_base_log

        st.write("1. Bentuk Soal Sesuai Sifat:")
        st.latex(
            rf"{{}}^{a_s3}\log ({x_s3}^{{{n_pangkat}}})"
            rf" = {n_pangkat} \cdot {{}}^{a_s3}\log {x_s3}"
        )

        st.write("2. Substitusi Hasil:")
        st.latex(rf"= {n_pangkat} \cdot {format_number(val_base_log)}")

        st.write("3. Hasil Akhir:")
        st.latex(
            rf"{{}}^{a_s3}\log {numerus_total} = "
            rf"{format_number(hasil_akhir)}"
        )
    except ValueError as error:
        st.error(str(error))


# =============================================================================
# MENU 4 — SIFAT C: PANGKAT BASIS & NUMERUS
# =============================================================================
elif selected_key == "Sifat C":
    st.markdown("### c. Pangkat Basis & Numerus:")
    st.latex(
        r"a > 0, \, a \neq 1, \, x > 0 "
        r"\quad (a, m, n, x \in \mathbb{R})"
    )
    st.latex(r"{{}}^{a^n}\log x^m = \frac{m}{n} \cdot {{}}^a\log x")

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Input Basis (aⁿ)")
        a_base = st.number_input(
            "Basis Utama (a):", value=2, step=1, min_value=2, key="a_base_s4"
        )
        n_exp = st.number_input(
            "Pangkat Basis (n):", value=2, step=1, min_value=1, key="n_exp_s4"
        )

    with col2:
        st.subheader("Input Numerus (xᵐ)")
        x_base_c = st.number_input(
            "Numerus Utama (x):", value=2, step=1, min_value=1, key="x_base_s4"
        )
        m_exp = st.number_input(
            "Pangkat Numerus (m):", value=3, step=1, key="m_exp_s4"
        )

    basis_total = int(math.pow(a_base, n_exp))
    numerus_total_c = int(math.pow(x_base_c, m_exp))

    show_steps_title()

    try:
        base_log = safe_log(x_base_c, a_base)
        hasil_frac = Fraction(m_exp, n_exp) * Fraction(str(base_log)).limit_denominator()
        hasil_latex = format_fraction(hasil_frac)

        st.write("1. Bentuk Soal Disederhanakan:")
        st.latex(
            rf"{{}}^{basis_total}\log {numerus_total_c}"
            rf" \implies {{}}^{{{a_base}^{n_exp}}}\log "
            rf"({x_base_c}^{m_exp})"
        )

        st.write("2. Gunakan Rumus Sifat:")
        st.latex(
            rf"\frac{{{m_exp}}}{{{n_exp}}} \cdot "
            rf"{{}}^{a_base}\log {x_base_c}"
            rf" = \frac{{{m_exp}}}{{{n_exp}}} \cdot {format_number(base_log)}"
        )

        st.write("3. Hasil Akhir:")
        st.latex(rf"{{}}^{basis_total}\log {numerus_total_c} = {hasil_latex}")
    except ValueError as error:
        st.error(str(error))


# =============================================================================
# MENU 5 — SIFAT D: PENJUMLAHAN LOGARITMA
# =============================================================================
elif selected_key == "Sifat D":
    st.markdown("### d. Penjumlahan Logaritma:")
    st.latex(
        r"a > 0, \, a \neq 1, \, x > 0, \, y > 0 "
        r"\quad (a, x, y \in \mathbb{R})"
    )
    st.latex(r"{{}}^a\log x + {{}}^a\log y = {{}}^a\log(x \cdot y)")

    st.divider()
    col1, col2, col3 = st.columns(3)

    with col1:
        a_d = st.number_input(
            "Basis (a):", value=2, step=1, min_value=2, key="a_d"
        )

    with col2:
        x_d = st.number_input(
            "Numerus Pertama (x):", value=2, step=1, min_value=1, key="x_d"
        )

    with col3:
        y_d = st.number_input(
            "Numerus Kedua (y):", value=16, step=1, min_value=1, key="y_d"
        )

    xy_prod = x_d * y_d

    show_steps_title()

    st.write("1. Gabungkan Numerus (Perkalian):")
    st.latex(
        rf"{{}}^{a_d}\log {x_d} + {{}}^{a_d}\log {y_d}"
        rf" = {{}}^{a_d}\log ({x_d} \cdot {y_d})"
    )

    st.write("2. Hasil Perkalian Numerus:")
    st.latex(rf"= {{}}^{a_d}\log {xy_prod}")

    try:
        val_res = safe_log(xy_prod, a_d)
        st.write("3. Hasil Akhir:")
        st.latex(rf"= {format_number(val_res)}")
    except ValueError as error:
        st.error(str(error))


# =============================================================================
# MENU 6 — SIFAT E: PENGURANGAN LOGARITMA
# =============================================================================
elif selected_key == "Sifat E":
    st.markdown("### e. Pengurangan Logaritma:")
    st.latex(
        r"a > 0, \, a \neq 1, \, x > 0, \, y > 0 "
        r"\quad (a, x, y \in \mathbb{R})"
    )
    st.latex(
        r"{{}}^a\log x - {{}}^a\log y = "
        r"{{}}^a\log\left(\frac{x}{y}\right)"
    )

    st.divider()
    col1, col2, col3 = st.columns(3)

    with col1:
        a_e = st.number_input(
            "Basis (a):", value=2, step=1, min_value=2, key="a_e"
        )

    with col2:
        x_e = st.number_input(
            "Numerus Pertama (x):", value=32, step=1, min_value=1, key="x_e"
        )

    with col3:
        y_e = st.number_input(
            "Numerus Kedua (y):", value=2, step=1, min_value=1, key="y_e"
        )

    show_steps_title()

    st.write("1. Gabungkan Numerus (Pembagian):")
    st.latex(
        rf"{{}}^{a_e}\log {x_e} - {{}}^{a_e}\log {y_e}"
        rf" = {{}}^{a_e}\log\left(\frac{{{x_e}}}{{{y_e}}}\right)"
    )

    div_frac = Fraction(x_e, y_e)
    xy_div_str = format_fraction(div_frac)

    st.write("2. Hasil Pembagian Numerus:")
    st.latex(rf"= {{}}^{a_e}\log\left({xy_div_str}\right)")

    try:
        val_res = safe_log(x_e / y_e, a_e)
        st.write("3. Hasil Akhir:")
        st.latex(rf"= {format_number(val_res)}")
    except ValueError as error:
        st.error(str(error))


# =============================================================================
# MENU 7 — SIFAT F: PERKALIAN LOGARITMA BERANTAI
# =============================================================================
elif selected_key == "Sifat F":
    st.markdown("### f. Perkalian Logaritma Berantai:")
    st.latex(
        r"a > 0, \, a \neq 1, \, x > 0, \, y > 0 "
        r"\quad (a, x, y \in \mathbb{R})"
    )
    st.latex(r"{{}}^a\log x \cdot {{}}^x\log y = {{}}^a\log y")

    st.divider()
    col1, col2, col3 = st.columns(3)

    with col1:
        a_f = st.number_input(
            "Basis Pertama (a):", value=2, step=1, min_value=2, key="a_f"
        )

    with col2:
        x_f = st.number_input(
            "Numerus 1 / Basis 2 (x):", value=3, step=1, min_value=2, key="x_f"
        )

    with col3:
        y_f = st.number_input(
            "Numerus Kedua (y):", value=16, step=1, min_value=1, key="y_f"
        )

    show_steps_title()

    st.write("1. Bentuk Perkalian Logaritma Berantai:")
    st.latex(rf"{{}}^{a_f}\log {x_f} \cdot {{}}^{x_f}\log {y_f}")

    st.write("2. Penyederhanaan (Menghilangkan Basis & Numerus x yang Sama):")
    st.latex(rf"= {{}}^{a_f}\log {y_f}")

    try:
        val_res = safe_log(y_f, a_f)
        st.write("3. Hasil Akhir:")
        st.latex(rf"= {format_number(val_res)}")
    except ValueError as error:
        st.error(str(error))


# =============================================================================
# MENU 8 — SIFAT G: MENGUBAH BASIS LOGARITMA
# =============================================================================
elif selected_key == "Sifat G":
    st.markdown("### g. Mengubah Basis Logaritma:")
    st.latex(
        r"a > 0, \, a \neq 1, \, b > 0, \, b \neq 1, \, x > 0 "
        r"\quad (a, b, x \in \mathbb{R})"
    )
    st.latex(
        r"{{}}^a\log x = "
        r"\frac{{{}}^b\log x}{{{}}^b\log a} = "
        r"\frac{1}{{{}}^x\log a}"
    )

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("A. Mengubah Basis ke-b")

        a_g = st.number_input(
            "Basis Awal (a):", value=4, step=1, min_value=2, key="a_g"
        )
        x_g = st.number_input(
            "Numerus (x):", value=8, step=1, min_value=2, key="x_g"
        )
        b_g = st.number_input(
            "Basis Baru (b):", value=2, step=1, min_value=2, key="b_g"
        )

        st.write("**Proses Ubah Basis:**")
        st.latex(
            rf"{{}}^{a_g}\log {x_g} = "
            rf"\frac{{{{}}^{b_g}\log {x_g}}}{{{{}}^{b_g}\log {a_g}}}"
        )

        try:
            log_bx = safe_log(x_g, b_g)
            log_ba = safe_log(a_g, b_g)
            result = log_bx / log_ba

            st.write("**Hasil Akhir:**")
            st.latex(
                rf"= \frac{{{format_number(log_bx)}}}"
                rf"{{{format_number(log_ba)}}}"
                rf" = {format_number(result)}"
            )
        except ValueError as error:
            st.error(str(error))

    with col2:
        st.subheader("B. Kebalikan Basis & Numerus")
        st.write("**Bentuk Sifat:**")
        st.latex(
            rf"{{}}^{a_g}\log {x_g} = "
            rf"\frac{{1}}{{{{}}^{x_g}\log {a_g}}}"
        )


# =============================================================================
# MENU 9 — SIFAT H: EKSPONEN LOGARITMA BASIS SAMA
# =============================================================================
elif selected_key == "Sifat H":
    st.markdown("### h. Eksponen Logaritma Basis Sama:")
    st.latex(r"a > 0, \, a \neq 1, \, x > 0 \quad (a, x \in \mathbb{R})")
    st.latex(r"a^{{{}}^a\log x} = x")

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        a_h = st.number_input(
            "Basis Utama / Basis Logaritma (a):",
            value=2,
            step=1,
            min_value=2,
            key="a_h",
        )

    with col2:
        x_h = st.number_input(
            "Numerus / Hasil (x):",
            value=7,
            step=1,
            min_value=1,
            key="x_h",
        )

    show_steps_title()

    st.write("1. Bentuk Pangkat Logaritma:")
    st.latex(rf"{a_h}^{{{{}}^{a_h}\log {x_h}}}")

    st.write("2. Berdasarkan Sifat (Basis Pangkat == Basis Logaritma):")
    st.latex(rf"= {x_h}")


# =============================================================================
# MENU 10 — SIFAT I: EKSPONEN LOGARITMA BERKOEFISIEN
# =============================================================================
elif selected_key == "Sifat I":
    st.markdown("### i. Eksponen Logaritma Berkoefisien:")
    st.latex(
        r"a > 0, \, a \neq 1, \, x > 0 "
        r"\quad (a, x, n \in \mathbb{R})"
    )
    st.latex(r"a^{n \cdot {{}}^a\log x} = x^n")

    st.divider()
    col1, col2, col3 = st.columns(3)

    with col1:
        a_i = st.number_input(
            "Basis Utama / Basis Log (a):",
            value=3,
            step=1,
            min_value=2,
            key="a_i",
        )

    with col2:
        n_i = st.number_input(
            "Koefisien Pangkat (n):",
            value=2,
            step=1,
            key="n_i",
        )

    with col3:
        x_i = st.number_input(
            "Numerus Logaritma (x):",
            value=5,
            step=1,
            min_value=1,
            key="x_i",
        )

    hasil_i = int(math.pow(x_i, n_i))

    show_steps_title()

    st.write("1. Bentuk Soal Sesuai Sifat:")
    st.latex(rf"{a_i}^{{{n_i} \cdot {{}}^{a_i}\log {x_i}}}")

    st.write("2. Pindahkan Koefisien Menjadi Pangkat Numerus:")
    st.latex(rf"= {a_i}^{{{{}}^{a_i}\log ({x_i}^{{{n_i}}})}}")

    st.write("3. Hasil Akhir:")
    st.latex(rf"= {x_i}^{{{n_i}}} = {hasil_i}")


# =============================================================================
# FOOTER
# =============================================================================
st.sidebar.divider()
st.sidebar.caption("Oleh : Mochammad Rifqi Al Khadziq")
