file1 = open("sample.txt","r")
text1 = file1.read()

html_msg = "<html><body>" + text1.replace("\n","<br/>") + "</body></html>"
print(html_msg)