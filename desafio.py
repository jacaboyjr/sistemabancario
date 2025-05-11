from datetime import datetime
menu = '''
    [d] Depositar
    [S] Sacar
    [e] Extrato
    [q] Sair

'''

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
quantidades_saques = 0

while True:

    opcao = input(menu)

    #DEPOSITO
    if opcao == 'd':
        deposito = float(input('Informe o valor depositado.:'))
        if deposito <= 0:
            print(f'Deposito não pode ser negativo você depositou R${deposito:.2f}, realize operação novamente.')
        else:
            saldo += deposito
            data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato += f'{data_hora_atual} - Depósito: R${deposito:.2f} - Saldo: R${saldo:.2f}\n'
        
        print(f"deposito de R${deposito:.2f} realizado com sucesso !!")

    #SAQUE    
    elif opcao == 's':
        saque = float(input('Informe o valor do saque.: '))
        if saque > saldo:
            print(f"Saldo insuficiente --> SALDO {saldo}")
        elif saque > 500:
            print(f"Limite para saque é de R$500,00 --> VALOR SAQUE {saque}")
        elif LIMITE_SAQUES == quantidades_saques:
            print(f"Você atingiu o limite de saques diários {LIMITE_SAQUES}")
        else:
            saldo -= saque            
            quantidades_saques += 1
            extrato += f'{data_hora_atual} - Saque: R${saque:.2f} - Saldo: R${saldo:.2f}\n'
            print(LIMITE_SAQUES, quantidades_saques)
            print(f"Saque de R${saque:.2f} realizado com sucesso !! RESTAM {LIMITE_SAQUES - quantidades_saques}")
    
    #EXTRATO BANCARIO
    elif opcao == 'e':
        print(f"----------EXTRATO BANCARIO----------""\n")
        if extrato:
            print(extrato)
        else:
            print('---SEM MOVIMENTAÇÕES REALIZADAS---\n')
        print(f'Saldo atual: R${saldo:.2f}\n')
        print(f"------------------------------------")
    
    #SAINDO DO SISTEMA
    elif opcao == "q":
        break