# Is the App Live ?
APP_LIVE = False


# Database details
LIVE_DATABASE = ''
BUILD_DATABASE = 'database.sqlite'


# Device objects are
#  key = I/O location for the Pi to find it
#  value = MyHome device list identifier

# BME280 Devices
LIVE_BME280_DEVICES = {
	'76': 1
}
BUILD_BME280_DEVICES = {}

# DHT22 Devices
LIVE_DHT22_DEVICES = {
	4: 2
}
BUILD_DHT22_DEVICES = {}


# API Details
LIVE_HTTP_URI = ''
BUILD_HTTP_URI = 'http://localhost:8000/api/home/reading'

LIVE_TOKEN = ''
BUILD_TOKEN = 'eyJ0eXAiOifKV1QiLCJhbGcaOiJSUzI1NiJ9.......'


LIVE_TEST_DATA = True

