from conta import Conta
from cliente import Cliente
 
p1 = Cliente('aleff', '123455', 'no clocal lá', '11223333')
p2 = Cliente('Ffela', '554321', 'no outro clocal lá', '33221111')
c = Conta('1234', p1, '123', 500, 1000 )
b = Conta('4321', p2, '321', 500, 1000 )
c.sacar(100)
b.transferir(c, 200)
# print(c.saldo)
# print(b.saldo)
c.extratos()
b.extratos()

#Alteração#