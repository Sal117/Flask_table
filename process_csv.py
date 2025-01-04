import pandas as pd

df=pd.read_csv("Table_input.csv")

alpha=df.loc[df['Index #']=='A5','Value'].values[0]+df.loc[df['Index #']=='A20','Value'].values[0]
beta=df.loc[df['Index #']=='A15','Value'].values[0]/df.loc[df['Index #']=='A7','Value'].values[0]
charlie=df.loc[df['Index #']=='A13','Value'].values[0]*df.loc[df['Index #']=='A12','Value'].values[0]

print(f"Alpha: {alpha}, Beta:{beta}, Charlie: {charlie}")