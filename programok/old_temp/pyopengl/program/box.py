from objloader import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

class Box:
    def __init__(self):
        self.model=OBJ("../models/Crate/Crate1.obj", swapyz=True)
        self.models=[]


    def generate(self):
        for i in range(0, 82):
            self.models.append(self.model)
            self.models[i].generate()
            self.models[i].x =-24
            self.models[i].y = -33
            self.models[i].z = 15

    def drawn(self):
        for i in range(20):
            glPushMatrix() 
            glTranslate(self.models[i].x+(2*i), self.models[i].y, self.models[i].z)
            self.models[i].render()
            glPopMatrix() 
        for i in range(20, 38):
            glPushMatrix() 
            glTranslate(self.models[i].x+(2*i), self.models[i].y, self.models[i].z)
            glTranslate(-62+(i*2), -31, 15)
            self.models[i].render()
            glPopMatrix() 
        for i in range(38, 54):
            glPushMatrix() 
            glTranslate(self.models[i].x+(2*i), self.models[i].y, self.models[i].z)
            glTranslate(-97+(2*i), -29, 15)
            self.models[i].render()
            glPopMatrix() 
        for i in range(54, 66):
            glPushMatrix() 
            glTranslate(self.models[i].x+(2*i), self.models[i].y, self.models[i].z)
            glTranslate(-124+(i*2), -27, 15)
            self.models[i].render()
            glPopMatrix() 
        for i in range(66,74):
            glPushMatrix() 
            glTranslate(self.models[i].x+(2*i), self.models[i].y, self.models[i].z)
            glTranslate(-144+(2*i), -25, 15)
            self.models[i].render()
            glPopMatrix() 
        for i in range(74, 78):
            glPushMatrix() 
            glTranslate(self.models[i].x+(2*i), self.models[i].y, self.models[i].z)
            glTranslate(-156+(i*2), -23, 15)
            self.models[i].render()
            glPopMatrix() 
        for i in range(78, 80):
            glPushMatrix() 
            glTranslate(self.models[i].x+(2*i), self.models[i].y, self.models[i].z)
            glTranslate(-162+(i*2), -21, 15)
            self.models[i].render()
            glPopMatrix() 
        for i in range(80, 81):
            glPushMatrix() 
            glTranslate(self.models[i].x+(2*i), self.models[i].y, self.models[i].z)
            glTranslate(-165+(i*2), -19, 15)
            self.models[i].render()
            glPopMatrix() 
