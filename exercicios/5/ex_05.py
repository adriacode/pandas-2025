# %%
import pandas as pd

clientes = pd.read_csv("../../data/clientes.csv")
transacoes = pd.read_csv("../../data/transacoes.csv")

# %%
# 05.01 - Crie uma coluna nova “twitch_points” que e resultado da multiplicação do saldo de pontos e a marcação da twitch
clientes["twitch_points"] = clientes["qtdePontos"] * clientes["flTwitch"]
clientes
# %%
# 05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova
import numpy as np
clientes["logQtdePontos"] = np.log(clientes["qtdePontos"]+1)
clientes
# %%
# 05.03 - Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.
clientes["pelo_menos_uma_rede"] = (clientes["flEmail"] == 1) | (clientes["flTwitch"] == 1) | (clientes["flYouTube"] == 1) | (clientes["flBlueSky"] == 1) | (clientes["flInstagram"] == 1)
clientes 
# %%
# 05.04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor?
clientes.sort_values(by="qtdePontos", ascending=False).head(1)["idCliente"]
clientes.sort_values(by="qtdePontos", ascending=True).head(1)["idCliente"]
# %%
# 05.05 - Selecione a primeira transação diária de cada cliente.
transacoes["data"] = pd.to_datetime(transacoes["dtCriacao"]).dt.date

transacoes = transacoes.sort_values(by="dtCriacao")
transacoes.drop_duplicates(keep="first", subset=["idCliente", "data"])

# %%

transacoes = transacoes.sort_values(by="dtCriacao")

first = transacoes.drop_duplicates(keep="first", subset=["idCliente", "data"])

last = transacoes.drop_duplicates(keep="last", subset=["idCliente", "data"])

pd.concat([last, first])