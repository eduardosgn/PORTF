#tabuada exercicios de repetição
# while repetidor
# repétir a tabuada até 10
t = 1
#repetir tabuadas do 1 ao 10
while t <=10:
    print (f'Tabuada do {t}')
    n = 1
    #repetidor dentro do repetidor
    #repetir numeros de cada tabuada
    while n <=15:
        print (f'{t} x {n} = {t*n}')
        n = n +1
    t = t + 1
    print ()
