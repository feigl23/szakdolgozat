from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import cv2
from animation import *

class DirectDraw:
    def __init__(self):
        self.animation = Animation()

    def direct(self, model_d, game):
                if( model_d['anim'] != ""):
                    self.which_animation(model_d, game.penguins[model_d['id']], game.user_id, game)
                else:
                    game.penguins[model_d['id']].draw_model(model_d)


    def which_animation(self,model_d,peng, id, game):
        if model_d['id'] == id:
            block = game.collision.collision(peng, model_d, game.models_data)
        else:
            block =  False
        if(model_d['anim_i'] == (model_d['length']-1)):
            model_d['anim_i'] = -1
            model_d['anim'] = ""
        if(model_d['anim_i'] != -1):
            if("walk" in model_d['anim']):
                self.animation.walk(model_d, peng,model_d['anim_i'])
            elif("jump" in model_d['anim']):
                self.animation.jump(model_d, peng,model_d['anim_i'])
            elif("grab" in model_d['anim']):
                self.animation.grab(model_d, peng,model_d['anim_i'])
            model_d['anim_i'] +=1
