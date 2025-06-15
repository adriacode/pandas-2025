# %%
import pandas as pd
import sqlalchemy
from sklearn import cluster

# %%
with open("etl.sql") as open_file:
    query = open_file.read()

print(query)

# %%

engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")

df = pd.read_sql_query(query, con=engine)

kmean = cluster.KMeans(n_clusters=4)
kmean.fit(df[['totalRevenue', 'qtSalles']])

df["cluster"] = kmean.labels_
df