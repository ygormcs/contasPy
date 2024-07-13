from contas import Conta
from cliente import Cliente

cliente1 = Cliente(12345678910, "Ygor", "Rua Victoria's Secret, 321")
cliente2 = Cliente(98765432110, "Vini", "Rua Djonga Livre, 3847")
cliente3 = Cliente(76509823490, "Tulio", "Rua Billabong Pato, 456")
cliente4 = Cliente(23409745678,"Edson", "Rua Lanternas dos Afogados, 678")

conta1 = Conta([cliente1, cliente2, cliente3, cliente4], 1, 0)

conta1.gerarSaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarSaldo()

for clientes in conta1.clientes:
    print(f'O cliente se chama {cliente.nome}, cujo CPF e {cliente.cpf} e reside em {cliente.endereco}')

