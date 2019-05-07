from motorDriver import Motor
import math


# Default is upper left corner
class StringLengths:
    def __init__(self):
        self.left = 0
        self.right = WIDTH


class Rotations:
    def __init__(self):
        self.left = 0
        self.right = 0


WIDTH = 1000 # constant which keeps track of width - distance between motors of canvas                   
HEIGHT = 1000 # constant which keeps track of height of canvas                                          
CIRCUMFERENCE = 1.3 # 13 millimeters                                                                     

global_string_lengths = StringLengths();
global_string_lengths.left = 0
global_string_lengths.right = WIDTH
globalX = 0 # global variable to hold x coordinate of robot                                              
globalY = 0 # global variable to hold y coordinate of robot 


class robot:
    def __init__(self, left_port, right_port):
        self.left_motor = Motor(left_port)
        self.right_motor = Motor(right_port)

    # function to calculate left and right string lengths given an x and a y coordinate.                
    def coordinate_to_string_length(self, x, y):
        string_pair = StringLengths()
        string_pair.left = math.sqrt(math.pow(x,2) + math.pow(y,2))
        string_pair.right = math.sqrt(math.pow(WIDTH,2) - 2*WIDTH*x + math.pow(x,2) + math.pow(y,2))
        return string_pair

    # gets the string movement change between two string lengths                                       
    def get_string_length_change(self, current_string_lengths, desired_string_lengths):
        string_length_change = StringLengths()
        string_length_change.left = desired_string_lengths.left - current_string_lengths.left
        string_length_change.right = desired_string_lengths.right - current_string_lengths.right
        return string_length_change

    def get_rotations_in_degrees(self, current_string_lengths, desired_string_lengths):
        strings_change = get_string_length_change(current_string_lengths, desired_string_lengths)
        rotations_change = Rotations()
        rotations_change.left = strings_change.left/CIRCUMFERENCE * 360
        rotations_change.right = strings_change.right/CIRCUMFERENCE * 360
        return rotations_change

    def moveTo(self, xCord, yCord):
        new_string_pair = self.coordinate_to_string_length(xCord, yCord)
        string_pair_change = self.get_string_length_change(global_string_lengths, new_string_pair)
        rotations_pair_change = self.get_rotations_in_degrees(global_string_lengths, new_string_pair)
        self.left_motor.move(rotations_pair_change.left)
        self.right_motor.move(rotations_pair_change.right)

        globalX = xCord
        globalY = yCord
        global_string_lengths = new_string_pair

wbb = robot("/dev/ttyACM0", "/dev/ttyACM1") #WhiteBoard Bot

yCoor = float(input("Choose a new y coor (0 to quit) "))
xCoor = float(input("Choose a new x coor (0 to quit) "))

#moves in y-direction to user-designated position
while yCoor != 0 and xCoor != 0: #need a better sentinel value... idk what would make most sense
    wbb.moveTo(xCoor, yCoor)
    
    print("Done moving!")
    yCoor = float(input("Choose a new y coor (0 to quit) "))
    xCoor = float(input("Choose a new x coor (0 to quit) "))
