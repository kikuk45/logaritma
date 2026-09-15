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
# SIDEBAR NAVIGATION
# -----------------------------------------------------------------------------
st.sidebar.header("🎯 Navigasi Materi")

menu_options = {
    "Definisi Logaritma": "📘 Definisi Logaritma",
    "Sifat A": "🔹 Sifat a: Logaritma Basis & Numerus Sama",
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
