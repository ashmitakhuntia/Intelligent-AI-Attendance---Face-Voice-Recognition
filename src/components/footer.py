import streamlit as st

def footer_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style='margin-top:0.5rem; display:flex; gap:6px; justify-content:center; item-align:center;'>
            <p style='max-height:25px; font-weight:bold; color: white;'>Created with ❤️ by me</p>
        </div>

                """,unsafe_allow_html=True)

    
def footer_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style='margin-top:0.5rem; display:flex; gap:6px; justify-content:center; item-align:center;'>
            <p style='max-height:25px; font-weight:bold; color: black;'>Created with ❤️ by me</p>
        </div>

                """,unsafe_allow_html=True)