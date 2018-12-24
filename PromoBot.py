#!/usr/bin/env python
import sys
from twython import Twython

# https://pimylifeup.com/raspberry-pi-twitter-bot/

# Define our constant variables, this is all the data we wrote down in the first part of the tutorial.
CONSUMER_KEY = '***************YOUR DATA*****************'
CONSUMER_SECRET = '***************YOUR DATA*****************'
ACCESS_KEY = '***************YOUR DATA*****************'
ACCESS_SECRET = '***************YOUR DATA*****************'

# Emojis - http://unicode.org/emoji/charts/full-emoji-list.html
GAMEPAD_EMOJI = u'\U0001F3AE'
JOYSTICK_EMOJI = u'\U0001F579'
ROBOT_EMOJI = u'\U0001F916'
GEAR_EMOJI = u'\U00002699'
ROCKET_EMOJI = u'\U0001F680'
FLOPPY_EMOJI = u'\U0001F4BE'

# Urls
SITE_URL = 'https://idlemachinery.com'
ARCADE_URL = 'https://arcade.idlemachinery.com'

# Define our other variables
msg = ''
hashtags = '#raspberrypi #diy #bot'
arg = ''

if len(sys.argv) > 1:
	arg = sys.argv[1]

if arg=='arcade':
	hashtags = '#indiegames #indiedev '+hashtags
	msg = 'I make games with @HaxeFlixel and @code! '+GAMEPAD_EMOJI+JOYSTICK_EMOJI+'\nFollow my journey: '+ARCADE_URL+'\n'+hashtags
else:
	hashtags = '#fullstack #code ' + hashtags
	msg = 'Make it work! '+FLOPPY_EMOJI+'\nFull Stack .NET Developer based in Richmond, VA.\nContact me: '+SITE_URL+'\n'+hashtags

# Create a copy of the Twython object with all our keys and secrets to allow easy commands.
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

# Send tweet
api.update_status(status=msg)
