from random import randrange

numero_aleatorio = randrange(9)

numero_usuario = int(input('Chute um número entre (0 e 9): '))

if numero_usuario == numero_aleatorio:
    print(f'Você acertou o numero: {numero_aleatorio}')
else:
    while numero_aleatorio != numero_usuario:
        numero_usuario = int(input('Você errou, tente novamente: '))
    print(f'Até que fim você acertou! {numero_usuario}')
