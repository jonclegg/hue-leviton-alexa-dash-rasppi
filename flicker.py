from time import sleep
from random import randint
import hue

class LightFade:
   step = 0
   end = 0
   currentVal = 0
   hue = 0
   light = 0

   def __init__( self, _light ):
       self.hue = hue.Lights()
       self.hue.connect()
       self.light = _light

   def setup( self, _step, _end ):
       self.step = _step;
       self.end = _end;
   
   def doStep( self ):
       self.currentVal += self.step

       if self.step > 0 and self.currentVal >= self.end:
           return False
       elif self.step < 0 and self.currentVal <= self.end:
           return False

       return True

   def setupNewRange( self ):
       self.step = randint( 20, 50  )
       self.end = randint( 1, 250 )

       if self.currentVal > self.end:
           self.step = -self.step
       #print "New range: %d %d" % (self.step, self.end )

   def tick( self ):
       if self.step == 0 or self.doStep() == False:
           self.setupNewRange()
       #print "light %d = %d" % (self.light, self.currentVal )
       self.hue.setLight( self.light, self.currentVal )       

livingRoomLights = [ 3, 5, 6, 8, 14, 9, 10 ]
lightFades = []
for l in livingRoomLights:
  lightFades.append( LightFade( l )  )

while True:
    for l in lightFades:
      l.tick()
    sleep(0.05)



       
