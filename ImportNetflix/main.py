import pandas as pd

df= pd.read_csv(r"C:\UCD2021\PandasTesting\netflix_titles.csv")

print(df.head(2))

print(df.tail(2))

print(df.shape)

print(df.columns)

df.isnull().sum

df.dtypes
