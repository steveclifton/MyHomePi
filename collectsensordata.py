from database import getDatabase
from sensor_bme280 import collectSensorData

# Program start
db = getDatabase()

collectBME280SensorData(db)

collectDHT22SensorData(db)

db.commit()
db.close()
