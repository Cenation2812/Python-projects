from flask import abort, jsonify, request
import flask
import json
# Flask initialization

app=flask.Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
	data=request.get_json(force=True)
	emailofuser=data.get("email")
	passofuser=data.get("password")
	if emailofuser == "shourjadeepdatta@gmail.com" and passofuser == "dodo2812":
		text="User authenticated"
		dit={}
		dit["name"]="Shourjadeep Datta"
		dit["age"] = "19"
		return jsonify(dit)
	else:
		text="User authentication failed"
		return jsonify(text)


@app.route('/profile',methods=['POST'])
def makeProfile():
	data=request.get_json(force=True)

	dit={}

	dit["name"] = {'firstName':"Shourjadeep",'LastName':"Datta"}
	dit["age"]	= {'Age':"20"}
	dit["Location"] = {'City':"Mumbai",'State':"Maharashtra",'Country':"India"}

	return jsonify(dit)

if __name__ == '__main__':
	app.run(host="127.0.0.1",port="5001",debug=False)