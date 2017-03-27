""" File push_db.py - Reads sensor data from arduino and dumps into mysql database"""

#Required imports
import serial
import time
from datetime import datetime
from datetime import timedelta
import pymysql

#connection to database 
conn = pymysql.connect(host='localhost', db='smartjacket_sensors', user='root')
cur = conn.cursor()

#serial connection to arduino
arduinoData=serial.Serial('COM4',9600)

#reading data from arduino and pushing into the database table "sensor" with columns "time" (time) and "values" (varchar(10))
while(1):
	uid = 1;
	mydata =(arduinoData.readline())
	mydata = mydata.decode('utf-8')
	print(mydata)
	now = datetime.now()
	#insert = int(mydata)
	q = """INSERT INTO sensor_input_raw VALUES(%s,%s,%s)"""
	cur.execute(q, (uid, now, mydata))
	conn.commit()
	#print(mydata.decode('utf-8'))
	print(cur)
	
cur.close()
conn.close()
arduinoData.close()