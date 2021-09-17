tag=input()
l=len(tag)

if isalnum(tag[2]):
    for i in range(l):
        sum=0
        if i!=2 or i!=6:
            if i<l-1:
                sum=sum+tag[i]+tag[i+1]


'''
A -- Apple -->B1,C1,D1
B -- Ball -->B2,E1,F1
C -- Cat -->C2,D2,E2
D -- Dog -->A1,D3,C3
E -- Elee -->F2,G1,A2 
F -- Flag -->A3,G2,B3
G -- Gun -->E3,F3,G3

B, C

(B,B),(C,C2)

(Ball,B2)

'''