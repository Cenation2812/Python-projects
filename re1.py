import requests,re
import os

docs = []

files = os.listdir()

expression = r".py"

for item in files:
    docs.append(re.findall(expression,item))

print(docs)
