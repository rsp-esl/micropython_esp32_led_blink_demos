#############################################################
# LED blink Demo 1
# Date: 2020-04-18
#############################################################

from machine import Pin
import utime as time

LED_OFF  = 1 # 1=OFF, 0=ON
LED_GPIO = 5 # use GPIO5 for LED output

def main_loop( led ):
    while True:
        # read, modify (toggle), write LED state
        led.value( not led.value() )
        # delay for 0.1 seconds
        time.sleep_ms( 100 )

try:
    # create a LED object for LED output 
    led = Pin( LED_GPIO, Pin.OUT )
    # enter main loop (press Ctrl+C to stop)
    main_loop( led )
except KeyboardInterrupt:
    pass
finally:
    led.value( LED_OFF ) # turn off LED 

#############################################################
    