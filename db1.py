import mysql.connector
import pymongo
import csv 

def mysql_connect():
	my_conf ={ 'host' : '127.0.0.1','port' : '3306','user' : 'root','password': 'Dodo@2812','database' : 'cars'}
				
	cnx = mysql.connector.connect(**my_conf)
	return cnx 
				
				

def mongo_connect():
	myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
	mydb = myclient["Shourjadeep"]
	return mydb
