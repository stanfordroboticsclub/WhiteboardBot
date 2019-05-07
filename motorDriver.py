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



#start by initializing motors
left_motor = Motor("/dev/ttyACM0")
right_motor = Motor("/dev/ttyACM1")

#vars for overall position
y = 0
x = 0

yCoor = float(input("Choose a new y coor (0 to quit) "))
xCoor = float(input("Choose a new x coor (0 to quit) "))

#moves in y-direction to user-designated position
while yCoor != 0 and xCoor != 0: #need a better sentinel value... idk what would make most sense
    #figure out how to do x coor using string length thingy
    dy = (yCoor - y) / 1.3 #circumference of pulley

    changeLeft = -1
    changeRight = 1

    if dy < 0:
        changeLeft *= -1
        changeRight *= -1
        dy *= -1
    for i in range(int(dy * 360)):
        left_motor.move(changeLeft)
        right_motor.move(changeRight) 

    print("Done moving!")
    yCoor = float(input("Choose a new y coor (0 to quit) "))
#    xCoor = float(input("Choose a new x coor (0 to quit) "))
