# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
import json
import urllib

import lighting
# Custom MQTT message callback
def customCallback(client, userdata, message):
	print("Received a new message: ")
	print(message.payload)
	js = json.loads(message.payload)
	if js['on'] == True:
		
		lighting.lightsOn(js['light'])
		
		print("True")
	else:
		lighting.lightsOff(js['light'])
		print("False")
	print("from topic: ")
	print(message.topic)
	print("--------------\n\n")


while True:
	try:
		file = urllib.urlopen('http://google.com');
		print('Connect');
		break;
	
	except:
		print('No connect');
		time.sleep(3);


# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("RaspberryPi")
# For Websocket connection
# myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
# Configurations
# For TLS mutual authentication
myMQTTClient.configureEndpoint("afcywtkpbovht.iot.us-east-1.amazonaws.com", 8883)
# For Websocket
# myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
myMQTTClient.configureCredentials("/home/pi/deviceSDK/certs/root-CA.crt", "/home/pi/deviceSDK/certs/312b67f390-private.pem.key", "/home/pi/deviceSDK/certs/312b67f390-certificate.pem.crt")
# For Websocket, we only need to configure the root CA
# myMQTTClient.configureCredentials("YOUR/ROOT/CA/PATH")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

myMQTTClient.connect()

myMQTTClient.subscribe("PhilipsLight", 1, customCallback)
print("subscribe successful")
while True:
	
	time.sleep(1)

