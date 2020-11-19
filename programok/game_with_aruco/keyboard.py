
class Keyboard:
    def keyboardF(self,game,key):
        ## blue
        if key == b'a':
                game.blue.rot_z -=90
        elif key == b'w':
            if(game.run_blue != True):
                game.blue.anim = "walk"
                game.anim = True
                game.run_blue = True
                game.blue.length = 31
                if game.blue.rot_z == 90 or game.blue.rot_z ==-270 :
                    game.blue.axis = "x"
                    game.blue.dist =game.blue.const_dist
                elif game.blue.rot_z == 180 or game.blue.rot_z == -180:
                    game.blue.axis = "y"
                    game.blue.dist =game.blue.const_dist
                elif game.blue.rot_z == 270 or game.blue.rot_z == -90:
                    game.blue.axis = "x"
                    game.blue.dist =-1*game.blue.const_dist
                else:
                    game.blue.axis = "y"
                    game.blue.dist =-1*game.blue.const_dist
        elif key == b's':
            if(game.run_blue != True):
                game.blue.anim="walk"
                game.run_blue= True
                game.anim = True
                game.blue.length = 31
                if  game.blue.rot_z == -90 or game.blue.rot_z == 270:
                    game.blue.axis = "x"
                    game.blue.dist =game.blue.const_dist
                elif  game.blue.rot_z == 180 or game.blue.rot_z == -180:
                    game.blue.axis = "y"
                    game.blue.dist =-1*game.blue.const_dist
                elif  game.blue.rot_z == -270 or game.blue.rot_z == 90:
                    game.blue.axis = 'x'
                    game.blue.dist =-1*game.blue.const_dist
                else:
                    game.blue.axis = 'y'
                    game.blue.dist =game.blue.const_dist

        elif key ==  b'd':
                game.blue.rot_z +=90
        elif key == b'e':
            if(game.run_blue != True):
                game.blue.anim="grab"
                game.run_blue = True
                game.anim = True
                game.blue.length=16
        elif key == b' ':
            if(game.run_blue != True):
                game.blue.anim="jump"
                game.run_blue = True
                game.anim = True
                game.blue.length=21

        if(game.blue.rot_z==360 or game.blue.rot_z ==-360):
            game.blue.rot_z = 0

        ## lilac
        if key == b'l':
            game.lilac.rot_z =90
        elif key == b'i':
            if(game.run_lilac != True):
                game.lilac.anim="walk"
                game.run_lilac= True
                game.anim = True
                game.lilac.length = 31
                if game.lilac.rot_z == 90 or game.lilac.rot_z == -270:
                    game.lilac.axis="x"
                    game.lilac.dist=game.lilac.const_dist
                elif game.lilac.rot_z == 180:
                    game.lilac.axis="y"
                    game.lilac.dist=game.lilac.const_dist
                elif game.lilac.rot_z ==-180:
                    game.lilac.axis="y"
                    game.lilac.dist=game.lilac.const_dist
                elif game.lilac.rot_z == 270 or game.lilac.rot_z == -90:
                    game.lilac.axis="x"
                    game.lilac.dist=-1*game.lilac.const_dist
                else:
                    game.lilac.axis="y"
                    game.lilac.dist=-1*game.lilac.const_dist

        elif key == b'k':
            if(game.run_lilac != True):
                game.lilac.anim="walk"
                game.run_lilac = True
                game.anim = True
                game.lilac.length = 31
                if  game.lilac.rot_z == -90 or game.lilac.rot_z == 270:
                    game.lilac.axis="x"
                    game.lilac.dist=game.lilac.const_dist
                elif  game.lilac.rot_z == 180 :
                    game.lilac.axis="y"
                    game.lilac.dist=-1*game.lilac.const_dist
                elif game.lilac.rot_z == -180 :
                    game.lilac.axis="y"
                    game.lilac.dist=-1*game.lilac.const_dist
                elif  game.lilac.rot_z == -270 or game.lilac.rot_z == 90:
                    game.lilac.axis="x"
                    game.lilac.dist=-1*game.lilac.const_dist
                else:
                    game.lilac.axis="y"
                    game.lilac.dist=game.lilac.const_dist
        elif key == b'j':
                    game.lilac.rot_z =90

        elif key == b'p':
            if(game.run_lilac != True):
                game.lilac.length=21
                game.lilac.anim="jump"
                game.run_lilac = True
                game.anim = True
        elif key == b'o':
            if(game.run_lilac != True):
                game.lilac.length=16
                game.lilac.anim="grab"
                game.run_lilac = True
                game.anim = True

        if(game.lilac.rot_z==360 or game.lilac.rot_z ==-360):
            game.lilac.rot_z = 0
