#Matthew Wilson
#mlw0420@unt.edu
#CSCE 3530.003
#5/6/2022
#UDP server for network programming assignment

import random
import socket

IP      = "127.0.0.1"
Port    = 8008
buffer  = 1024

msg     = "PONG"
bSend   = str.encode(msg)

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind((IP, Port))

print("UDP Server by Matthew Wilson, mlw0420")

print("[server] : ready to accept data...")

while(True):
    bAddrPr = sock.recvfrom(buffer)
    
    message = bAddrPr[0]
    
    addr = bAddrPr[1]
    
    num = random.randrange(1, 10)
    
    if num > 0 and num < 8:        
        print("[client] : PING")
        
        sock.sendto(bSend, addr)
        
    elif num > 7 and num < 11:
        print("[server] : packet dropped")
 
