import pandas as pd
import streamlit as st

st.title("🌿 AlGaia")
st.subheader("Microalgae Decision Support System")

st.write(
"""
Select the environmental conditions on the left.

The program will search the database and display all suitable microalgae species.
"""
)   

df = pd.read_excel("output.xlsx", header=2)
df.columns = df.columns.str.strip()

# Clean text columns
for col in [
    "Habitat_(Freshwater/Marine)",
    "Salinity",
    "Co2_Tolerance"
]:
    df[col] = df[col].astype(str).str.strip()

habitat = st.selectbox(
    "Habitat",
    ["Freshwater", "Marine"]
)
result = df[df["Habitat_(Freshwater/Marine)"] ==habitat]

temp = st.slider(
    "Temperature",
    min_value=-5,
    max_value=50,
    value=25
)
result = result[
    (result["Temperature_Min"]<= temp) & 
    (result["Temperature_Max"]>= temp)
    ]

co2 = st.selectbox(
    "CO₂ Tolerance",
    sorted(df["Co2_Tolerance"].dropna().unique())
)
result = result[result["Co2_Tolerance"] ==co2]

pH = st.slider(
    label="pH",
    min_value=0.0,
    max_value=14.0,
    value=7.0
)
result = result[
    (result["pH_Min"]<= pH) & 
    (result["pH_Max"]>= pH)
    ]

salinity = st.selectbox(
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