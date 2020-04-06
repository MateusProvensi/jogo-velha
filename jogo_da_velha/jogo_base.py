from os import system  # É importado da biblioteca os a função system que será usado para limpara a tela
from time import sleep  # É importado da biblioteca time a função sleep, que serve para p pc "dormir"
from random import randint, choice  # É importado da biblioteca random a função randint, que serve para a jogada do pc
#  A função choice serve para escolher dentre algo

'''
Desenvolvido por: Mateus Provensi
Ultima atualização: 25/03/2020
A função limpa_tela não tenho certeza se funcionará no terminal de uma máquina linux ou IOS
'''

pontos_jogador1 = pontos_jogador2 = empates = pontos_jogador_contra_pc = pontos_pc = 0
numero_do_jogo = 1
escolha = ''
continuar = ''
jogou = None  # Foi utilizado essa variável para não deixar o PC jogar 2 vezes
vitoria = None  # Essa variavel teve de ser criado para evitar um bud de o usuário ganhar na ultima rodada
combinacao_vitoria = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])
# É registrado todas as formas de ser ganhar no jogo da velha, lembrando que o indice começa em 0


def limpa_tela():
    system('cls')  # Função que limpar a tela do prompt do WINDOWS, não foi testado em máquina Linux e IOS


def menu():
    global escolha
    while True:
        print('=' * 25)
        print(
            '1 - Como jogar\n'
            '2 - Iniciar o jogo'
        )
        print('=' * 25)
        escolha = input('Digite a sua escolha: ')
        if escolha == '1':
            print(
                '''
                                            --- COMO JOGAR ---
                Digite o número correspondente à posição no tabuleiro para fazer sua jogada nela.
                Por exemplo, caso sua opção seja o canto superior direito, seria digitado o valor 3.
                                                 |     |     
                                              1  |  2  |  3  
                                            _____|_____|_____
                                                 |     |     
                                              4  |  5  |  6  
                                            _____|_____|_____
                                                 |     |     
                                              7  |  8  |  9  
                                                 |     |     
                '''
            )
        elif escolha == '2':
            break
        else:
            print(
                '\nA escolha deve ser válida.\n'
            )


def redefinindo_tabuleiro():
    print(f'''
O PLACAR SÓ É ATUALIZADO NO JOGO SEGUINTE
Partida: {numero_do_jogo}  
Vitórias {nome_jogador1}({tipo_jogador1}): {pontos_jogador1}
Vitórias {nome_jogador2}({tipo_jogador2}): {pontos_jogador2}
Empates(velha): {empates}

                                                         |     |
                                                      {tabuleiro_mostrado_usuario[0]}  |  {tabuleiro_mostrado_usuario[1]}  |  {tabuleiro_mostrado_usuario[2]}
                                                    _____|_____|_____
                                                         |     |
                                                      {tabuleiro_mostrado_usuario[3]}  |  {tabuleiro_mostrado_usuario[4]}  |  {tabuleiro_mostrado_usuario[5]}
                                                    _____|_____|_____
                                                         |     |
                                                      {tabuleiro_mostrado_usuario[6]}  |  {tabuleiro_mostrado_usuario[7]}  |  {tabuleiro_mostrado_usuario[8]}
                                                         |     |
        '''
          )


def jogada_multiplayer():
    while True:
        jogada = input(f'''
                                            Vez de {nome_jogador1 if cont % 2 != 0 else nome_jogador2}({tipo_jogador1 if cont % 2 != 0 else tipo_jogador2}), digite a jogada: '''
                       )
        # Se o estiver na joga impar, o jogador 1 joga, se for par o jogador 2 joga
        if jogada in tabuleiro and jogada not in ('X', 'O'):  # Verifica se a jogada do jogador está na variavel
            # tabuleiro, no caso do 1 ao 9 e também verifica se a jogada não foi um X ou O
            tabuleiro[int(jogada) - 1] = tipo_jogador1 if cont % 2 != 0 else tipo_jogador2  # Diminui a jogada do
            # jogador já que o indice da lista começa em 0 e acrescenta o X ou O onde ele escolheu
            tabuleiro_mostrado_usuario[int(jogada) - 1] = tipo_jogador1 if cont % 2 != 0 else tipo_jogador2
            break  # Quebra o laço infinito
        else:
            print(f'''
                                        Poxa {nome_jogador1 if cont % 2 != 0 else nome_jogador2} por favor, uma jogada válida, vai'''
                  )


