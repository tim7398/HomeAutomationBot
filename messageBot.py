#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json


apiCall = "https://api.telegram.org/{YOUR BOT TOKEN}"

static_commands = {'lights on', 'lights off', '/help'}
userList = {'{YOUR USER CHAT ID}'} # can get this by sending the bot a message and looking at the http endpoint url

def ChatBot(event, context): # event holds the content of the messages
	print("Received event: " + json.dumps(event, indent=2))
	
	parse_message(event)
	print("event ends")
	return {'statusCode': 200, 'headers': { 'Content-Type': 'application/json' },'body': 'successful'} # confirm event occurred successfully
	

def get_url(url): #interacts with the HTTP endpoint 
	response = requests.get(url)
	urlContent = response.content
	return urlContent


def parse_message(update): # parses the message 

	text = update["message"]["text"] #gets the message
	chatId = update["message"]["chat"]["id"] #unique chat id
	
	if str(chatId) not in userList: # only grands access to specific users
	    print "Unauthorized Access ", chatId
	    text = "Unauthorized Access"
	
	elif text.lower() not in static_commands:
	    text = "not a valid command"
	
	elif text.lower() == '/help':
	    text = "The current valid commands, \n 1) lights on \n 2) lights off"
	
	elif text.lower() == 'lights on':
	    lightsOn() # add to this later
	    text = "The lights are now on"
	
	elif text.lower() == 'lights off':
	    lightsOff()
	    text = "The lights are now off"
	    
	    
	
	send_Message(text, chatId)
		

def send_Message(text, chatId): # sets up the send url
	sendUrl = apiCall +"/sendMessage?chat_id={}&text={}".format(chatId,text)
	get_url(sendUrl)
	
def lightsOn(): #add to this later
    print("lights turn on")

def lightsOff(): #add to this later
    print("lights turn off")

if __name__ == '__main__': #only if not imported by another script
	main()