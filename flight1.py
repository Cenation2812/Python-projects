import requests

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/USA/GBP/en-GB/"

querystring = {"query":"Mumbai"}

headers = {
    'x-rapidapi-key': "f2a42e970dmsh9f444138ec6fc80p1bdc5djsn6a5f8f18cfde",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)