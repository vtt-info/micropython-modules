# ESP32 running MicroPython 
#
# Brandon Gant
# 2019-02-08
#
# Source: https://github.com/micropython/micropython/tree/master/ports/esp32#configuring-the-wifi-and-using-the-board
# Source: https://boneskull.com/micropython-on-esp32-part-1/
# Source: https://docs.micropython.org/en/latest/library/network.WLAN.html
#
# /home/pi/.local/bin/ampy --port /dev/ttyUSB0 put boot.py
# screen /dev/ttyUSB0 115200
#    Ctrl+a Shift+k to kill screen connection

# Create exceptions (feedback) in cases where normal RAM allocation fails (e.g. interrupts)
import esp
import machine
import micropython
import network
import ntptime
import uos
import utime

micropython.alloc_emergency_exception_buf(100)

# Connect to WiFI
def wlan_connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active() or not wlan.isconnected():
        wlan.active(True)
        print('WiFi SSID: ', ssid)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('WiFi DHCP: ', wlan.ifconfig()[0])

def ntp():
    # Set clock using NTP
    print('')
    print("NTP Server:", ntptime.host)
    try:
        ntptime.settime()
    except:
        print("    Connection to %s failed" % ntptime.host)
    print('UTC Time:   {}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}'.format(*utime.localtime()))
    print('')
         

# Suppress ESP debug messages in the REPL
def no_debug():
    esp.osdebug(None)

no_debug()
wlan_connect('<SSID>', '<password>')
ntp()

print("List of files on this device:")
print(uos.listdir('/'))
print('')
