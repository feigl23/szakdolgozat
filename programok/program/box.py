from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *
from is_active import *

class Box:
    def __init__(self):
        self.isActive = isActive()
        self.is_over = False
        self.model = None


    def model_init(self):
            self.model = OBJ("models/Crate/Crate1.obj", swapyz=True)
            self.model.generate()

    def draw_model(self, model):
            glPushMatrix()
            glPushAttrib(GL_CURRENT_BIT)
            glColor(model['color'][0],model['color'][1],model['color'][2])
            glTranslatef(model['position'][0],model['position'][1],model['position'][2])
            self.model.render()
            glPopAttrib()
            glPopMatrix()

    def new_pos(self,model, axis, game):
        if(game.dist>0):
            dist = game.dist+0.1
        else:
            dist = game.dist-0.1
        if("y" in axis):
            model['position'][1]= model['position'][1]+dist
        else:
            model['position'][0]= model['position'][0]+dist
        self.isActive.check_spot(game.fountain,box, game.max)
        #if len(self.remove) == len(self.boxes['model']):
        #    self.is_over = True
