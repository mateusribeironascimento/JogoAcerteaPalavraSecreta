print(f'{"ACERTE A PALAVRA SECRETA":-^30}')
print('-' * 30)
palavra_secreta = 'cadeira'
letras_acertadas = ''
c = 0
while True:
    letra = input('Digite uma letra: ').lower().strip()
    if len(letra) > 1:
        print('Não digite mais de uma letra!')
        continue
    c += 1
    if letra in palavra_secreta:
        letras_acertadas += letra
    for i in palavra_secreta:
        if i in letras_acertadas:
            print(i, end='')
        else:
            print('*', end='')
    print('')
    print('-' * 30)
    chute = input('Qual a palavra secreta? ').lower().strip()
    if chute == palavra_secreta:
        break
    else:
        print('Errou!')
        continue
print(f'Parabéns! Você acertou a palavra secreta em {c} tentativa(s)!')