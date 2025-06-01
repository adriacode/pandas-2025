# %%
import pandas as pd

clientes = pd.read_csv("../../data/clientes.csv")
transacoes = pd.read_csv("../../data/transacoes.csv")
transacao_produto = pd.read_csv("../../data/transacao_produto.csv")
produtos = pd.read_csv("../../data/produtos.csv")

clientes
# %%
# 06.01 - Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?
clientes["totalRedes"] = (clientes['flEmail'] + 
                          clientes['flTwitch'] + 
                          clientes['flYouTube'] + 
                          clientes['flBlueSky'] +
                          clientes['flInstagram'])

media = clientes["totalRedes"].mean()
variancia = clientes["totalRedes"].var()
maximo = clientes["totalRedes"].max()


print("media:",media)
print("variancia:",variancia)
print("maximo:",maximo)


# %%
# 06.02 - Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.
cliente_num_transacoes = transacoes.groupby(["idCliente"], as_index=False)["idTransacao"].count()
cliente_num_transacoes.columns = ("idCliente", "qtdeTransacao")
dez_primeiros = cliente_num_transacoes.sort_values(by="qtdeTransacao", ascending=False)
dez_primeiros.head(10)

# %%
# 06.03 - Qual usuário teve maior quantidade de pontos debitados?

filtro = transacoes['qtdePontos'] < 0

(transacoes[filtro].groupby(by='idCliente')['qtdePontos']
                   .sum()
                   .sort_values(ascending=True)
                   .head(1))

# %%
# 06.04 - Quem teve mais transações de Streak?

cliente_transacao_produto = transacoes.merge(
    transacao_produto, 
    on="idTransacao",
    how="left",
)[["idTransacao", "idCliente", "idProduto"]]

df_full = cliente_transacao_produto.merge(
    produtos,
    on=["idProduto"],
    how="left",

)

df_full = df_full[df_full["descProduto"]=="Presença Streak"]

(df_full.groupby(by=["idCliente"])["idTransacao"]
    .count()
    .sort_values(ascending=False)
    .head(1)
)
# %%
# 06.05 - Qual a média de transações / dia?
transacoes["data"] = pd.to_datetime(transacoes["dtCriacao"]).dt.date
media_por_dia = transacoes.groupby(["data"])[["idTransacao"]].count().mean()
media_por_dia

# %%
# 06.06 - Como podemos calcular as estatísticas descritivas dos pontos das transações de cada usuário?
transacoes.groupby(by=["idCliente"], as_index=False)["qtdePontos"].describe()
                       