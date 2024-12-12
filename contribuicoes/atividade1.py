nome = input("Informe seu nome: ")
altura = float(input("Informe sua altura: "))
idade = int(input("Informe sua idade: "))

eh_maior_de_idade = idade >= 18

print("\n*** Detalhes da Pessoa ***")
print(f"Nome: {nome}")
print(f"Altura: {altura:.2f} metros")
print(f"Idade: {idade} anos")

if eh_maior_de_idade:
    print("A pessoa é maior de idade.")
else:
    print("A pessoa é menor de idade.")
