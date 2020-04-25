from database import getDatabase
from export import exportSensorData

# start program
db = getDatabase()

db.execute("INSERT INTO bme280 (temperature, humidity, pressure) VALUES(22,24,45)")

exportSensorData(db)

db.commit()
db.close()
