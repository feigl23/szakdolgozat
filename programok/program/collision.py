from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Collision:
    def __init__(self):
        self.limit = [-17.8,-7.8,17.8]
        self.criteria = [0.4, 1.8]
        self.stop = False

    def collision(self,peng,model, models_data, game):
        self.stop =False

        for l in models_data:
            for m in models_data[l]['boxes']:
                if (model['position'][1]*5 + peng.dist <= models_data[l]['boxes'][m]['position'][1]+self.criteria[1] and model['position'][1]*5 + peng.dist >= models_data[l]['boxes'][m]['position'][1]-self.criteria[1]
                    and model['position'][0]*5 + peng.dist <= models_data[l]['boxes'][m]['position'][0]+self.criteria[1] and model['position'][0]*5 + peng.dist >= models_data[l]['boxes'][m]['position'][0]-self.criteria[1]):
                        self.stop = True
                        model['box'] = models_data[l]['boxes'][m]['id']
                        model['box_axis'] = model['axis']
                        if(model['color'] == models_data[l]['boxes'][m]['color']):
                            game.boxes[models_data[l]['boxes'][m]['id']].new_pos(game.own_model["boxes"][m],model['axis'], peng.dist,game, model['anim'])


        if('y' in model['axis']):
            if(model['position'][1]*5+peng.dist <= self.limit[1] or model['position'][1]*5+peng.dist >= self.limit[2]):
                self.stop = True
        if('x' in model['axis']):
            if(model['position'][0]*5+peng.dist  <= self.limit[0] or model['position'][0]*5+peng.dist >= self.limit[2]):
                self.stop = True

        for k in models_data:
            if(k != str(model['id'])):
                if('y' in model['axis']):
                    if((model['position'][1] +peng.dist) <= models_data[k]['penguin']['position'][1]+self.criteria[0] and model['position'][0] <= models_data[k]['penguin']['position'][0]+self.criteria[0]/2
                        and model['position'][0] >= models_data[k]['penguin']['position'][0]-self.criteria[0]/2 and (model['position'][1] +peng.dist) >= models_data[k]['penguin']['position'][1]-self.criteria[0]):
                            self.stop = True
                if('x' in model['axis']):
                    if((model['position'][0] +peng.dist) <= models_data[k]['penguin']['position'][0]+self.criteria[0] and (model['position'][0] +peng.dist) >= models_data[k]['penguin']['position'][0]-self.criteria[0]
                        and model['position'][1] <= models_data[k]['penguin']['position'][1]+self.criteria[0]/2 and model['position'][1] >= models_data[k]['penguin']['position'][1]-self.criteria[0]/2 ):

                            self.stop = True

        if(self.stop):
            block = True
        else:
            block = False
        return block
