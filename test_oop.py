import pytest
from oop import Engine2D, Circle, Triangle, Rectangle
import tkinter as tk
engine = Engine2D(tk.Tk())

def test_check_engine_can_add_circle():    
    engine.addFigure(Circle(300, 200, 90))
    assert len(engine.canvas) == 1
    assert engine.canvas[0].x == 300
    assert engine.canvas[0].y == 200
    assert engine.canvas[0].radius == 90

def test_check_engine_can_add_triangle():    
    engine.addFigure(Triangle((100, 300), (200, 200), (300, 300)))
    assert len(engine.canvas) == 2
    assert engine.canvas[1].first_point == (100, 300)
    assert engine.canvas[1].second_point == (200, 200)
    assert engine.canvas[1].third_point == (300, 300)

def test_check_engine_can_add_rectangle():    
    engine.addFigure(Rectangle(120, 120, 400, 200))
    assert len(engine.canvas) == 3
    assert engine.canvas[2].x_left_upper_angle_point == 120
    assert engine.canvas[2].y_left_upper_angle_point == 120
    assert engine.canvas[2].x_side == 400
    assert engine.canvas[2].y_side == 200
            
def test_check_engine_can_clear_canvas():    
    engine.draw()
    assert len(engine.canvas) == 0

def test_check_engine_can_set_color():
    engine.addFigure(Circle(400, 350, 50))
    engine.set_pen_color('Red')
    engine.draw()
    assert engine.pen_color[0] == 'Red'
    engine.addFigure(Rectangle(200, 200, 100, 100))
    engine.set_pen_color('Green')
    engine.draw()
    assert engine.pen_color[0] == 'Green'