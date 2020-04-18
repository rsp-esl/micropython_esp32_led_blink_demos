#############################################################
# LED blink Demo 5
# Date: 2020-04-18
#############################################################

from machine import Pin, PWM
import utime as time

LED_OFF  = 1 # 1=OFF, 0=ON
LED_GPIO = 5 # use GPIO5 for LED output

def main_loop():
    while True:
        time.sleep(-1)
try:
    led = Pin( LED_GPIO, Pin.OUT )
    # create a PWM object for the specified pin
    pwm = PWM( led )
    pwm.freq(5) # note: 1Hz is the lowest frequency
    main_loop( )
except KeyboardInterrupt:
    pass
finally:
    led.value( LED_OFF ) # turn off LED 
    pwm.deinit()         # turn off PWM 

#############################################################
