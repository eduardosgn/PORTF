#programa de digitação de notas
#cód feito para notas de 0 a 10
#aviso caso a nota esteja fora das aceitas
nota = float(input('Digite uma nota:'))
while nota<=0 or nota >= 10:
    print('Notas entre 0 e 10:')
    nota = float(input('Digite uma nota:'))
