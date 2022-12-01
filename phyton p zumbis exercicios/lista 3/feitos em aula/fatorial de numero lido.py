#fatorial
#elemento neutro da multiplicação é UM
#alterem esse cód, para ler o fat de um número lido
k = 1
fat = 1
n = int(input('Digite um Número: '))
while k <= n:
    fat = fat * k
    k = k + 1
print(F'fatorial de {n} = {fat}')
