#############################################################
# LED blink Demo 7
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
    try:
        while not finished:
            pass  
    except KeyboardInterrupt:
        finished = True
        _thread.exit()

def led_thread_func(id, led, delay,lock):
    global finished
    try:
        while not finished:
            lock.acquire()
            led.value( id )
            time.sleep_ms( delay )
            lock.release()
    except KeyboardInterrupt:
        finished = True
        _thread.exit()
    finally:
        led.value( LED_OFF )

led = Pin( LED_GPIO, Pin.OUT )
lock = _thread.allocate_lock()

_thread.start_new_thread( led_thread_func, (0,led,100,lock,) )
_thread.start_new_thread( led_thread_func, (1,led,100,lock,) )

main_loop()

#############################################################
