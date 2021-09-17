list1=[10,20,30,40,50,60,70]

list2=[5,15,25,35,45,55,65,75,85,95]

l1=len(list1)
l2=len(list2)

l=max(l1,l2)
list3=[]
for item in range(l):
    list3.append(list2[item])
    if item<=l1-1:
        list3.append(list1[item])
    
print("Merged list is: ",list3)