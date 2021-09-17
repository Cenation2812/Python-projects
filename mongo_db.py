from db1 import mongo_connect



mydb = mongo_connect()

mycol = mydb["computer"]

d1 = [{'name':"M", 'city': "nagpur", 'rank':4},{'name':"N", 'city': "nagpur", 'rank':5}]

mycol.insert_many(d1)

for x in mycol.find():
  print(x)
