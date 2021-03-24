import firebase_admin
from firebase_admin import auth,credentials,firestore

import flask
from flask import abort, jsonify, request,redirect
import json
import requests

#------------------------Flask APP INIT---------------------------
app=flask.Flask(__name__)
#------------------------Flask APP INIT---------------------------

#---------------------------------------Firestore Database INIT-------------------------------------------
cred = credentials.Certificate("/content/tinder-api-clone-1fd2c-firebase-adminsdk-fvs9t-05d5ef9a45.json")
firebase_admin.initialize_app(cred)
store=firestore.client()
#---------------------------------------Firestore Database INIT------------------------------------------

@app.route('/login', methods=['POST'])
def login():
  data=request.get_json(force=True)
  emailofuser=data.get("email")
  uid=""
  message=""
  try:
    user=auth.get_user_by_email(emailofuser)
    message="Woohooo!!!!, successfully logged in"
    uid=user.uid
  except:
    message="OOPS!!, no user found"

  return jsonify({"Response":200,"uid":uid,"message":message})


@app.route('/signup', methods=['POST'])
def signup():
  data=request.get_json(force=True)

  emailofuser=data.get("email")
  passwordofuser=data.get("password")
  uid=""
  message=""
  try:
    user = auth.create_user(
        email=emailofuser,
        email_verified=False,
        password=passwordofuser)
    message="Successfully created new user"
    uid=user.uid
  except:
    message="User already exists"
  
  return jsonify({"response":200,"uid":uid,"message":message})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001,debug=False)

# Creating the User profile

#1. Name
#2. Image
#3. Desp
'''4. Location
  1. Lat lng
  2. City
  3. state
  4. country
5. Job
6. Passion
7. Company
8. Gender
9. DOB/Age
10. Number'''


user_data={}

user_data["name"]="Prachi"
user_data["Image"]="gs://tinder-api-clone-1fd2c.appspot.com/InShot_20200109_204623574 (1).jpg"
user_data["Desp"]="Amazing person"
user_data["Location"]={"Latitude":27.2046,"Longitude":77.4977,"City":"London","State":"YK","Country":"England"}
user_data["Job"]="Game developer"
user_data["Passion"]="Teacher"
user_data["Company"]="DJ Sanghvi College"
user_data["Gender"]="Female"
user_data["DOB"]="30th December 2000"
user_data["Number"]="9284573820"
user_data["CreatedAt"]=firestore.SERVER_TIMESTAMP

def userUpdateInfo(uid,user_data):
  user_info={}
  user_info["name"]=user_data["name"]
  user_info["Image"]=user_data["Image"]
  user_info["Desp"]=user_data["Desp"]
  user_info["Location"]=user_data["Location"]
  user_info["Job"]=user_data["Job"]
  user_info["Passion"]=user_data["Passion"]
  user_info["Company"]=user_data["Company"]
  user_info["Gender"]=user_data["Gender"]
  user_info["DOB"]=user_data["DOB"]
  user_info["Number"]=user_data["Number"]
  user_info["CreatedAt"]=user_data["CreatedAt"]

  store.collection("abc").document(uid).set(user_info)

userUpdateInfo("52fQrHnyRqXTzOezfSP8Fx9tnPx2",user_data)

# Feed function

def feed(Country):
  docs=store.collection("abc").stream()
  dit={}
  for doc in docs:
    if doc.to_dict().get("Location").get("Country") == Country:
      dit[doc.id]=doc.to_dict()

  return dit

allProfiles=feed("England")

allProfiles

# Swipe function

def Swipe(uidA,uidB,isYesA,isYesB,firstTime):
  dit={}
  dit["UIDA"]=uidA
  dit["UIDB"]=uidB
  dit["UserA_reply"]=isYesA
  dit["UserB_reply"]=isYesB
  dit["viewedAtleastOnce"]=firstTime
  dit["CreatedAt"]=firestore.SERVER_TIMESTAMP

  store.collection("Swipes").add(dit)

uidA="52fQrHnyRqXTzOezfSP8Fx9tnPo1"
uidB="52fQrHnyRqXTzOezfSP8Fx9tnPx2"
isYesA=True
isYesB=False
firstTime=False

Swipe(uidA,uidB,isYesA,isYesB,firstTime)

#Match function

def Match(uid):
  docs=store.collection("Swipes").stream()
  match_dit={}
  for doc in docs:
    if (doc.to_dict().get("UIDA") == uid or doc.to_dict().get("UIDB") == uid) and (doc.to_dict().get("UserA_reply") == True and doc.to_dict().get("UserB_reply") == True):
      match_dit[doc.id]=doc.to_dict()


  return match_dit
