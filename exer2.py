import random

FORCAIMG = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

palavras = 'formiga babuino encefalo elefante girafa hamburger chocolate giroscopio'.split()


def main():
    """
    Funcao Principal do programa
    """
    global FORCAIMG

    print('F O R C A')
    letrasErradas = ''  # criamos uma string de letras erradas vazia
    letrasAcertadas = ''  # string de letras acertadas vazia
    palavraSecreta = geraPalavraAleatoria().upper()
    jogando = True

    while jogando:  # enquanrto o usuario estiver jogando ou seja enquanto jogando for true
        imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)  # chama a funcao imprime jogo

        palpite = recebePalpite(
            letrasErradas + letrasAcertadas)  # pal,pite vai receber funcao com as letras erradas e a letras certas

        if palpite in palavraSecreta:  # se o palpite for uma letra que ta na palavra certa
            letrasAcertadas += palpite  # minhas letras certas terao que incrementar 1 + o palpite

            if VerificaSeGanhou(palavraSecreta, letrasAcertadas):  # aqui a gente verifica se o jogo foi vencido
                print("Parabens! A palavra secreta e " + palavraSecreta + '! Voce ganhou!!')
                jogando = False
        else:
            letrasErradas += palpite

            if len(letrasErradas) == len(
                    FORCAIMG) - 1:  # verifica se o numero de letras erradas e igual o numero de imagens da forca
                imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)  # se sim vai ser imprimido o jogo

                print("Voce exagerou o seu limite de palpites!")
                print("Depois de " + str(len(letrasErradas)) + ' letras erradas e' + str(len(letrasAcertadas)), end=' ')
                print('palpites corretos, a palavra era ' + palavraSecreta + '.')

                jogando = False

        if not jogando:  # verifica se jogando e falso
            if JogarNovamente():
                letrasErradas = ''  # reinicio as letra erradas
                letrasAcertadas = ''  # reinicia letras certas
                jogando = True
                palavraSecreta = geraPalavraAleatoria().upper()  # ele vai gerar palavra aleatoria


def geraPalavraAleatoria():
    """
    Funcao que retorna uma string a partir da
    lista de palavras global
    """
    global palavras
    return random.choice(palavras)


def imprimeComEspacos(palavra):
    """
    Recebe uma string palavra ou lista e imprime essa com
    espaco entre suas letras ou strings
    """
    for letra in palavra:
        print(letra, end=' ')

    print()


def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
    """
    Feito a partir da variavel global que contem as imagens
    do jogo em ASCII art, e tambem as letras chutadas de
    maneira correta e as letras erradas e a palavra secreta
    """
    global FORCAIMG  # defi uma variavel global
    print(FORCAIMG[len(letrasErradas)] + '\n')  # essa variavel ira receber a quantidade de letras erradas a ela

    print("Letras Erradas:", end=' ')  # estamos pedidndo todas as letras erradas que rebera um espaco entre elas
    imprimeComEspacos(letrasErradas)  # dai ele chama o metodo de espaco das letras erradas

    vazio = '_' * len(
        palavraSecreta)  # criando o espaco vazio, que vai ter o anderline como o mesmo numero de letras da palavra
    for i in range(len(palavraSecreta)):  # para cada acerto do usuario irremos percorrer o len da palavra
        if palavraSecreta[i] in letrasAcertadas:  # verifica se o indice da palavra esta em letras
            vazio = vazio[:i] + palavraSecreta[i] + vazio[
                                                    i + 1:]  # se caso sim, o vazio adiciona o indice e depois soma mais 1

    imprimeComEspacos(vazio)  # chama o metodo para imprimir com espacos


def recebePalpite(palpiteFeitos):
    ''' Essa funcao garante que o usuario digite so uma letra e que confere se a mesma ja foi chutada '''

    while True:  # enquanto o palpiteFeitos for verdadeiro
        palpite = input(
            'Adivinhe alguma letra. \n').upper()  # aqui a variavel ira receber uma letra e passala para Maiuscula

        if len(palpite) != 1:  # verifica se apalavra escrita em palpite tem uma letra so.
            print('Coloque uma unica letra')
        elif palpite in palpiteFeitos:  # se palpite esta dentro de palpites feitos
            print('Voce ja digitou essa letra, digite de novo!')
        elif not 'A' <= palpite <= 'Z':  # verifica se palpite e menor ou igual a A ou se e menor ou igual a Z
            print('Escolha Somente uma letra!')
        else:
            return palpite  # se estiver dentro dos conformes ele retorna o palpite


def JogarNovamente():
    """
    Funcao que pede para o usuario decidir se ele quer
    jogar novamente e retorna um booleano representando
    a resposta
    """
    return input("Voce quer jogar novamente? (sim ou nao)\n").upper().startswith(
        'S')  # se a resposta do usuario convertido em maiusculo for verdadeiro


def VerificaSeGanhou(palavraSecreta, letrasAcertadas):
    '''
    Funcao que verifica se o usuario acertou todas as
    letras da palavra secreta '''

    ganhou = True
    for letra in palavraSecreta:  # percorrrese cada uma das letras da palavra secreta
        if letra not in letrasAcertadas:  # se a letra nao esta nas letras acertadas
            ganhou = False  # o meu ganhou passa a ser falso
            break  # o for loop e parado

    return ganhou  # retorna o que ganhou


main()