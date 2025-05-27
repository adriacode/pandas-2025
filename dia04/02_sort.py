# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")

max_ponto = clientes["qtdePontos"].max()
filtro = clientes["qtdePontos"] == max_ponto
clientes[filtro]

# %% 
top_5 = (clientes.sort_values(by="qtdePontos", ascending=False)
        .head(5)["idCliente"] )
type(top_5)

# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "ana", "nah", "jose"],
        "idade": [32, 43, 35, 42],
        "salario": [2345, 4533, 3245, 4533],
    }
)

brinquedo

# %%

brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])

# %%
