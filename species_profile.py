#This is species_profile.py

import streamlit as st
import os

from utils.loader import load_data
from utils.cleaner import clean_dataframe

df = clean_dataframe(load_data())

if st.button("⬅ Back to Search"):
    st.switch_page("app2.py")

if "selected_species" not in st.session_state:
    st.error("No species selected.")
    st.stop()
species = st.session_state["selected_species"]

row = df[
    df["Species_Name"] == species
].iloc[0]

st.title(row["Species_Name"])
st.subheader("Basic Information")
st.write(f"**Habitat:** {row['Habitat_(Freshwater/Marine)']}")
st.write(f"**Temperature:** {row['Temperature_Min']}°C - {row['Temperature_Max']}°C")
st.write(f"**Protein:** {row['Average_Protein']}%")
st.write(f"**Lipid:** {row['Average_Lipid']}%")
st.write(f"**Growth Rate:** {row['Growth_Rate_(L/m/h)']}")
st.write(f"**Carbon Fixation:** {row['Carbon_Fixation_Rate_(L^-1 day^-1)(l/M/H)']}")
st.write(f"**Applications:** {row['Suitable_Applications']}")
image_path = f"images/{species}.jpg"

if os.path.exists(image_path):
    st.image(image_path, width=350)
else:
    st.info("Image not available.")