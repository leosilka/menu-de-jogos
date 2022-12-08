import random
from time import sleep
print('\033[1;32m===============================\033[m')
print('\033[1;35m PROJETO - MENU DE ESCOLHAS\033[m')
print('\033[1;32m===============================\033[m')
print('')
escolha = 0
while escolha != 5:
    r = 'S'
    print('''    [ 1 ] - Jogo de Adivinhação
    [ 2 ] - Jogo de Jokenpô
    [ 5 ] - Encerrar Menu''')
    escolha = int(input('Digite a sua escolha: '))
    if escolha == 1:  # Aqui está o programa de Adivinhação
        cont = 0
        erros = 0
        acertos = 0
        while r == 'S':
            cont += 1
            nsorteado = random.randint(1, 10)
            nescolhido = int(
                input('Tente adivinhar o número que estou pensando entre 0 e 10: '))
            if nescolhido == nsorteado:
                print('Parabéns, você acertou o número que estava pensando.')
                acertos += 1
                r = str(
                    input('Deseja continuar jogando? [S/N]')).strip().upper()
            elif nescolhido != nsorteado:
                print('Infelizmente você errou o número qeu estava pensando. O número que pensei foi {}.' .format(
                    nsorteado))
                erros += 1
                r = str(
                    input('Deseja continuar jogando? [S/N]')).strip().upper()
        print('Você jogou {} vezes, teve {} acertos e {} erros.' .format(
            cont, acertos, erros))
        print('Retornando ao menu...')
    elif escolha == 2:  # Aqui está o programa de Jokenpô
        cont = 0
        erros = 0
        acertos = 0
        empates = 0
        while r == 'S':
            cont += 1
            jokenpo = ('Pedra', 'Papel', 'Tesoura')
            ia = random.randint(0, 2)
            print('''Escolha sua opção:
                    [ 0 ] - PEDRA
                    [ 1 ] - PAPEL
                    [ 2 ] - TESOURA''')
            player = int(input('O que deseja jogar? '))
            print('-'*20)
            print('Computador jogou {}' .format(jokenpo[ia]))
            print('Jogador jogou {}' .format(jokenpo[player]))
            print('-'*20)
            if ia == 0:  # IA jogou Pedra
                if player == 0:
                    print('Empatamos!')
                    empates += 1
                elif player == 1:
                    print('Você Ganhou!')
                    acertos += 1
                elif player == 2:
                    print('Você Perdeu!')
                    erros += 1
                else:
                    print('Jogada Inválida!')
                r = str(
                    input('Deseja continuar jogando? [S/N]')).strip().upper()
            elif ia == 1:  # IA jogou Papel
                if player == 0:
                    print('Você Perdeu!')
                    erros += 1
                elif player == 1:
                    print('Empatamos')
                    empates += 1
                elif player == 2:
                    print('Você Ganhou!')
                    acertos += 1
                else:
                    print('Jogada Inválida!')
                r = str(
                    input('Deseja continuar jogando? [S/N]')).strip().upper()
            elif ia == 2:  # IA jogou Tesoura
                if player == 0:
                    print('Você Ganhou!')
                    acertos += 1
                elif player == 1:
                    print('Você Perde!')
                    erros += 1
                elif player == 2:
                    print('Empatamos!')
                    empates += 1
                else:
                    print('Jogada Inválida!')
                r = str(
                    input('Deseja continuar jogando? [S/N]')).strip().upper()
        print('Você teve {} acertos, {} empates e {} derrotas.' .format(
            acertos, empates, erros))
        print('Retornando ao menu...')
        sleep(3)
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Comando Inválido. Tente Novamente.')
    print('-'*15)
    sleep(3)
print('Fim do Programa. Volte Sempre!')
