
class Keyboard:
    def keyboardF(self,model,peng,game,key):

        if key == b'a':
                model['rot_z'] -=90
        elif key == b'w':
                model['anim'] = "walk"
                model['length'] = 31
                model["anim_i"] =0
                if model['rot_z'] == 90 or model['rot_z'] ==-270 :
                    model['axis'] = "x"
                    peng.dist =peng.const_dist
                elif model['rot_z'] == 180 or model['rot_z'] == -180:
                    model['axis'] = "y"
                    peng.dist =peng.const_dist
                elif model['rot_z'] == 270 or model['rot_z'] == -90:
                    model['axis'] = "x"
                    peng.dist =-1*peng.const_dist
                else:
                    model['axis'] = "y"
                    peng.dist =-1*peng.const_dist
        elif key == b's':
                model['anim']="walk"
                model['length'] = 31
                model["anim_i"] =0
                if  model['rot_z'] == -90 or model['rot_z'] == 270:
                    model['axis'] = "x"
                    peng.dist =peng.const_dist
                elif  model['rot_z'] == 180 or model['rot_z'] == -180:
                    model['axis'] = "y"
                    peng.dist =-1*peng.const_dist
                elif  model['rot_z'] == -270 or model['rot_z'] == 90:
                    model['axis'] = 'x'
                    peng.dist =-1*peng.const_dist
                else:
                    model['axis'] = 'y'
                    peng.dist =peng.const_dist

        elif key ==  b'd':
                model['rot_z'] +=90
        elif key == b'e':
                model['anim']="grab"
                model['length']=16
                model["anim_i"] =0
        elif key == b' ':
                model['anim']="jump"
                model['length']=21
                model["anim_i"] =0
        if(model['rot_z']==360 or model['rot_z'] ==-360):
            model['rot_z'] = 0
        game.models_data[str(game.user_id)] = game.own_model
        game.requests.upload_world_changes(game.models_data)
