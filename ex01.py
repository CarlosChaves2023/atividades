cont = 0
maior = 0
while cont < 3:
    n = int(input(f'digite o {cont +1}º número: '))
    cont += 1
    if n > maior:
        maior = n
print(f'O maior número é {maior}')
