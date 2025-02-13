notas = [8, 7, 9, 6] 

notas_aprovadas = list(filter(lambda nota: nota >= 8, notas))

print(notas_aprovadas)