tag=input()
l=len(tag)

if isalnum(tag[2]):
    for i in range(l):
        sum=0
        if i!=2 || i!=6:
            if i<l-1:
                sum=sum+tag[i]+tag[i+1]