#!/usr/bin/python
from scapy.all import *
import hue
import config
import urllib2

def setLights( mode ):
    l = hue.Lights()
    l.connect()
    l.setLights( mode ) 
        
lastTime = 0
lastMAC = ""

def arp_display(pkt):
    global lastTime
    global lastMAC

    if pkt.haslayer(ARP):
        curMAC = pkt[ARP].hwsrc
        if not curMAC in config.dashMACs:
            return

        buttonName = config.dashMACs[curMAC]
        print "found: " + curMAC
        print "name: " + buttonName

        diff = time.time() - lastTime
        if pkt[ARP].hwsrc == lastMAC and diff < 5:
           print "i've seen this before delta: %d" % ( diff )
           print "ignoring 2nd arp"
           return

        lastTime = time.time()
        lastMAC = pkt[ARP].hwsrc
        print "accepting " + lastMAC

        if buttonName == 'tideMAC':
            urllib2.urlopen( config.iftttBase % ( "bedroom_64" ) ).read()
        if buttonName == 'tropicanaMAC':
            setLights('makeup')
        if buttonName == 'angleSoftMAC':
            setLights('tv')
        if buttonName == 'happyBellyMAC':
            setLights('off')
        if buttonName == 'cascadeMAC':
            setLights('')
        if buttonName == 'natureValleyMAC':
            setLights('reading')
        if buttonName == 'milanoMAC':
            #setLights('normal')
            setLights('relax')
        if buttonName == 'ethicalBeanMAC':
            #setLights('relax')
            setLights('normal')
        if buttonName == 'adamiaMAC':
            urllib2.urlopen( config.iftttBase % ( "hallway_72" ) ).read()
        if buttonName == 'ampMAC':
            print "setting tv mode"
            os.system( "/home/pi/dev/tv_dim_and_sleep.sh &" )

    # older dash buttons use llc instead arp
    """
    if pkt.haslayer(Dot3):
        print "found: " + pkt[Dot3].src
        if pkt[Dot3].src == config.bountyMAC:
            setLights('relax')
            """

print "listening for dash buttons.."
print sniff(prn=arp_display, filter="arp or llc", store=0, count=0)

