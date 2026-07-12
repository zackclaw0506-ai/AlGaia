import streamlit as st

def sort_species(result, sort_options):

    ascending = st.checkbox(
        "Ascending Order",
        key="ascending_sort"
    )

    choice = st.selectbox(
        "Sort By",
        list(sort_options.keys()),
        key="sort_choice"
    )

    return result.sort_values(
        by=sort_options[choice],
        ascending=ascending
    )