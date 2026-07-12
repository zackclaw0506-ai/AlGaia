import streamlit as st

def show_charts(result):

    st.bar_chart(
        result.set_index("Species_Name")["Average_Protein"]
    )

    st.bar_chart(
        result.set_index("Species_Name")["Average_Lipid"]
    )