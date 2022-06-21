from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('Suas opções:\n[ 0 ] Pedra \n[ 1 ] Papel \n[ 2 ] Tesoura')

jogador = int(input('Qual é a sua jogada? '))
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po!!!')
print('-=' * 12)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-=' * 12)

if computador == 0: #Pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('O jogador venceu!')
    elif jogador == 2:
        print('O computador venceu!')
    else:
        print('Jogada Inválida!')
if computador == 1: #Papel
    if jogador == 0:
        print('O computador venceu!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('O jogador venceu!')
    else:
        print('Jogada Inválida!')
if computador == 2: #Tesoura
    if jogador == 0:
        print('O jogador venceu!')
    elif jogador == 1:
        print('O computador venceu!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada Inválida!')