import socket
import threading
d_dict = {}
def main():
	host = '192.168.137.143'
	port = 5232
	s = socket.socket()
	s.bind((host, port))
	s.listen(10)
	print('server is started..')
	threading.Thread(target = server, args = ()).start()
	while True:
		conn, addr = s.accept()
		print("client entered:")
		conn.send('welcome to the group chat..please enter your name:'.encode())
		if conn not in d_dict:
			d_dict[conn] = "user name"
			threading.Thread(target = grp_chat, args = (conn, "user name")).start()
		else:
			conn.send("connection failed..try after sometime!!".encode())
			d_dict.pop(conn)
	s.close()

def grp_chat(conn, name):
	name = conn.recv(1024).decode()
	d_dict[conn] = name
	msg = name + " : " +" has joined the group chat.!"
	broad_cast(msg, conn)
	while conn in d_dict:
		msg = conn.recv(1024).decode()
		if msg != 'quit':
			msg = name + "-->" + msg
			broad_cast(msg, conn)
		else:
			msg = name + " : " + "Has exited the group chat.!"
			broad_cast(msg, conn)
			conn.send("you left the group".encode())
			d_dict.pop(conn)

def broad_cast(msg, conn):
	ip = d_dict.keys()
	print(msg)
	for x in ip:
		if conn != x:
			x.send(msg.encode())

def server():
	while True:
		msg = input("-->")
		if not msg:
			continue
		else:
			msg = "server" + " : " + msg
			ip = d_dict.keys()
			print(msg)
			for x in ip:
				x.send(msg.encode())

if __name__ == '__main__':
	main()