import sqlite3
import env

def getDatabase():
	if env.APP_LIVE:
		return sqlite3.connect(env.LIVE_DATABASE)
	else:
		return sqlite3.connect(env.BUILD_DATABASE)
