import serial
import time

class Motor:
    def __init__(self, port):
        self.serial = serial.Serial(port, 115200)
        self.serial.write("x") # should probably only use one line for these writes
        self.serial.write("y")
        self.serial.write("r0")
        self.angle = 0
        print("motor initialized")

    def move(self, angleChange):
        self.angle = self.angle + angleChange
        self.serial.write("r")
        self.serial.write(str(self.angle))
        print("moving %d" %(angleChange))

    def getPosition(self):
        angle = self.serial.write("p")
        return float(angle)

    def drive(self, pos):
        pass


left_motor = Motor("/dev/ttyACM0")

time.sleep(1)

right_motor = Motor("/dev/ttyACM1")

time.sleep(5)

#figure out how to read all lines

#left_motor.move(360)
#time.sleep(.1)
#right_motor.move(360)

#left_motor.move(-360)
#right_motor.move(-360)

for i in range(100):
    left_motor.move(10)
    right_motor.move(10)
    print(left_motor.getPosition())
    print(right_motor.getPosition())


