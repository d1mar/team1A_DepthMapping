#!/usr/bin/env python
import freenect
import time
import signal

keep_running = True
last_time = 0
led = 0
tilt = 0
def body(dev,ctx):
    global last_time
    global led
    global tilt
    if not keep_running:
        raise freenect.Kill
    if led>6 and tilt>30:
        return
    freenect.set_led(dev, led)
    freenect.set_tilt_degs(dev, tilt)
    print('led[%d] tilt[%d] accel[%s]' % (led,tilt,freenect.get_accel(dev)))
    time.sleep(1)
    led =  led+1
    tilt = tilt+5
def handler(signum,frame):
    global keep_running
    keep_running = False

print('Press Ctrl-C to stop')
dev = freenect.open_device(freenect.init(),0)
while True:
    body(dev,0)

signal.signal(signal.SIGINT,handler)
#freenect.runloop(body=body)
