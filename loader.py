import pandas as pd

def load_data():

    df = pd.read_excel("output.xlsx", header=2)
    df.columns = df.columns.str.strip()

    return df