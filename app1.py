from flask import Flask, render_template, request,jsonify
import json
import winsound
import time
import requests
import geopy
from geopy.geocoders import Nominatim
import random
from math import sin, cos, sqrt, atan2, radians

url = "https://pokemon-go1.p.rapidapi.com/shiny_pokemon.json"

headers = {
    'x-rapidapi-key': "f2a42e970dmsh9f444138ec6fc80p1bdc5djsn6a5f8f18cfde",
    'x-rapidapi-host': "pokemon-go1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

pokemon = []
pokemon_dit={}
pokemon=response.content
l=len(pokemon)
pokemon_dit = json.loads(pokemon.decode('utf-8'))
#print(pokemon)
#print(pokemon_dit)


places=["Malad","Andheri","Churchgate","Dahisar","Vile Parle","Ashok Nagar","Asha Nagar","Borivali"
,"Navi Mumbai","Panvel","Powai"]


'''for key,value in pokemon_dit.items():
    address = random.choice(places)
    geolocator = Nominatim(user_agent=".")
    location = geolocator.geocode(address)
    plat = location.latitude
    plong = location.longitude
    value['lat'] = plat
    value['long'] = plong'''
    

R = 6373.0

app = Flask(__name__)
count=1

@app.route('/catch',methods=['GET','POST'])
def catch_pokemon():
    print(f"The method is {request.method}")
    if request.method == "POST":
        name = request.form["pokemon"]
        for key,value in pokemon_dit.items():
            if name == value['name']:
                frequency = 500  
                duration = 500
                for i in range(4):
                    winsound.Beep(frequency,duration)
                    time.sleep(1)

                return {"Message":"Congratulations!! pokemon found"}
                break

            else:
                return {"message":"Pokemon not found"}
            

    return render_template("pokemon.html")



@app.route('/read',methods=['GET'])
def read_data():
    for key,value in pokemon_dit.items():
        address = random.choice(places)
        geolocator = Nominatim(user_agent=".")
        location = geolocator.geocode(address)
        plat = location.latitude
        plong = location.longitude
        value['lat'] = plat
        value['long'] = plong
    return jsonify(pokemon_dit)

@app.route('/hunt',methods=['GET','POST'])
def hunt_poke():
    pokemon_lst=[]
    dit={}
    print(f"the method is {request.method}")
    if request.method == "POST":
        address = request.form["location"]
        r = 5
        geolocator = Nominatim(user_agent=".")
        location = geolocator.geocode(address)
        lat = location.latitude
        longit = location.longitude
        with open("poke.json",'r') as logs:
            logdata = json.load(logs)
            
        for key,value in logdata.items():
            lat1 = radians(lat)
            lon1 = radians(longit)
            lat2 = radians(value["lat"])
            lon2 = radians(value["long"])

            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
            c = 2 * atan2(sqrt(a), sqrt(1-a))
            proximity = R * c

            if proximity <= r:
                #print(proximity)
                pokemon_lst.append(value)

        l1 = len(pokemon_lst)
        #dit = dict(pokemon_lst)
        if l1<1:
            return {"message":"No pokemon found near you"}

        else:
            frequency = 500  
            duration = 500
            for i in range(2):
                winsound.Beep(frequency,duration)
                time.sleep(1)
            #print(pokemon_lst)
            with open("catch.json",'w') as logs:
                logs.write(json.dumps(pokemon_lst))
            #return(dit)
            
    return render_template("hunt.html",POKEMON = pokemon_lst)
               
@app.route('/pokeball',methods=['GET','POST'])
def catch():
    print(f"The method is{request.method}")
    pokedata={}
    if request.method == 'GET':
        dit={}
        with open("catch.json",'r') as logs:
            logdata = json.load(logs)
            dit = random.choice(logdata)
            global count
            count+=1
            with open("mypokemon.json",'r') as poke:
                pokedata = json.load(poke)
                pokedata["poke_data"][count] = dit
            with open("mypokemon.json",'w') as poke:
                poke.write(json.dumps(pokedata))
            
            #return {"message":"Pokemon caught successfully, check your pokemon deck"}
    
    return {"message":"Pokemon caught successfully, check your pokemon deck"}

        
if __name__ == '__main__':
    app.run(host="127.0.0.1",port="5000",debug=False)