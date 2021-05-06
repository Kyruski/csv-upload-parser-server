import pandas as pd


def read_file(file, xAxis):
    df = pd.read_csv(file)
    if xAxis == 'columns':
        df = df.transpose()
