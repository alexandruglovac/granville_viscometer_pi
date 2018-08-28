import time
import serial

print "Starting program"

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
time.sleep(1)
try:
    ser.write('Hello World\r\n')
    ser.write('Serial Communication Using Raspberry Pi\r\n')
    ser.write('By: Viscometer 1\r\n')
    print 'Data Echo Mode Enabled'
    while True:
        if ser.inWaiting() > 0:
            data = ser.read()
            print data
        
except KeyboardInterrupt:
    print "Exiting Program"

except:
    print "Error Occured, Exiting Program"

finally:
    ser.close()
    pass