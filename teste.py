from banco import *

# CONTA CORRENTE
cont01 = ContaCorrente(1,3021,'Fabricio Paim','79228810530', 8.000)

# AQUI DEI UM PRINT NA CONTA CORRENTE
print(cont01.nome, cont01.saldo, cont01.limite)

# AQUI IREI FAZER UM DEPOSITO 

cont01.deposito(4.000)

# AQUI IREI PEDIR UM PRINT ATUAL DEPOIS DO DEPOSITO FEITO

print(cont01.nome, cont01.saldo, cont01.limite )