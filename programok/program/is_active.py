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

    def check_spot(self,fountain,model,leng):
        if (model['position'][0] <=self.left_positions_x[0] and model['position'][0] >=self.left_positions_x[1] and
        model['position'][1] >=self.left_positions_y[0] and model['position'][1] <=self.left_positions_y[1]
        and fountain['left']==True and model['color'] not in self.colors):
                self.colors.append(model['color'])
                self.left+=1
                self.check_is_active(fountain, leng)
                return True

        elif(model['position'][0] >=self.right_positions_x[0] and model['position'][0] <=self.right_positions_x[1] and
        model['position'][1] >=self.right_positions_y[0] and model['position'][1] <=self.right_positions_y[1]
        and fountain['right']==True and model['color'] not in self.colors):
                self.colors.append(model['color'])
                self.right+=1
                self.check_is_active(fountain, leng)
                return True

    def check_is_active(self,fountain, leng):
        if self.right == leng and fountain.right:
            self.right=0
            fountain['right'] =False
            fountain['left']=True
            self.colors = []


        if self.left ==leng and fountain.left:
            self.left=0
            fountain['left'] =False
            fountain['right']=True
            self.colors = []
