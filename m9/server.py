import socket
import threading
import random

def guess_num(c, addr, value):
	count = 0
	while True:
		count += 1
		g_val = c.recv(1024).decode()
		if (int(g_val) < value):
			c.send('number guessed is less:'.encode())
		elif (int(g_val) > value):
			c.send('number guessed is greater:'.encode())
		elif (int(g_val) == value):
			c.send(('the number guessed is correct' +" " + str(count)+" attempts").encode())
	c.close()

def main():
	host = '10.10.9.66'
	port = 5053

	s = socket.socket()
	s.bind((host, port))

	s.listen(10)
	print ('server is started')
	while True:
		c, addr = s.accept()
		value = random.randint(1, 50)
		c.send("welcome...guess a number between 1 and 50".encode())
		threading.Thread(target = guess_num, args = (c, addr, value)).start()

if __name__ == '__main__':
	main()



