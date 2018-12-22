import socket
import csv
lst = []
rows = []
def main():
	host = '10.10.9.66'
	port = 1140
	s = socket.socket()
	s.bind((host, port))
	s.listen(10)
	print('server is started...')
	file = "data.csv"
	with open(file, 'r') as csvfile:
		lst = csv.reader(csvfile)
		for row in lst:
			rows.append(row)
			
	while True:
		conn, addr = s.accept()
		conn.send('Welcome..please enter your roll number.'.encode())
		msg = conn.recv(1024).decode()
		msg = msg.split(' ')
		if msg[0] == 'MARK-ATTENDANCE':
			val = msg[1]
			check(val, conn)
		elif msg[0] == 'SECRETANSWER':
			val = msg[1]
			answer(val, conn)

def check(val, conn):
	for i in range(0, 9):
		if val == rows[i][0]:
			conn.send(('SECRETQUESTION' + rows[i][1]).encode())
		else:
			conn.send('ROLLNUMBER-NOTFOUND'.encode())
def answer(val, conn):
	for i in range(0, 9):
		if val == rows[i][2]:
			conn.send('ATTENDANCE SUCCESS'.encode())
		else:
			conn.send('ATTENDANCE FAILURE'.encode())

if __name__ == '__main__':
	main()