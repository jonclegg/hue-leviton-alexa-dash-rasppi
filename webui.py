#!/usr/bin/python
from bottle import post, route, request, run
import os
import hue
import config
import urllib2

@route('/')
@route('/', method='POST')
def release_control():
    l = hue.Lights()
    if request.method == 'POST':
         l.connect()

    if (request.POST.get("tv")):
         l.setLights("tv")
    if (request.POST.get("relax")):
         l.setLights("relax")
    if (request.POST.get("normal")):
         l.setLights("normal")
    if (request.POST.get("off")):
         l.setLights("off")
    if (request.POST.get("bedroom64")):
         urllib2.urlopen( config.iftttBase % ( "bedroom_64" ) ).read()
    if (request.POST.get("hallway72")):
         urllib2.urlopen( config.iftttBase % ( "hallway_72" ) ).read()
    if (request.POST.get("hallway74")):
         urllib2.urlopen( config.iftttBase % ( "hallway_74" ) ).read()
    if (request.POST.get("hallway76")):
         urllib2.urlopen( config.iftttBase % ( "hallway_76" ) ).read()

    return """
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <form method="POST" action="/">
        <div id="content"><p><input id="submit" name="tv" type="submit" value="TV"></p>
        <div id="content"><p><input id="submit" name="relax" type="submit" value="Relax"></p>
        <div id="content"><p><input id="submit" name="normal" type="submit" value="Normal"></p>
        <div id="content"><p><input id="submit" name="off" type="submit" value="Off"></p>
        <div id="content"><p><input id="submit" name="bedroom64" type="submit" value="Bedroom 64"></p>
        <div id="content"><p><input id="submit" name="hallway72" type="submit" value="Hallway 72"></p>
        <div id="content"><p><input id="submit" name="hallway74" type="submit" value="Hallway 74"></p>
        <div id="content"><p><input id="submit" name="hallway76" type="submit" value="Hallway 76"></p>
     </form></div>
     <style>
         body {
         font: 15px/25px 'Fira Sans', sans-serif;
         }
         #content {
         margin: 0px auto;
         text-align: center;
         }
         #submit {
         width: 11em;  height: 2em;
         background: rgb(66, 184, 221);
         border-radius: 5px;
         color: #fff;
         font-family: 'Fira Sans', sans-serif;
         font-size: 25px;
         font-weight: 900;
         text-shadow: 0 1px 1px rgba(0, 0, 0, 0.2);
         letter-spacing: 3px;
         border:none;
         }
     </style>"""
run(host="0.0.0.0",port=5001, debug=True)

