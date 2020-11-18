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
                glPushMatrix()
                glRotate(180,1,0,0)
                glRotate(-180,0,0,1)
                glTranslatef(0,0,-30)
                glEnable(GL_TEXTURE_2D)
                self.model.render()
                glDisable(GL_TEXTURE_2D)
                glPopMatrix()
