import pickle 

fr = open("pickle.txt", "rb")

a = pickle.load(fr)
b = pickle.load(fr)
c = pickle.load(fr)

print (a)
print (b)
print (c, type(c))

fr.close()