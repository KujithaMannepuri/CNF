import socket

def main():
	host = '10.10.9.66'
	port = 5011

	s = socket.socket()
	s.bind((host, port))

	s.listen(1)
	print ("server is connected..")
	c, addr = s.accept()
	print ("connected:" + str(addr))
	while True:
		data = c.recv(1024).decode()
		if not data:
			break
		print ("from connected user:" + str(data))
		data = str(data).upper()
		print ("sending:" + str(data))
		c.send(data.encode())
	c.close()

if __name__ == '__main__':
	main()