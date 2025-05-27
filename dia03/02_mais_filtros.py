# %%

import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv")
df

# %%
filtro = (df["idProduto"] == 5) | (df["idProduto"] == 11)
df[filtro]


# %%
filtro = df["idProduto"].isin([5,11])
df[filtro]

# %%
clientes = pd.read_csv("../data/clientes.csv")
clientes.head()

filtro = clientes["dtCriacao"].notna()
clientes[filtro]

# %%
~clientes["dtCriacao"].notna()
clientes["dtCriacao"].notna()