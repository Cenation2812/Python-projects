n=int(input())

l=n*2+2

length=n+l

for i in range(1,length+1):
    if i%3==0:
        print("*****")
    else:
        print("*   *")
