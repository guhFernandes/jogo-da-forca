import random

arquivo = open("br-sem-acentos.txt")
linhas = arquivo.readlines()
palavra = ''

while len(palavra) < 5 or len(palavra) > 10:
    sorteio = random.randint(0, len(linhas))
    palavra = linhas[sorteio]
    palavra = palavra.upper().strip()
    arquivo.close()


tentativas = 6
j = i = y = 0

verifica_letra = False
letra_jogada = False
stop = False

vetor_palavra = []
palavras_jogadas = []

while i < len(palavra):
    vetor_palavra.append('_')
    i += 1

letra_usuario = input('Digite a letra: ')
letra_usuario = letra_usuario.upper()

while tentativas > 0 and not stop:
    while j < len(palavra):
        if letra_usuario == palavra[j]:
            vetor_palavra[j] = letra_usuario
            verifica_letra = True
        j += 1

    if not verifica_letra:
        tentativas -= 1
        verifica_letra = False
        j = 0
    else:
        verifica_letra = False
        j = 0

    palavras_jogadas.append(letra_usuario)

    print('')
    print(f'Tentativas: {tentativas}')
    print('Palavras jogodas: ', end = '')
    print(*palavras_jogadas, sep = ", ")
    print(*vetor_palavra)
    print('')

    if vetor_palavra == list(palavra):
        stop = True
        print('Parabens voce acertou a palavra')

    
    if tentativas > 0 and not stop:
        letra_usuario = input('Digite a letra: ')
        letra_usuario = letra_usuario.upper()

        while y < len(palavras_jogadas):
            for letra_jogadas in palavras_jogadas:
                if letra_usuario == letra_jogadas:
                    letra_usuario = input('Letra ja jogada, digite novamente a letra: ')
                    letra_usuario = letra_usuario.upper()
                    y -= 1
            y += 1


if tentativas == 0:
    print('Acabou suas tentativas')
