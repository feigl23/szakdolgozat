from objloader import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Penguin:
    def __init__(self):
        self.model=OBJ("../models/Penguin/PenguinBaseMesh.obj", swapyz=True)
        self.model.rot_z=180
        self.model.x = 0
        self.model.y = 0
        self.model.z = -40
        #self.model.generate()

    def drawn(self):
        glPushMatrix()
        glEnable(GL_TEXTURE_2D)
        glRotatef(self.model.rot_z,1,0,0)
        glTranslatef(self.model.x,self.model.y,self.model.z)
        glScalef(6,6,6)
        self.model.render()
        glPopMatrix()
