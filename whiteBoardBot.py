from motorDriver import Motor

class robot:
    def __init__(self, left_port, right_port):
        self.left_motor = Motor(left_port)
        self.right_motor = Motor(right_port)

wbb = robot("/dev/ttyACM0", "/dev/ttyACM1") #WhiteBoard Bot

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
        wbb.left_motor.move(changeLeft)
        wbb.right_motor.move(changeRight) 

    print("Done moving!")
    yCoor = float(input("Choose a new y coor (0 to quit) "))
#    xCoor = float(input("Choose a new x coor (0 to quit) "))
