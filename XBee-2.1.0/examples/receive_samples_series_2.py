#! /usr/bin/python

"""
receive_samples.py

By Kevin Glavin, 2013
archen.sol@gmail.com

This example continuously reads the serial port and processes IO data
received from a remote XBee.
"""

from xbee import ZigBee
import serial

PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
xbee = ZigBee(ser)

# Continuously read and print packets
while True:
    try:
        response = xbee.wait_read_frame()
        print response
    except KeyboardInterrupt:
        break

xbee.halt()        
ser.close()
