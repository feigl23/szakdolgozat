class Data:
    def getdata(self):
        models_data = {
        '0':{'penguin':{
            "id" :0,
            "position":(0,3.2,5.5),
            "rot_z" : 180,
            "axis" : "y",
            "anim" : "",
            "color" : [1,0,1],
            "length":0,
            "box" :-1,
            "box_axis" : "" ,
            "anim_i":0,
            "disap": False
            },
            'boxes':{
            '1':{
            "id" :1,
            "color" : [1,0,1],
            "position" : (-14,13,30),
            },
            '2':{
            "id" :2,
            "color" : [1,0,1],
            "position" : (-10,-2,30),
            },
            '3':{ "id" :3,
            "color" : [1,0,1],
            "position" : (-6,13,30),
            },
            '4':{
            "id" :4,
            "color" : [1,0,1],
            "position" : (-2,-2,30),
            }},
            'castle':{
                "position" : (0,0,-30),
                "fountain_left": True,
                "fountain_right": False,
                "fountain_box":0
        }},
        '1':{'penguin':{
            "id" :1,
            "position":(0,-0.9,5.5),
            "rot_z" : 0,
            "axis" : "y",
            "anim" : "",
            "color" : [0,0.8,1],
            "length":0,
            "box" :-1,
            "box_axis" : "" ,
            "anim_i":0,
            "disap":False
            },
            'boxes':{
            '5':{
            "id" :5,
            "color" : [0,0.8,1],
            "position" : (-14,-2,30),
            },
            '6':{
            "id" :6,
            "color" : [0,0.8,1],
            "position" : (-10,13,30),
            },
            '7':{ "id" :7,
            "color" : [0,0.8,1],
            "position" : (-6,-2,30),
            },
            '8':{
            "id" :8,
            "color" : [0,0.8,1],
            "position" : (-2,13,30),
            }},
            'castle':{
                "position" : (0,0,-30),
        }}}
        return models_data
