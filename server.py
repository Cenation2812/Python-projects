import socket 
host = "127.0.0.1"
port = 12345
print ("Server is started")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port ))
decision = True

while decision:
    data=s.recvfrom(6666)
    print (data[0].decode())
    answer = input("Say something: ")
    #new_answer = data[0].decode()
    s.sendto(answer.encode(), data[1])
    if answer == "bye" or answer == "Bye":
        print("inside if")
        decision = False