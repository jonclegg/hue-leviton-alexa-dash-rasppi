#!/usr/bin/python

from phue import Bridge
import time
import urllib2
from flask import Flask
from flask_ask import Ask, statement
import sys


class Lights:
    kitchenLights = [1, 2, 4, 7]
    livingRoomLights = [ 3, 5, 6, 8 ]
    diningRoomLights = [9, 10]
    lightModes = {
            'tv': [0, 30, 0, 10],
            'mild': [60, 130, 150, 15],
            'bright': [150, 200, 200, 20],
            'superbright': [255, 255, 255, 30],
    }
    hueBridge = None

    def setTable( self, trigger ):
        iftttBase = "https://maker.ifttt.com/trigger/%s/with/key/bq9qMhMP4LmWQu0SwhNPgk"
        urllib2.urlopen( iftttBase % ( trigger ) ).read()

    def connect(self ):
        self.hueBridge = Bridge('192.168.40.156')
        self.hueBridge.connect()
        self.hueBridge.get_api()

    def setSection( self, section, brightness ):
        for light in section:
            if brightness == 0:
                self.hueBridge.set_light( light, 'on', False)
            else:
                self.hueBridge.set_light( light, 'on', True)
                self.hueBridge.set_light( light, 'bri', brightness)

    def setLights( self, mode ):
        self.setSection( self.livingRoomLights, self.lightModes[mode][0] )
        self.setSection( self.kitchenLights, self.lightModes[mode][1] )
        self.setSection( self.diningRoomLights, self.lightModes[mode][2] )
        self.setTable( "table_%d" % ( self.lightModes[mode][3]) )


def main():
    if len( sys.argv ) != 2:
        print "usage: hue [mode]"
        return

    mode = sys.argv[1]

    l = Lights()
    l.connect()
    l.setLights(mode)
    print "lights set to " + mode

if __name__ == '__main__':
    main()
