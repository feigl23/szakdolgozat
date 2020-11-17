from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *


class Box:
    def __init__(self):
        self.remove=[]
        self.is_over = False
        self.boxes ={
        "model" : [],
        "color" : [],
        "x" : [-14,-10,-6,-2,2,6,10,14,-14,-10,-6,-2,2,6,10,14],
        "y" : [13,-2,13,-2,13,-2,13,-2,-2,13,-2,13,-2,13,-2,13],
        "z" : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}


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
            self.boxes['x'][m]= self.boxes['x'][m]+dist-0.1
        self.check_spot(m)

    def check_spot(self, m):
        if (self.boxes['x'][m] >=10.5 and self.boxes['x'][m] <=13.5 and self.boxes['y'][m] >=4 and self.boxes['y'][m] <=5.5
        or self.boxes['x'][m] <=-10.5 and self.boxes['x'][m] >=-13.5 and self.boxes['y'][m] >=4 and self.boxes['y'][m] <=5.5 ):
            if( m not in self.remove):
                self.remove.append(m)
            if len(self.remove) == len(self.boxes['model']):
                self.is_over = True
