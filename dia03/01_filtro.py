# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df.head()

# %%

pontos = [10, 1, 1, 1, 50, 100, 130, 1, 1, 30, 25, 50]

valores_50_mais = [x for x in pontos if x >= 50]
valores_50_mais

# %%
pontos = [10, 1, 1, 1, 50, 100, 130, 1, 1, 30, 25, 50]
filtro = []
for i in pontos:
    filtro.append(i>=50)

resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])

resultado

# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32, 35, 14],
        "uf": ["sp", "pr", "rj"],
    }
)

filtro = brinquedo["idade"] >= 18
filtro

brinquedo[filtro]

# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df.head()

# Valores maiores que 50
filtro = df["qtdePontos"] >= 50

df[filtro]

# %%

# Valores entre 50 (inclusive) e 100
filtro = (df["qtdePontos"] >= 50) * (df["qtdePontos"] < 100)
df[filtro]

# %%

# Valores igual a 1 ou 100
filtro = (df["qtdePontos"] == 1) + (df["qtdePontos"] == 100)
df[filtro]

# %%

# pontos entre 0 e 50 ou do ano de 2025 pra frente
filtro = (df["qtdePontos"] > 0) & (df["qtdePontos"] <= 50) | (df["dtCriacao"] >= '2025-01-01')
df[filtro]
# %%
