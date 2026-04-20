from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("UDP Server ready di port", serverPort)

while True:
    print("\nMenunggu pesan dari client...")
    message, clientAddress = serverSocket.recvfrom(2048)
    print(f"Terima dari {clientAddress}: {message.decode()}")
    
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print(f"Kirim balik: {modifiedMessage}")