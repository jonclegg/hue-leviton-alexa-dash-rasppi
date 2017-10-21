#!/usr/bin/python

from phue import Bridge
import time
import urllib2
from flask import Flask
from flask_ask import Ask, statement
import sys
import config

class Lights:
    kitchenLights = [1, 2, 4, 7, 13]
    livingRoomLights = [ 3, 5, 6, 8, 14 ]
    diningRoomLights = [9, 10]
    hallwayRoomLights = [11]
    lightModes = {
            'tv':        [  0,  30,   0,  0,  0],
            'relax':     [ 60, 130, 150, 30, 15],
            'normal':    [150, 200, 200, 50, 16],
            'reading':   [150, 200, 200, 50, 25],
            'bright':    [255, 255, 255, 200,30],
            'makeup':    [255, 155, 155, 50, 16],
            'off':       [  0,   0,   0,  0,  0]
    }
    hueBridge = None

    def setTable( self, trigger ):
        urllib2.urlopen( config.iftttBase % ( trigger ) ).read()

    def connect(self ):
        self.hueBridge = Bridge(config.hueBridgeIP)
        self.hueBridge.connect()
        self.hueBridge.get_api()

    def setLight( self, light, brightness ):
        self.hueBridge.set_light( light, 'bri', brightness)

    def setSection( self, section, brightness ):
        for light in section:
            if brightness == 0:
                print "setting %d off" % ( light )
                self.hueBridge.set_light( light, 'on', False)
            else:
                self.hueBridge.set_light( light, 'on', True)
                self.hueBridge.set_light( light, 'bri', brightness)

    def setLights_int( self, mode ):
        self.setTable( "table_%d" % ( self.lightModes[mode][4]) )
        self.setSection( self.livingRoomLights, self.lightModes[mode][0] )
        self.setSection( self.kitchenLights, self.lightModes[mode][1] )
        self.setSection( self.diningRoomLights, self.lightModes[mode][2] )
        self.setSection( self.hallwayRoomLights, self.lightModes[mode][3] )
        
    def setLights( self, mode ):
        print "setting lights to: " + mode
        for i in range(1,3):
            self.setLights_int( mode )
            time.sleep(1)
        if mode == 'makeup':
            urllib2.urlopen( config.iftttBase % ( "hallway_72" ) ).read()

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
