import freenect
import time
import signal

led = 0
tilt = 0
def body(dev,ctx):
   freenect.set_led(dev,led)
   freenect.set_tilt_degs(dev,tilt)
   print('led[%d] tilt[%d] accel[%s]' % (led,tilt,freenect.get_accel(dev)))
   time.sleep(1)
   led += 1
   tilt +=5
freenect.runloop(body=body)
