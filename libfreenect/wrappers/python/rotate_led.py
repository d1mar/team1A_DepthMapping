#!/usr/bin/env python
import freenect
import time
import signal

keep_running = True
last_time = 0
led = -1
tilt = -5
def body(dev,ctx):
    global last_time
    if not keep_running:
        raise freenect.Kill
    if time.time() - last_time < 3:
        return
    last_time = time.time()
    led = led+1
    tilt = tilt+5
    freenect.set_led(dev, led)
    freenect.set_tilt_degs(dev, tilt)
    print('led[%d] tilt[%d] accel[%s]' % (led,tilt,freenect.get_accel(dev)))
    time.sleep(1)
    #led =  led+1
    #tilt = tilt+5
def handler(signum,frame):
    global keep_running
    keep_running = False

#while True:
#    body()
#    if led == 6:
#        break
signal.signal(signal.SIGINT,handler)
freenect.runloop(body=body)
