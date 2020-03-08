# server
import socket 
import select 
import sys 
from thread import *

# server sockets
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

# checks for sufficient arguments 
if len(sys.argv) != 3: 
	print "Correct usage: script, IP address, port number"
	exit() 

# IP address 
IP_address = str(sys.argv[1]) 

# port 
Port = int(sys.argv[2]) 

# binding
server.bind((IP_address, Port)) 

# start listening
server.listen(100) 

list_of_clients = [] 

def clientthread(conn, addr): 

	# sends a message 
	conn.send("Welcome to this chatroom!") 

	while True: 
			try: 
				message = conn.recv(64) 
				if message: 

					# print the message
					print "<" + addr[0] + "> " + message 

					# Calls broadcast function to send message to all 
					message_to_send = "<" + addr[0] + "> " + message 
					broadcast(message_to_send, conn) 

				else: 
					# if empty message then remove
					remove(conn) 

			except: 
				continue

# broadcast to all clients
def broadcast(message, connection): 
	for clients in list_of_clients: 
		if clients!=connection: 
			try: 
				clients.send(message) 
			except: 
				clients.close() 

				# if the link is broken, we remove the client 
				remove(clients) 
# function to remove
def remove(connection): 
	if connection in list_of_clients: 
		list_of_clients.remove(connection) 

while True: 
	# accept from new client
	conn, addr = server.accept() 
	
	# append that client to list
	list_of_clients.append(conn) 

	# prints the address of the user that just connected 
	print addr[0] + " connected"

	# creates and individual thread for every user that connects 
	start_new_thread(clientthread,(conn,addr))	 

conn.close() 
server.close() 
