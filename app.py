from decimal import Decimal
from fractions import Fraction
import math
import base64
from pathlib import Path
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
# FUNGSI UNTUK MEMUAT BACKGROUND (PNG LOKAL DENGAN FALLBACK MOTIF ADAPTIF)
# -----------------------------------------------------------------------------
def set_adaptive_background(image_file):
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    img_path = current_dir / image_file
    
    background_css = ""
    
    # Cek apakah file PNG lokal tersedia
    if img_path.exists():
        with open(img_path, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode()
        # Menggunakan PNG lokal dengan overlay transparan agar teks tetap kontras di tema terang/gelap
        background_css = f"""
        background-image: linear-gradient(rgba(var(--background-color-rgb, 255, 255, 255), 0.88), rgba(var(--background-color-rgb, 255, 255, 255), 0.88)), url("data:image/png;base64,{encoded_string}") !important;
        background-size: cover !important;
        background-position: center center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
        """
    else:
        # Fallback pola geometri SVG transparan yang otomatis tembus/menyesuaikan tema terang & gelap
        svg_pattern = '''
