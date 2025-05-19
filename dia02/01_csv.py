# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df

# %%

df.to_csv("clientes.csv", index=False)

# %%

df.to_parquet("clientes.parquet", index=False)
# %%

