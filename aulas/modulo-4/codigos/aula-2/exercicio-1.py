import pandas as pd

# df = pd.read_json("dados.json")
df = pd.read_csv("dados_convertidos.csv")

df["nascimento_convertido_str_data"] = pd.to_datetime(df["nascimento"])
df["ano"] = pd.DatetimeIndex(df["nascimento"]).year

# print(df)