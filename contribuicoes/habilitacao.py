nome = input("Informe seu nome: ")
altura = float(input("Informe sua altura: "))
idade = int(input("Informe sua idade: "))

maior_de_idade = idade >= 18

print(f"Nome: {nome}")
print(f"Altura: {altura:.2f} metros")
print(f"Idade: {idade} anos")

if maior_de_idade:
    print("A pessoa é maior de idade e pode ser habilitada para dirigir.")
else:
    print("A pessoa é menor de idade e não pode ser habilitada para dirigir.")