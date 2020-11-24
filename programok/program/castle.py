from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *

class Castle:
    def model_init(self):
        self.model =OBJ("models/Castle/CastleOBJ.obj", swapyz=True)
        self.model.generate()

    def draw_model(self, model):
        glPushMatrix()
        glRotate(180,1,0,0)
        glRotate(-180,0,0,1)
        glTranslatef(model['position'][0],model['position'][1],model['position'][2])
        glEnable(GL_TEXTURE_2D)
        self.model.render()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()
