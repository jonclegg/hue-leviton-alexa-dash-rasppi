from time import sleep


class LightFade:
   step = 0
   end = 0
   currentVal = 0
   
   def setup( self, _step, _end ):
       self.step = _step;
       self.end = _end;
   
   def doStep( self ):
       self.currentVal += step

       if self.step > 0 and self.currentVal >= end:
           return False
       elif self.step < 0 and self.currentVal <= end:
           return False

       return True

   def setupNewRange( self ):
       self.step = randint( 1, 20 )
       self.end = randint( 10, 250 )

       if self.currentVal > self.end:
           self.step = -self.step

   def tick( self ):
       if self.doStep() == False:
           self.setupNewRange()
        

l = LightFade()
while True:
    print l.currentVal
    l.tick()
    sleep(0.05)



       
