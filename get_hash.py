import wget
url = "https://bazaar.abuse.ch/export/txt/sha256/full/"

output = "D:\\antivirus\\full.zip"
file_name = wget.download(url, out=output)

print(file_name)