
import re

str1 = "What we think we became"

p = "WE"

m = re.finditer(p,str1,re.I) #re.I ignores the case
for each in m:
    print(each.group(),each.start(),each.end())