#! /usr/bin/python

import time

from xbee import ZigBee
import serial


PORT = '/dev/ttyUSB1'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
xbee = ZigBee(ser,escaped=True)

# Uncomment if you want to see api_response codes in the console
#import pprint
#pprint.pprint(xbee.api_responses)

DEST_ADDR_LONG = "\x00\x13\xA2\x00\x40\x76\x45\x6C"

# Continuously send packets
while True:
    try:
        print "send data"
        xbee.send("tx",data="AB",dest_addr_long=DEST_ADDR_LONG,
                  dest_addr="\xff\xfe")

        time.sleep(1)
    except KeyboardInterrupt:
        break
        
ser.close()