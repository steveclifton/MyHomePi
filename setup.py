import env
import database

# First create the database records
db = database.getDatabase()

try:
    db.execute('''CREATE TABLE IF NOT EXISTS bme280
           (ID INTEGER PRIMARY KEY AUTOINCREMENT,
           temperature REAL NOT NULL,
           humidity REAL NOT NULL,
           pressure REAL NOT NULL,
           deviceid INTEGER NOT NULL,
           created TIMESTAMP NOT NULL,
           exported INT DEFAULT 0);''')

    db.execute('''CREATE TABLE IF NOT EXISTS errorlogs
           (ID INTEGER PRIMARY KEY AUTOINCREMENT,
           log TEXT NOT NULL,
           deviceid INTEGER NOT NULL,
           created TIMESTAMP NOT NULL,
           exported INT DEFAULT 0);''')

except Exception as e:
    print(e)
    returnStatus = False


db.commit()
db.close()
