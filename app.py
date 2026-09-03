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

# Custom CSS Adaptif (Sesuai Mode Terang & Gelap)
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E88E5;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1rem;
        color: var(--text-color);
        opacity: 0.8;
        margin-bottom: 20px;
    }
    /* Bingkai otomatis untuk st.latex() mirip buku cetak */
    div[data-testid="stLatex"] {
        background-color: var(--secondary-background-color);
        border: 2px solid var(--text-color);
        border-radius: 8px;
        padding: 10px 20px;
        margin: 15px auto;
        width: fit-content;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .card {
        background-color: var(--secondary-background-color);
        color: var(--text-color);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1E88E5;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 15px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="main-title">📐 Kalkulator & Learning Media Logaritma</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="sub-title">Materi sesuai buku cetak Matematika Kelas X'
    ' (Definisi & Sifat-Sifat Logaritma)</div>',
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------------------------------------------------
st.sidebar.header("🎯 Pilih Materi/Sifat")
menu = st.sidebar.radio(
    "Navigasi Modul:",
    [
        "1. Definisi Logaritma",
        "2. Sifat Dasar",
        "3. Sifat Pangkat Numerus",
        "4. Sifat Pangkat Basis & Numerus",
    ],
)

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **Catatan:** Seluruh kalkulasi diset menggunakan bilangan bulat (tanpa"
    " koma)."
)

# -----------------------------------------------------------------------------
# MENU 1: DEFINISI LOGARITMA
# -----------------------------------------------------------------------------
if menu == "1. Definisi Logaritma":
    st.header("1. Definisi Logaritma")
    st.write("Bentuk umum logaritma adalah:")

    st.latex(r"^a\log x = n \iff a^n = x")

    st.write("**Dengan:**")
    st.write(
        "- $a$ = bilangan pokok/basis logaritma ($a > 0$ dan $a \\neq 1$)"
    )
    st.write(
        "- $x$ = numerus yaitu bilangan yang dicari logaritmanya ($x > 0$)"
    )
    st.write(
        "- $n$ = hasil logaritma, bisa bernilai positif, nol, atau negatif"
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("A. Perpangkatan ➔ Logaritma")
        st.caption("Ubah bentuk $a^n = x$ menjadi $^a\\log x = n$")

        a_1 = st.number_input("Basis (a):", value=2, step=1, key="a_1")
        n_1 = st.number_input("Pangkat (n):", value=3, step=1, key="n_1")

        x_1 = int(math.pow(a_1, n_1)) if a_1 != 0 else 0

        st.write("---")
        st.markdown(f"**Bentuk Pangkat:** ${a_1}^{{{n_1}}} = {x_1}$")
        st.success(f"**Bentuk Logaritma:** $^{{{a_1}}}\\log{{{x_1}}} = {n_1}$")

    with col2:
        st.subheader("B. Logaritma ➔ Perpangkatan")
        st.caption("Ubah bentuk $^a\\log x = n$ menjadi $a^n = x$")

        a_2 = st.number_input(
            "Basis Log (a):", value=3, step=1, min_value=2, key="a_2"
        )
        x_2 = st.number_input(
            "Numerus (x):", value=81, step=1, min_value=1, key="x_2"
        )

        try:
            n_2 = int(math.log(x_2, a_2))
            st.write("---")
            st.markdown(
                f"**Bentuk Logaritma:** $^{{{a_2}}}\\log{{{x_2}}} = {n_2}$"
            )
            st.success(f"**Bentuk Pangkat:** ${a_2}^{{{n_2}}} = {x_2}$")
        except ValueError:
            st.error("Masukkan nilai numerus dan basis yang valid!")

# -----------------------------------------------------------------------------
# MENU 2: SIFAT DASAR
# -----------------------------------------------------------------------------
elif menu == "2. Sifat Dasar":
    st.header("2. Sifat-sifat Logaritma")
    st.write("a. Untuk $a > 0$ dan $a \\neq 1$, berlaku:")

    st.latex(r"^a\log 1 = 0 \quad \text{dan} \quad ^a\log a = 1")

    a_val = st.number_input(
        "Masukkan Nilai Basis (a):", value=5, step=1, min_value=2
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Sifat A: $^a\\log 1 = 0$")
        st.write(f"**Contoh Input:** Basis $a = {a_val}$, Numerus $x = 1$")
        st.latex(rf"^{{{a_val}}}\log 1 = 0")
        st.caption(f"Bukti: {a_val}⁰ = 1")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Sifat B: $^a\\log a = 1$")
        st.write(f"**Contoh Input:** Basis $a = {a_val}$, Numerus $x = {a_val}$")
        st.latex(rf"^{{{a_val}}}\log {a_val} = 1")
        st.caption(f"Bukti: {a_val}¹ = {a_val}")
        st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# MENU 3: SIFAT EKSPONEN NUMERUS
# -----------------------------------------------------------------------------
elif menu == "3. Sifat Pangkat Numerus":
    st.header("3. Sifat Pangkat Numerus")
    st.write(
        "b. Untuk $a > 0, a \\neq 1, x > 0$ dan $a, n, x \\in \\mathbb{R}$,"
        " berlaku:"
    )

    st.latex(r"^a\log x^n = n \cdot {}^a\log x")

    col1, col2, col3 = st.columns(3)

    with col1:
        a_s3 = st.number_input(
            "Basis (a):", value=2, step=1, min_value=2, key="a_s3"
        )
    with col2:
        x_base = st.number_input(
            "Nilai dasar x:", value=2, step=1, min_value=1, key="x_s3"
        )
    with col3:
        n_pangkat = st.number_input(
            "Pangkat Numerus (n):", value=4, step=1, key="n_s3"
        )

    numerus_total = int(math.pow(x_base, n_pangkat))

    st.markdown("---")
    st.subheader("📋 Langkah Penyelesaian:")

    val_base_log = int(math.log(x_base, a_s3))
    hasil_akhir = n_pangkat * val_base_log

    st.write(
        f"1. Ubah ke bentuk sifat:"
        f" $^{{{a_s3}}}\\log({{{x_base}}}^{{{n_pangkat}}}) = {n_pangkat} \\cdot"
        f" ^{{{a_s3}}}\\log({x_base})$"
    )
    st.write(f"2. Hitung nilai $^{{{a_s3}}}\\log({x_base}) = {val_base_log}$")
    st.write(
        f"3. Kalikan dengan pangkat $n$: ${n_pangkat} \\cdot {val_base_log}$"
    )

    st.success(
        f"**Hasil Akhir:** $^{{{a_s3}}}\\log({numerus_total}) = {hasil_akhir}$"
    )

# -----------------------------------------------------------------------------
# MENU 4: SIFAT EKSPONEN BASIS & NUMERUS
# -----------------------------------------------------------------------------
elif menu == "4. Sifat Pangkat Basis & Numerus":
    st.header("4. Sifat Pangkat Basis dan Numerus")
    st.write(
        "c. Untuk $a > 0, a \\neq 1, x > 0$ dan $a, m, n, x \\in \\mathbb{R}$,"
        " berlaku:"
    )

    st.latex(r"^{a^n}\log x^m = \frac{m}{n} \cdot {}^a\log x")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Input Basis ($a^n$)")
        a_base = st.number_input(
            "Basis Utama (a):", value=2, step=1, min_value=2, key="a_base_s4"
        )
        n_exp = st.number_input(
            "Pangkat Basis (n):", value=2, step=1, min_value=1, key="n_exp_s4"
        )

    with col2:
        st.subheader("Input Numerus ($x^m$)")
        x_base = st.number_input(
            "Numerus Utama (x):", value=2, step=1, min_value=1, key="x_base_s4"
        )
        m_exp = st.number_input(
            "Pangkat Numerus (m):", value=4, step=1, key="m_exp_s4"
        )

    basis_total = int(math.pow(a_base, n_exp))
    numerus_total = int(math.pow(x_base, m_exp))

    st.markdown("---")
    st.subheader("📋 Langkah Penyelesaian:")

    base_log = int(math.log(x_base, a_base))
    pembagi = m_exp / n_exp
    hasil_akhir = int(pembagi * base_log)

    # Perbaikan: Menggunakan tanda $...$ agar LaTeX dirender rapi
    st.write(
        f"1. Bentuk Soal: $^{{{basis_total}}}\\log({numerus_total})$ disederhanakan"
        f" menjadi $^{{{a_base}^{n_exp}}}\\log({x_base}^{m_exp})$"
    )
    st.write(
        f"2. Gunakan rumus sifat: $\\frac{{{m_exp}}}{{{n_exp}}} \\cdot"
        f" ^{{{a_base}}}\\log({x_base})$"
    )
    st.write(
        f"3. Hitung pecahan: $\\frac{{{m_exp}}}{{{n_exp}}} \\cdot {base_log}$"
    )

    st.success(
        f"**Hasil Akhir:** $^{{{basis_total}}}\\log({numerus_total}) ="
        f" {hasil_akhir}$"
    )
