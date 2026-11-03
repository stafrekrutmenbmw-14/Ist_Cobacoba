import streamlit as st
import time

def render_subtest_1_se():
    if "step_se" not in st.session_state:
        st.session_state.step_se = "instruction"

    # TAHAP 1: INSTRUKSI (TANPA TIMER)
    if st.session_state.step_se == "instruction":
        st.title("📑 Petunjuk Subtes 01: SE (Melengkapi Kalimat)")
        st.info("💡 Bacalah petunjuk dengan cermat. Timer belum berjalan.")
        st.markdown("""
        Pilihlah kata yang paling tepat untuk menyempurnakan kalimat!
        *Contoh:* Seekor kuda mempunyai kesamaan terbanyak dengan seekor .....
        **Jawaban:** c) keledai
        """)
        if st.button("Mulai Kerjakan Subtes 1 🚀", type="primary"):
            st.session_state.step_se = "test"
            st.session_state.start_time_se = time.time()
            st.rerun()

    # TAHAP 2: SOAL & TIMER (6 MENIT)
    elif st.session_state.step_se == "test":
        st.title("🧠 Subtes 01: SE (Melengkapi Kalimat)")
        
        elapsed = int(time.time() - st.session_state.start_time_se)
        remaining = max(0, 360 - elapsed)
        m, s = divmod(remaining, 60)
        st.error(f"⏱️ **SISA WAKTU:** {m:02d}:{s:02d}")

        if remaining == 0:
            st.warning("⏰ Waktu habis!")
            st.session_state.current_subtest = 2  # Pindah ke Subtes 2
            st.rerun()

        with st.form("form_se"):
            # Contoh Soal SE
            st.write("Soal 01. Pengaruh seseorang terhadap orang lain bergantung pada .....")
            st.session_state.answers[1] = st.radio("Pilih:", ["a) kekuasaan", "b) bujukan", "c) kekayaan", "d) keberanian", "e) kewibawaan"], key="se_1")
            
            if st.form_submit_button("Lanjut ke Subtes 2 ➔"):
                st.session_state.current_subtest = 2  # Pindah ke Subtes 2
                st.rerun()
