from conta import Conta
from cliente import Cliente
import mysql.connector as mysql

conexao = mysql.connect(
	host = "localhost", 
	db = "banco", 
	user = "root", 
	password = "7650FNAF", 
	auth_plugin = 'mysql_native_password')

cursor = conexao.cursor(buffered = True)
cursor.execute("SELECT DATABASE();")

p1 = Cliente('aleff', '123455', 'no local la', '1999-12-11')	
#p2 = Cliente('Ffela', '554321', 'no outro local la', '2010-04-15')
#c1 = Conta('123455', 500.00, 'picapau', 1000.00)
#b = Conta('554321', 500.00, 'biruta', 1000.00)
print(p1.nome('aleff'))
#c.sacar(100)
#b.transferir(c, 200)
# print(c.saldo)
# print(b.saldo)
#a = c.extratos()

#Alteração#