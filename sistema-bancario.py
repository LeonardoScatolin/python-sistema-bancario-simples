menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao == 'd':
        depositando = float(input('Digite o valor que deseja depositar: '))
        if depositando > 0:
            saldo += depositando
            extrato += f'Depositou {depositando} \n'
            print(f'Você depositou {depositando}. Saldo atual de R$ {saldo: .2f}')
        else:
            print('Valor para depósito inválido.')

    elif opcao == 's':
        sacando = float(input('Digite o valor que deseja sacar: '))
        if numero_saques <= LIMITE_SAQUES:
            if sacando <= limite:  
                if saldo >= sacando:
                    saldo -= sacando
                    numero_saques += 1
                    extrato += f'Sacou {sacando} \n'
                    print(f'Você sacou {sacando}. Saldo atual de: R$ {saldo: .2f}')
                else: 
                    print('Não foi possível realizar o saque. Você não possui saldo.')
            else: 
                print(f'Limite de R$ {limite} por saque.')
        else:
            print('Você excedeu o limite de saque diário.')

    elif opcao == 'e':
        print('========== EXTRATO ========== \n')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print('============================= \n')

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')