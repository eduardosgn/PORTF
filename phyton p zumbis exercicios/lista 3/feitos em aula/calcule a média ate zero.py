#some a media de numeros lidos
# soma quantos numeros quiser até  digitar zero
#zero usado por ser o neutro da soma
n = 0
soma = 0
while True :
    x = int(input('digite um numero (zero para sair):'))
    if x == 0:
        break
    else:
        n = n+1
    soma = soma +  x
print (f'Média: {soma/n:.1f}')
