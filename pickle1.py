import pickle 

name = ["Ankur", "Bhaskar", "Sahil"]
age = [35,36,30]
skill = ["BA", "Java", "DL"]

fw = open("picke1.txt", "wb")

pickle.dump(name, fw)
pickle.dump(age, fw)
pickle.dump(skill, fw)

fw.close()