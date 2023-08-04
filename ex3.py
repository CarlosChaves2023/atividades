soma = 0
media = 0
for c in range(1, 6):
    n = float(input(f'Digite a {c}ª nota: '))
    soma += n
    media = soma/5
print(f'A soma vale {soma}')
print(f'A média vale {media}')
