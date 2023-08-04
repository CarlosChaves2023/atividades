while True:
    n = int(input('Digite o nùmero qde 1 a 10 para saber a taboada: '))
    if n < 1 or n > 10:
        print('Número inválido')
    else:
        for c in range(1, 11):
            print(f'{n} + {c} = {n + c}')
        break