import socket

host = "127.0.0.1"
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    message = input("Enter the message you want to send(type 'end' to end):")
    if message == "end":
        break
    else:
        s.sendto(f"{message}".encode(), (host,port))

        data=s.recvfrom(6666)
        print (data)
