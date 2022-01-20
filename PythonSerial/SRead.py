#!user/bin/env python
import time
import serial
import os

Tstr0 = time.localtime(time.time())
Dstr0 = str(Tstr0.tm_year)+str(Tstr0.tm_mon) + str(Tstr0.tm_mday)
Tstr1 = "T" + str(Tstr0.tm_hour) + str(Tstr0.tm_min)
FNameStr = "/media/pi/E69C-0568/Dump/datD"+Dstr0+Tstr1

fiout = open(FNameStr, "w")            

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
couter=0

readyToRead=False
readyToReadCnt=0

for Nn in range(1000000):
    try:
        xs=ser.readline()
        print(xs)
        if(len(xs)>100 and readyToRead):
            fiout.write(xs)
            fiout.write('\n')
        elif(xs=="STARTDATA\n" and readyToReadCnt>=5):
            readyToRead=True
            #if(fiout.closed):
            #    fiout = open(FNameStr, "a")
        elif(xs=="NODATA00NODATA00NODATA00NODATA\n"):
            if(readyToRead):
                fiout.close()
                print("Exiting\n")
                os.system("shutdown now")
                break
        
            readyToRead=False
            readyToReadCnt=readyToReadCnt +1
            print(xs)
    except:
        print("fail")

    print(Nn)
    print("Writing: ")
    print(readyToRead)
    print('\n')

if(readyToRead):
    fiout.close()
 
