from conta import Conta
from cliente import Cliente
import mysql.connector as mysql
 
p1 = Cliente('aleff', '123455', 'no local lá', '11223333')
p2 = Cliente('Ffela', '554321', 'no outro local lá', '33221111')
c = Conta(p1, '123', 500, 1000 )
b = Conta(p2, '321', 500, 1000 )
c.sacar(100)
b.transferir(c, 200)
# print(c.saldo)
# print(b.saldo)
a = c.extratos()

#Alteração#