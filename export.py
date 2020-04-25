import requests
import env

def exportSensorData(db):

	cur = db.cursor()

	cur.execute("SELECT * FROM bme280 WHERE exported = 0")
	rows = cur.fetchall()

	uploadData = []
	for row in rows:
		data = {
			'id' : row[0],
			'temperature' : row[1],
			'humidity' : row[2],
			'pressure' : row[3],
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

	# Check we have a successful post
	if response.status_code == 200:
		for dataVal in uploadData:
			cur.execute('UPDATE bme280 SET exported = 1 WHERE id = ?', (dataVal.get('id'),))
		return True

	# Token has expirted, do something
	elif response.status_code == 401:
		errorMsg = response.json().get('message')
        cur.execute("INSERT INTO errorlogs (log) VALUES(?)", (errorMsg,))
        return False


	cur.execute("INSERT INTO errorlogs (log) VALUES(?)", (response.text,))
	return False;

