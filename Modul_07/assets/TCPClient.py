from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

try:
    clientSocket.connect((serverName, serverPort))
    print("Terhubung ke server")
    
    sentence = input('Ketik kalimat: ')
    clientSocket.send(sentence.encode())
    
    modifiedSentence = clientSocket.recv(1024)
    print('Response dari server:', modifiedSentence.decode())
    
finally:
    clientSocket.close()
    print("Koneksi ditutup")