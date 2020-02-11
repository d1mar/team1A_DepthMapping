# imports for serial connection
import serial
import io

# import for hardware
import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT      = 1000      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
CUBE_DIM       = 10      # define cube dimension
LIT_LEDS       = 100     # number of LEDs lit at one time


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=0):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        #time.sleep(wait_ms/1000.0)

    strip.show()

def cubeCorrect(litLEDS):
    #for i in range(LIT_LEDS):
    for i in range(len(litLEDS)):
        led = 100*litLEDS[i][1] + 10*litLEDS[i][2] + litLEDS[i][0]
        x = led % (2*CUBE_DIM)
        if( x < CUBE_DIM):
            litLEDS[i][0] = (-1)*((x -(CUBE_DIM - 1)))

def mapCube(strip, litLEDS):
    """use litLEDinfo to light necessary LEDs"""

    #for i in range(LIT_LEDS):
    for i in range(len(litLEDS)):
        led = 100*litLEDS[i][1] + 10*litLEDS[i][2] + litLEDS[i][0]
        c = led % (2*CUBE_DIM)
        if(c < CUBE_DIM):
            led += CUBE_DIM - ((2*c)+1)


        if(led>((CUBE_DIM*CUBE_DIM)-1)):
            y = (led + 100) % (2*CUBE_DIM*CUBE_DIM)
            if( y >= CUBE_DIM*CUBE_DIM):
                y %= (CUBE_DIM*CUBE_DIM)
                y //= CUBE_DIM
                led += CUBE_DIM*CUBE_DIM - (((2*y)+1)*10)
                x = led % CUBE_DIM
                led += CUBE_DIM - ((2*x)+1)

        color = Color(litLEDS[i][4], litLEDS[i][3], litLEDS[i][5])
        strip.setPixelColor(led, color)
    #start_time = time.time()
    strip.show()
    #end_time = time.time() - start_time
    #print("end time strip.show: ", end_time)



# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')


    #create cube arrays
    cube = [[[0 for z in range (10)] for y in range (10)] for x in range (10)]
    litLEDS = [[1 for i in range (6)] for j in range (100)]

    #test leds
    #litLEDS[0] = [0,1,1,255,0,0]
    #litLEDS[1] = [2,3,1,255,0,0]
    #litLEDS[2] = [0,3,0,255,0,0]
    #litLEDS[3] = [0,3,1,255,0,0]
    #litLEDS[4] = [2,4,2,255,0,0]
    #litLEDS[5] = [1,4,1,255,0,0]
    #litLEDS[6] = [1,3,1,255,0,0]
    #litLEDS[7] = [0,2,1,255,0,0]
    #litLEDS[8] = [2,4,1,255,0,0]
    #litLEDS[9] = [0,2,0,255,0,0]
    #litLEDS[10] = [1,2,1,255,0,0]


    # Serial connection
    ser = serial.Serial(port = '/dev/serial0', baudrate = 115200, bytesize = serial.EIGHTBITS, timeout = 0)

    print("connected to: " + ser.port)

    counter = 0

    received = []
    tupled = []
    temp = False

    '''
    # main loop to light LED
    try:

        #correct for snake pattern
        #cubeCorrect(litLEDS)

        while True:
            #map cube
            mapCube(strip, litLEDS)
            print("LED LIT")

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
    '''

    # Always check serial connection
    try:
        while True:
            start_time = time.time()
            for c in ser.read(1).decode('utf-8'):
                if c == '\0':
                    temp = True
                    break

                t = int(chr(ord(c)))
                tupled.append(t)
                counter += 1

                if counter % 3 == 0:
                    tupled.append(255)
                    tupled.append(0)
                    tupled.append(0)
                    received.append(list(tupled))
                    tupled = []
                    counter = 0


            #print(type(t))
            end_time = time.time() - start_time
            #print("Serial Receive Time: ", end_time)
            if temp:
                start_time = time.time()
                colorWipe(strip, Color(0,0,0))
                end_time = time.time() - start_time
                print("colorwipe Time: ", end_time)
                #correct for snake pattern
                #print(received)
                #cubeCorrect(received)
                #map cube
                start_time = time.time()
                mapCube(strip, received)
                end_time = time.time() - start_time
                print("mapCube Time: ", end_time)
                received = []
                temp = False

        ser.close()

        for i in received:
            print(i)

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)

## DO NOT DELETE
'''
# Always check serial connection
while True:
    for c in ser.read(1).decode('utf-8'):
        if c == '\0':
            temp = True
            break

        t = int(chr(ord(c)))
        tupled.append(t)
        counter += 1

        if counter % 3 == 0:
            received.append(tuple(tupled))
            tupled = []
            counter Depth_mapping= 0


        #print(type(t))
    if temp:
        break

ser.close()

for i in received:
    print(i)
'''
