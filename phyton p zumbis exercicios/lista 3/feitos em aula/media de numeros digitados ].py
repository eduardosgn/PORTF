n=1
soma=0
# o Zero é elemento neutro da soma
# calcule a média dos números 
while n<=10:
    x=int(input(f' Número {n}:'))
    soma = soma+x
    n=n+1
    print(f'Média:{soma/10:.1f}')
    
