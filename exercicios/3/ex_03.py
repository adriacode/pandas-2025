# %%
import pandas as pd

clientes = pd.read_csv("../../data/clientes.csv")
transacoes = pd.read_csv("../../data/transacoes.csv")
produtos = pd.read_csv("../../data/produtos.csv")
# %%
# Quantas linhas há no arquivo clientes.csv ?
qtde_linhas = clientes.shape[0]
qtde_linhas

# %%
# Quantas colunas do tipo int há no arquivo transacoes.csv ?
tipos = transacoes.dtypes
tipo_int = [i for i in tipos if i == "int64"]
resp = len(tipo_int)
resp
# %%
# Quantas colunas do tipo object há no arquivo produtos.csv ?
tipos_prod = produtos.dtypes
tipo_object = [x for x in tipos_prod if x == "object"]
resp_2 = len(tipo_object)
resp_2
# %%
# Qual o id do cliente no índice 4 no arquivo clientes.csv ?
clientes["idCliente"][4]
# %%
# Qual o saldo de pontos do cliente na 10a posição (sem ordenar) do arquivo clientes.csv ?
clientes["qtdePontos"][10]