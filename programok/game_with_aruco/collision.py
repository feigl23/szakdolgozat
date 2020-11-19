from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Collision:
    def __init__(self):
        self.limit = [-17.8,-7.8,17.8]
        self.criteria = [0.4, 1.8]
        self.stop = False

    def collision(self,model,other,box):
        self.stop =False
        for i in range(0,len(box.boxes['model'])):
            if(i not in box.remove):
                if (model.y*5 + model.dist <= box.boxes['y'][i]+self.criteria[1] and model.y*5 + model.dist >= box.boxes['y'][i]-self.criteria[1]
                    and model.x*5 + model.dist <= box.boxes['x'][i]+self.criteria[1] and model.x*5 + model.dist >= box.boxes['x'][i]-self.criteria[1]):
                        self.stop = True
                        model.box =i
                        model.box_axis = model.axis

        if('y' in model.axis):
            if(model.y*5+model.dist >= self.limit[2] or model.y*5+model.dist <= self.limit[1]):
                    self.stop = True
            elif((model.y +model.dist) <= other.y+self.criteria[0] and model.x <= other.x+self.criteria[0]/2
                and model.x >= other.x-self.criteria[0]/2 and (model.y +model.dist) >= other.y-self.criteria[0]):
                    self.stop = True
        if('x' in model.axis):
            if(model.x*5+model.dist  >= self.limit[2] or model.x*5+model.dist <= self.limit[0]):
                    self.stop = True
            elif((model.x +model.dist) <= other.x+self.criteria[0] and (model.x +model.dist) >= other.x-self.criteria[0]
                and model.y <= other.y+self.criteria[0]/2 and model.y >= other.y-self.criteria[0]/2 ):
                    self.stop = True

        if(self.stop):
            model.block = True
        else:
            model.block = False
