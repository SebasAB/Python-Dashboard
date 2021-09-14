import serial 
from serial import Serial
import time 
import sqlite3 

conn = sqlite3.connect('DHT_DB.db')
c = conn.cursor() 

c.execute('CREATE TABLE IF NOT EXISTS Data(Humedad REAL, Tempratura REAL, Tiempo TEXT)')

serialArduino = Serial(port='COM2', baudrate = 9600, timeout=None) 


while True:
	data = serialArduino.readline().decode('utf-8')
	now = time.localtime()
	time_stamp = (str(now[3]) + ":" + str(now[4]) + ":" + str(now[5])) 
	data = data.split(",")
	hum = float(data[0])
	temp = float(data[1]) 
	hum = round(hum, 2)
	temp = round(temp, 2)

	c.execute('INSERT INTO Data (Humedad, Tempratura, Tiempo) VALUES (?, ?, ?)', (hum, temp, time_stamp)) 
	conn.commit() 
	time.sleep(1)















