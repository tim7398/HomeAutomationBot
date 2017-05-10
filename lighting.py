#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

def lightStatus(): # future implementation
	print("light status")
	response = requests.get("http://10.0.0.121/api/CchUsx3OQjX3HhayzdEtm6jtluO0Ze6p4Z4Ol5dz/lights/1")
	print(response)
	lightStatus=json.loads(response.content)
	state = lightStatus['state']['on']
	print("state: ", state)
	
	if state == False:
		print ("lights off")
	else:
		print("lights on")

	


def lightsOn(light): #execute the command 
	payload = {"on":True}
	if light == "all":
		for i in range(1,3):
			api = "http://10.0.0.121/api/CchUsx3OQjX3HhayzdEtm6jtluO0Ze6p4Z4Ol5dz/lights/"+str(i)+"/state"
			response = requests.put(api, json.dumps(payload))
			print"turn on ", i
			print (response)
			print (json.loads(response.content))
	else:
		api = "http://10.0.0.121/api/CchUsx3OQjX3HhayzdEtm6jtluO0Ze6p4Z4Ol5dz/lights/"+light+"/state"
		response = requests.put(api, json.dumps(payload))
		print"turn on ", light
		print (response)
		print (json.loads(response.content))
	
def lightsOff(light): #turn lights off
	payload = {"on":False}
	if(light == "all"):
		for i in range(1,3):
			api = "http://10.0.0.121/api/CchUsx3OQjX3HhayzdEtm6jtluO0Ze6p4Z4Ol5dz/lights/"+str(i)+"/state"
			response = requests.put(api, json.dumps(payload))
			print"turn off " , i
			print (response)
			print (json.loads(response.content))


	else:
		api = "http://10.0.0.121/api/CchUsx3OQjX3HhayzdEtm6jtluO0Ze6p4Z4Ol5dz/lights/"+light+"/state"
		response = requests.put(api, json.dumps(payload))
		print"turn off " , light
		print (response)
		print (json.loads(response.content))
