# client
import socket 
import select 
import sys 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

if len(sys.argv) != 3: 
	print "Correct usage: script, IP address, port number"
	exit() 

# ip
IP_address = str(sys.argv[1]) 

# port
Port = int(sys.argv[2]) 

# connect to server
server.connect((IP_address, Port)) 

while True: 

	# list of input streams 
	sockets_list = [sys.stdin, server] 

	# separates sockets as per type
	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 

	for socks in read_sockets: 
		if socks == server: 
			message = socks.recv(2048) 
			print message 
		else: 
			message = sys.stdin.readline() 
			server.send(message) 
			sys.stdout.write("<You>") 
			sys.stdout.write(message) 
			sys.stdout.flush() 
server.close() 
