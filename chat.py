import socket
import sys
from _thread import *
from threading import Thread

def receive_message(IP_address, Port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((IP_address, Port))

    while True:
        message = server.recv(2048)
        sys.stdout.write(message.decode('UTF-8'))

def send_message(IP_address, Port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((IP_address, Port))

    while True:
        message = sys.stdin.readline()
        server.send(message.encode('UTF-8'))
        # sys.stdout.write("<Vc> ")
        # sys.stdout.write(message)
        sys.stdout.flush()

IP_address = "localhost"
Port = 65432



receive_thread = Thread(target=receive_message,args=(IP_address, Port))
send_thread = Thread(target=send_message,args=(IP_address, Port))

receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()

