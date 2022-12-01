#fatorial
#elemento neutro da multiplicação é UM
#alterem esse cód, para ler o fat de um número lido
# soma quantos numeros quiser até  digitar zero
#zero usado por ser o neutro da soma
soma = 0
while True :
    x = int(input('digite um numero (zero para sair):'))
    if x == 0:
        break
    soma = soma +  x
print (f'Soma: {soma}')
