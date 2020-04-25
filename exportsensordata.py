from database import getDatabase
from export import exportSensorData
import env

# start program
db = getDatabase()

# Change this to True if you want to test inserting random data to try export
if env.LIVE_TEST_DATA:
	db.execute("INSERT INTO bme280 (temperature, humidity, pressure) VALUES(23,33,44)")

exportSensorData(db)

db.commit()
db.close()
