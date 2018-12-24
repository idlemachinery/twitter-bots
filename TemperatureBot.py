#!/usr/bin/env python
import os
import time
from twython import Twython

# https://pimylifeup.com/raspberry-pi-twitter-bot/

# Define our constant variables, this is all the data we wrote down in the first part of the tutorial.
CONSUMER_KEY = '***************YOUR DATA*****************'
CONSUMER_SECRET = '***************YOUR DATA*****************'
ACCESS_KEY = '***************YOUR DATA*****************'
ACCESS_SECRET = '***************YOUR DATA*****************'


# Emojis - http://unicode.org/emoji/charts/full-emoji-list.html
ROBOT_EMOJI = u'\U0001F916'
DEGREE_SYMBOL = u'\U000000B0'
DEGREE_FAHRENHEIT = u'\U00002109'
DEGREE_CELCIUS = u'\U00002103'

# Define our other variables
msg = ''
greet = ''
hashtags = '#raspberrypi #diy #bot'
timestamp = 'At '+time.strftime("%I:%M%p %Z")+' on '+time.strftime("%m/%d/%Y")
hour = int(time.strftime("%H"))

# Evening starts at 6pm
if hour >= 18:
	greet = 'Good evening'
# Afternoon starts at 12pm
elif hour >= 12:
	greet = 'Good afternoon'
# Morning starts at 2am
elif hour >= 2:
	greet = 'Good morning'
else:
	greet = 'Good evening'  

# Get CPU temperature
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]
fahrenheit = str(9.0/5.0 * int(float(temp)) + 32)

# Construct message
msg = 'Hello world! '+greet+' from the Idle Machinery Twitter bot on Raspberry Pi. '+timestamp+' my CPU temperature is '+fahrenheit+DEGREE_FAHRENHEIT+'.\n'+hashtags

# Create a copy of the Twython object with all our keys and secrets to allow easy commands.
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

# Send tweet 
api.update_status(status=msg)
