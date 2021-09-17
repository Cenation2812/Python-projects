import db1
car_data = open("cars.xls","r")
try:
	table_name = "cars"
    for items in car_data:
        print(items)
#         q1 = f"insert into {table_name} (vin,car_name,price,distance,fuel_type,owner,status) values(%s,%s,%s,%s,%s,%s,%s)"
#         data = items
#         conn = db1.mysql_connect()
#         cursor = conn.cursor()
#         cursor.execute(q1,data)
#         conn.commit()

# except Exception as e:
# 	print (e)
	    
    
# finally:
# 	conn.close()
# 	cursor.close()