from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *
import time

class Animation:
    def walk(self,model,peng,index):
            if(peng.block == False):
                if("y" in model["axis"]):
                    model['position'][1] = model["position"][1] + peng.dist
                if("x" in model['axis']):
                    model['position'][0] = model['position'][0] + peng.dist
            glPushMatrix()
            glScale(5,5,5)
            glTranslate(model['position'][0], model['position'][1], model['position'][2])
            glRotate(model['rot_z'],0,0,1)
            glRotate(180,0,1,0)
            glPushAttrib(GL_CURRENT_BIT)
            glColor(model['color'][0],model['color'][1], model['color'][2])
            peng.walk_models[index-1].render()
            glPopAttrib()
            glPopMatrix()


    def jump(self,model,peng, ind):
            glPushMatrix()
            glScale(5,5,5)
            glTranslate(model['position'][0],model['position'][1],model['position'][2])
            glRotate(model['rot_z'],0,0,1)
            glRotate(180,0,1,0)
            glPushAttrib(GL_CURRENT_BIT)
            glColor(model['color'][0],model['color'][1], model['color'][2])
            peng.jump_models[ind-1].render()
            glPopAttrib()
            glPopMatrix()

    def grab(self,model,peng,i_n):
            if(model['box'] !=-1):
                if("y" in model['axis']):
                    model['position'][1] = model['position'][1]+peng.dist
                else:
                    model['position'][0] = model['position'][0]+peng.dist
                glPushMatrix()
                glScale(5,5,5)
                glTranslate(model['position'][0],model['position'][1],model['position'][2])
                glRotate(model['rot_z'],0,0,1)
                glRotate(180,0,1,0)
                glPushAttrib(GL_CURRENT_BIT)
                glColor(model['color'][0],model['color'][1], model['color'][2])
                peng.grab_models[i_n-1].render()
                glPopAttrib()
                glPopMatrix()
            else:
                glPushMatrix()
                glScale(5,5,5)
                glTranslate(model['position'][0],model['position'][1],model['position'][2])
                glRotate(model['rot_z'],0,0,1)
                glRotate(180,0,1,0)
                glPushAttrib(GL_CURRENT_BIT)
                glColor(model['color'][0],model['color'][1], model['color'][2])
                peng.grab_models[i_n-1].render()
                glPopAttrib()
                glPopMatrix()
