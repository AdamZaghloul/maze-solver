import time
import random
from cell import *

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        if seed is not None:
            random.seed(seed)

        self._create_cells()
    
    def _create_cells(self):
        self._cells = []
        for i in range(0, self.num_cols):
            self._cells.append([])
            for j in range(0, self.num_rows):
                self._cells[i].append(Cell(self.win))
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        x1 = self.x1 + ((i+1) * self.cell_size_x)
        x2 = x1 + self.cell_size_x

        y1 = self.y1 + ((j+1) * self.cell_size_y)
        y2 = y1 + self.cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self.win is not None:
            self.win.redraw()
            time.sleep(0.5)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)

        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            temp = []
            if j < self.num_rows-1:
                if not self._cells[i][j+1].visited:
                    temp.append(self._cells[i][j+1])
            if j > 0:
                if not self._cells[i][j-1].visited:
                    temp.append(self._cells[i][j-1])
            if i < self.num_cols-1:
                if not self._cells[i+1][j].visited:
                    temp.append(self._cells[i+1][j])
            if i > 0:
                if not self._cells[i-1][j].visited:
                    temp.append(self._cells[i-1][j])

            if len(temp) == 0:
                self._cells[i][j].draw()
                return
            else:
                choice = random.randrange(0, len(temp))
                if j < self.num_rows-1:
                    if temp[choice] == self._cells[i][j+1]:
                        temp[choice].has_top_wall = False
                        self._cells[i][j].has_bottom_wall = False

                        temp[choice].draw()
                        self._cells[i][j].draw()

                        self._break_walls_r(i, j + 1)
                if j > 0:
                    if temp[choice] == self._cells[i][j-1]:
                        temp[choice].has_bottom_wall = False
                        self._cells[i][j].has_top_wall = False

                        temp[choice].draw()
                        self._cells[i][j].draw()

                        self._break_walls_r(i, j - 1)
                if i < self.num_cols-1:
                    if temp[choice] == self._cells[i+1][j]:
                        temp[choice].has_left_wall = False
                        self._cells[i][j].has_right_wall = False

                        temp[choice].draw()
                        self._cells[i][j].draw()

                        self._break_walls_r(i+1, j)
                if i > 0:
                    if temp[choice] == self._cells[i-1][j]:
                        temp[choice].has_right_wall = False
                        self._cells[i][j].has_left_wall = False

                        temp[choice].draw()
                        self._cells[i][j].draw()

                        self._break_walls_r(i-1, j)
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False