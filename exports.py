import streamlit as st
def download_csv(result):

    csv = result.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download CSV",
        csv,
        "results.csv",
        "text/csv"
    )