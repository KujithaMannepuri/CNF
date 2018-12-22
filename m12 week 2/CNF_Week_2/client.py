import socket
import os

def main():
	host = '10.10.9.66'
	port = 1140

	s = socket.socket()
	s.connect((host, port))

	message = input("->")
	while True:
		msg = s.recv(1024).decode()
		print(str(msg))
		if msg != 'ATTENDANCE SUCCESS':
			s.send(message.encode())
		else: 
			os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
			break
		message = input("->")
	s.close()

if __name__ == '__main__':
	main()
