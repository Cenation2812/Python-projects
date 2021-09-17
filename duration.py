num=input()
num=int(num)
for i in range(num):
    count=0
    SH=int(input(" "))
    SM=int(input())
    EH=int(input(" "))
    EM=int(input())
    RH=EH-SH
    while SM<EM:
        SM+=1
        count+=1
    print(RH," ",count)