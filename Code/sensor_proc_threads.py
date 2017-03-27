
'''
Upload arduino file and run this after sensor_push_db.py
Open one more prompt and run tree code to traverse tree.
'''





import pymysql
import time
from datetime import datetime
from datetime import timedelta
from threading import *

print("waiting first 36 sec to initialise values...")
print()
counter=0
while(1):

	time.sleep(15)
	c=0 #accel
	g=0 #gsr
	t=0
	#connection to database 
	conn = pymysql.connect(host='localhost', db='smartjacket_sensors', user='root')
	cur_a = conn.cursor()
	uid = 1;

	t1_a = datetime.now() 
	t2_a = datetime.now() - timedelta(seconds=12)
		#print(t1,t2)
		#q = """SELECT * FROM accel WHERE dt=%s"""
		# executing query
	q_a = """SELECT * FROM sensor_input_raw WHERE time BETWEEN %s AND %s""" #gets all rows btw the specified date
	

	r_a = cur_a.execute(q_a, (t2_a,t1_a,))
	#print(r)
	rows_a = cur_a.fetchall()
	#print(rows)
	accel_count=0
	for i in rows_a:
		if(i[2][0:1]=='A'):
			c=c+int(i[2][1:5])
			accel_count = accel_count+1
	#print(c)	
	print(c/accel_count)
	avg_accel = c/accel_count
	
	
	
	cur_g = conn.cursor()
	r_g = cur_g.execute(q_a,(t2_a, t1_a,))
	rows_g = cur_g.fetchall()
	gsr_count=0
	
	for i in rows_g:
		if(i[2][0:1]=='G'):
			#print(i[2][0:1])
			g=g+int(i[2][1:5])
			gsr_count = gsr_count +1
	#print(c)	
	print(g/gsr_count)
	avg_gsr = g/gsr_count
	
	
		
	cur_t=conn.cursor()
	r_t= cur_t.execute(q_a, (t2_a, t1_a))
	rows_t = cur_t.fetchall()
	temp_count=0
	for i in rows_t:
		if(i[2][0:1]=='T'):
			t=t+int(i[2][1:4])
			temp_count=temp_count+1
	print(t/temp_count)
	avg_tmp = t/temp_count
	
	counter=counter+1
	if(counter>1):
		z_a=avg_accel;
		z_g=avg_gsr;
		z_t=avg_tmp
		break;
'''	

def t_hb():
		
	while(1):	
		c=0
		conn = pymysql.connect(host='localhost', db='smartjacket_sensors', user='root')
		cur_t = conn.cursor()
		cur_h = conn.cursor()
		
		
		#for hb
		t1 = datetime.now() 
		t2 = datetime.now() - timedelta(seconds=30)
		
		# for temp
		t_temp = datetime.now()
		
		q1 = """SELECT * FROM sensor_input_raw WHERE time=%s"""
		
		q2 = """SELECT * FROM sensor_input_raw WHERE time BETWEEN %s AND %s"""
		
		temp = cur_t.execute(q1, (t_temp,))
		#t_temp = t_temp + timedelta(seconds=30)
		
		heart = cur_h.execute(q2, (t2,t1))
		
		rows_t = cur_t.fetchall()
		print(rows_t)
		rows_h = cur_h.fetchall()
		
		print(temp, heart)
		
		for i in rows_t:
			if(i[2][0:1] == 'T'):
				print("Temperature: ", i[2])
				temp_db= i[2][1:3]
		now = datetime.now()
		q = """INSERT INTO temperature VALUES(%s,%s,%s)"""
		cur_t.execute(q, (uid,now,temp_db))
		conn.commit()
		#print("here")		
		
		
		for i in rows_h:
			
			if(i[2][0:1]=='P'):
				#print(i[2][1:4])
				if(int(i[2][1:4])>10):
					#print("in ppulse")
					c=c+1;
					#print(c)
		now = datetime.now()
		d = c*2
		q = """INSERT INTO pulse VALUES(%s,%s,%s)"""
		cur_h.execute(q, (uid,now,d))
		conn.commit()
		print("Pulse: ", c)	
		
		time.sleep(30)
		
'''


