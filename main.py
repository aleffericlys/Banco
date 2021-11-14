import mysql.connector as mysql

conexao = mysql.connect(
	host = "localhost", 
	user = "root",
	db = "banco", 
	password = "Ericly$2", 
	auth_plugin = 'mysql_native_password')

cursor = conexao.cursor(buffered = True)
cursor.execute("USE banco;")
command = "SELECT * FROM clientes WHERE cpf = '{}'".format("1111")
cursor.execute(command)
for i in cursor:
	conta = i

print(conta)
cursor.execute("UPDATE clientes SET nome = %s WHERE cpf = %s", ('aleff','1111'))
conexao.commit()
valor = float('100')
saldo: float = conta[2]
limite: float = conta[4]
dep = int(conta[0])
print("saldo de: {}\nlimite: {}".format(saldo, limite))
if saldo + valor > limite:
	print("não deu")
else:
	command = """UPDATE contas SET saldo = """ + str(saldo + valor) + """ WHERE numeros = """+str(dep)
	cursor.execute(command)
	conexao.commit()



# from conta import Conta
# from cliente import Cliente


# p1 = Cliente('aleff', '123455', 'no local la', '1999-12-11')	
# p2 = Cliente('Ffela', '554321', 'no outro local la', '2010-04-15')
# c1 = Conta('123455', 500.00, 'picapau', 1000.00)
# c2 = Conta('554321', 700.00, 'biruta', 1000.00)
#print(p1.nome())
#c.sacar(100)
#b.transferir(c, 200)
# print(c.saldo)
# print(b.saldo)
#a = c.extratos()

#Alteração#