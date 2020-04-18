##############################################################
# LED blink Demo 9
# Date: 2020-04-18
#############################################################

# https://github.com/peterhinch/micropython-async/blob/master/TUTORIAL.md

from machine import Pin
import uasyncio as asyncio

LED_OFF  = 1 # 1=OFF, 0=ON
LED_GPIO = 5 # use GPIO5 for LED output

led = Pin( LED_GPIO, Pin.OUT )

async def led_toggle(led,duration):
    try:
        while True:
            await asyncio.sleep_ms( duration )
            led.value( not led.value() )
    except KeyboardInterrupt:
        pass
    
async def shutdown(task, duration):
    asyncio.cancel( task )
    await asyncio.sleep(0)

try:
   loop = asyncio.get_event_loop()
   task = led_toggle(led, 100)
   loop.run_until_complete( task )
except KeyboardInterrupt:
   loop.run_until_complete( shutdown(task, 0) )
finally:
    led.value( LED_OFF )

#############################################################
