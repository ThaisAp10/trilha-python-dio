# Arquivo original está no seguinte link:
# https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py
# Foi apenas implementada a opção "[t] Transferir" no menu com algumas condições

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[t] Transferir 
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

# Transferência 
    elif opcao == "t":
        valor = float(input("Informe o valor que deseja transferir: "))
        banco = input("Digite o nome do banco que deseja transferir: ")
        nome_conta_transferencia = input("Digite o nome da conta que deseja trasnferir: ")

        excedeu_saldo = valor > saldo
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Valor trasnferido: R$ {valor:.2f} para conta {nome_conta_transferencia} do banco {banco.upper()}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")        
# Transferência

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")