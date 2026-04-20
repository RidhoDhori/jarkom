from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("TCP Server ready di port", serverPort)
print("Menunggu koneksi...")

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"\nClient terhubung dari {addr}")
    
    try:
        sentence = connectionSocket.recv(1024).decode()
        print(f"Terima pesan: {sentence}")
        
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())
        print(f"Kirim balik: {capitalizedSentence}")
    finally:
        connectionSocket.close()
        print("Koneksi ditutup")
        print("\nMenunggu koneksi berikutnya...")