def placar():
    print(
        f'\nO placar ficou da seguinte forma:\n'
        f'{nome_jogador1}({tipo_jogador1}) está com {pontos_jogador1} ponto em {numero_do_jogo} partidas\n'
        f'{nome_jogador2}({tipo_jogador2}) está com {pontos_jogador2} ponto em {numero_do_jogo} partidas\n'
        f'Empates(Velha): {empates}'
    )


def checar_se_ha_vitoria():
    global pontos_jogador1, pontos_jogador2
    for combinacao in combinacao_vitoria:  # Um for para percorrer toda a lista das combinações de vitória
        if (tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]]) and \
                (tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]]):  # Verifica se dentro da lista tabuleiro existe
            # alguma combinação de vitória
            if tabuleiro[combinacao[1]] == tipo_jogador1:
                pontos_jogador1 += 1
                print(
                    f'O jogador(a) {nome_jogador1} ganhou, mais um ponto para ele(a). :-)'
                )
                sleep(2)  # Dois segundos para melhorar leitura
                placar()
                return True
            elif tabuleiro[combinacao[1]] == tipo_jogador2:
                pontos_jogador2 += 1
                print(
                    f'O jogador(a) {nome_jogador2} ganhou, mais um ponto para ele(a). :-)'
                )
                sleep(2)  # Dois segundos para melhorar leitura
                placar()
                return True
    return False  # Foi utilizado os valores booleanos pois facilita na verificação com um IF


def jogada_jogador_contra_pc():
    while True:
        jogada = input(f'''
                                            Vez de {nome_jogador_contra_pc}({tipo_jogador}), digite a jogada: '''
                       )
        if jogada in tabuleiro and jogada not in ('X', 'O'):  # Verifica se a jogada está no tabuleiro e se ela não é
            # X ou O
            tabuleiro[int(jogada) - 1] = tipo_jogador  # O tabuleiro na posição escolhida (menos 1 pois começa em 0 o
            # indice) recebe o tipo do jogador
            tabuleiro_mostrado_usuario[int(jogada) - 1] = tipo_jogador
            break
        else:
            print(f'''
                                        Poxa {nome_jogador_contra_pc} por favor, uma jogada válida, vai'''
                  )


def jogada_padrao_pc():
    while True:
        jogada = randint(1, 9)  # Pensa em um número aleatório de 1 a 9 (posições do tabuleiro)
        jogada = str(jogada)  # Transforma a jogada em string pois na lista tabuleiro todas são strings
        if jogada in tabuleiro:
            tabuleiro[int(jogada) - 1] = tipo_pc  # O tabuleiro na posição randomizado (menos 1 pois começa em 0 o
            # indice) recebe o tipo do jogador
            tabuleiro_mostrado_usuario[int(jogada) - 1] = tipo_pc
            break
        else:
            continue


def jogada_pc_facil():
    print('''
                                                     Estou pensando...
    '''
          )
    sleep(2)  # sleep para fazer uma forma de o pc "pensar"
    jogada_padrao_pc()


