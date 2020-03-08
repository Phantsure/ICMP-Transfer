# first of all import library
import socket               
from threading import *
import random

# next create a socket object
s = socket.socket()         
print("Socket successfully created")

# reserve a port on your computer
port = 4

# Next bind to the port
s.bind(('', port))        
print("socket binded to %s" %(port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            dialogs = [b'server:hi back', b'server:shut up', b'server:get lost', b'server:pardon me']
            print('Client sent:', self.sock.recv(1024).decode())
            self.sock.send(dialogs[random.randint(0, 3)])

# socket into listening mode
s.listen(4)
print("socket is listening")   

# a forever loop until we interrupt it or 
# an error occurs
while True:
   # Establish connection with client.
   c, addr = s.accept()     
   print('Got connection')
   client(c, addr)
#    data = c.recv(1024).decode()
#    print(data)

#    # send a thank you message to the client. 
#    c.send(b"server:Thank you for connecting")
#    # Close the connection with the client
#    c.close()                
