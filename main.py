from window import *
from line import *
from point import *

def main():
    win = Window(800, 600)

    win.draw_line(Line(Point(0,0), Point(600,100)), "black")
    win.draw_line(Line(Point(300,200), Point(500,700)), "red")
    win.draw_line(Line(Point(150,400), Point(100,200)), "black")
    
    win.wait_for_close()

main()