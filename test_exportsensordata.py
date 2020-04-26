from database import getDatabase
from export import exportSensorData
import env
import datetime

# start program
db = getDatabase()

# Change this to True if you want to test inserting random data to try export
if env.LIVE_TEST_DATA:
	currentDT = datetime.datetime.now()
	dateTime = currentDT.strftime("%Y-%m-%d %H:%M:%S")
	db.execute("INSERT INTO bme280 (temperature, humidity, pressure, created) VALUES(23, 50.5, 1002, ?)", [dateTime])

# Here we export the data
exportSensorData(db)

db.commit()
db.close()
