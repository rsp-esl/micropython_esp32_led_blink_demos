#############################################################
# LED blink Demo 4
# Date: 2020-04-18
#############################################################

from machine import Pin, Timer
import utime as time

LED_OFF  = 1 # 1=OFF, 0=ON
LED_GPIO = 5 # use GPIO5 for LED output

def main_loop( ):
    while (True):
        time.sleep(-1) # wait forever 

try:
    led = Pin( LED_GPIO, Pin.OUT )
    # create a software-based timer 
    timer = Timer(-1)
    # start the timer in periodic mode (100msec period)
    timer.init( mode=Timer.PERIODIC, period=100,
        callback=lambda t: led.value(not led.value()) )
    main_loop()
except KeyboardInterrupt:
    pass
finally:
    led.value( LED_OFF )
    timer.deinit()

#############################################################
