from objloader import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Castle():

    def __init__(self):
        self.model = OBJ("../models/Castle/CastleOBJ.obj", swapyz=True)


    def drawn(self):
        glPushMatrix()
        glRotatef(180,1,0,0)
        glTranslatef(0,0,60)
        glScalef(0.4,0.4,0.4)
        glEnable(GL_TEXTURE_2D)
        self.model.render()
        glPopMatrix()
