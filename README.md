# twitter-bots

Collection of Twitter bots developed in Python for use on a [Raspberry Pi](raspberrypi.org). Scripts adapted from an article on [PiMyLifeUp](https://pimylifeup.com/raspberry-pi-twitter-bot/). Both scripts can be seen in action on my [Twitter feed](https://twitter.com/idlemachinery).

## Libraries

In addition to Python system libraries, the `Twython` Twitter-API wrapper library is used. Check out the [repo](https://github.com/ryanmcgrath/twython) and [documentation](https://twython.readthedocs.io/en/latest/).

## Features

### Emojis and Unicode

Emojis can be used in tweets if you specify their code in proper Unicode format.  For example, the code for the Robot emoji is listed as `U+1F916` so the Python code would look like:
```python
ROBOT_EMOJI = u'\U0001F916'
```

The full list of Unicode Emojis can be found [here](http://unicode.org/emoji/charts/full-emoji-list.html).

### Command Line Arguments

The `PromoBot` script has the ability to pass in arguments in order to switch between different promotional messages.  This allows you to set up multiple CRON jobs pointing at the same script to send out different tweets. 

### CPU Temperature and Time of Day

The `TemperatureBot` script can read the CPU temperature in Celcius and convert to Fahrenheit. I've included the Unicode symbol for both.  Also, it can determine the time of day:
+ 2am to 12pm is considered morning
+ Noon to 6pm is considered afternoon
+ 6pm to 2am is considered evening

## Usage

In order to use these scripts you must follow the first 4 steps under *Registering a Twitter app* on the[PiMyLifeUp tutorial](https://pimylifeup.com/raspberry-pi-twitter-bot/) to generate your keys and then enter them at the top of each script. You must also install python and twython, copy your scripts over and make them executable according to the instructions.  

Finally, follow the *Automating your Twitter Bot* instructions to set up a CRON job.  I have the `PromoBot` run once per day. The `TemperatureBot` runs 3 times per day at 6am, 2pm and 10pm so the CRON looks like this:
```
0 6,14,22 * * *
```
If you just wanted it to run at 15 minutes past the hour every 8 hours the CRON would look like:
```
15 */8 * * * 
```
The [Crontab Guru](https://crontab.guru) site is very helpful.

## Further Help

Clone, download, customize and enjoy! Contact me on [GitHub](https://github.com/idlemachinery) if you have any questions or find any bugs.
