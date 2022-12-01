#sequencia de fibonaci
print(' Qual a sequencia de fibonaci do valor digitado abaixo:')
n = int(input('Digite o valor: '))
a, b = 1, 1
k = 1
while k <= n-2:
     a, b = b, a +b
     k = k +1
print()
print (f'A Sequencia de fibonaci do valor {n} é de {b}')
