# import tkinter
# m = tkinter.Tk()
#
# w = tkinter.Canvas(m, width=200, height=100)
# w.pack()
#
# w.create_line(0, 0, 200, 100)
# w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
#
# w.create_rectangle(50, 25, 150, 75, fill="blue")
#
# m.mainloop()
#
#
# #Set defaults
# btn1pressed = False
# newline = True
#
# def main():
#   root = TK.Tk()
#   the_canvas = TK.Canvas(root)
#   the_canvas.pack()
#   the_canvas.bind("<Motion>", mousemove)
#   the_canvas.bind("<ButtonPress-1>", mouse1press)
#   the_canvas.bind("<...

from Tkinter import *

master = Tk()

start = []

prev = [0,0]
curr = []

boxHalfSize = 10

def callback(event):
    global start
    print( "clicked at", event.x, event.y, "start", start)

    if start == []:
        start = [event.x, event.y]
    else:
        canvas.create_line(start[0], start[1], event.x, event.y, fill="red")
        start = []

def draw(event):
    canvas.create_line(prev[0], prev[1], event.x, event.y, fill="red")
    prev[0] = event.x
    prev[1] = event.y
    if 'robot' in globals():
        canvas.delete(robot);
    robot = canvas.create_rectangle(event.x - boxHalfSize, event.y - boxHalfSize,\
                            event.x + boxHalfSize, event.y + boxHalfSize, outline="#fb0", fill="#fb0")


canvas = Canvas(master, width=1000, height=1000)

boxHalfSize = 10
startX = 100
startY = 100
robot = canvas.create_rectangle(startX, startY, startX + (2 * boxHalfSize), startY + (2 * boxHalfSize), outline="#fb0", fill="#fb0")

#canvas.bind("<Button-1>", callback)
canvas.bind("<B1-Motion>", draw)
canvas.pack()

master.mainloop()
