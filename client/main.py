#Much code stolen - er, _borrowed_ - from https://github.com/nicoladaniello/python-udp-server/blob/master/client.py
import socket

from .CONFS import Config

HOST = Config["HOST"]
PORT = Config["PORT"]

comms = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    item = ""
    comms.sendto("GET".encode(), (HOST, PORT))
    while len(item) == 0:
        item = sock.recv(50).decode()
    # do some logic here, like for example:
    print(f"Our item was {item}")
