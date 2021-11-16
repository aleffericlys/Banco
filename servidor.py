import socket
import threading

class ClientThreading(threading.Thread):
    def __init__(self, clientAddress, clientSocket):
        threading.Thread.__init__(self)
        self.csocket = clientSocket
        print(f"Nova conexao: {clientAddress}")

    def run(self, msg):
        print(f"Conectado de: {clientAddress}")
        while True:
            data = self.csocket.recv(1024)
            msg = data.decode()
            self.csocket.send(msg.encode())
            print(f"From client: {msg}")
            if msg == 'bye':
                break
        print(f"Client at {clientAddress} disconnected...")
    
if __name__ == '__main__':
    LOCALHOST = ''
    PORT = 7003
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print("Servidor iniciado.")
    print("Aguardando nova conexão")
    while True:
        server.listen(1)
        clientSocket, clientAddress  = server.accept()
        newThread = ClientThreading(clientAddress, clientSocket)
        newThread.start()
