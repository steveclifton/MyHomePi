from database import getDatabase
from sensor_bme280 import collectBME280SensorData
from sensor_dht22 import collectDHT22SensorData
from export import exportSensorData


# Program start
db = getDatabase()


# Collect Data
collectBME280SensorData(db)
collectDHT22SensorData(db)


# Here we export the data
exportSensorData(db)


# Finish
db.commit()
db.close()