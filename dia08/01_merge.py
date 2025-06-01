# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()

# %%
clientes = pd.read_csv("../data/clientes.csv")
clientes.head()

transacoes.merge(right=clientes, 
                 how="left", 
                 on=["idCliente"], 
                 suffixes=["Transacao", "Cliente"]
)

# %%

df_1 = pd.DataFrame({
    "transacao": [1,2,3,4,5],
    "idCliente": [1,2,3,2,2],
    "valor": [10,45,32,17,87],
})

df_2 = pd.DataFrame({
    "id": [1,2,3,4],
    "nome": ["teo", "nah", "mah", "jose"],
})

df_1.merge(df_2, left_on=["idCliente"], 
           right_on=["id"],
           how="left",
           suffixes=["Transacao", "Cliente"],
)
