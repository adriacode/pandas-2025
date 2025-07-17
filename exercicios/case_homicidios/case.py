# %%

import pandas as pd
import os

def read_file(file_name:str):
    df = (pd.read_csv(f"../../data/ipea/{file_name}.csv", sep=";")
            .rename(columns={"valor":file_name})
            .set_index(["nome", "período"])
            .drop(["cod"], axis=1))
    return df

# %%
file_names = os.listdir("../../data/ipea/")

dfs = []
for i in file_names:
    file_name = i.split(".")[0]
    dfs.append(read_file(file_name))

# %%

df_full = pd.concat(dfs, axis=1).reset_index().sort_values(["período", "nome"])

df_full.to_csv("homicidios-consolidado.csv", index=False, sep=";")

