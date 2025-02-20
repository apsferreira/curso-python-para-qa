import pandas as pd
import requests

resposta = requests.get("http://127.0.0.1:5000/usuarios")
usuarios = resposta.json()

df = pd.DataFrame(usuarios)

# print(df)

df.to_csv("data/usuarios.csv", index=False)
print("Relatorio de usuarios gerado com sucesso")