import random

biblioteca_secretas = "banana", "computador", "oceano", "energia", "aventura",
"coração", "mistério", "relâmpago", "biblioteca", "viagem",
"universo", "silêncio", "maratona", "felicidade", "esmeralda",
"harmonia", "foguete", "enigma", "girassol", "labirinto"

palavra_secreta = random.choice(biblioteca_secretas)
letra_acertada = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'           
            
    print(palavra_formada) 

    if palavra_formada == palavra_secreta:
        print('PARABÉNS VOCÊ GANHOU O JOGO!!')
        print(f'A palavra secreta era {palavra_secreta}!!')
        print(f'Você precisou de {numero_tentativas}')
        palavra_secreta = random.choice(biblioteca_secretas)
        letra_acertada = ''
        numero_tentativas = 0