import sqlite3
import env

class Database:

	def __INIT__(self):

		if env.APP_LIVE:
			self.db = sqlite3.connect(env.LIVE_DATABASE)
		else:
			self.db = sqlite3.connect(env.BUILD_DATABASE)

	def getDatabase():
		if env.APP_LIVE:
			return sqlite3.connect(env.LIVE_DATABASE)
		else:
			return sqlite3.connect(env.BUILD_DATABASE)


	# Map of values to add
	def logReading(self, table, deviceid, reading):

		currentDT = datetime.datetime.now()
		dateTime = currentDT.strftime("%Y-%m-%d %H:%M:%S")

		try:
			query = "INSERT INTO `{table}` ({col}, deviceid, created) VALUES({val:0.2f}, ?, ?)".format(table=table, col=table, val=reading)
			db.execute(query, [ int(deviceid) , dateTime])

		except Exception as e:
			errorMsg = str(e)
			db.execute("INSERT INTO errorlogs (log, deviceid, created) VALUES(?, ?, ?)", [errorMsg, int(deviceid), dateTime])

		return True




