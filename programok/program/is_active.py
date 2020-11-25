from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class isActive:

    def __init__(self):
        self.left_positions_x = [-10.5,-14.5]
        self.left_positions_y = [4,6.5]
        self.right_positions_x = [10.5,14.5]
        self.right_positions_y = [4,6.5]

    def check_spot(self,model,leng, game):
        if(game.user_id ==0 ):
            castle = game.own_model['castle']
        else:
            castle =game.models_data['0']['castle']

        if (model['position'][0] <=self.left_positions_x[0] and model['position'][0] >=self.left_positions_x[1] and
        model['position'][1] >=self.left_positions_y[0] and model['position'][1] <=self.left_positions_y[1]
        and castle['fountain_left']==True and game.own_model['penguin']['disap'] == False):
                game.own_model['penguin']['disap'] = True
                castle['fountain_box'] +=1
                self.check_is_active(leng, game, castle)
                return True

        elif(model['position'][0] >=self.right_positions_x[0] and model['position'][0] <=self.right_positions_x[1] and
        model['position'][1] >=self.right_positions_y[0] and model['position'][1] <=self.right_positions_y[1]
        and castle['fountain_right']==True and game.own_model['penguin']['disap'] == False):
                game.own_model['penguin']['disap'] = True
                castle['fountain_right'] +=1
                self.check_is_active( leng,game, castle)
                return True
        else:
            return False


    def check_is_active(self, leng, game, castle):
        if castle['fountain_box']%2 ==0 and castle['fountain_right']:
            castle['fountain_right'] =False
            castle['fountain_left']=True
            game.own_model['penguin']['disap'] == False


        if castle['fountain_box']%2 ==0 and castle['fountain_left']:
            castle['fountain_left'] =False
            castle['fountain_right']=True
            game.own_model['penguin']['disap'] == False
