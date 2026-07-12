import pandas as pd

def range_to_average(x):

    x = str(x).replace("%","").strip()

    if "-" in x:
        low, high = x.split("-")
        return (float(low)+float(high))/2

    return float(x)


def clean_dataframe(df):

    df["Lipid_Content(%)"] = df["Lipid_Content(%)"].apply(range_to_average)
    df["Protein_Content(%)"] = df["Protein_Content(%)"].apply(range_to_average)

    df["Average_Lipid"] = df["Lipid_Content(%)"]
    df["Average_Protein"] = df["Protein_Content(%)"]

    # all pd.to_numeric

    # strip()

    # nitrogen extraction

    return df