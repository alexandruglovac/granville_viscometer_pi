import serial
import time
from time import gm
time, strftime
import
struct
#serial port setti ngs
dmm = serial.Serial(
port='/dev/ttyUSB0',
baudrate=9600,
bytesi ze=8,
parity=serial.PARITY_NONE,
stop
bits
=serial.STOPBITS_ONE,
)
#handli ng exceptions
try:
dmm.open()
except Exception, e:
print
"problem faced while openning the port : " +str(e)
exit()
print "Fluke 189 Digital Multimeter"
print "
-------------------------------------------------------
"
dmm.isOpen()
file = open("/home/pi/Ramzan_project/py_Serial/dmmLogFile.txt", "a")
whi le True:
dmm.write('QM
\
r')
dmm.flushInput()
data = dmm.read(14)
if data == '':
dmm.close()
else:
print data
time.sleep(1)
print >>file,data,'
-
> ',strftime("%d %b %Y,%H:%M:%S")
file.flush()
file.close()
