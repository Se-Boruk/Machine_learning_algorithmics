import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Columns
column_names = [
    "CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS",
    "RAD","TAX","PTRATIO","B","LSTAT","MEDV"
]

df = pd.read_csv(
    "boston.txt",
    sep=r"\s+", #Separator is just blank space (in not definet lenght)
    header=None, #No headers, but column names from hardcoded list
    names=column_names,
    skiprows=22  #Skip 22 lines
)

#Pair and un-pair (0,2,4..) (1,3,5...)
even_rows = df.iloc[::2].reset_index(drop=True) #11 kolumn
odd_rows = df.iloc[1::2].reset_index(drop=True) #3 ostatnie kolumny

#Nadpisanie
even_rows.iloc[:, -3:] = odd_rows.iloc[:, :3]

# Rezultat to zmergowane wiersze
df = even_rows
del even_rows, odd_rows
