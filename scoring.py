#the is scoring.py
def calculate_score(row, user):

    score = 0
    reasons = []

    if user["use_habi"]:
        if row["Habitat_(Freshwater/Marine)"] == user["habitat"]:
            score += 20
            reasons.append("✔ Habitat matches")

    if user["use_temp"]:
        if row["Temperature_Min"] <= user["temp"] <= row["Temperature_Max"]:
            score += 20
            reasons.append("✔ Temperature compatible")

    if user["use_co2"]:
        if row["Co2_Tolerance"] == user["co2"]:
            score += 15
            reasons.append("✔ CO₂ tolerance")

    if user["use_ph"]:
        if row["pH_Min"] <= user["ph"] <= row["pH_Max"]:
            score += 15
            reasons.append("✔ pH compatible")

    if user["use_salinity"]:
        if row["Salinity"] == user["salinity"]:
            score += 10
            reasons.append("✔ Salinity")

    if user["use_n"]:
        if row["Nitrogen_Requirements(Low/Med/High)(mgN/L)"] == user["nitrogen"]:
            score += 10
            reasons.append("✔ Nitrogen")

    if user["use_app"]:
        if user["application"].lower() in row["Suitable_Applications"].lower():
            score += 10
            reasons.append("✔ Application")

    explanation = "\n".join(reasons)

    return score, "\n".join(reasons)