from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)     

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, cliente, numero, saldo, agencia, historico):
        self._cliente = 0
        self._numero = numero
        self._saldo = "0001"
        self._agencia = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)    
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor - saldo

        if excedeu_saldo:
            print("\n Operação falhou! O valor informado é invalido.")
        elif valor > 0:
            self._saldo = str(int(saldo) - valor)
            print("\n Saque realizado com sucesso!")
            return True
        
        else:
            print("\n Operação falhou! O valor informado é invalido.")

        return False   

    def depositar(self, valor):
        if valor > 0:
            self._saldo = str(int(self._saldo) + valor)
            print("\n Depósito realizado com sucesso!")

        else:
            print("\n Operação falhou! O valor informado é invalido.")
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacao if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques    

        if excedeu_limite:
            print("\n Operação falhou! O valor saque excedeu o limite.")
        
        elif excedeu_saques:
            print("\n Operação falhou! O número máximo de saques foi excedido.")

        else:
            return super().sacar(valor)
        
        return False

    def __str__(self) -> str:
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            """
            

        
class Historico:
    def __init__(self):
        self._transacao = []

    @property
    def transacao(self):
        return self._transacao
    
    def adcionar_transacao(self, transacao):
        self._transacao.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(cls, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property  
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    @property
    def valor(self):
        return self.valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
    
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# Validação de CPF e autenticação de usuários
def validar_cpf(cpf, usuarios):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return False
    return True

def autenticar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    print("Usuário não encontrado.")
    return None


def main():
    usuarios = []
    contas = []
    while True:
        opcao = input("\n[d] Depósito\n[s] Saque\n[t] Transferência\n[h] Histórico\n[c] Criar Conta\n[u] Criar Usuário\n[q] Sair\n=> ").lower()
        if opcao == "d":
            cpf = input("Informe o CPF do cliente: ")
            usuario = autenticar_usuario(cpf, usuarios)
            if usuario:
                numero_conta = int(input("Informe o número da conta: "))
                conta = next((conta for conta in usuario.contas if conta.numero == numero_conta), None)
                if conta:
                    valor = float(input("Informe o valor do depósito: "))
                    usuario.realizar_transacao(conta, Deposito(valor))
        elif opcao == "s":
            cpf = input("Informe o CPF do cliente: ")
            usuario = autenticar_usuario(cpf, usuarios)
            if usuario:
                numero_conta = int(input("Informe o número da conta: "))
                conta = next((conta for conta in usuario.contas if conta.numero == numero_conta), None)
                if conta:
                    valor = float(input("Informe o valor do saque: "))
                    usuario.realizar_transacao(conta, Saque(valor))
        elif opcao == "t":
            cpf_origem = input("Informe o CPF da conta de origem: ")
            usuario_origem = autenticar_usuario(cpf_origem, usuarios)
            if usuario_origem:
                numero_conta_origem = int(input("Informe o número da conta de origem: "))
                conta_origem = next((conta for conta in usuario_origem.contas if conta.numero == numero_conta_origem), None)
                if conta_origem:
                    cpf_destino = input("Informe o CPF da conta de destino: ")
                    usuario_destino = autenticar_usuario(cpf_destino, usuarios)
                    if usuario_destino:
                        numero_conta_destino = int(input("Informe o número da conta de destino: "))
                        conta_destino = next((conta for conta in usuario_destino.contas if conta.numero == numero_conta_destino), None)
                        if conta_destino:
                            valor = float(input("Informe o valor da transferência: "))
                            conta_origem.transferir(valor, conta_destino)
        elif opcao == "h":
            cpf = input("Informe o CPF do cliente: ")
            usuario = autenticar_usuario(cpf, usuarios)
            if usuario:
                numero_conta = int(input("Informe o número da conta: "))
                conta = next((conta for conta in usuario.contas if conta.numero == numero_conta), None)
                if conta:
                    conta.exibir_historico()
        elif opcao == "c":
            cpf = input("Informe o CPF do cliente: ")
            usuario = autenticar_usuario(cpf, usuarios)
            if usuario:
                numero_conta = len(contas) + 1
                conta = ContaCorrente(usuario, numero_conta)
                usuario.adicionar_conta(conta)
                contas.append(conta)
                print(f"Conta {numero_conta} criada com sucesso!")
        elif opcao == "u":
            nome = input("Informe o nome do cliente: ")
            data_nascimento = input("Informe a data de nascimento: ")
            cpf = input("Informe o CPF: ")
            if validar_cpf(cpf, usuarios):
                endereco = input("Informe o endereço: ")
                usuario = PessoaFisica(nome, data_nascimento, cpf, endereco)
                usuarios.append(usuario)
                print("Usuário criado com sucesso!")
            else:
                print("CPF já cadastrado.")
        elif opcao == "q":
            break

if __name__ == "__main__":
    main()
