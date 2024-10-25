#sistema de login

usuario = "cr7dograu123"
senha = "neymar10"
tentativas = 3

for i in range(tentativas):
    usuario_input = input('Usuário: ')
    senha_input = input('Senha: ')

    
    if usuario_input == usuario and senha_input == senha:
        print(f'Seja bem vindo {usuario}!')
        
        break
    else:
        tentativas_restantes = tentativas - (i + 1)
        if tentativas_restantes > 0:
            print(f'Usuário ou senha inválida! Você tem apenas {tentativas_restantes} tentativas')
        else:
            print("Acesso Bloqueado")

            for i in range(3):
                print("Acesso Negado!")