def jogada_dificil_extremo():
    global jogou
    for combinacao in combinacao_vitoria:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]]:  # Verifica o indice 0 da combinação, que está sendo
            # percorrida nas combinacao_vitoria, na lista tabuleiro, é igual a o indice 1
            if tabuleiro[combinacao[1]] == tipo_pc:  # Verifica se é do pc mesmo a sequencia
                if tabuleiro[combinacao[2]] != tipo_jogador:  # Verifica se o jogador já não jogou naquela posição
                    tabuleiro[combinacao[2]] = tipo_pc  # Recebe  a jogada do PC no lugar onde ele ganha a partida
                    tabuleiro_mostrado_usuario[combinacao[2]] = tipo_pc  # Recebe  a jogada do PC no lugar onde ele
                    # ganha a partida
                    jogou = True
                    break  # Quebra o For
            if tabuleiro[combinacao[1]] == tipo_jogador:  # Verifica se é do jogador mesmo a sequencia
                if tabuleiro_mostrado_usuario[combinacao[2]] != tipo_pc:  # Verifica se pc já não jogou naquela posição
                    tabuleiro[combinacao[2]] = tipo_pc  # Recebe  a jogada do PC no lugar onde invalida a chance do
                    # jogador ganhar
                    tabuleiro_mostrado_usuario[combinacao[2]] = tipo_pc
                    jogou = True
                    break  # Quebra o For
        elif tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]]:  # Verifica o indice 1 da combinação, que está sendo
            # percorrida nas combinacao_vitoria, na lista tabuleiro, é igual a o indice 2
            if tabuleiro[combinacao[1]] == tipo_pc:  # Verifica se é do pc mesmo a sequencia
                if tabuleiro[combinacao[0]] != tipo_jogador:  # Verifica se o jogador já não jogou naquela posição
                    tabuleiro[combinacao[0]] = tipo_pc  # Recebe  a jogada do PC no lugar onde ele ganha a partida
                    tabuleiro_mostrado_usuario[combinacao[0]] = tipo_pc  # Recebe  a jogada do PC no lugar onde ele
                    # ganha a partida
                    jogou = True
                    break  # Quebra o For
            if tabuleiro[combinacao[1]] == tipo_jogador:  # Verifica se é do jogador mesmo a sequencia
                if tabuleiro[combinacao[0]] != tipo_pc:  # Verifica se pc já não jogou naquela posição
                    tabuleiro[combinacao[0]] = tipo_pc  # Recebe  a jogada do PC no lugar onde invalida a chance do
                    # jogador ganhar
                    tabuleiro_mostrado_usuario[combinacao[0]] = tipo_pc
                    jogou = True
                    break  # Quebra o For
        elif tabuleiro[combinacao[0]] == tabuleiro[combinacao[2]]:  # Verifica o indice 0 da combinação, que está sendo
            # percorrida nas combinacao_vitoria, na lista tabuleiro, é igual a o indice 2
            if tabuleiro[combinacao[2]] == tipo_pc:  # Verifica se é do pc mesmo a sequencia
                if tabuleiro[combinacao[1]] != tipo_jogador:  # Verifica se o jogador já não jogou naquela posição
                    tabuleiro[combinacao[1]] = tipo_pc  # Recebe  a jogada do PC no lugar onde ele ganha a partida
                    tabuleiro_mostrado_usuario[combinacao[1]] = tipo_pc  # Recebe  a jogada do PC no lugar onde ele
                    # ganha a partida
                    jogou = True
                    break  # Quebra o For
            if tabuleiro[combinacao[2]] == tipo_jogador:  # Verifica se é do jogador mesmo a sequencia
                if tabuleiro[combinacao[1]] != tipo_pc:  # Verifica se pc já não jogou naquela posição
                    tabuleiro[combinacao[1]] = tipo_pc  # Recebe  a jogada do PC no lugar onde invalida a chance do
                    # jogador ganhar
                    tabuleiro_mostrado_usuario[combinacao[1]] = tipo_pc
                    jogou = True
                    break  # Quebra o For


def jogada_pc_dificil():
    global jogou
    print('''
                                                    Estou pensando...
       '''
          )
    sleep(2)  # sleep para fazer uma forma de o pc "pensar"
    jogou = False  # Foi utilizado essa variável para não deixar o PC jogar 2 vezes
    jogada_dificil_extremo()
    if not jogou:  # Verifica se o jogou continuou false, ou seja, nada foi validado
        jogada_padrao_pc()  # Chama a função jogada_padrao (fácil e randomica)


