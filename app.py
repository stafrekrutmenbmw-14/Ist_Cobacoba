import streamlit as st

# Impor fungsi subtes dari folder 'subtests'
from subtests.subtest_1_se import render_subtest_1_se
from subtests.subtest_2_wa import render_subtest_2_wa

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Portal Psikotes IST - PT Bumi Mas Wahyu",
    page_icon="🧠",
    layout="wide"
)

# --- INISIALISASI STATE UTAMA ---
if "page" not in st.session_state:
    st.session_state.page = "register"
if "current_subtest" not in st.session_state:
    st.session_state.current_subtest = 1
if "user_info" not in st.session_state:
    st.session_state.user_info = {}
if "answers" not in st.session_state:
    st.session_state.answers = {}

# ==================================================================
# 1. HALAMAN REGISTRASI AWAL (DATA DIRI PELAMAR)
# ==================================================================
if st.session_state.page == "register":
    st.title("🏛️ PT Bumi Mas Wahyu")
    st.subheader("Portal Psikotes Online - IST (Intelligenz-Struktur-Test)")
    st.info("Mohon isi data diri Anda dengan lengkap sebelum memulai ujian.")

    with st.form("form_registrasi_awal"):
        nama = st.text_input("Nama Lengkap:")
        email = st.text_input("Alamat Email:")
        no_hp = st.text_input("Nomor WhatsApp / HP:")
        posisi = st.selectbox(
            "Posisi yang Dilamar:",
            [
                "Staff Closing (Sales / CS)",
                "Admin Rekrutmen / HR",
                "Supervisor Penjualan",
                "Staff Keuangan / Akuntansi",
                "Arsitek / Site Engineer",
                "Posisi Lainnya"
            ]
        )

        btn_start = st.form_submit_button("Mulai Tes IST 🚀", type="primary")

        if btn_start:
            if not nama or not email or not no_hp:
                st.error("⚠️ Mohon isi seluruh data diri secara lengkap!")
            else:
                st.session_state.user_info = {
                    "nama": nama,
                    "email": email,
                    "no_hp": no_hp,
                    "posisi": posisi
                }
                st.session_state.page = "test"
                st.session_state.current_subtest = 1
                st.rerun()

# ==================================================================
# 2. HALAMAN UTAMA PENGERJAAN SUBTES
# ==================================================================
elif st.session_state.page == "test":
    # Header Identitas Pelamar
    st.caption(
        f"👤 Kandidat: **{st.session_state.user_info.get('nama', '')}** | "
        f"💼 Posisi: **{st.session_state.user_info.get('posisi', '')}**"
    )
    st.markdown("---")

    # Pemanggilan Subtes Aktif
    if st.session_state.current_subtest == 1:
        render_subtest_1_se()

    elif st.session_state.current_subtest == 2:
        render_subtest_2_wa()

    elif st.session_state.current_subtest == 3:
        st.title("🎉 Subtes 1 & Subtes 2 Selesai!")
        st.success("Jawaban Anda untuk Subtes 1 (SE) dan Subtes 2 (WA) telah berhasil disimpan.")
        st.info("Silakan hubungi tim HR/Admin untuk instruksi subtes selanjutnya.")