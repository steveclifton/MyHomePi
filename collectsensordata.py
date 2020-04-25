from database import getDatabase
from bme280sensor import collectSensorData

# Program start
db = getDatabase()

collectSensorData(db)

db.commit()
db.close()