def jogada_pc_extremo():
    global cont, jogou
    print('''
                                                    Estou pensando...
       '''
          )
    sleep(2)  # sleep para fazer uma forma de o pc "pensar"
    jogou = False  # Foi utilizado essa variável para não deixar o PC jogar 2 vezes
    if cont == 2:  # Verifica se está na primeira jogada do PC
        while True:
            jogada_um_pc_extremo = choice([0, 2, 6, 8])  # O computador escolhe entre os cantos para jogar
            if tabuleiro[jogada_um_pc_extremo] != tipo_jogador:  # Verifica se o usuário já não jogou neste canto
                break
            else:
                continue
        if tabuleiro[4] != tipo_jogador:  # Verifica se o usuário não jogou no meio no inicio da partida
            tabuleiro[4] = tipo_pc  # Coloca a jogada do PC no meio
            tabuleiro_mostrado_usuario[4] = tipo_pc
            jogou = True
        elif tabuleiro[jogada_um_pc_extremo] != tipo_jogador:
            tabuleiro[jogada_um_pc_extremo] = tipo_pc  # O local que o choice escolheu recebe a jogada do PC
            tabuleiro_mostrado_usuario[jogada_um_pc_extremo] = tipo_pc
            jogou = True
    if not jogou:  # Verifica se o PC já jogou
        jogada_dificil_extremo()
    if not jogou:  # Verifica se o jogou continuou false, ou seja, nada foi validado
        jogada_padrao_pc()  # Chama a função jogada_padrao (fácil e randomica)


def redefinindo_tabuleiro_contra_pc():
    print(f'''
O PLACAR SÓ É ATUALIZADO NO JOGO SEGUINTE
Partida: {numero_do_jogo}
Vitórias {nome_jogador_contra_pc}({tipo_jogador}): {pontos_jogador_contra_pc}
Vitórias PC({tipo_pc}): {pontos_pc}
Empates(velha): {empates}

                                                         |     |
                                                      {tabuleiro_mostrado_usuario[0]}  |  {tabuleiro_mostrado_usuario[1]}  |  {tabuleiro_mostrado_usuario[2]}
                                                    _____|_____|_____
                                                         |     |
                                                      {tabuleiro_mostrado_usuario[3]}  |  {tabuleiro_mostrado_usuario[4]}  |  {tabuleiro_mostrado_usuario[5]}
                                                    _____|_____|_____
                                                         |     |
                                                      {tabuleiro_mostrado_usuario[6]}  |  {tabuleiro_mostrado_usuario[7]}  |  {tabuleiro_mostrado_usuario[8]}
                                                         |     |
        '''
          )


def checar_se_ha_vitoria_contra_pc():
    global pontos_jogador_contra_pc, pontos_pc
    for combinacao in combinacao_vitoria:  # Um for para percorrer toda a lista das combinações de vitória
        if (tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]]) and \
                (tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]]):  # Verifica se dentro da lista tabuleiro, no
            # indice da lista combinação e no indice 0, 1, 2 são iguais
            if tabuleiro[combinacao[1]] == tipo_jogador:  # Verifica se é igual ao tipo do jogador (X ou O)
                pontos_jogador_contra_pc += 1
                print(
                    f'Você, {nome_jogador_contra_pc}, ganhou, mais um ponto para ti. :-)'
                )
                sleep(2)  # sleep para facilitar a leitura
                placar_contra_pc()
                return True
            elif tabuleiro[combinacao[1]] == tipo_pc:  # Verifica se é igual ao tipo do PC (X ou O)
                pontos_pc += 1
                print(
                    f'O PC ganhou, mais um ponto para ele. :-)'
                )
                sleep(2)  # sleep para facilitar a leitura
                placar_contra_pc()
                return True
    return False  # Foi utilizado os valores booleanos pois facilita na verificação com um IF


def placar_contra_pc():
    print(
        f'\nO placar ficou da seguinte forma:\n'
        f'{nome_jogador_contra_pc}({tipo_jogador}) está com {pontos_jogador_contra_pc} ponto em {numero_do_jogo}'
        f' partidas\n'
        f'PC({tipo_pc}) está com {pontos_pc} ponto em {numero_do_jogo} partidas\n'
        f'Empates(Velha): {empates}'
    )


