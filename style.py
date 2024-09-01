menu = """

[d] = depositar
[s] = sacar
[e] = extrato
[q] = sair

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
            extrato += f"Depósito: R$ {valor: .2f}\n"

        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor informado excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! O valor informado excede o limite de saques.")   


        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor: .2f}\n"     
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é invalido.")      


    elif opcao == "e":
        print("\n=============EXTRATO===============")     
        print("Não foram realizadas movimentações." if not extrato else extrato)  
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

        
        