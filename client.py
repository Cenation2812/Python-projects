import socket
host = "127.0.0.1"
port = 12345
print("This is client")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.bind((host,port))
decision = True
while decision:
    msg = input("Enter your message:")
    s.sendto(msg.encode(), (host,port))
    reply = s.recvfrom(6666)
    new_reply = reply[0].decode()
    print(new_reply)
    if new_reply == "bye" or new_reply == "Bye":
        print("inside if")
        decision = False