def continuar_a_jogar():
    global continuar
    while True:
        continuar = input(
            '\nDeseja continuar [S/N]? '
        ).upper()
        if continuar == 'S':
            return True
        elif continuar == 'N':
            return False
        else:
            print(
                'Digite um S para sim ou N para não.'
            )


while True:
    print('=' * 35)
    print(
        '1 - Contra o PC(Singleplayer)\n'
        '2 - Contra algum amigo(Multiplayer)'
    )
    print('=' * 35)
    opcao = input(
        'Digite sua opção: '
    )
    if opcao not in ('1', '2'):  # Verifica se a escolha é diferente de 1 ou 2
        print('Escolha uma opção válida, por favor.\n')
        continue
    else:
        break
limpa_tela()
if opcao == '1':
    print('=' * 35)
    print(
        f'1 - Fácil\n'
        f'2 - Dificil\n'
        f'3 - Extremo'
    )
    print('=' * 35)
    while True:
        dificuldade = input(
            'Digite a dificuldade: '
        )
        if dificuldade not in ('1', '2', '3'):  # Verifica se a escolha é diferente de 1, 2 ou 3
            print(
                'Escolha uma opção válida, por favor.\n'
            )
            continue
        else:
            break
    while True:
        nome_jogador_contra_pc = input(
            '\nDigite seu nome: '
        ).strip()
        if nome_jogador_contra_pc == '':
            print(
                'Seu nome não pode ser em branco.'
            )
        else:
            break
    while True:
        tipo_jogador = input(
            f'\n{nome_jogador_contra_pc}, você será o X ou o O: '
        ).upper().strip()
        if tipo_jogador == '':
            print('Por favor, X ou O.')
            continue
        if tipo_jogador not in ('X', 'O'):  # Verifica se não esta em X ou O
            print(
                'É necessários que seja X ou O.'
            )
        else:
            break
    if tipo_jogador == 'X':
        tipo_pc = 'O'
    else:
        tipo_pc = 'X'
    limpa_tela()
    print(
        f'{nome_jogador_contra_pc} será {tipo_jogador}\n'
        f'O PC será {tipo_pc}'
    )
    print(
        '\nPressione enter para continuar...'
    )
    input()
    while True:
        limpa_tela()
        menu()
        limpa_tela()
        tabuleiro = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # Cria a lista tabuleiro que é usada para verificar
        # vitórias.
        tabuleiro_mostrado_usuario = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # Cria outra lista tabuleiro, mas
        # essa é a mostrada para o usuário
        redefinindo_tabuleiro_contra_pc()
        cont = 0
        while True:  # Cria um laço infinito para as jogadas dos jogadores
            cont += 1
            jogada_jogador_contra_pc()
            limpa_tela()
            redefinindo_tabuleiro_contra_pc()
            if checar_se_ha_vitoria_contra_pc():  # Verifica se o checar vitória contra o PC retorna True (verdadeiro)
                numero_do_jogo += 1
                vitoria = True
                break
            if cont == 9:  # Verifica se o contador for igual a nove, número máximo de jogadas
                vitoria = False
                break
            cont += 1
            if dificuldade == '1':
                jogada_pc_facil()
            elif dificuldade == '2':
                jogada_pc_dificil()
            elif dificuldade == '3':
                jogada_pc_extremo()
            redefinindo_tabuleiro_contra_pc()
            if checar_se_ha_vitoria_contra_pc():  # Verifica se o checar vitória contra o PC retorna True (verdadeiro)
                numero_do_jogo += 1
                break
        if cont == 9 and not vitoria:  # Verifica se o contador é igual a nove e se a vitória é falso (False)
            print(
                '\nInfelizmente deu velha, o chamado empate\n'
            )
            empates += 1
            sleep(2)  # sleep para facilitar a leitura
            placar_contra_pc()
            numero_do_jogo += 1
        var_continuar_jogar = continuar_a_jogar()  # Coloca a função continuar a jogar em uma variável para evitar um
        # bug do qual ela era pedida duas vezes
        if var_continuar_jogar:  # Verifica se retorna verdadeiro (True)
            continue  # Inicia o loop principal novamente
        elif not var_continuar_jogar:  # Verifica se retorna falso (False)
            print(
                '\nPor que nos abandonastes??? :-('
            )
            sleep(1.5)  # sleep para melhorar a leitura
            input(
                '\nPressione enter para sair'
            )
        break  # Quebra o laço principal e termina o jogo
