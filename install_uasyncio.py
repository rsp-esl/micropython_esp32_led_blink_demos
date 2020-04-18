#############################################################
# MicroPython script for install uasyncio package
#############################################################

import network
import utime as time
import upip as pip
import uos as os

# Specify the SSID and password of your WiFi network
WIFI_CFG = { 'ssid': "XXXXX", 'password': "XXXXXXX" }

def connect_wifi( wifi_cfg, max_retries=10 ):
    # use WiFi in station mode (not AP)
    wifi_sta = network.WLAN( network.STA_IF )
    # activate the WiFi interface (up)
    wifi_sta.active(True)
    # connect to the specified WiFi AP
    wifi_sta.connect( wifi_cfg['ssid'], wifi_cfg['password']  )
    retries = 0
    while not wifi_sta.isconnected():
        retries += 1
        if retries >= max_retries:
            return None
        time.sleep_ms(500)
    return wifi_sta

if connect_wifi( WIFI_CFG ):
    # install uasyncio package
    pip.install('micropython-uasyncio', '/lib')
    pip.install('micropython-uasyncio.synchro', '/lib')
    pip.install('micropython-uasyncio.queues', '/lib')
    print( os.listdir('/lib') ) 

#############################################################
