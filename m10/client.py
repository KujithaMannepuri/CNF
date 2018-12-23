import socket
import threading
import os, signal
s= socket.socket()
def main():
	host = '192.168.137.143'
	port = 5232
	
	s.connect((host, port))
	threading.Thread(target = sender, args = ()).start()
	threading.Thread(target = reciever, args = ()).start()

def reciever():
	while True:
		msg = s.recv(1024).decode()
		print(msg)
		if msg == "you left the group":
			os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
		if not msg:
			continue
	s.close()
	
def sender():
	while True:
		msg = input("-->")
		s.send(msg.encode())
	s.close()

if __name__ == '__main__':
	main()