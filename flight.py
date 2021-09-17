import http.client

conn = http.client.HTTPSConnection("skyscanner-skyscanner-flight-search-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "f2a42e970dmsh9f444138ec6fc80p1bdc5djsn6a5f8f18cfde",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

conn.request("GET", "/apiservices/browsedates/v1.0/US/USD/en-US/SFO-sky/LAX-sky/2019-09-01?inboundpartialdate=2019-12-01", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))