def hb():
	stop=0
	while(1):
		conn = pymysql.connect(host='localhost', db='smartjacket_sensors', user='root')
		q1 = """SELECT * FROM sensor_input_raw WHERE time BETWEEN %s AND %s"""
		cur_h = conn.cursor()
		t1_h = datetime.now() 
		t2_h = datetime.now() - timedelta(seconds=123)
		heart = cur_h.execute(q1, (t2_h, t1_h, ))
		rows_h = cur_h.fetchall()
		
		for i in rows_h:
				if(i[2][0:1] == 'H'):
					print("Pulse: ", i[2])
					heart_db= i[2][1:5]
					print("*******************", heart_db)
					
					if(int(i[2][1:5])>85):
						str_h = "highpulse"
						print(str_h)
					else:
						str_h = "lowpulse"
						print(str_h)
		now = datetime.now()
		q = """INSERT INTO pulse VALUES(%s,%s,%s,%s)"""
		cur_h.execute(q, (uid,now,heart_db, str_h))
		conn.commit()
		time.sleep(120)
		stop=stop+1
		if(stop>60):
			print("instop")
			break
		print("out of while hb")
		time.sleep(123)
	
	
def accel():
	stop=0
	while(1):
		c=0;
		g=0;
		t=0
		conn = pymysql.connect(host='localhost', db='smartjacket_sensors', user='root')
		q3 = """SELECT * FROM sensor_input_raw WHERE time BETWEEN %s AND %s"""
		t1_a = datetime.now() 
		t2_a = datetime.now() - timedelta(seconds=12)
		
		# for accel
		cur_a = conn.cursor()
		accel = cur_a.execute(q3, (t2_a, t1_a))
		rows_a = cur_a.fetchall()
		
		# for accelerometer
		accel_count1=0	
		for i in rows_a:
			if(i[2][0:1]=='A'):
				c = c + int(i[2][1:5])
				accel_count1=accel_count1+1
				#print(c)
		print(c/accel_count1)
		y = c/accel_count1
		if((y>z_a+400)|(y<z_a-400)):
			str = "mov"
			print(str)
		else:
			str = "nomove"
			print(str)
			
		now = datetime.now()
		aa = """INSERT INTO accel VALUES(%s,%s,%s)"""
		cur_a.execute(aa, (uid,now,str))
		conn.commit()
		

		
		#for gsr
		conn = pymysql.connect(host='localhost', db='smartjacket_sensors', user='root')
		cur_g = conn.cursor()
		gsr_exe = cur_g.execute(q3, (t2_a, t1_a))
		rows_g = cur_g.fetchall()
		
		gsr_count1=0
		for i in rows_g:
			if(i[2][0:1]=='G'):
				#print(i[2][1:5])
				g = g + int(i[2][1:5])
				gsr_count1= gsr_count1+1
				#print(c)
		print(g/gsr_count1)
		avg_gsr = g/gsr_count1
		
		if((avg_gsr>z_g+150)|(avg_gsr<z_g-150)):
			str1 = "sweating"
			print(str1)
		else:
			str1 = "nosweating"
			print(str1)
		now = datetime.now()
		gg = """INSERT INTO gsr VALUES(%s,%s,%s)"""
		cur_g.execute(gg, (uid,now,str1))
		conn.commit()
		
		 
		 
		
		
		#conn.commit()
		
		# for temp
		conn = pymysql.connect(host='localhost', db='smartjacket_sensors', user='root')
		cur_t = conn.cursor()
		temp_exe = cur_t.execute(q3, (t2_a, t1_a))
		rows_t = cur_t.fetchall()	
		temp_count1=0
		for i in rows_t:
			if(i[2][0:1]=='T'):
				#print(i[2][1:5])
				#t = t + int(i[2][1:5])
				#temp_count1= temp_count1+1
				temp_count1 = int(i[2][1:5])
				#print(c)
		#print(t/temp_count1)
		#avg_tmp = t/temp_count1
		
		#if(avg_tmp<z_g):
		if(temp_count1<27):
			str1 = "lowtemp"
			print(str1)
		else:
			str1 = "normaltemp"
			print(str1)
		now = datetime.now()
		#avg_tmp=int(avg_tmp)
		tt = """INSERT INTO temperature VALUES(%s,%s,%s,%s)"""
		#cur_t.execute(tt, (uid,now,avg_tmp,str1))
		cur_t.execute(tt, (uid,now,temp_count1,str1))
		conn.commit()
		stop=stop+1
		if(stop>120):
			print("in if")
			break
		time.sleep(12)

	print("out of while accel")

class MyThread(Thread):
	def __init__(self, t_hb):
		print("hb called")
		Thread.__init__(self, target=hb)
		
	def run(self):
		Thread.run(self)
		
t1 = MyThread(hb) # register thread
t1.start()
accel()
t1.join()

	