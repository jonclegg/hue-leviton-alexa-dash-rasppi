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

@ask.intent("LightMode")
def TVMode( mode ):
    l = hue.Lights()
    l.connect()
    print "mode: %s" % (mode)
    if mode == "TV" or mode == "V":
        l.setLights("tv")
    elif mode == "dim" or mode == "dinner" or mode =="mild" or mode == "relax":
        l.setLights("relax")
    elif mode == "bright" or mode == "brand" or mode == "right":
        l.setLights("bright") 
    elif mode == "normal":
        l.setLights("normal")
    elif mode == "off":
        l.setLights("off")
    elif mode == "reading" or mode == "most":
        l.setLights("reading")
    else:
        print "unknown mode: " + mode
        return statement("unknown mode " + mode)

    return statement("%s Mode set" % (mode) )

#    return statement("<speak>Can you believe it?<emphasis level=\"strong\">really like</emphasis></speak>")

if __name__ == '__main__':
    app.run()

