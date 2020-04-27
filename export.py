import requests
import env
import datetime

def exportSensorData(db):

	cur = db.cursor()

	cur.execute("SELECT * FROM bme280 WHERE exported = 0")
	rows = cur.fetchall()

	uploadData = []
	uploadIds = []
	for row in rows:

		if env.APP_LIVE == False:
			print(row)

		# Add the record id
		uploadIds.append(row[0])

		data = {
			'temperature' : row[1],
			'humidity' : row[2],
			'pressure' : row[3],
			'deviceid' : row[6],
			'created' : row[4],
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
			cur.execute('UPDATE bme280 SET exported = 1 WHERE id = ?', [recordId])
		return True

	# Token has expirted, do something
	elif response.status_code == 401 or response.status_code == 429:
		errorMsg = response.json().get('message')
		cur.execute("INSERT INTO errorlogs (log, created) VALUES(?, ?)", [errorMsg, dateTime])
		return False


	cur.execute("INSERT INTO errorlogs (log, created) VALUES(?, ?)", [str(response.text), dateTime])
	return False;
