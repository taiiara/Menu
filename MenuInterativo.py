# Menu interativo versão 1.0
# Por Taiiara

escolha = ''

while escolha != '5':
    numero1 = int(input('Digite um valor: '))
    numero2 = int(input('Digite outro valor: '))

    print('_.' * 20)

    print('Escolha uma das opções a seguir...')
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')

    escolha = str(input('Qual opção deseja executar? ')).strip()
    print('_.'*20)

    if escolha == '1':
        print(f'{numero1} + {numero2} = {numero1 + numero2}')
    elif escolha == '2':
        print(f'{numero1} x {numero2} = {numero1 * numero2}')
    elif escolha == '3':
        if numero2 > numero1:
            print(f'{numero2} é maior que {numero1}')
        elif numero1 > numero2:
            print(f'{numero1} é maior que {numero2}')
        else:
            print(f'{numero1} e {numero2} são iguais')
    if escolha > '5':
        print('Opção inválida, tente novamente.')
    if '5' != escolha != '4':
        escolha = str(input('Digite [4] para continuar ou [5] para sair: ')).strip()
    print('_.' * 20)

print('Programa encerrado com sucesso!')
