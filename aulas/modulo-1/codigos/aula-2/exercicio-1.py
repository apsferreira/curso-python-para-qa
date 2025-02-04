Idade = int(input("Digite a sua idade: "))  
Nome = input("Digite o seu nome: ")
Altura = float(input("Digite a sua altura: "))
pessoa_habilitada_insano = False
pessoa_habilitada_capsula = False
pessoa_habilitada_prainha = False

# Validação da Idade
"""
Este é um comentario
com mais de uma linha
"""
if Idade > 18:
    maior_idade = True
else:
    maior_idade = False

if maior_idade and Altura > 1.50:
    pessoa_habilitada_insano = True

if maior_idade or Altura > 1.50:
    pessoa_habilitada_capsula = True

if not maior_idade: 
    pessoa_habilitada_prainha = True

novo_nome = Nome.replace("Antonio", "Ferreira").lower() 

print(f"As informaçoes do meu usuario sao: Nome: {novo_nome}, Idade: {Idade}, Altura: {Altura} \n {maior_idade} \n Habilitada a descer o toboga: {pessoa_habilitada_insano}")