from database import getDatabase
from export import exportSensorData

# start program
db = getDatabase()

# Here we export the data
exportSensorData(db)

db.commit()
db.close()
