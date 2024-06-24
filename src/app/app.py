import streamlit as st
from backend.main import run

class UI:
    def __init__(self):
        st.set_page_config(page_title="Hikmah Wealth Program", page_icon="📊")

    def sidebar(self):
        with st.sidebar:
            st.header("📊 - Hikmah Wealth Program")
            ticker = st.text_input("Enter The Ticker: ", key="ticker", placeholder="Ex. TCS (Tata Consultancy Services)")
            if st.button("Generate Report", use_container_width=True):
                st.session_state.generating = True

    def render(self):
        if "ticker" not in st.session_state:
            st.session_state.ticker = ""
        if "generating" not in st.session_state:
            st.session_state.generating = False

        if st.session_state.generating:
            results = run(st.session_state.ticker)
            st.write(results)

    def run(self):
        self.sidebar()
        if "generating" not in st.session_state:
            st.session_state.generating = False

        if st.session_state.generating:
            results = run(st.session_state.ticker)
            st.success("Report Generated Successfully!")
        else:
            self.render()

if __name__ == "__main__":
    UI().run()
