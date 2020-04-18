#############################################################
# LED blink Demo 3
# Date: 2020-04-18
#############################################################

from machine import Pin
import utime as time

LED_OFF  = 1 # 1=OFF, 0=ON
LED_GPIO = 5 # use GPIO5 for LED output

def next_state_generator():
    while True:
        yield 0
        time.sleep_ms( 100 )
        yield 1
        time.sleep_ms( 100 )

def main_loop( led ):
    for state in next_state_generator():
        led.value( state )

try:
    led = Pin( LED_GPIO, Pin.OUT )
    main_loop( led )
except KeyboardInterrupt:
    pass
finally:
    led.value( LED_OFF ) # turn off LED 

#############################################################
