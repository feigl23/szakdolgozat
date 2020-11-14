from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Collision:
    def __init__(self):
        self.korlat = [-17.8,-8,17.8]
        self.criteria = 0.4

    def collision(self,model,other,box):
        if('y' in model.axis):
            for i in range(0,len(box.blue_box)):
                print(model.y*5+model.dist, box.by[i])
                if (model.y*5 + model.dist <= box.by[i]+self.criteria and model.x*5 <= box.bx[i] + self.criteria/2
                    and model.x*5 >= box.bx[i]-self.criteria/2 and model.y*5 + model.dist >= box.by[i]-self.criteria):
                        model.block = True

            for i in range(0,len(box.lilac_box)):
                if ((model.y*5 +model.dist) <= box.ly[i]+self.criteria and model.x*5 <= box.lx[i] + self.criteria/2
                    and model.x*5 >= box.lx[i]-self.criteria/2 and (model.y*5 +model.dist) >= box.ly[i]-self.criteria):
                        model.block = True

            if(model.y*5+model.dist >= self.korlat[2] or model.y*5+model.dist <= self.korlat[1]):
                    model.block = True
            elif((model.y +model.dist) <= other.y+self.criteria and model.x <= other.x+self.criteria/2
                and model.x >= other.x-self.criteria/2 and (model.y +model.dist) >= other.y-self.criteria):
                    model.block = True
            else:
                    model.block = False
        if('x' in model.axis):
            if(model.x*5+model.dist  >= self.korlat[2] or model.x*5+model.dist <= self.korlat[0]):
                    model.block = True
            elif((model.x +model.dist) <= other.x+self.criteria and model.y <= other.y+self.criteria/2
                and model.y >= other.y-self.criteria/2 and (model.x +model.dist) >= other.x-self.criteria):
                    model.block = True
            #else:
                #model.block = False
