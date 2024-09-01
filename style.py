menu = """

# Lembrando que primeiramente o SALDO da conta está zerado, o USER tem que depositar para poder realizar as outras operações.

[d] = depositar
[s] = sacar
[e] = extrato
[p] = pix
[q] = sair

=> """

saldo = 0
limite = 2000
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
            print("Operação falhou! Não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor informado excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Você excedeu o número de saques diários.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\nEXTRATO")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}\n")

    elif opcao == "p":
        valor = float(input("Informe o valor do PIX: "))
        chave_pix = input("Informe a chave PIX do destinatário: ")

        if valor > 0 and valor <= saldo:
            saldo -= valor
            extrato += f"PIX enviado para {chave_pix}: R$ {valor:.2f}\n"
            print(f"PIX de R$ {valor:.2f} enviado para {chave_pix} com sucesso!")
        else:
            print("Operação falhou! Saldo insuficiente ou valor inválido.")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
