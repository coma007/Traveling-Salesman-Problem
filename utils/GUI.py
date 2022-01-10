from tkinter import *
import utils.constants as c


def draw_point(pt, canvas_name):
    scalex = 0.6
    scaley = 0.55
    x = 15 + pt.x * scalex
    y = 15 + pt.y * scaley
    r = 2
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas_name.create_oval(x0, y0, x1, y1)


def connect_dots(array, canvas_name):
    start = array[0]
    for pt in array[1:]:
        end = pt
        scalex = 0.6
        scaley = 0.55
        x1 = 15 + start.x * scalex
        y1 = 15 + start.y * scaley
        x2 = 15 + end.x * scalex
        y2 = 15 + end.y * scaley
        canvas_name.create_line(x1, y1, x2, y2)
        start = end


def play(population):
    root = Tk()
    myCanvas = Canvas(root, width=c.CANVAS_WIDTH, height=c.CANVAS_HEIGHT)
    myCanvas.pack()

    for pt in population:
        print(pt)
        # draw_point(pt, myCanvas)
    # connect_dots(population, myCanvas)

    root.mainloop()
