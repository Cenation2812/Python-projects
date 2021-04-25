str=input("Enter a string:")
l=len(str)
finalstring=""
for i in range(l):
    val=ord(str[i])
    newval=val+3
    if newval>ord('z'):
        newval=newval-26
        ch=chr(newval)
        finalstring=finalstring+ch
    else:
        ch=chr(newval)
        finalstring=finalstring+ch
print("The new string is:",finalstring)