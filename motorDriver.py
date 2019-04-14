import serial
import time

class Motor:
    def __init__(self, port):
        self.serial = serial.Serial(port, 115200)
        self.serial.write("nxr0")
        self.angle = 0

    def move(self, angleChange):
        self.angle = self.angle + angleChange
        self.serial.write("r")
        self.serial.write(self.angle)        

    def drive(self, pos):
        pass


left_motor = Motor("/dev/ttyACM0")
right_motor = Motor("/dev/ttyACM1")

time.sleep(5)

#figure out how to read all lines
move(left_motor, 360)
move(right_motor, 360)

move(left_motor, -360)
move(right_motor, -360)

