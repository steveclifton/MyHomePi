import Adafruit_DHT
import time
import datetime
import env

DHT_SENSOR = Adafruit_DHT.DHT22

def collectDHT22SensorData(db):

	currentDT = datetime.datetime.now()
	dateTime = currentDT.strftime("%Y-%m-%d %H:%M:%S")

	if env.APP_LIVE:
	    devices = env.LIVE_DHT22_DEVICES
	else:
	    devices = env.BUILD_DHT22_DEVICES

	for deviceid, name in devices.items():

		for x in range(5):
			try:
			    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, int( deviceid ))

			    if humidity is not None and temperature is not None:
			        query = "INSERT INTO readings (temperature, deviceid, created) VALUES({0:0.2f}, ?, ?)".format(temperature)
			        db.execute(query, [ int(deviceid) , dateTime])
			        db.commit()
			        query = "INSERT INTO readings (humidity, deviceid, created) VALUES({0:0.2f}, ?, ?)".format(humidity)
			        db.execute(query, [ int(deviceid) , dateTime])
			        db.commit()
			        break

			except Exception as e:
				errorMsg = str(e)
				db.execute("INSERT INTO errorlogs (log, deviceid, created) VALUES(?, ?, ?)", [errorMsg, int(deviceid), dateTime])
				db.commit()

        	# Sleep for 2s to allow the sensor to regenerate data
			time.sleep(2);
	    #end for

	#end for

#end Function
