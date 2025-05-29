# %%

# Leia o arquivo transações.csv com as formatações corretas.

import pandas as pd

df = pd.read_csv("../../data/transacoes.csv")
df

# Adicione uma coluna com valores 1 

df["nova_coluna"] = 1
df

# Salve o dataframe com o nome: transacoes_1.csv

df.to_csv("transacoes_1.csv")
