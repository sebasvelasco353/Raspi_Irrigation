#!/usr/bin/env python
# encoding: utf-8
import RPi.GPIO as GPIO
import json
import time
from flask import Flask

app = Flask(__name__)

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print("no water")
    else:
        print("water")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)


@app.route('/')
def index():
    print(GPIO.input(channel))
    return json.dumps({'humidity': not(GPIO.input(channel)), 'status': 200})

app.run(host='0.0.0.0', port= 8090)
