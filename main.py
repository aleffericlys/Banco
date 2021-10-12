from conta import Conta
from cliente import Cliente
 
p1 = Cliente('aleff', 'erl', '123455')
p2 = Cliente('Ffela', 'lre', '554321')
c = Conta('1234', p1, 500, 1000 )
b = Conta('4321', p2, 500, 1000 )
c.sacar(100)
b.transferir(c, 200)
# print(c.saldo)
# print(b.saldo)
c.extratos()
b.extratos()

#Alteração#