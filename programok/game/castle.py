from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *


class Castle:
    def __init__(self):
        self.x =0
        self.y =-1
        self.z =0

    def model_init(self):
        self.model =OBJ("models/Castle/CastleOBJ.obj", swapyz=True)
        self.model.generate()

    def draw_model(self):
        self.model.render()
