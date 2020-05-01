import requests
import env
import datetime

def exportSensorData(db):

	cur = db.cursor()

	cur.execute("SELECT * FROM readings WHERE exported = 0")
	rows = cur.fetchall()

	uploadData = []
	uploadIds = []
	for row in rows:

		# Add the record id
		uploadIds.append(row[0])

		# 1|temperature|22.14|76|2020-05-01 19:03:58|0

		data = {
			'key'      : row[1],
			'value'    : row[2],
			'deviceid' : row[3],
			'created'  : row[4],
		}
		uploadData.append(data)

	# Make sure we have something to send
	if len(uploadData) <= 0:
		print('Nothing to do')
		return False

	# Setup request data
	url = env.LIVE_HTTP_URI if env.APP_LIVE else env.BUILD_HTTP_URI
	token = env.LIVE_TOKEN if env.APP_LIVE else env.BUILD_TOKEN

	response = requests.post(
		url,
		json={'data': uploadData},
		headers={'Authorization': 'Bearer ' + token, 'Accept': 'application/json'}
	)

	currentDT = datetime.datetime.now()
	dateTime = currentDT.strftime("%Y-%m-%d %H:%M:%S")

	# Check we have a successful post
	if response.status_code == 200:
		for recordId in uploadIds:
			cur.execute('UPDATE reading SET exported = 1 WHERE id = ?', [recordId])
		return True

	# Token has expirted, do something
	elif response.status_code == 401 or response.status_code == 429:
		errorMsg = response.json().get('message')
		cur.execute("INSERT INTO errorlogs (log, created) VALUES(?, ?)", [errorMsg, dateTime])
		return False


	cur.execute("INSERT INTO errorlogs (log, created) VALUES(?, ?)", [str(response.text), dateTime])
	return False;
