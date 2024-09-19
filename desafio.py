import textwrap
from datetime import datetime

# Função para exibir o menu
def menu():
    menu = """\n
    ====== MENU ======
[d]  = Depositar
[s]  = Sacar
[e]  = Extrato
[p]  = PIX
[un] = Cadastrar Usuário
[cn] = Cadastrar Conta
[lc] = Listar Contas
[q]  = Sair
=> """
    return input(textwrap.dedent(menu))

# Função para depósito (recebe argumentos apenas por posição)
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Função para saque (recebe argumentos apenas por nome)
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print("Operação falhou! Valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Função para exibir o extrato
def exibir_extrato(saldo, /, *, extrato):
    print("\nEXTRATO")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}\n")

# Função para cadastrar um novo usuário
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_usuario(cpf, usuarios):
        print("Erro: Usuário já cadastrado.")
        return
    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")
    usuarios.append({"nome": nome, "data_nasc": data_nasc, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

# Função para filtrar usuário pelo CPF
def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

# Função para criar uma conta bancária
def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print(f"Conta criada com sucesso! Agência: {agencia}, Número da conta: {numero_conta}")
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
        return numero_conta + 1
    else:
        print("Erro: Usuário não encontrado.")
        return numero_conta

# Função para listar contas
def listar_contas(contas):
    for conta in contas:
        linha = f"""\nAgência: {conta['agencia']}
Número da conta: {conta['numero_conta']}
Titular: {conta['usuario']['nome']}"""
        print("=" * 100)
        print(textwrap.dedent(linha))

# Função principal
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 2000
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo, valor=valor, extrato=extrato, limite=limite,
                numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "un":
            criar_usuario(usuarios)

        elif opcao == "cn":
            numero_conta = criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
