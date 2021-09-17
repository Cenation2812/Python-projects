import requests
import json

#state = input("Enter your state:")

#district = input("Enter your district:")

date = input("Enter the vaccination date:")
id = input("Enter district id:")

'''# 1st end-point
state_lst=[]
states={}

link1 = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
url = link1
response = requests.request("GET",url)
state_lst = response.content
states = json.loads(state_lst.decode('utf-8'))

print(state_lst)

#2nd end-point
state_lst=[]
states={}

link2 = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/21"
url = link2

response = requests.request("GET",url)
state_lst = response.content
#states = json.loads(state_lst.decode('utf-8'))

print(state_lst)'''

# 3rd end-point
link3 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="+id+"&date="+date
url = link3

response = requests.request("GET",url)

vaccine_lst=[]
vaccine_dit={}

vaccine_lst = response.content

vaccine_dit = json.loads(vaccine_lst.decode('utf-8'))

print(vaccine_dit)