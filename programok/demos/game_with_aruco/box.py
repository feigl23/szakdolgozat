from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *
from is_active import *

class Box:
    def __init__(self):
        self.isActive = isActive()
        self.remove=[]
        self.is_over = False
        self.right=True
        self.left = False
        self.boxes ={
        "model" : [],
        "color" : [],
        "x" : [-14,-10,-6,-2,2,6,10,14,-14,-10,-6,-2,2,6,10,14],
        "y" : [13,-2,13,-2,13,-2,13,-2,-2,13,-2,13,-2,13,-2,13],
        "z" : [30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]}


    def load_boxes(self):
        for i in range(0,16):
            self.boxes['model'].append(OBJ("models/Crate/Crate1.obj", swapyz=True))
            self.boxes['model'][i].generate()
            if(i % 2 ==0):
                self.boxes['color'].append([1,0,1])
            else:
                self.boxes['color'].append([0,0.8,1])

    def draw_models(self):
        for i in range(0,len(self.boxes['x'])):
            if( i not in self.remove):
                glPushMatrix()
                glPushAttrib(GL_CURRENT_BIT)
                glColor(self.boxes['color'][i][0],self.boxes['color'][i][1],self.boxes['color'][i][2])
                glTranslatef(self.boxes['x'][i],self.boxes['y'][i],self.boxes['z'][i])
                self.boxes['model'][i].render()
                glPopAttrib()
                glPopMatrix()

    def draw_single_box(self,m, axis, dist):
        if(dist>0):
            dist = dist+0.1
        else:
            dist = dist-0.1
        if("y" in axis):
            self.boxes['y'][m]= self.boxes['y'][m]+dist
        else:
            self.boxes['x'][m]= self.boxes['x'][m]+dist

        self.isActive.check_spot(self,m)
        if len(self.remove) == len(self.boxes['model']):
            self.is_over = True
