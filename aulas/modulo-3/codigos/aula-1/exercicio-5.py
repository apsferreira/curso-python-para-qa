def gerar_relatorio(nome_teste="teste", resultado="Em execuçao"):
    return f"Caso de Teste:  {nome_teste} - Status: {resultado}"


print(gerar_relatorio("Login"))
print(gerar_relatorio(resultado="Pass"))