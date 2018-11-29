import socket
import time
import os

UDP_IP = "127.0.0.1"
UDP_PORT = 9193
UDP_PORT_ROBOT = 9180
MESSAGES = [bytes.fromhex('012400da0000000000000000000000000000000000000000000000000000000000000000'), bytes.fromhex('012400d90100000000000000000000000000000000000000000000000000000000000000'), bytes.fromhex('012400d80200000000000000000000000000000000000000000000000000000000000000'), bytes.fromhex('012400d70300000000000000000000000000000000000000000000000000000000000000'), bytes.fromhex('012400d60400000000000000000000000000000000000000000000000000000000000000'), bytes.fromhex('012400d50500000000000000000000000000000000000000000000000000000000000000'), bytes.fromhex('012400d40600000000000000000000000000000000000000000000000000000000000000'), bytes.fromhex('012400d30700000000000000000000000000000000000000000000000000000000000000')]
state = 0;

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

sock.bind((UDP_IP, UDP_PORT))

while True:
    data, address = sock.recvfrom(1024)
    if data[4] != state:
        state = data[4]
        print('carlas code ', state)
        if state == 0:
            os.system("python faseProducao2.py")
        time.sleep(1)
    else:
        message = MESSAGES[state]
        sock.sendto(message, (UDP_IP, UDP_PORT_ROBOT))
        time.sleep(0.05)

