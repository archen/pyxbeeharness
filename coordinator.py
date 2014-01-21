#! /usr/bin/python

from xbee import ZigBee
import serial

PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
xbee = ZigBee(ser, escaped=True)

# Continuously read and print packets
while True:
    try:
        print "waiting"
        response = xbee.wait_read_frame()
        print response
    except KeyboardInterrupt:
        break

ser.close()