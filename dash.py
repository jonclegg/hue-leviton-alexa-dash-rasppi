#!/usr/bin/python
from scapy.all import *
import hue
import config
import urllib2

def setLights( mode ):
    l = hue.Lights()
    l.connect()
    l.setLights( mode ) 
            
def arp_display(pkt):

    if pkt.haslayer(ARP):
        if pkt[ARP].hwsrc == config.gladMAC:
            print "Glad pressed, setting makeup"
            setLights('makeup')
        if pkt[ARP].hwsrc == config.angleSoftMAC:
            print "anglesoft pressed, setting tv"
            setLights('tv')
        if pkt[ARP].hwsrc == config.happyBellyMAC:
            print "happy belly pressed, setting off"
            setLights('off')
        if pkt[ARP].hwsrc == config.tideMAC:
            print "tide pressed, making bedroom COLD"
            urllib2.urlopen( config.iftttBase % ( "bedroom_64" ) ).read()

    # older dash buttons use llc instead arp
    if pkt.haslayer(Dot3):
        print "found: " + pkt[Dot3].src
        if pkt[Dot3].src == config.bountyMAC:
            print "Bounty pressed, setting relax"
            setLights('relax')

print "listening for dash buttons.."
print sniff(prn=arp_display, filter="arp or llc", store=0, count=0)

