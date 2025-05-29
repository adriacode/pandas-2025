# %%
import pandas as pd

clientes = pd.read_csv("../../data/clientes.csv")
transacoes = pd.read_csv("../../data/transacoes.csv")

# %%
# 04.01 - Quantos clientes tem vínculo com a Twitch?
filtro = clientes["flTwitch"] == 1
clientes[filtro].shape[0]
# %%
# 04.02 - Quantos clientes tem um saldo de pontos maior que 1000?
filtro = clientes["qtdePontos"] >= 1000
clientes[filtro].shape[0]
# %%
# 04.03 - Quantas transações ocorreram no dia 2025-02-01?
filtro = transacoes["dtCriacao"] == "2025-02-01"
transacoes[filtro].shape[0]
