import streamlit as st


def show_results_table(result):

    if result.empty:
        st.error(
            "🌱 No species matched.\n\n"
            "Try:\n"
            "• Reducing filters\n"
            "• Selecting a wider temperature\n"
            "• Choosing another application."
        )
        return

    display = result[
        [
            "Species_Name",
            "Recommendation",
            "Compatibility",
            "Average_Protein",
            "Average_Lipid",
            "Suitable_Applications"
        ]
    ].rename(
        columns={
            "Species_Name": "🧬 Species",
            "Recommendation": "⭐ Rating",
            "Compatibility": "🎯 Compatibility",
            "Average_Protein": "🥩 Protein (%)",
            "Average_Lipid": "🛢 Lipid (%)",
            "Suitable_Applications": "🎯 Applications"
        }
    )

    st.success(f"{len(result)} species found.")

    st.dataframe(
        display,
        width="stretch",
        hide_index=True
    )