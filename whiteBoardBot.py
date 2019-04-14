from motorDriver import motor

class robot:
    def __init__(self, left_port, right_port):
        left_motor = Motor(left_port)
        time.sleep(1)
        right_motor = Motor(right_port)

wbb = robot("/dev/ttyACM0", "/dev/ttyACM1") #WhiteBoard Bot

