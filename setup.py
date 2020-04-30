import env
from database import Database

# First create the database records
database = Database()
db = database.getDatabase()

try:
    db.execute('''
                CREATE TABLE IF NOT EXISTS `temperature`
                (id INT PRIMARY KEY,
                temperature REAL NOT NULL,
                deviceid INTEGER NOT NULL,
                created DATETIME,
                exported TINYINT default '0');
                ''')

    db.execute('''
                CREATE TABLE IF NOT EXISTS `humidity`
                (id INT PRIMARY KEY,
                humidity REAL NOT NULL,
                deviceid INTEGER NOT NULL,
                created DATETIME,
                exported TINYINT default '0');
                ''')

    db.execute('''
                CREATE TABLE IF NOT EXISTS `pressure`
                (id INT PRIMARY KEY,
                pressure REAL NOT NULL,
                deviceid INTEGER NOT NULL,
                created DATETIME,
                exported TINYINT default '0');
                ''')

    db.execute('''CREATE TABLE IF NOT EXISTS errorlogs
           (ID INTEGER PRIMARY KEY AUTOINCREMENT,
           log TEXT NOT NULL,
           created TIMESTAMP NOT NULL,
           exported INT DEFAULT 0);''')



except Exception as e:
    print(e)
    returnStatus = False


db.commit()
db.close()
