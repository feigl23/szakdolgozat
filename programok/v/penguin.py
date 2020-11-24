from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *

class Penguin:
    def __init__(self):
        self.model = None
        self.walk_models = []
        self.jump_models = []
        self.grab_models = []
        self.dist = 0
        self.const_dist =0
        self.block = False

    def model_init(self):
        self.model = OBJ("models/Penguin/PenguinBaseMesh.obj", swapyz=True)
        self.model.generate()
        #for i in range(1,31):
        #    if(i<10):
        #        self.walk_models.append(OBJ("models/walk/RiggedPenguin_00000"+str(i)+".obj", swapyz=True))
        #    else:
        #        self.walk_models.append(OBJ("models/walk/RiggedPenguin_0000"+str(i)+".obj", swapyz=True))
        #    self.walk_models[i-1].generate()

        self.const_dist = 0.4 / (len(self.walk_models)-1)

        #for i in range(1,21):
        #    if(i<10):
         #        self.jump_models.append(OBJ("models/jump/RiggedPenguin_00000"+str(i)+".obj", swapyz=True))
        #    else:
        #        self.jump_models.append(OBJ("models/jump/RiggedPenguin_0000"+str(i)+".obj", swapyz=True))
        #    self.jump_models[i-1].generate()

        for i in range(1,16):
            if(i<10):
                self.grab_models.append(OBJ("models/grab/RiggedPenguin_00000"+str(i)+".obj", swapyz=True))
            else:
                self.grab_models.append(OBJ("models/grab/RiggedPenguin_0000"+str(i)+".obj", swapyz=True))
            self.grab_models[i-1].generate()

    def draw_model(self, model):
        glPushMatrix()
        glScale(5,5,5)
        glTranslate(model['position'][0],model['position'][1], model['position'][2])
        glRotate(model['rot_z'],0,0,1)
        glRotate(180,0,1,0)
        glPushAttrib(GL_CURRENT_BIT)
        glColor(model['color'][0], model['color'][1], model['color'][2])
        self.model.render()
        glPopAttrib()
        glPopMatrix()
