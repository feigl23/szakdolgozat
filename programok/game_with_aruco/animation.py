from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *
import time

class Animation:
    def walk(self,model,i):
            if(model.block == False):
                if("y" in model.axis):
                    model.y = model.y+model.dist
                else:
                    model.x = model.x+model.dist
            glPushMatrix()
            glScale(5,5,5)
            glTranslate(model.x,model.y,model.z)
            glRotate(model.rot_z,0,0,1)
            glRotate(180,1,0,0)
            glPushAttrib(GL_CURRENT_BIT)
            glColor(model.color[0],model.color[1], model.color[2])
            model.walk_models[i-1].render()
            glPopAttrib()
            glPopMatrix()
            #time.sleep(0.00001)

    def jump(self,model,i):
            glPushMatrix()
            glScale(5,5,5)
            glTranslate(model.x,model.y,model.z)
            glRotate(model.rot_z,0,0,1)
            glRotate(180,1,0,0)
            glPushAttrib(GL_CURRENT_BIT)
            glColor(model.color[0],model.color[1], model.color[2])
            model.jump_models[i-1].render()
            glPopAttrib()
            glPopMatrix()
            #time.sleep(0.00001)

    def grab(self,model,i,box):
            if(model.box !=-1 and model.color == box.boxes['color'][model.box]):
                if("y" in model.axis):
                    model.y = model.y+model.dist
                else:
                    model.x = model.x+model.dist
                glPushMatrix()
                glScale(5,5,5)
                glTranslate(model.x,model.y,model.z)
                glRotate(model.rot_z,0,0,1)
                glRotate(180,1,0,0)
                glPushAttrib(GL_CURRENT_BIT)
                glColor(model.color[0],model.color[1], model.color[2])
                box.draw_single_box(model.box, model.box_axis, model.dist)
                model.grab_models[i-1].render()
                glPopAttrib()
                glPopMatrix()
                #time.sleep(0.00001)
            elif(model.box ==-1):
                glPushMatrix()
                glScale(5,5,5)
                glTranslate(model.x,model.y,model.z)
                glRotate(model.rot_z,0,0,1)
                glRotate(180,1,0,0)
                glPushAttrib(GL_CURRENT_BIT)
                glColor(model.color[0],model.color[1], model.color[2])
                model.grab_models[i-1].render()
                glPopAttrib()
                glPopMatrix()
                #time.sleep(0.00001)
