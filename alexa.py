#!/usr/bin/python

import time
import sys
import urllib2
from flask import Flask
from flask_ask import Ask, statement
import hue

# Prints if light 1 is on or not

app = Flask(__name__)
ask = Ask(app, '/')

aport = int(sys.argv[1])
amode = sys.argv[2]

@ask.launch
def intro():
    global amode
    print "setting lights to " + amode
    l = hue.Lights()
    l.connect()
    l.setLights(amode)
    return statement("%s mode set" % amode)

if __name__ == '__main__':
    print "running on port %d mode %s" % ( aport, amode)
    app.run( host='0.0.0.0', port=aport)

