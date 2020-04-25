from database import getDatabase
from export import exportSensorData

# start program
db = getDatabase()

# Change this to True if you want to test inserting random data to try export
if False:
	db.execute("INSERT INTO bme280 (temperature, humidity, pressure) VALUES(23,33,44)")

exportSensorData(db)

db.commit()
db.close()
