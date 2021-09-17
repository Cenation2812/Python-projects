import re

str1 = "What we think we became"

p = "WE"

m = re.search(p,str1,re.I) #re.I ignores the case

print(m)

if m:
	print(m.group(),m.start(),"-->",m.end())