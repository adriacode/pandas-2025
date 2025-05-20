# %%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv")
df_clientes

# %%

df_clientes.head() # mostra as 5 primeiras linhas do dataframe

# %%

df_clientes.head(n=10)

# %%

df_clientes.tail() # mostra as últimas linhas do dataframe

df_clientes.tail(n=10)

# %%

df_clientes.sample(10) # amostra aleatória


# %%

df_clientes.shape

# %%
df_clientes.columns

# %%
df_clientes.index

# %%
df_clientes.info(memory_usage="deep", max_cols=2)

# %%
df_clientes.dtypes["qtdePontos"]
df_clientes.dtypes["idCliente"]

# dtypes é uma série que mostra a tipagem de cada coluna do dataframe.

