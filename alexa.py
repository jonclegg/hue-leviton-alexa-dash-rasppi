#!/usr/bin/python

import time
import urllib2
from flask import Flask
from flask_ask import Ask, statement
import hue

# Prints if light 1 is on or not

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def intro():
    return statement("You can set modes tv, dim, bright or superbright")

@ask.intent("TVMode")
def TVMode( mode ):
    print "mode: %s" % (mode)
    if mode == "TV" or mode == "V":
        hue.setLights("tv")
    elif mode == "dim" or mode == "dinner" or mode =="mild" or mode == "relax":
        hue.setLights("mild")
    elif mode == "bright":
        hue.setLights("bright")
    elif mode == "super bright":
        hue.setLights("superbright")
    else:
        return statement("unknown mode")

    return statement("%s Mode set" % (mode) )


def waitForNetwork():
    while True:
	try:
            print "checking internet.."
            time.sleep(1)
	    answ = urllib2.urlopen("http://www.google.com")
	    if answ:
                print "internet up"
                break
	except Exception,e : print e

waitForNetwork()

if __name__ == '__main__':
    app.run()

