##############################################################
# LED blink Demo 8
# Date: 2020-04-18
#############################################################

from machine import Pin
import utime as time
import esp32

LED_OFF  = 1 # 1=OFF, 0=ON
LED_GPIO = 5 # use GPIO5 for LED output

led = Pin( LED_GPIO, Pin.OUT )

# Use the RMT module to generate pulses
# The freq. of input clock to RMT is always 80MHz.
# 80MHz/250/32000 = 10Hz 
rmt = esp32.RMT(id=0, pin=led, clock_div=250)
# Generate pulses repeatedly
rmt.loop(True)
# Send 0 first, followed by 1
# The pulse width for 1 and 0 is 32000 (15-bit value).
rmt.write_pulses( [32000,32000], start=0 ) 

try:
    while True:
        time.sleep(-1)
except KeyboardInterrupt:
    rmt.loop(False)
finally:
    rmt.deinit()
    led.init(mode=Pin.IN, value=1)

#############################################################
