#Matthew Wilson
#mlw0420@unt.edu
#CSCE 3530.003
#5/6/2022
#UDP client for network programming assignment

import socket

msg         = "PING"
bSend       = str.encode(msg)
svrAddrPort = ("127.0.0.1", 8008)
buffer      = 1024

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

count = 1

print("UDP Client by Matthew Wilson, mlw0420")

while(count < 11):    
    sock.settimeout(0.00001)
    
    try:
        sock.sendto(bSend, svrAddrPort)
    
        message = sock.recvfrom(buffer)
    
        if count > 9:
            print("%d : sent PING... received {}".format(message[0]) % (count))
        
        else:
            print("%d  : sent PING... received {}".format(message[0]) % (count))
        
    except socket.timeout:        
        if count > 9:
            print("%d : sent PING... Timed Out" % (count))
        
        else:
            print("%d  : sent PING... Timed Out" % (count))
        
    count+=1
