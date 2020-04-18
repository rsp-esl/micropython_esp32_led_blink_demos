#############################################################
# LED blink Demo 6
# Date: 2020-04-18
#############################################################

from machine import Pin
import utime as time
import _thread

LED_OFF  = 1 # 1=OFF, 0=ON
LED_GPIO = 5 # use GPIO5 for LED output

finished = False

def main_loop( ):
    global finished
    print( 'thread ID (main):', _thread.get_ident())
    try:
        while not finished:
            pass  
    except KeyboardInterrupt:
        finished = True
        _thread.exit()

def led_thread_func(led, delay):
    global finished
    print( 'thread ID (led):', _thread.get_ident())
    try:
        while not finished:
            led.value(not led.value())
            time.sleep_ms( delay )
    except KeyboardInterrupt:
        finished = True
        led.value( LED_OFF )
        _thread.exit()

led = Pin( LED_GPIO, Pin.OUT )
_thread.start_new_thread( led_thread_func, (led,100,) )
main_loop()

#############################################################
