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
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self._win is not None:
            if self.has_left_wall:
                self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "black")
            if self.has_right_wall:
                self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "black")
            if self.has_top_wall:
                self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "black")
            if self.has_bottom_wall:
                self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "black")
    
    def draw_move(self, to_cell, undo=False):

        fill = "red"
        if undo:
            fill = "gray"

        line = Line(Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2), Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)).draw(self._win.canvas, fill)

