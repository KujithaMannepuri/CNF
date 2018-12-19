import socket

def main():
	host = '10.10.9.66'
	port = 5011

	s = socket.socket()
	s.connect((host, port))

	message = input("input:")
	while message != "q":
		s.send(message.encode())
		data = s.recv(1024)
		print("message is recieved:" + str(data.decode()))
		message = input("Input:")
	s.close()

if __name__ == '__main__':
	main()