import socket

def main():
	host = '10.10.9.66'
	port = 5129
	lst = []
	c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	c.bind((host, port))

	print ("server is started")
	while True:
		data, addr = c.recvfrom(1024)
		print("from:" + data.decode())
		lst = data.decode().split()

		if lst[1] == "Dollar":
			if lst[4] == "INR":
				val = str(int(lst[2])*67)
				c.sendto(val.encode(), addr)
			elif lst[4] == "Pounds":
				val = str(int(lst[2])*0.75)
				c.sendto(val.encode(), addr)
			elif lst[4] == "Yen":
				val = str(int(lst[2])*113.41)
				c.sendto(val.encode(), addr)

		if lst[1] == "INR":
			if lst[4] == "Dollar":
				val = str(int(lst[2]) / 67)
				c.sendto(val.encode(), addr)
			elif lst[4] == "Pounds":
				val = str((int(lst[2])*0.75)/67)
				c.sendto(val.encode(), addr)
			elif lst[4] == "Yen":
				val = (str(int(lst[2])*113.41)/67)
				c.sendto(val.encode(), addr)

		if lst[1] == "Pounds":
			if lst[4] == "Dollar":
				val = str(int(lst[2]) / 0.75)
				c.sendto(val.encode(), addr)
			elif lst[4] == "INR":
				val = str((int(lst[2])*67)/0.75)
				c.sendto(val.encode(), addr)
			elif lst[4] == "Yen":
				val = (str(int(lst[2])*113.41)/0.75)
				c.sendto(val.encode(), addr)

		if lst[1] == "Yen":
			if lst[4] == "Dollar":
				val = str(int(lst[2]) / 113.41)
				c.sendto(val.encode(), addr)
			elif lst[4] == "INR":
				val = str((int(lst[2])*67)/113.41)
				c.sendto(val.encode(), addr)
			elif lst[4] == "Pounds":
				val = (str(int(lst[2])*0.75)/113.41)
				c.sendto(val.encode(), addr)
		
	c.close()

if __name__ == '__main__':
	main()
