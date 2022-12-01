#rolo de arame de 21mt e outro de 15mt o maior pedaço comum aos dois é de:?

a = int(input('Valor de a:'))
b = int(input('Valor de b:'))
while a % b != 0:
    a , b = b, a%b
print (f' mds = {b}')
