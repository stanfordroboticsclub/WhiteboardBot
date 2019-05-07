import serial
import time
import math

class Motor:
    def __init__(self, port):
        self.serial = serial.Serial(port, 115200)
        self.serial.write("x") # should probably only use one line for these writes
        self.serial.write("y")
        self.serial.write("r0")
        self.angle = 0
        time.sleep(.1)
        print("motor initialized")

    def move(self, angleChange):
        self.angle = self.angle + angleChange
#        print("the self.angle is %d" %(self.angle))
        self.serial.write("r%d" %(self.angle))

    def getPosition(self):
        self.serial.reset_input_buffer()
        self.serial.write("p")
        anglePrintout = self.serial.readline()
        angleSplit = anglePrintout.split(' ')
        while angleSplit[0] != "stepNumber:": 
              print(angleSplit)
              anglePrintout = self.serial.readline()
              angleSplit = anglePrintout.split(' ')
        print(angleSplit)
        angle = angleSplit[4]
        angle = angle[:-1]
        time.sleep(.1)
        self.serial.write("x")
        time.sleep(.1)
        self.serial.write("y")
        time.sleep(.1)
        return float(angle)

    def drive(self, pos):
        pass
