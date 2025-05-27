# %%

import pandas as pd

# %%

df = pd.read_csv("../data/clientes.csv")

# %%
df["qtdePontos"].astype(float).astype(str)

# %%

replace = {"0000-00-00 00:00:00.000": "2024-02-01 09:00:00.000"}

df["dtCriacao"] = pd.to_datetime(df["dtCriacao"].replace(replace))
df["dtCriacao"]

# %% 

df["dtCriacao"].dt.date
# %%
