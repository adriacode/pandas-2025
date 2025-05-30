# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df.head()

# %%

def get_last_id(x):
    return x.split("-")[-1]

# %%

get_last_id("00684343-40b5-4ce7-b2e8-71a5340973bf")

# %%
id_novo = []
for i in df["idCliente"]:
    novo = get_last_id(i)
    id_novo.append(novo)

df["novo_id"]= id_novo
df.head()

# %%
df["idCliente"].apply(get_last_id)
