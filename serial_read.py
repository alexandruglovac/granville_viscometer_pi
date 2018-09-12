import serial
import time
from time
import gmtime, strftime
import struct# serial port settings
dmm = serial.Serial(
  port = '/dev/ttyAMA0',
  baudrate = 9600,
  bytesize = 8,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
)# handling exceptions
try:
dmm.open()
except Exception, e:
  print "problem faced while openning the port : " + str(e)
exit()
print "Lab Viscometer"
print "-------------------------------------------------------"
dmm.isOpen()
file = open("/home/pi/granville/py_Serial/dmmLogFile.txt", "a")
while True:
  dmm.write('QM\r')
dmm.flushInput()
data = dmm.read(14)
if data == '':
  dmm.close()
else :
  print data
time.sleep(1)
print >> file, data, ' -> ', strftime("%d %b %Y,%H:%M:%S")
file.flush()
file.close()