#Calcule a média de notas digitadas 
nota = [ ]
k = 0
soma = 0
while k <= 3:
    nota .append( float( input( 'Nota: ')))
    soma = soma + nota [k]
    k = k+1
print (f'Média {nota} é {soma/4: .1f}')


