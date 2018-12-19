import socket

def main():
	host = '10.10.9.66'
	port = 5502

	server = ('10.10.9.66', 5129)

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	message = input("Input:")
	while message != "q":
		s.sendto(message.encode(), server)
		data = s.recv(1024)
		print("recieved:" + str(data.decode()))
		message = input("Input:")
	s.close()

if __name__ == '__main__':
	main()