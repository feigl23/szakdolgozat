from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class isActive:

    def __init__(self):
        self.right=0
        self.left=0
        self.left_positions_x = [-10.5,-14.5]
        self.left_positions_y = [4,6.5]
        self.right_positions_x = [10.5,14.5]
        self.right_positions_y = [4,6.5]
        self.colors = []
        self.leng = 2 ## az agensek szama lesz

    def check_spot(self,box,index):
        if (box.boxes['x'][index] <=self.left_positions_x[0] and box.boxes['x'][index] >=self.left_positions_x[1] and
        box.boxes['y'][index] >=self.left_positions_y[0] and box.boxes['y'][index] <=self.left_positions_y[1]
        and box.left==True and box.boxes['color'][index] not in self.colors):
            if( index not in box.remove):
                box.remove.append(index)
                self.colors.append(box.boxes['color'][index])
                self.left+=1
                self.check_is_active(box)

        elif(box.boxes['x'][index] >=self.right_positions_x[0] and box.boxes['x'][index] <=self.right_positions_x[1] and
        box.boxes['y'][index] >=self.right_positions_y[0] and box.boxes['y'][index] <=self.right_positions_y[1]
        and box.right==True and box.boxes['color'][index] not in self.colors):
            if( index not in box.remove):
                box.remove.append(index)
                self.colors.append(box.boxes['color'][index])

                self.right+=1
                self.check_is_active(box)

    def check_is_active(self,box):
        if self.right==self.leng and box.right:
            self.right=0
            box.right =False
            box.left=True
            self.colors = []


        if self.left ==self.leng and box.left:
            self.left=0
            box.left =False
            box.right=True
            self.colors = []
