def validar_teste(resultado):
    def mensagem(status):
        return f"O teste foi {status}"

    if resultado == "Pass":
        return mensagem("Bem sucedido")
    else: 
        return mensagem("Falhou")
    

print(validar_teste("Pass"))
print(validar_teste("Fail"))