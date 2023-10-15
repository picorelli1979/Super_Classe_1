
# AQUI É UMA SUPER CLASSE 
class Conta:
    def __init__(self,numc, agencia ,nome,cpf):
        self.numer = numc
        self.agencia = agencia
        self.__nome = nome
        self.cpf = cpf
        self._saldo = 0

# AQUI É UM GETTERS:
    @property              
    def saldo(self):
        return self._saldo
    
# AQUI É UM SETTERS:
    @saldo.setter
    def saldo(self,valor):
        print('Não pode fazer isso. Faça um depósito ou um saque.')
        
# AQUI É UM GETTERS:
    @property
    def nome(self):
        return self.__nome
    
# AQUI É UM SETTERS:
    @nome.setter
    def nome(self,valor):
        print('Não pode fazer isso. Faça uma troca de nome.')

# AQUI É UMA FUNÇÃO DE DEPOSITO :
    def deposito(self,valor):
        self._saldo += valor

# AQUI UMA FUNÇÃO DE SAQUE:
    def saque(self,valor):
        self._saldo -= valor
    
# AQUI ALTERA O NOME DA CONTA :    
    def troca_nome(self,novonome):
        print(f'Atenção: {self.__nome} TROCOU O NOME PARA {novonome}')
        self.__nome = novonome

# AQUI ESTÃO 3 SUB-CLASSES : CONTA CORRENTE / CONTA INVESTIMENTO / CONTA SALARIO

class ContaCorrente(Conta):
    def __init__(self, numc, agencia, nome, cpf,limite):
        super().__init__(numc, agencia, nome, cpf)
        self.limite = limite

    def saque(self,valor):
        atual = self._saldo - valor
        if atual <= self.limite:
            self._saldo = atual
        else:
            print(f'{self.nome} não tem limite para este saque')


class ContaInvestimento(Conta):
    def __init__(self, numc, agencia, nome, cpf,rendimento):
        super().__init__(numc, agencia, nome, cpf)
        self.rendimento = rendimento


class ContaSalario(Conta):
    def __init__(self, numc, agencia, nome, cpf,empresa):
        super().__init__(numc, agencia, nome, cpf)
        self.empresa = empresa

    def saque(self,valor):
        atual = self._saldo - valor
        if atual < 0:
            print(f'{self.nome} não tem limite para este saque')