if opcao == '2':
    while True:  # Cria um laço infinito
        nome_jogador1 = input(
            '\nDigite seu nome, jogador1: '
        ).strip()
        if nome_jogador1 == '':
            print(
                'Seu nome não pode ser em branco.'
            )
        else:
            break
    while True:
        nome_jogador2 = input(
            '\nDigite seu nome, jogador2: '
        ).strip()
        if nome_jogador2 == '':
            print(
                'Seu nome não pode ser em branco.'
            )
        else:
            break
    while True:
        tipo_jogador1 = input(
            f'\n{nome_jogador1}, você será o X ou o O: '
        ).upper().strip()
        if tipo_jogador1 == '':  # Verifica se o tipo estiver em branco
            print('Por favor, X ou O..')
            continue
        if tipo_jogador1 not in ('X', 'O'):  # Verifica se não esta em X ou O
            print(
                'É necessários que seja X ou O.'
            )
        else:
            break
    if tipo_jogador1 == 'X':
        tipo_jogador2 = 'O'
    else:
        tipo_jogador2 = 'X'
    limpa_tela()
    print(
        f'O(a) jogador(a) {nome_jogador1} será o {tipo_jogador1}\n'
        f'O(a) jogador(a) {nome_jogador2} será o {tipo_jogador2}'
    )
    print(
        '\nPressione enter para continuar...'
    )
    input()
    while True:  # Cria um laço infinito principal para o multiplayer
        limpa_tela()
        menu()
        limpa_tela()
        tabuleiro = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # Cria a lista tabuleiro que é usada para verificar
        # vitórias.
        tabuleiro_mostrado_usuario = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # Cria outra lista tabuleiro, mas
        # essa é a mostrada para o usuário
        redefinindo_tabuleiro()
        cont = 0
        while True:  # Cria um laço infinito para as jogadas dos jogadores
            cont += 1
            jogada_multiplayer()
            limpa_tela()
            redefinindo_tabuleiro()
            if checar_se_ha_vitoria():  # Verifica se o checar vitória no multiplayer retorna True (verdadeiro)
                numero_do_jogo += 1
                vitoria = True
                break
            if cont == 9:  # Verifica se o contador é igual a nove e se a vitória é falso (False)
                vitoria = False
                break
            cont += 1
            jogada_multiplayer()
            limpa_tela()
            redefinindo_tabuleiro()
            if checar_se_ha_vitoria():  # Verifica se o checar vitória no multiplayer retorna True (verdadeiro)
                numero_do_jogo += 1
                break
        if cont == 9 and not vitoria:  # Verifica se o contador é igual a 9 e se vitória é falso (False)
            print(
                '\nInfelizmente deu velha, o chamado empate\n'
            )
            empates += 1
            sleep(2)  # sleep para melhorar a leitura
            placar()
        var_continuar_jogar = continuar_a_jogar()  # Coloca a função continuar a jogar em uma variável para evitar um
        # bug do qual ela era pedida duas vezes
        if var_continuar_jogar:  # Verifica se a função retornou verdadeiro (True)
            continue  # Inicia o laço novamente
        elif not var_continuar_jogar:  # Verifica se a função retornou falso (False)
            print(
                '\nPor que nos abandonastes??? :-('
            )
            sleep(1.5)  # sleep para melhorar a leitura para o usuário
            input(
                '\nPressione enter para sair'
            )
        break  # Quebra o laço infinito principal e termina o jogo
