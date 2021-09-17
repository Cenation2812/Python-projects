import requests
from lxml import html
import csv
all_data = []

def remove_dupr(lst,item):
    count = lst.count(item)
    for i in range(count):
        lst.remove(item)

    return lst

def extract_vin(lst):
    id = []
    for url in lst:
        id.append(url[url.rfind('-')+1:len(url)-1])
    
    return id

url = "https://www.cars24.com/buy-used-cars-ludhiana/"

data = requests.get(url).text

tree = html.fromstring(data)

name = tree.xpath("//h2[@itemprop]/text()")

price = tree.xpath("//h3[@class='_6KkG6']/text()")

distance = tree.xpath("//div[@class='_Ecri']/p/span[1]/text()")

fuel = tree.xpath("//span[@itemprop]/span/text()")

links = tree.xpath("//a[@title]/@href")

#image_url = tree.xpath("//div/div/img/@src")

car_number = extract_vin(links)

price = remove_dupr(price,'₹ ')

distance = remove_dupr(distance,'km')
print(distance)

ownership = tree.xpath("//div[@class='_Ecri']/p/span[3]/text()")
print(ownership)

ownership = remove_dupr(ownership,' Owner')

all_data = list(zip(car_number,name,price,distance,fuel,ownership))

#print(all_data)

for each in all_data:
    print(each)
    
#print(type(all_data))
with open("cars.xls","w") as cardata:
    writer = csv.writer(cardata)
    writer.writerows(all_data)