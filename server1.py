import socket
import threading

def udp():
	udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	udp.bind(("192.168.15.247", 1024))
	threads = {}
	nextPort = 1025
	ports = []
	connections = []

	while(True):
		data, addr = udp.recvfrom(1024)
		udp.sendto(str(nextPort).encode('UTF-8'),addr)
		ports.append(nextPort)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind(("192.168.15.247",nextPort))
		s.listen(1)
		conn, address = s.accept()
		connections.append(conn)
		threads[nextPort] = threading.Thread(target=tcp,args=(connections,conn,))
		threads[nextPort].start()
		nextPort += 1

def tcp(connections,conn):
	message = ""
	while(message.decode('UTF-8') != "quit"):
		message = conn.recv(1024)
		if message != '':
			announce(message,connections)
	conn.close

def announce(msg,connections):
	for conn in connections:
		conn.send(msg)

def server():
	udp()
server()
