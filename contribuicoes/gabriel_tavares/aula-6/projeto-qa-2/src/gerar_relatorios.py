import pandas as pd
import requests

resposta = requests.get("http://127.0.0.1:5000/usuarios")
users = resposta.json()

df = pd.DataFrame(users)

print(df)

df.to_csv("data/usuarios.csv", index=False)
print("Relatório de usuários gerados com sucesso!")