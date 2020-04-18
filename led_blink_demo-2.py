#############################################################
# LED blink Demo 2
# Date: 2020-04-18
#############################################################

from machine import Pin
import utime as time

LED_OFF  = 1 # 1=OFF, 0=ON
LED_GPIO = 5 # use GPIO5 for LED output

def main_loop( led ):
    t = time.ticks_ms() # read time ticks (in msec)
    while True:
       if time.ticks_ms() - t >= 100:
           # update the timestamp
           t += 100
           # toggle LED state
           led.value( not led.value() )

try:
    led = Pin( LED_GPIO, Pin.OUT )
    main_loop( led )
except KeyboardInterrupt:
    pass
finally:
    led.value( LED_OFF ) # turn off LED 

#############################################################
