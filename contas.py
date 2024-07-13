class Conta: #chamada da classe >Conta< onde futuramente serao criados os objetos

#criacao dos metodos da classe
  def __init__(self, clientes, numero, saldo):
    self.clientes
    self.numero
    self.saldo
  def depositar(self, valor): #criacao da funcao de depositar
    self.saldo += valor
  def sacar(self, valor): #criacao da funcao sacar
    if self.saldo < valor:
      return False
    else:
      self.saldo -= valor
      return True
  def transfValores(self, cDestino, valor): #criacao da funcao de transf.
      if self.saldo < valor:
        return ("Nao existe saldo suficiente")
      else:
        cDestino.depositar(valor)
        self.saldo -= valor
        return("Tranferencia realizada")
  def gerarSaldo(self): #criacao da funcao de mostrar saldo
    print(f'numero:{self.numero}\n saldo:{self.saldo}')