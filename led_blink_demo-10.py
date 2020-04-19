##############################################################
# LED blink Demo 10
# Date: 2020-04-18
#############################################################

from machine import Pin
from micropython import const
import utime as time

LED_OFF  = 1 # 1=OFF, 0=ON
LED_GPIO = 5 # use GPIO5 for LED output

led = Pin( LED_GPIO, Pin.OUT )

async def next_state(led, delay):
    state = 0
    try:
        while True:
            state = not state
            yield state
            time.sleep_ms( delay )
    except KeyboardInterrupt:
        pass

async def coro(): # coroutine
    return await next_state(led, 100)

c = coro()

try:
    while True:
        led.value( c.send(None) )
except StopIteration:
    c.close()
    led.value( LED_OFF )
    print('Done')

#############################################################
