#-*-coding: utf-8-*-
#apt-get install python-pip
#pip install pyserial
#sudo apt-get install python-dev  #for gpio lib
import serial
import time
from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector
gpio.init()
gpio.setcfg(port.PA12, gpio.OUTPUT)
gpio.setcfg(port.STATUS_LED, gpio.OUTPUT)
delay_print = 2# 2 sec
counter = 0
status = True
start = time.time()
ser = serial.Serial(port = "/dev/ttyS1", baudrate=9600)
ser.close()
ser.open()
for i in range (20):  
    time. sleep(0.25)
    if status==True:
        gpio.output(port.STATUS_LED, gpio.HIGH)
        gpio.output(port.PA12, gpio.LOW)  
        status=False			
    elif status==False:
	gpio.output(port.STATUS_LED, gpio.LOW)
        gpio.output(port.PA12, gpio.HIGH)
	status=True
while(1):
    if ser.isOpen():
        if time.time() - start > delay_print:
            counter = counter + 1
            ser.write(str(counter)+"\n")
            print("порт открыт")
            ser.write("Please enter the command\n")
            print("message sent")
            start = time.time()
        if (ser.inWaiting()>0):
            data_str = ser.read(ser.inWaiting()).decode()
            ser.write("you are writed "+str(data_str)+"\n")
            print("Data received = ", data_str)
            if data_str=="LED_ON":
                print("LED_ON")
	        gpio.output(port.STATUS_LED, gpio.HIGH)
            elif data_str=="LED_OFF":
                print("LED_OFF")
                #gpio.output(port.PA1, gpio.LOW)
                gpio.output(port.STATUS_LED, gpio.LOW)    
