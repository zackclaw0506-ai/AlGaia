import streamlit as st

def show_metrics(result):

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "🌿 Species Found",
        len(result)
    )

    filters = 0

    if "Compatibility" in result.columns:
        best = round(result["Compatibility"].max(), 1)
    else:
        best = "--"

    col2.metric(
        "🔥 Highest Compatibility",
        best
    )

    for column in [
        "Habitat_(Freshwater/Marine)",
        "Suitable_Applications"
    ]:
        if column in result.columns:
            filters += result[column].nunique()

    col3.metric(
        "📊 Unique Categories",
        filters
    )