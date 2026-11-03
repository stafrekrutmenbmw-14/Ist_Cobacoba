import streamlit as st
import time

def render_subtest_2_wa():
    if "step_wa" not in st.session_state:
        st.session_state.step_wa = "instruction"

    # TAHAP 1: INSTRUKSI (TANPA TIMER)
    if st.session_state.step_wa == "instruction":
        st.title("📑 Petunjuk Subtes 02: WA (Mencari Kata Berbeda)")
        st.info("💡 Bacalah petunjuk dengan cermat. Timer belum berjalan.")
        st.markdown("""
        Pilihlah 1 kata yang TIDAK memiliki kesamaan dengan 4 kata lainnya!
        *Contoh:* a) meja  b) kursi  c) burung  d) lemari  e) tempat tidur
        **Jawaban:** c) burung
        """)
        if st.button("Mulai Kerjakan Subtes 2 🚀", type="primary"):
            st.session_state.step_wa = "test"
            st.session_state.start_time_wa = time.time()
            st.rerun()

    # TAHAP 2: SOAL & TIMER (6 MENIT)
    elif st.session_state.step_wa == "test":
        st.title("🧠 Subtes 02: WA (Mencari Kata Berbeda)")
        
        elapsed = int(time.time() - st.session_state.start_time_wa)
        remaining = max(0, 360 - elapsed)
        m, s = divmod(remaining, 60)
        st.error(f"⏱️ **SISA WAKTU:** {m:02d}:{s:02d}")

        if remaining == 0:
            st.warning("⏰ Waktu habis!")
            st.session_state.current_subtest = 3  # Pindah ke Subtes 3
            st.rerun()

        with st.form("form_wa"):
            # Contoh Soal WA
            st.write("Soal 21. Pilihlah kata yang tidak memiliki kesamaan:")
            st.session_state.answers[21] = st.radio("Pilih:", ["a) lingkaran", "b) panah", "c) elips", "d) busur", "e) lengkungan"], key="wa_21")
            
            if st.form_submit_button("Lanjut ke Subtes 3 ➔"):
                st.session_state.current_subtest = 3  # Pindah ke Subtes 3
                st.rerun()
