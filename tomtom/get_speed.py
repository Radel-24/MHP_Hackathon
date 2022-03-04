from urllib import response
from attr import define
import requests
import json
import sys
from dotenv import load_dotenv
import os


def getSpeed(key, x, y):
	url = 'https://api.tomtom.com/traffic/services/4/flowSegmentData/relative0/10/json?point={}%2C{}&unit=KMPH&openLr=false&key={}'.format(x, y, key)
	try:
		response =  requests.get(url)
		text = response.json()
		return text.get('flowSegmentData').get('currentSpeed')
	except:
		return -1


#load .env file
load_dotenv()

if len(sys.argv) != 3:
	print('Wrong usage, usage: python3 get_speed.py [x-coordinate] [y-coordinate]')
	exit(1)

#set key to envioren variable API_KEY (either from .env file or env list)
key = os.environ['API_KEY']

#get speed at x and y coordinate
speed = getSpeed(key=key, x=float(sys.argv[1]), y=float(sys.argv[2]))
print(speed)