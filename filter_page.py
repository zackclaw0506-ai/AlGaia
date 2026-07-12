import streamlit as st

def sidebar_filters(df):

    st.sidebar.title("⚙️ Filter Species")

    st.sidebar.caption(
        "Select only the conditions important to your application."
    )

    st.sidebar.divider()

    result = df.copy()