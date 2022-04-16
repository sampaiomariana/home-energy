import pandas as pd

df = pd.read_excel('consumo.xlsx',skiprows=2)

df
#Soma por produto
df.groupby(by=["componente"]).sum()
#Soma por produto em Janeiro
df.groupby(by=["componente"]).sum()[["Jan"]]
#Soma por produto em Janeiro Ordenados
df.groupby(by=["componente"]).sum()[["Jan"]].sort_values(by="Jan")


