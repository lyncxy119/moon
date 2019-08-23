import socket
import threading
import os

class myThread(threading.Thread):
	def __init__(self,args,func):
		threading.Thread.__init__(self)
		self.args = args
		self.func = func

	def run(self):
		self.func(*self.args)
#create socket
def initSocket():
	tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	return tcp_socket

#client thread func
def clientFunc(threadName,dstIP,port):
	print("%s thread is running dstIP %s port %s"%(threadName,dstIP,port))
	socket = initSocket()
	#bind port
	socket.bind(("",int(port)))
	#input IP & port
	IpAddress = input("input IP:\n")

	#if int(IpAddress) != 0:
	port = input("input port:\n")
	socket.connect((IpAddress,int(port)))

	while True:
		cmd = input(">:\n")
		if cmd == "QUIT":
			print("退出聊天")
			socket.close()
			break
		socket.send(cmd.encode())

#server thread func
def serverFunc(threadName,port):
	print("%s thread is running"%threadName)
	serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serverSocket.bind(("",int(port)))
	serverSocket.listen(128)

	clientSocket,clientIP = serverSocket.accept()
	print("client IP ",clientIP)
	while True:
		rcvData = clientSocket.recv(1024)
		print(rcvData.decode())
		if rcvData.decode() == "QUIT":
			print("client quit")
			clientSocket.close()
			clientSocket,clientIP = serverSocket.accept()
			print("client IP ",clientIP)

if __name__ == '__main__':
	clientThread = myThread(("client","192.168.1.1",8089),clientFunc)
	serverThread = myThread(("server",8088),serverFunc)

	clientThread.start()
	serverThread.start()

	clientThread.join()
	serverThread.join()


