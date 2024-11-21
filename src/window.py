from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width=None, height=None):
        self.__root = Tk()
        self.width = self.__root.winfo_screenwidth() if width is None else width
        self.height = self.__root.winfo_screenheight() if height is None else height
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=self.width, height=self.height)
        self.__canvas.pack()
        self.__running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line: 'Line', colour="black"):
        line.draw(self.__canvas, colour)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, colour):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=colour, width=2)