import socket
import os

#create socket
def initSocket():
	tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	return tcp_socket
if __name__ == '__main__':
	socket = initSocket()
	#bind port
	socket.bind(("",8088))
	#input IP & port
	IpAddress = input("input IP:\n")
	port = input("input port:\n")
	socket.connect((IpAddress,int(port)))

	while True:
		cmd = input("input command:\n")
		if cmd == "QUIT"
			print("退出聊天")
			socket.close()
			break
		socket.send(cmd.encode())

