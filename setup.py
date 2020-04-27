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
           created TIMESTAMP NOT NULL,
           exported INT DEFAULT 0);''')

    db.execute('''CREATE TABLE IF NOT EXISTS errorlogs
           (ID INTEGER PRIMARY KEY AUTOINCREMENT,
           log TEXT NOT NULL,
           created TIMESTAMP NOT NULL,
           exported INT DEFAULT 0);''')

    # Migration to add deviceid
    db.execute('''ALTER TABLE bme280
      ADD deviceid INTEGER NOT NULL DEFAULT 0
      ''')
    db.execute('''ALTER TABLE errorlogs
      ADD deviceid INTEGER NOT NULL DEFAULT 0
      ''')
    # End Migration

except Exception as e:
    print(e)
    returnStatus = False


db.commit()
db.close()
