#This is filters.py from utils folder
import streamlit as st

def sidebar_filters(df):
    result = df.copy()
    
    st.sidebar.title("⚙️ Filter Species")
    st.sidebar.caption(
        "Select only the conditions important to your application."
    )
    st.sidebar.divider()

    # Default values
    habitat = None
    temp = None
    co2 = None
    ph = None
    salinity = None
    nitrogen = None
    application = None

    user = {

        "use_habi": False,
        "habitat": None,

        "use_temp": False,
        "temp": None,

        "use_co2": False,
        "co2": None,

        "use_ph": False,
        "ph": None,

        "use_salinity": False,
        "salinity": None,

        "use_n": False,
        "nitrogen": None,

        "use_app": False,
        "application": None,
    }


    # Sidebars
    with st.sidebar.expander("🌊 Habitat"):
         user["use_habi"] = st.toggle(
        "Use this filter",
        key="Habi_toggle"
)
    if user["use_habi"]:
        habitat = st.selectbox(
            "Habitat",
            sorted(df["Habitat_(Freshwater/Marine)"].dropna().unique())
        )
        result = result[
            result["Habitat_(Freshwater/Marine)"] == habitat
        ]

    with st.sidebar.expander("🌡 Temperature"):
     user["use_temp"] = st.toggle(
    "Use this filter",
    key="temp_toggle"
)
    if user["use_temp"]:
        temp = st.slider(
            "Temperature (°C)",
            -5,
            50,
            25
        )
        result = result[
            (result["Temperature_Min"] <= temp) &
            (result["Temperature_Max"] >= temp)
        ]

    with st.sidebar.expander("🌍 CO₂ Tolerance"):
     user["use_co2"] = st.toggle(
    "Use this filter",
    key="co2_toggle"
)
    if user["use_co2"]:
        co2 = st.selectbox(
            "CO₂",
            sorted(df["Co2_Tolerance"].dropna().unique())
        )
        result = result[
            result["Co2_Tolerance"] == co2
        ]

    with st.sidebar.expander("🧪 pH Range"):
     user["use_ph"] = st.toggle(
    "Use this filter",
    key="ph_toggle"
)
    if user["use_ph"]:
        ph = st.slider(
            "pH",
            0.0,
            14.0,
            7.0
        )
        result = result[
            (result["pH_Min"] <= ph) &
            (result["pH_Max"] >= ph)
        ]

    with st.sidebar.expander("💧 Salinity"):
     user["use_salinity"] = st.toggle(
    "Use this filter",
    key="salinity_toggle"
)
    if user["use_salinity"]:
        salinity = st.selectbox(
            "Select Salinity",
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
        
    with st.sidebar.expander("🌱 Nitrogen"):
     user["use_n"] = st.toggle(
    "Use this filter",
    key="nitrogen_toggle"
)
    if user["use_n"]:
        nitrogen = st.selectbox(
       "🌱 Nitrogen Requirement",
        sorted(
        df[
            "Nitrogen_Requirements(Low/Med/High)(mgN/L)"
        ]
        .dropna()
        .astype(str)
        .unique()
      )
     )
        result = result[
            result["Nitrogen_Requirements(Low/Med/High)(mgN/L)"] == nitrogen
        ]

    with st.sidebar.expander("🎯 Applications"):
     user["use_app"] = st.toggle(
    "Use this filter",
    key="application_toggle"
)
    if user["use_app"]:
        application = st.selectbox(
            "Application",
            [
                "Food",
                "Biofuel",
                "Carbon Capture",
                "Wastewater Treatment",
                "Cosmetics"
            ]
        )
        result = result[
            result["Suitable_Applications"]
            .str.contains(application, case=False, na=False)
        ]
        
        st.write("habitat =", habitat)
        st.write("temp =", temp)
        st.write("co2 =", co2)
        st.write("ph =", ph)
        st.write("salinity =", salinity)
        st.write("nitrogen =", nitrogen)
        st.write("application =", application)
    user = {
    "use_habi": user["use_habi"],
    "habitat": habitat,
    "use_temp": user["use_temp"],
    "temp": temp,
    "use_co2": user["use_co2"],
    "co2": co2,
    "use_ph": user["use_ph"],
    "ph": ph,
    "use_salinity": user["use_salinity"],
    "salinity": salinity,
    "use_n": user["use_n"],
    "nitrogen": nitrogen,
    "use_app": user["use_app"],
    "application": application,
}

    if st.sidebar.button("🔄 Reset Filters"):

        for key in list(st.session_state.keys()):
         del st.session_state[key]

         st.rerun()

    return result, user