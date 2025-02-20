usuario_bd = "gtav"
senha_mestre  = '123123'
acesso_concedido = False

while not acesso_concedido:    
    usuario = input('Digite o nome do usuário: ')
    senha = input('Digite a senha: ')

    if usuario_bd == usuario and senha == senha_mestre:
        print(f'Olá {usuario}, acesso permitido!')
        acesso_concedido = True
    else:
        print(f'Olá {usuario}, acesso negado!')
        acesso_concedido = False
