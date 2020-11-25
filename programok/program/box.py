from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *
from is_active import *

class Box:
    def __init__(self):
        self.isActive = isActive()
        self.is_over = False
        self.model = None


    def model_init(self):
            self.model = OBJ("models/Crate/Crate1.obj", swapyz=True)
            self.model.generate()

    def draw_model(self, model):
            glPushMatrix()
            glPushAttrib(GL_CURRENT_BIT)
            glColor(model['color'][0],model['color'][1],model['color'][2])
            glTranslatef(model['position'][0],model['position'][1],model['position'][2])
            self.model.render()
            glPopAttrib()
            glPopMatrix()

    def new_pos(self,model, axis,dist, game,anim):

        in_spot=self.isActive.check_spot(model, game.max, game)
        if(anim =="grab"):
            if(dist>0):
                dist_add = dist+0.2
            else:
                dist_add = dist-0.2
            pos=list(model['position'])
            if("y" in axis):
                pos[1] = pos[1]+dist_add
            if("x" in axis):
                pos[0] = pos[0]+dist_add
            model['position'] = tuple(pos)
            if(in_spot):
                del game.own_model['boxes'][str(model['id'])]
            game.models_data[str(game.user_id)] = game.own_model
            game.requests.upload_world_changes(game.models_data)
