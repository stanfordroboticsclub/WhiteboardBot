import serial


class Motor:
    def __init__(self, port):
        self.serial = serial.Serial(port, 115200)
        pass

    def step(self, numSteps):
	for i in range(numSteps):
	    self.serial.write("s")

    def drive(self, pos):
        pass



left_motor = Motor("/dev/ttyACM0")
right_motor = Motor("/dev/ttyACM1")

for i in range(50):
    left_motor.step(1)
    right_motor.step(1)

