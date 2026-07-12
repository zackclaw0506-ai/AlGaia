import streamlit as st

def hero():
 st.markdown("""
    <div style="
        background:linear-gradient(90deg,#0f5132,#198754,#20c997);
        padding:40px;
        border-radius:20px;
        text-align:center;
        color:white;
        margin-bottom:30px;
    ">
        <h1>🌿 AlGaia</h1>
        <h3>Microalgae Decision Support System</h3>
        <p>
        Discover the most suitable microalgae species using intelligent compatibility scoring.
        </p>
    </div>
    """, unsafe_allow_html=True)