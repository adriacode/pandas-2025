# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df

qtde_linhas = df.shape[0]
qtde_linhas

# %%
df.info(memory_usage="deep")

# %%
df.dtypes

# %%
# RENOMEANDO COLUNAS

renamed_columns = {
    "qtdePontos":"qtPontos", 
    "descSistemaOrigem": "SistemaOrigem"  
}

df.rename(columns=renamed_columns, inplace=True)
df

# %%
df["idCliente"]

# %%
df[["idCliente", "qtPontos"]]
df[["idCliente"]]



# %%
# SELECT * FROM df
df

# %%
# SELECT idCliente FROM df
df[["id_cliente"]]

# %%
# SELECT idCliente, qtPontos FROM df LIMIT 5

df[["idCliente", "qtPontos"]].tail(5)

# %%
# SELECT idCliente, idTransacao, qtPontos
# FROM df
# LIMIT 5

df[["idCliente", "idTransacao", "qtPontos"]].head(5)

# %%
# ORDENANDO COLUNAS
colunas = df.columns.tolist()
colunas.sort()
colunas


df = df[colunas]
df
