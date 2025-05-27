# %%

import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv")
df.head()

# %%

df["pontos_100"] = df["qtdePontos"] + 100
df

# %%
nova_coluna = []
for i in df["qtdePontos"]:
    nova_coluna.append(i+100)

nova_coluna

# %%

df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()

# %%

df["flEmail"] * df["flTwitch"]

# %%
df["qtdeSocial"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df

# %%
df["todas_social"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"]


# %%

df["qtdePontos"].describe()
# %%

df["logPontos"] = np.log(df["qtdePontos"]+1)
df["logPontos"].describe()


# %%

import matplotlib.pyplot as plt

plt.hist(df["logPontos"])
plt.grid(True)
plt.show()