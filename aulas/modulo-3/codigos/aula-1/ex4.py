usuario_bd = "marcosfilho"
senha_mestre  = '123456'
acesso_concedido = False

def validar_login(usuario, senha):
    
    if usuario_bd == usuario and senha == senha_mestre:
        print(f'Olá {usuario}, acesso permitido!')
        acesso_concedido = True
    else:
        print(f'Olá {usuario}, acesso negado!')
        acesso_concedido = False


validar_login("admin", "12345")
validar_login("apsferreira", "123456")

    