from window import *
from line import *
from point import *
from cell import *
from maze import *

def main():
    win = Window(800, 600)

    maze = Maze(0, 0, 2, 3, 100, 100, win)

    win.wait_for_close()

def old_main_cells():
    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell1.draw(50,50,150,150)

    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.has_right_wall = False
    cell2.draw(150,50,250,150)
    
    cell3 = Cell(win)
    cell3.has_left_wall = False
    cell3.has_bottom_wall = False
    cell3.draw(250,50,350,150)

    cell4 = Cell(win)
    cell4.has_top_wall = False
    cell4.draw(50,150,150,250)

    cell5 = Cell(win)
    cell5.has_top_wall = False
    cell5.draw(150,150,250,250)
    
    cell6 = Cell(win)
    cell6.has_top_wall = False
    cell6.draw(250,150,350,250)

    cell7 = Cell(win)
    cell7.draw(50,250,150,350)

    cell8 = Cell(win)
    cell8.draw(150,250,250,350)
    
    cell9 = Cell(win)
    cell9.draw(250,250,350,350)

    cell1.draw_move(cell2)
    cell2.draw_move(cell3)
    cell3.draw_move(cell6)
    cell6.draw_move(cell5)
    cell6.draw_move(cell5, True)

main()