#calcular enquanto tempo uma papolação passa a outra
#com taxa de acrescimo, como jusros composto

a = 80000
b = 200000
anos = 0
print(f'a cidade A tendo {a} habitantes e a cidade B com {b}, a diferença de anos entre a população é de:')
while a <= b:
    a = a + a * 0.03
    b = b + b * 0.015
    anos = anos + 1
print(f'{anos}anos')
