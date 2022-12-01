p = input('Palavra: ')
k = 0
t = ' '
while k < len(p):
    if p [k] in 'aeiou':
        t = t + '*'
    else:
        t = t + p [k]
    k = k +1
print(t)
