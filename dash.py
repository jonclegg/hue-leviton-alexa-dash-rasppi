#!/usr/bin/python
from scapy.all import *
import hue


def arp_display(pkt):
    pkt.show()
    if pkt.haslayer(Dot3):
        if pkt[Dot3].src == config.bountyMAC:
            print "Bounty pressed, setting relax"
            l = hue.Lights()
            l.connect()
            l.setLights('relax')

print "listening for dash buttons.."
print sniff(prn=arp_display, filter="llc", store=0, count=0)

