from objloader import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Castle():

    def __init__(self):
        self.model = OBJ("../models/Castle/CastleOBJ.obj", swapyz=True)


    def drawn(self):
        glPushMatrix()
        glEnable(GL_TEXTURE_2D)
        #glRotatef(180,1,0,0)
        glTranslatef(0,0,-20)
        glTranslatef(0,0,0)
        glScalef(4,4,4)
        self.model.render()
        glPopMatrix()
