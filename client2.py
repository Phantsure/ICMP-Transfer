import socket
import threading

BUFFER_SIZE = 1024

class ChatListener(threading.Thread):

    def __init__(self, my_host, my_port):
        threading.Thread.__init__(self, name="listener")
        self.host = my_host
        self.port = my_port

    def listen(self):
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.bind((self.host, self.port))
        listen_socket.listen(5)
        
        while True:

            connection, address = listen_socket.accept()

            # print("Established connection with: ", address)

            try:
                message = ""
                while True:
                    data = connection.recv(BUFFER_SIZE)
                    message = message + data.decode()
                    if not data:
                        # not striping the message
                        print("{}: {}".format(address, message))
                        break
            finally:
                connection.shutdown(2)
                connection.close()
    
    def run(self):
        self.listen()

class ChatSender(threading.Thread):

    def __init__(self, their_host, their_port):
        threading.Thread.__init__(self, name="sender")
        self.address = their_host
        self.port = their_port

    def run(self):
        while True:
            message = input("")

            send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            send_socket.connect((self.address, self.port))

            if message.lower() == "quit":
                break
            else:
                send_socket.sendall(message.encode())
            
            send_socket.shutdown(2)
            send_socket.close()

def main():
    my_host = input("Your ip: ")
    my_port = int(input("Your port: "))
    chat_listener = ChatListener(my_host, my_port)
    chat_listener.start()

    their_host = input("Their ip: ")
    their_port = int(input("Their port: "))
    chat_sender = ChatSender(their_host, their_port)
    chat_sender.start()

if __name__ == "__main__":
    main()