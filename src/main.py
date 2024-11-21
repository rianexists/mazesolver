import sys
from maze import Maze
from window import Line, Window, Point
from cell import Cell

def main():
    num_rows = 32
    num_cols = 36
    margin = 50

    sys.setrecursionlimit(10000)
    win = Window(800, 600)

    cell_size_x = (win.width - 2 * margin) / num_cols
    cell_size_y = (win.height - 2 * margin) / num_rows

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    print("maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("maze can not be solved!")
    else:
        print("maze solved!")

    win.wait_for_close()

main()