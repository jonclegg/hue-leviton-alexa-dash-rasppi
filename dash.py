#!/usr/bin/python
from scapy.all import *
import hue

bountyMAC = "f0:27:2d:3a:25:a7"

def arp_display(pkt):
    pkt.show()
    if pkt.haslayer(Dot3):
        if pkt[Dot3].src == bountyMAC:
            print "Bounty pressed, setting dim"
            l = hue.Lights()
            l.connect()
            l.setLights('mild')

print "listening for dash buttons.."
print sniff(prn=arp_display, filter="llc", store=0, count=0)

