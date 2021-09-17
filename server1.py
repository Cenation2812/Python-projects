import socket

host = "127.0.0.1"
port = 12345
print ("Server is started")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port ))
decision = True
while decision:
    #print("receive")
    data=s.recvfrom(6666)
    print(data[0].decode())
    if data[0].decode() == "end":
        decision = False
    else:
        print (data)
        s.sendto("message from server ".encode(), data[1])