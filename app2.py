#this is app2.py , the main code for AlGaia

import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
##Pages##
#Hero
from components.hero import hero
#Loader
from utils.loader import load_data
#scoring
from utils.scoring import calculate_score
#Charts
from utils.charts import show_charts
#exports
from utils.exports import download_csv
#cleaner
from utils.cleaner import clean_dataframe
df = clean_dataframe(load_data())
#filters
from utils.filters import sidebar_filters
#metric
from utils.metric import show_metrics
#Stars
from utils.star import add_recommendation
#soting
from utils.sorting import sort_species
#comparison
from pages.compare import comparison
#Result table
from pages.result_table import show_results_table

#hero
hero()


sort_options = {
    "Species Name":"Species_Name",
    "Compatibility":"Compatibility",
    "Protein":"Average_Protein",
    "Lipid":"Average_Lipid",
    "Growth Rate":"Growth_Rate_(L/m/h)",
    "Carbon Fixation":"Carbon_Fixation_Rate_(L^-1 day^-1)(l/M/H)"
}

result, user = sidebar_filters(df)

st.divider()

st.subheader("🔍 Search & Filter")

st.caption("Search species or use the filters in the sidebar.")
species = st.selectbox(
    "🧬 Search Species",
    ["All Species"] +
    sorted(
        df["Species_Name"]
        .dropna()
        .astype(str)
        .unique()
    ))
if species != "All Species":
    if st.button("🔍 View Species Profile"):

        st.session_state["selected_species"] = species

        st.switch_page("pages/species_profile.py")


st.divider()
st.subheader("📋 Matching Species")
st.caption(
    "These species match your current filters."
)

# ⭐ Calculate compatibility HERE
scores = result.apply(
    calculate_score,
    axis=1,
    user=user
)

result["Compatibility"] = scores.apply(lambda x: x[0])
result["Why Recommended"] = scores.apply(lambda x: x[1])


result = add_recommendation(result)

# NOW show metrics
show_metrics(result)

# THEN sort
result = sort_species(result, sort_options)

# THEN display dataframe
st.success(f"{len(result)} species found.")

#why recom
st.divider()

st.subheader("🧠 Recommendation Insights")
st.caption(
    "See why each species was recommended."
)

# Show only the Top 3 recommendations
top3 = result.sort_values(
    by="Compatibility",
    ascending=False
).head(3)

for _, row in top3.iterrows():

    with st.expander(f"🧬 {row['Species_Name']}"):
        st.write(f"### ⭐ {row['Recommendation']}")

        st.progress(row["Compatibility"] / 100)

        st.write(
            f"**Compatibility Score:** {row['Compatibility']}%"
        )
        st.write("### 📊 Basic Information")
        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                "🥩 Protein",
                f"{row['Average_Protein']}%"
            )
            st.metric(
                "🛢 Lipid",
                f"{row['Average_Lipid']}%"
            )

        with col2:
            st.metric(
                "⚡ Growth Rate",
                row["Growth_Rate_(L/m/h)"]
            )
            st.metric(
                "🌍 Carbon Fixation",
                row["Carbon_Fixation_Rate_(L^-1 day^-1)(l/M/H)"]
            )
        st.write("### 🎯 Applications")
        st.info(
            row["Suitable_Applications"]
        )
        st.write("### ✅ Why Recommended")
        st.success(
            row["Why Recommended"]
        )
#Charts
st.divider()
st.subheader("📊 Data Insights")
st.caption(
    "Charts summarise the filtered species."
)
show_charts(result)

#CSV
csv = result.to_csv(index=False).encode("utf-8")
st.divider()
st.subheader("📥 Export")
st.caption(
    "Download your filtered dataset."
)
st.download_button(
    "📥 Download CSV",
    csv,
    "AlGaia_Results.csv",
    "text/csv"
)
