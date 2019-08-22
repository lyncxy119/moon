import socket

def rcvMain():
    udpSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    udpSocket.bind(("",8088))
    udpSocket.listen(128)

    clientSocket,clientIP = udpSocket.accept()
    print("client IP ",clientIP)
    while True:
        udpData = clientSocket.recv(1024)
        print(udpData.decode())
        if udpData.decode() == "QUIT":
            print("client quit")
            clientSocket.close()
            clientSocket,clientIP = udpSocket.accept()
            print("client IP ",clientIP)
            
if __name__ == '__main__':
    rcvMain()


