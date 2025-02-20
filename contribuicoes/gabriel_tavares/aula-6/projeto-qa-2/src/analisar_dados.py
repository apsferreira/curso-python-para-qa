import pandas as pd
import numpy as np


df = pd.read_csv("data/usuarios.csv")
total_users = len(df)

ids_users = np.array(df["id"])

print(f"O total de usuarios é {total_users}")
print(f"Os ids dos usuarios são: {total_users}")