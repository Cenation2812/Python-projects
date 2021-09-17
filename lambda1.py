# fun1 = lambda x,y : x+y

# print(fun1(20,30))

# lst = [i for i in range(1,11)]
# print(lst)

# def fun2(m):
#     print(m)

lst = [1,2,3,4,5,6]

def fun1(item):
    if item%2!=0:
        return item

new_lst = filter(fun1,lst)
print(list(new_lst))