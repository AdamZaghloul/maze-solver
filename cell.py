from window import *
from line import *
from point import *

class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = 0
        self._x2 = 0
        self._y1 = 0
        self._y2 = 0
        self._win = win
        self.visited = False
    
    def draw(self, x1=None, y1=None, x2=None, y2=None):
        if x1 is not None:
            self._x1 = x1
        if x2 is not None:
            self._x2 = x2
        if y1 is not None:
            self._y1 = y1
        if y2 is not None:
            self._y2 = y2
            
        color = "black"
        wall_color = "black"
        no_wall_color = "#D9D9D9"

        if self._win is not None:
            if self.has_left_wall:
                color = wall_color
            else:
                color = no_wall_color
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), color)
            if self.has_right_wall:
                color = wall_color
            else:
                color = no_wall_color
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), color)
            if self.has_top_wall:
                color = wall_color
            else:
                color = no_wall_color
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), color)
            if self.has_bottom_wall:
                color = wall_color
            else:
                color = no_wall_color
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), color)
    
    def draw_move(self, to_cell, undo=False):

        fill = "red"
        if undo:
            fill = "gray"

        line = Line(Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2), Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)).draw(self._win.canvas, fill)

