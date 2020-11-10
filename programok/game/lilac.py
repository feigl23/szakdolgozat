from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *


class Lilac:
    def __init__(self):
        self.x =0
        self.y =3.5
        self.z =0
        self.rot_z =-180

    def model_init(self):
        self.model =OBJ("models/Penguin/PenguinBaseMesh.obj", swapyz=True)
        self.model.generate()

    def draw_model(self):
        glPushMatrix()
        glScale(5,5,5)
        glTranslate(self.x,self.y,self.z)
        glRotate(self.rot_z,0,0,1)
        print(self.rot_z)
        glPushAttrib(GL_CURRENT_BIT)
        glColor(1,0,1)
        self.model.render()
        glPopAttrib()
        glPopMatrix()
