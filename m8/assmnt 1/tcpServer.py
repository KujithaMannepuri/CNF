import socket

def main():
	host = '10.10.9.66'
	port = 5128
	lst = []
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
		lst = data.split()

		if lst[1] == "Dollar":
			if lst[4] == "INR":
				val = str(int(lst[2])*67)
				c.send(val.encode())
			elif lst[4] == "Pounds":
				val = str(int(lst[2])*0.75)
				c.send(val.encode())
			elif lst[4] == "Yen":
				val = str(int(lst[2])*113.41)
				c.send(val.encode())

		if lst[1] == "INR":
			if lst[4] == "Dollar":
				val = str(int(lst[2]) / 67)
				c.send(val.encode())
			elif lst[4] == "Pounds":
				val = str((int(lst[2])*0.75)/67)
				c.send(val.encode())
			elif lst[4] == "Yen":
				val = (str(int(lst[2])*113.41)/67)
				c.send(val.encode())

		if lst[1] == "Pounds":
			if lst[4] == "Dollar":
				val = str(int(lst[2]) / 0.75)
				c.send(val.encode())
			elif lst[4] == "INR":
				val = str((int(lst[2])*67)/0.75)
				c.send(val.encode())
			elif lst[4] == "Yen":
				val = (str(int(lst[2])*113.41)/0.75)
				c.send(val.encode())

		if lst[1] == "Yen":
			if lst[4] == "Dollar":
				val = str(int(lst[2]) / 113.41)
				c.send(val.encode())
			elif lst[4] == "INR":
				val = str((int(lst[2])*67)/113.41)
				c.send(val.encode())
			elif lst[4] == "Pounds":
				val = (str(int(lst[2])*0.75)/113.41)
				c.send(val.encode())
		
	c.close()

if __name__ == '__main__':
	main()
