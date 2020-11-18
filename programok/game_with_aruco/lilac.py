from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *
from animation import *

class Lilac:
    def __init__(self):
        self.x =0
        self.y =-0.9
        self.z =5.5
        self.rot_z =-180
        self.walk_models = []
        self.jump_models= []
        self.release_models = []
        self.grab_models = []
        self.axis =""
        self.dist =0
        self.const_dist =0
        self.anim=""
        self.block = True
        self.color = [1,0,1]
        self.animation = Animation()
        self.length = 0
        self.box =0
        self.box_axis=""

    def model_init(self):
        self.model =OBJ("models/Penguin/PenguinBaseMesh.obj", swapyz=True)
        self.model.generate()
        for i in range(1,31):
            if(i<10):
                self.walk_models.append(OBJ("models/walk/RiggedPenguin_00000"+str(i)+".obj", swapyz=True))
            else:
                self.walk_models.append(OBJ("models/walk/RiggedPenguin_0000"+str(i)+".obj", swapyz=True))
            self.walk_models[i-1].generate()
        self.const_dist = 0.4 /(len(self.walk_models)-1)

        for i in range(1,21):
            if(i<10):
                self.jump_models.append(OBJ("models/jump/RiggedPenguin_00000"+str(i)+".obj", swapyz=True))
            else:
                self.jump_models.append(OBJ("models/jump/RiggedPenguin_0000"+str(i)+".obj", swapyz=True))
            self.jump_models[i-1].generate()

        for i in range(1,16):
            if(i<10):
                self.grab_models.append(OBJ("models/grab/RiggedPenguin_00000"+str(i)+".obj", swapyz=True))
            else:
                self.grab_models.append(OBJ("models/grab/RiggedPenguin_0000"+str(i)+".obj", swapyz=True))
            self.grab_models[i-1].generate()

    def draw_model(self):
        glPushMatrix()
        glScale(5,5,5)
        glTranslate(self.x,self.y,self.z)
        glRotate(self.rot_z,0,0,1)
        glRotate(180,1,0,0)
        glPushAttrib(GL_CURRENT_BIT)
        glColor(1,0,1)
        self.model.render()
        glPopAttrib()
        glPopMatrix()

    def which_animation(self,i, box):
        if("walk" in self.anim):
            self.animation.walk(self,i)
        elif("jump" in self.anim):
            self.animation.jump(self,i)
        elif("grab" in self.anim):
            self.animation.grab(self,i, box)
