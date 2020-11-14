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
                glPushAttrib(GL_CURRENT_BIT)
                glColor(model.color[0],model.color[1], model.color[2])
                model.walk_models[i-1].render()
                glPopAttrib()
                glPopMatrix()
                time.sleep(0.001)
            else:
                glPushMatrix()
                glScale(5,5,5)
                glTranslate(model.x,model.y,model.z)
                glRotate(model.rot_z,0,0,1)
                glPushAttrib(GL_CURRENT_BIT)
                glColor(model.color[0],model.color[1], model.color[2])
                model.walk_models[i-1].render()
                glPopAttrib()
                glPopMatrix()
                time.sleep(0.001)



    def jump(self,model,i):
            #model.z = model.z+model.dist
            glPushMatrix()
            glScale(5,5,5)
            glTranslate(model.x,model.y,model.z)
            glRotate(model.rot_z,0,0,1)
            glPushAttrib(GL_CURRENT_BIT)
            glColor(1,0,1)
            model.jump_models[i-1].render()
            glPopAttrib()
            glPopMatrix()
            time.sleep(0.001)

    def release(self,model,i):
            glPushMatrix()
            glScale(5,5,5)
            glTranslate(model.x,model.y,model.z)
            glRotate(model.rot_z,0,0,1)
            glPushAttrib(GL_CURRENT_BIT)
            glColor(1,0,1)
            model.release_models[i-1].render()
            glPopAttrib()
            glPopMatrix()
            time.sleep(0.001)

    def grab(self,model,i):
            glPushMatrix()
            glScale(5,5,5)
            glTranslate(model.x,model.y,model.z)
            glRotate(model.rot_z,0,0,1)
            glPushAttrib(GL_CURRENT_BIT)
            glColor(1,0,1)
            model.grab_models[i-1].render()
            glPopAttrib()
            glPopMatrix()
            time.sleep(0.001)
