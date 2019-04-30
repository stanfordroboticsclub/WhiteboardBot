# this file calculates the string lengths given a certain position
# on a white board.
# the position on the white board is defined with the top left corner
# being (0,0) and the positive x direction being to the right, positive
# y direction being down.
#
# I guess the units that I'm using are centimeters
#
# note: this assumes that strings meet up at a singular point on the robot
import math


class StringLengths:
    def __init__(self):
        self.left = 0
        self.right = 0


class Rotations:
    def __init__(self):
        self.left = 0
        self.right = 0


WIDTH = 1000 # constant which keeps track of width - distance between motors of canvas
HEIGHT = 1000 # constant which keeps track of height of canvas

CIRCUMFERENCE = 1.3 # 13 millimeters

global_string_lengths = StringLengths
globalX = 0 # global variable to hold x coordinate of robot
globalY = 0 # global variable to hold y coordinate of robot


# function to calculate left and right string lengths given an x and a y coordinate.
def coordinate_to_string_length(x, y):
    string_pair = StringLengths()
    string_pair.left = math.sqrt(math.pow(x,2) + math.pow(y,2))
    string_pair.right = math.sqrt(math.pow(WIDTH,2) - 2*WIDTH*x + math.pow(x,2) + math.pow(y,2))
    return string_pair


# gets the string movement change between two string lengths
def get_string_length_change(current_string_lengths, desired_string_lengths):
    string_length_change = StringLengths()
    string_length_change.left = desired_string_lengths.left - current_string_lengths.left
    string_length_change.right = desired_string_lengths.right - current_string_lengths.right
    return string_length_change


def get_rotations_in_degrees(current_string_lengths, desired_string_lengths):
    strings_change = get_string_length_change(current_string_lengths, desired_string_lengths)
    rotations_change = Rotations()
    rotations_change.left = strings_change.left/CIRCUMFERENCE * 360
    rotations_change.right = strings_change.right/CIRCUMFERENCE * 360
    return rotations_change


global_string_lengths.left = 0
global_string_lengths.right = 0
#while 1:
newX = float(input("what x coordinate do you want to go to? (from 0 to {}) ".format(WIDTH)))
newY = float(input("y coordinate? (from 0 to {}) ".format(HEIGHT)))
new_string_pair = coordinate_to_string_length(newX, newY)

#print("Your left string should have length", new_string_pair.left)
#print("Your right string should have length", new_string_pair.right)

string_pair_change = get_string_length_change(global_string_lengths, new_string_pair)

#print("Your left string change should be", string_pair_change.left)
#print("Your right string change should be", string_pair_change.right)

rotations_pair_change = get_rotations_in_degrees(global_string_lengths, new_string_pair)

print("Your left motor change should be (in degrees)", rotations_pair_change.left)
print("Your right motor change should be (in degrees)", rotations_pair_change.right)

print("------------------------- end --------------------------")

global_string_lengths = new_string_pair
