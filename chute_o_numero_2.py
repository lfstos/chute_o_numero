from random import randint

total_tentativas = 3
numero_secreto = randint(0, 9)

for rodade in range(1, total_tentativas):
    print(f'Tentativa {rodade} de {total_tentativas}')

    chute = int(input('Digite o número: '))
    print('Você digitou ', chute)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print('Você acertou!')
        break
    elif (maior):
        print('Você errou! O seu chute foi maior que o número secreto')
    elif (menor):
        print('Você errou! O seu chute foi menor que o número secreto')

print('Fim do jogo')