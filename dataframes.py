import pandas as pd
import numpy as np

print('============== ZADANIE 1 ==============')

data = pd.read_csv('exams.csv')
head = list(data.head(0))
print(head)

choice = list([head[0],head[2]])
measure = list(data.select_dtypes(include=['number']).columns)

print(choice)
print(measure)

gr = data.groupby(choice).mean()
print(gr)

# Jak zamiast wskazania kolumny uzyc choice i measure, mam error skladniowy "SyntaxError: positional argument follows keyword argument"

def reindex_df(df_dataframe):

    df = df_dataframe.reset_index()
    df = pd.DataFrame(df, columns = [head[5],head[6],head[7],head[0],head[2]])
    return df

print(reindex_df(gr))

print('============== ZADANIE 2 ==============')

# ODPOWIEDZ W PLIKU ML-classifier.py
