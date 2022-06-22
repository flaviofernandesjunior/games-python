from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[ 0 ] Pedra
[ 1 ] Papel 
[ 2 ] Tesoura''')
jogador = int(input('Qual é sua jogada? '))
print('-=' * 11)
print('PEEDRA')
sleep(1)
print('PAPEEEL')
sleep(1)
print('TESOURA???')
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #Computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VITÓRIA')
    elif jogador == 2:
        print('DERROTA')
elif computador == 1: #Computador jogou papel
    if jogador == 0:
        print('DERROTA')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VITÓRIA')
elif computador == 2: #Computador jogou tesoura
    if jogador == 0:
        print('DERROTA')
    elif jogador == 1:
        print('VITÓRIA')
    elif jogador == 2:
        print('EMPATE')
