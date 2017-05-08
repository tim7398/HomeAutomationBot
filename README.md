# AWS Home Automation Bot
This is a home automation program that can control smart devices around the house. Currently it only controls philips hue smart lights, but the functionality will improve as I get more smart devices. This program is hosted on AWS Lambdas services and interacts with the Telegram API. 

# How this works

This uses the AWS lambdas/AWS API-Gateway services to interact with the Telegram Bot API to make a serverless chatbot. The chatbot serves as a central hub that controls all the various smart devices in the users home. Currently it only supports the Philips Hue Lights, but it will support more smart devices as I obtain them. 

# Accepted Commands
1) Lights on. 
    * turns on the lights
2) Lights off.
    * turns off the lights
3) /help
    * gives the user a list of commands
    

# Bot Responses
1) Not a valid command
    * Tells the user the command they issued is not valid.
2) Echos the command
    * confirms that the issued command has been successfully completed. 



# Future additions
1) DynamoDB database to store different users in the home and state of smart devices.
2) command for state of smart device.
3) ability to add new users to give the bot commands.
    1) privilages to control only some or all devices in the home.
4) Make the bot more flexible to take in variations of a command. Turn the lights on, the lights should be turned on, etc should all be acceptable inputs. 
