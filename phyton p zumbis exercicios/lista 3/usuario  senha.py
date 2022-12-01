#crie um login
#que avise que a senha nao pode ser o mesmo que usuario

usuário = input('usuário:')
senha = input('senha:')
while usuário == senha:
    print('senha deve ser diferente do Usuário')
    usuário = input('usuário:')
    senha = input('senha:')
    
