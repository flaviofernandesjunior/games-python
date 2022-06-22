from random import randint
computador = randint(0,10)
print('Sou seu computador e acabei de pensar em um número de 0 a 10...')
print('Tente adivinhar!!')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente')
        elif jogador > computador:
            print('Menos... Tente novamente')
print('Você acertou com {} palpites.. Parabéns'.format(palpites))

