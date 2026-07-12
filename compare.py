import streamlit as st

from utils.loader import load_data
from utils.cleaner import clean_dataframe

df = clean_dataframe(load_data())

#Field
FIELDS = {

    "Protein (%)": "Average_Protein",

    "Lipid (%)": "Average_Lipid",

    "Growth Rate": "Growth_Rate_(L/m/h)",

    "Carbon Fixation": "Carbon_Fixation_Rate_(L^-1 day^-1)(l/M/H)"

}

species1 = st.selectbox(
    "Species A",
    df["Species_Name"]
)

species2 = st.selectbox(
    "Species B",
    df["Species_Name"],
    index=1
)

# Extract rowss
row1 = df[
    df["Species_Name"] == species1
].iloc[0]

row2 = df[
    df["Species_Name"] == species2
].iloc[0]

#Comparison table
comparison = {
    "Property":[
        "Habitat",
        "Protein",
        "Lipid",
        "Temperature",
        "Growth Rate"
    ],

    species1:[
        row1["Habitat_(Freshwater/Marine)"],
        row1["Average_Protein"],
        row1["Average_Lipid"],
        f"{row1['Temperature_Min']}-{row1['Temperature_Max']}",
        row1["Growth_Rate_(L/m/h)"]
    ],

    species2:[
        row2["Habitat_(Freshwater/Marine)"],
        row2["Average_Protein"],
        row2["Average_Lipid"],
        f"{row2['Temperature_Min']}-{row2['Temperature_Max']}",
        row2["Growth_Rate_(L/m/h)"]
    ]
}

#Column
col1, col2 = st.columns(2)
with col1:
    st.subheader(species1)
    for label, column in FIELDS.items():
        st.metric(
            label,
            row1[column]
        )

with col2:
    st.subheader(species2)
    for label, column in FIELDS.items():
        st.metric(
            label,
            row2[column]
        )
        
import os    
image = f"images/{species1}.jpg"

if os.path.exists(image):
    st.image(image, width=250)
   
st.subheader("🏆 Winners")
for label, column in FIELDS.items():
    value1 = row1[column]
    value2 = row2[column]
    if value1 > value2:
        st.success(f"{label}: 🏆 {species1}")
    elif value2 > value1:
        st.success(f"{label}: 🏆 {species2}")
    else:
        st.info(f"{label}: Tie; Both are Equal")