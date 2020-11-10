from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *


class Box:
    def __init__(self):
        self.lilac_box = []
        self.blue_box= []
        self.lx = [-18,-14,-10,-6,-2,2,6,10,14,18]
        self.ly=[-2,-2,-2,-2,-2,-2,-2,-2,-2,-2]
        self.lz =[0,0,0,0,0,0,0,0,0,0]
        self.bx =[-18,-14,-10,-6,-2,2,6,10,14,18]
        self.by =[13,13,13,13,13,13,13,13,13,13]
        self.bz=[0,0,0,0,0,0,0,0,0,0]

    def load_lilac(self):
        for i in range(0,11):
            self.lilac_box.append(OBJ("models/Crate/Crate1.obj", swapyz=True))
            self.lilac_box[i].generate()

    def load_blue(self):
        for i in range(0,10):
            self.blue_box.append(OBJ("models/Crate/Crate1.obj", swapyz=True))
            self.blue_box[i].generate()

    def draw_models(self):
        for i in range(0,10):
            glPushMatrix()
            glPushAttrib(GL_CURRENT_BIT)
            glColor(1,0,1)
            glTranslate(self.lx[i],self.ly[i],self.lz[i])
            self.lilac_box[i].render()
            glPopAttrib()
            glPopMatrix()
            glPushMatrix()
            glPushAttrib(GL_CURRENT_BIT)
            glColor(0,0.8,1)
            glTranslate(self.bx[i],self.by[i],self.bz[i])
            self.blue_box[i].render()
            glPopAttrib()
            glPopMatrix()

    def draw_blue(self,i):
        glPushMatrix()
        glPushAttrib(GL_CURRENT_BIT)
        glColor(0,0.8,1)
        glTranslate(self.bx,self.by,self.bz)
        self.blue_box[i].render()
        glPopAttrib()
        glPopMatrix()

    def draw_lilac(self,i):
        glPushMatrix()
        glPushAttrib(GL_CURRENT_BIT)
        glColor(1,0,1)
        glTranslate(self.lx,self.ly,self.lz)
        self.lilac_box[i].render()
        glPopAttrib()
        glPopMatrix()
