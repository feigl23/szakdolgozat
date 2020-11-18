from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class isActive:

    def __init__(self):
        self.right=0
        self.left=0
        self.right_active = True
        self.left_active = False
        self.left_positions_x = [-10.5,-13.5]
        self.left_positions_y = [4,5.5]
        self.right_positions_x = [10.5,13.5]
        self.right_positions_y = [4,5.5]
    def check_spot(self,box,index):

        if (box.boxes['x'][index] >=self.left_positions_x[0] and box.boxes['x'][index] <=self.left_positions_x[1] and
        box.boxes['y'][index] >=self.left_positions_y[0] and box.boxes['y'][index] <=self.left_positions_y[1]
        and self.left_active ==True):
            if( index not in box.remove):
                box.remove.append(index)
                self.left+=1
                self.check_is_active()

        elif(box.boxes['x'][index] >=self.right_positions_x[0] and box.boxes['x'][index] <=self.right_positions_x[1] and
        box.boxes['y'][index] >=self.right_positions_y[0] and box.boxes['y'][index] <=self.right_positions_y[1]
        and self.right_active ==True):
            if( index not in box.remove):
                box.remove.append(index)
                self.right+=1
                self.check_is_active()


    def check_is_active(self):
        if self.right==2 and self.right_active:
            self.right=0
            self.right_active =False
            self.left_active=True
        if self.left ==2 and self.left_active:
            self.left=0
            self.left_active =False
            self.right_active=True
