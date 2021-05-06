import pandas as pd


def read_file(file):
    df = pd.read_csv(file)
    print(df)
