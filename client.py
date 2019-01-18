# Import socket module
import socket               

# Create a socket object
s = socket.socket()         

# Define the port on which you want to connect
port = 4

# connect to the server on local computer
s.connect(('127.0.0.1', port))

while 1:
    r = input('client:')
    # send data to server
    s.send(r.encode())
    # receive data from server
    data = ''
    data = s.recv(1024).decode()
    print(data)
# close the connection
s.close()   