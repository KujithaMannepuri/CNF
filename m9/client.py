import socket

def main():
	host = '10.10.9.66'
	port = 5053

	s = socket.socket()
	s.connect((host, port))

	message = ""
	while message != "q":
		message = s.recv(1024)
		print("message is recieved:" + str(message.decode()))	
		message = input("Input:")
		s.send(message.encode())
	s.close()

if __name__ == '__main__':
	main()