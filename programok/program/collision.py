from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Collision:
    def __init__(self):
        self.limit = [-17.8,-7.8,17.8]
        self.criteria = [0.4, 1.8]
        self.stop = False

    def collision(self,game, model):
        id = game.user_id
        self.stop =False

        for box in models_data['box']:
            if (model['position'][1]*5 + game.dist <= box['position'][1]+self.criteria[1] and model['position'][1]*5 + game.dist >= box['position'][1]-self.criteria[1]
                and model['position'][0]*5 + game.dist <= box['position'][0]+self.criteria[1] and model['position'][0]*5 + game.dist >= box['position'][0]-self.criteria[1]):
                    self.stop = True
                    model['box'] = box['id']
                    model['box_axis'] = model['axis']
                    game.boxes[box['id']].new_pos(box,model['axis'], game)


        for other in models_data['penguins']:
            if('y' in model['axis']):
                if(model['position'][1]*5+game.dist >= self.limit[2] or model['position'][1]*5+game.dist <= self.limit[1]):
                        self.stop = True
                elif((model['position'][1] +game.dist) <= other['y'][1]+self.criteria[0] and model['position'][0] <= other['x'][0]+self.criteria[0]/2
                    and model['position'][0] >= other['x'][0]-self.criteria[0]/2 and (model['position'][1] +game.dist) >= other['y'][1]-self.criteria[0]):
                        self.stop = True
            if('x' in model['axis']):
                if(model['position'][0]*5+game.dist  >= self.limit[2] or model['position'][0]*5+game.dist <= self.limit[0]):
                        self.stop = True
                elif((model['position'][0] +game.dist) <= other['x'][0]+self.criteria[0] and (model['position'][0] +game.dist) >= other['x'][0]-self.criteria[0]
                    and model['position'][1] <= other['y'][1]+self.criteria[0]/2 and model['position'][1] >= other['y'][1]-self.criteria[0]/2 ):
                        self.stop = True

        if(self.stop):
            model.block = True
        else:
            model.block = False
        return model.block
