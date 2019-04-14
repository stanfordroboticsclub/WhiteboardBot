import serial


class Motor:
    def __init__(self, port):
        self.serial = serial.Serial(port, 115200)
        self.serial.write("n")
        self.serial.write("t")

    def step(self, numSteps):
        for i in range(numSteps):
            self.serial.write("s")

    def drive(self, pos):
        pass


left_motor = Motor("/dev/ttyACM0")
right_motor = Motor("/dev/ttyACM1")

#figure out how to read all lines

for i in range(150):
    left_motor.step(1)
    right_motor.step(1)

