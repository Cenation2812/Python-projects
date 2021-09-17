import re
str1 = "what we think WE became We"

p = "we"

new1 = re.sub(p,"I",str1,1,re.I)

print(new1)