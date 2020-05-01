from database import getDatabase
from sensor_bme280 import collectBME280SensorData
from sensor_dht22 import collectDHT22SensorData

# Program start
db = getDatabase()

collectBME280SensorData(db)

collectDHT22SensorData(db)

db.commit()
db.close()
