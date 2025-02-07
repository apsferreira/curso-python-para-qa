import pandas as pd
import numpy as np

df = pd.read_csv("data/usuarios.csv")

total_usuarios = len(df)

ids_usuarios = np.array(df["id"])

print(f"O total de usuarios é: {total_usuarios}")
print(f"Os ids dos usuarios sao: {ids_usuarios}")
print(f"O maior Id é : {np.max(ids_usuarios)}")
print(f"O maior Id é : {np.mean(ids_usuarios)}")