#!/usr/bin/python

# Read & print/write data
ser = serial.Serial('/dev/ttyUSB0',19200, 8, 'N', 1, timeout = 5)
# Open ve_direct.csv
file_data = open('ve_data.csv', 'w')
print "Reading data and writing to ve_data.csv"
# Listen for the input, exit if nothing received in timeout period
output = " "
while True:
  while output != "":
    output = ser.readline()
    file_data.write(output)
