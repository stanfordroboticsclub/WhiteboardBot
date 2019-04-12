import serial


class Motor:
    def __init__(self, port):
        self.serial = serial.Serial(port, 115200)
        pass

    def drive(self, pos):
        pass



left_motor = Motor("/dev/tty/ACM0")
right_motor = Motor()


right_motor.drive(1)
