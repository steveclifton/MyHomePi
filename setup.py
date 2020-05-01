import env
import database

# First create the database records
db = database.getDatabase()

try:

    # Migration to add reading table
    db.execute('''
          CREATE TABLE IF NOT EXISTS readings
           (ID INTEGER PRIMARY KEY AUTOINCREMENT,
           key TEXT NOT NULL,
           value REAL NOT NULL,
           deviceid INTEGER NOT NULL DEFAULT 0,
           created TIMESTAMP NOT NULL,
           exported INT DEFAULT 0);
           ''')

    # End Migration

    # Migration to add reading table
    db.execute('''
          CREATE TABLE IF NOT EXISTS readings
           (ID INTEGER PRIMARY KEY AUTOINCREMENT,
           key TEXT NOT NULL,
           value REAL NOT NULL,
           deviceid INTEGER NOT NULL DEFAULT 0,
           created TIMESTAMP NOT NULL,
           exported INT DEFAULT 0);
           ''')
    # End Migration

except Exception as e:
    print(e)
    returnStatus = False


db.commit()
db.close()
