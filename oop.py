import tkinter as tk
from abc import ABCMeta, abstractmethod, abstractproperty

class Figure:
    def init(self):
        pass
    @abstractmethod
    def draw(self):
        pass

class Circle(Figure):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius         
    def draw(self, tk_canvas, pen_color):
        print(f"Drawing Circle: ({str(self.x)}, {str(self.y)}) with radius {str(self.radius)} and color {pen_color[0]}")
        tk_canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill='', outline=pen_color[1])

class Triangle(Figure):
    def __init__(self, first_point, second_point, third_point):
        self.first_point = first_point
        self.second_point = second_point
        self.third_point = third_point
    def draw(self, tk_canvas, pen_color):
        print(f"Drawing Triangle with first_point: {str(self.first_point)}, second_point: {str(self.second_point)}, " + \
                f"third_point: {str(self.third_point)} and color {pen_color[0]}")
        tk_canvas.create_polygon((self.first_point,self.second_point,self.third_point), fill='', outline=pen_color[1])

class Rectangle(Figure):
    def __init__(self, x_left_upper_angle_point, y_left_upper_angle_point, x_side, y_side):
        self.x_left_upper_angle_point = x_left_upper_angle_point
        self.y_left_upper_angle_point = y_left_upper_angle_point
        self.x_side = x_side
        self.y_side = y_side          
    def draw(self, tk_canvas, pen_color):
        print(f"Drawing Rectangle with left upper angle point x: {str(self.x_left_upper_angle_point)}, " + \
               f"left upper angle point y: {str(self.y_left_upper_angle_point)}, " + \
                f"side x: {str(self.x_side)}, side y: {str(self.y_side)} and color {pen_color[0]}")
        tk_canvas.create_rectangle((self.x_left_upper_angle_point, self.y_left_upper_angle_point), \
                                    (self.x_left_upper_angle_point + self.x_side, self.y_left_upper_angle_point + self.y_side), \
                                          fill='', outline=pen_color[1])

class Engine2D:

    canvas = []
    color_dict = {
        "Red": '#fff000000',
        "Green": "#000fff000",
        "Blue": "#000000fff",
        "Black": '#000000'
        }
    pen_color = ("Black", '#000000')

    def __init__(self, root):
        self.root = root
        self.root.geometry('800x600')
        self.root.title('Canvas Demo')
        self.tk_canvas = tk.Canvas(self.root, width=600, height=400, bg='white')
        self.tk_canvas.pack(anchor=tk.CENTER, expand=True)

    def set_pen_color(self, color):
        self.pen_color = (color, self.color_dict[color])

    def addFigure(self, figure):
        self.canvas.append(figure)

    def draw(self):
        for figure in self.canvas:
            figure.draw(self.tk_canvas, self.pen_color)
        self.root.update()
        self.tk_canvas.after(3000, self.tk_canvas.delete('all'))
        self.root.update()        

engine = Engine2D(tk.Tk())
engine.addFigure(Triangle((100, 300), (200, 200), (300, 300)))
engine.addFigure(Circle(300, 200, 90))
engine.addFigure(Rectangle(120, 120, 400, 200))
engine.draw()
engine.set_pen_color('Green')
engine.draw()
engine.set_pen_color('Red')
engine.draw()
engine.set_pen_color('Blue')
engine.draw()
pass