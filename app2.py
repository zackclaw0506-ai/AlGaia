import pandas as pd
import streamlit as st

st.title("🌿 AlGaia")
st.subheader("Microalgae Decision Support System")

st.write(
"""
Search and compare microalgae species
for carbon capture,
biofuel,
food,
and biotechnology.

"""
)   
df = pd.read_excel("output.xlsx", header=2)
df.columns = df.columns.str.strip()

def range_to_average(x):
    x = str(x).replace("%", "").strip()

    if "-" in x:
        low, high = x.split("-")
        return (float(low) + float(high)) / 2

    return float(x)


df["Lipid_Content(%)"] = df["Lipid_Content(%)"].apply(range_to_average)
df["Protein_Content(%)"] = df["Protein_Content(%)"].apply(range_to_average)
df["Average_Lipid"] = df["Lipid_Content(%)"].apply(range_to_average)
df["Average_Protein"] = df["Protein_Content(%)"].apply(range_to_average)


search = st.text_input("Search Species")
result = df.copy()

sort_by = st.selectbox(
    "Sort Results By",
    [
        "Species_Name",
        "Average_Lipid",
        "Average_Protein",
        "Growth_Rate_(L/m/h)",
        "Carbon_Fixation_Rate_(L^-1 day^-1)(l/M/H)"
    ]
)
result = result.sort_values(sort_by)
ascending = st.checkbox("Ascending Order")

result = result.sort_values(
    by=sort_by,
    ascending=ascending
)

result["Lipid_Content(%)"].mean()

df["Lipid_Content(%)"] = pd.to_numeric(
    df["Lipid_Content(%)"],
    errors="coerce"
)
df["Protein_Content(%)"] = pd.to_numeric(
    df["Protein_Content(%)"],
    errors="coerce"
)

df["Temperature_Min"] = pd.to_numeric(
    df["Temperature_Min"],
    errors="coerce"
)

df["Temperature_Max"] = pd.to_numeric(
    df["Temperature_Max"],
    errors="coerce"
)

df["pH_Min"] = pd.to_numeric(
    df["pH_Min"],
    errors="coerce"
)

df["pH_Max"] = pd.to_numeric(
    df["pH_Max"],
    errors="coerce"
)


if search:
    result = result[
        result["Species_Name"].str.contains(search, case=False)
    ]

# Clean text columns
for col in [
    "Habitat_(Freshwater/Marine)",
    "Salinity",
    "Co2_Tolerance"
]:
    df[col] = df[col].astype(str).str.strip()

habitat = st.sidebar.selectbox(
    "Habitat",
    ["Freshwater", "Marine"]
)
result = df[df["Habitat_(Freshwater/Marine)"] ==habitat]

temp = st.sidebar.slider(
    "Temperature",
    min_value=-5,
    max_value=50,
    value=25
)
result = result[
    (result["Temperature_Min"]<= temp) & 
    (result["Temperature_Max"]>= temp)
    ]

co2 = st.sidebar.selectbox(
    "CO₂ Tolerance",
    sorted(df["Co2_Tolerance"].dropna().unique())
)
result = result[result["Co2_Tolerance"] ==co2]

pH = st.sidebar.slider(
    label="pH",
    min_value=0.0,
    max_value=14.0,
    value=7.0
)
result = result[
    (result["pH_Min"]<= pH) & 
    (result["pH_Max"]>= pH)
    ]

salinity = st.sidebar.selectbox(
    "Salinity",
    [
        "Freshwater",
        "Marine",
        "Brackish",
        "High alkalinity",
        "Low–Moderate",
        "Extreme salinity"
    ]
)
result = result[
    result["Salinity"] == salinity
    ]


col1,col2,col3 = st.columns(3)

col1.metric("Species Found",len(result))
col2.metric(
    "Average Lipid %",
    round(result["Average_Lipid"].mean(), 1)
)
col3.metric(
    "Average Protein %",
    round(result["Average_Protein"].mean(), 1)
)

st.success(f"{len(result)} species found.")

if result.empty:
    st.error("No species match these conditions.")

else:
    st.dataframe(result)

st.dataframe(
    result[
        [
            "Species_Name",
            "Temperature_Min",
            "Temperature_Max",
            "Lipid_Content(%)",
            "Protein_Content(%)",
        ]
    ]
)

st.bar_chart(result.set_index("Species_Name")["Average_Protein"])
st.bar_chart(result.set_index("Species_Name")["Average_Lipid"])
