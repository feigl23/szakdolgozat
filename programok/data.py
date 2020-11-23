p_model_data={ # ezek az adatok a kek pingvin kezdoadatai voltak a demoban
    "x" :0, #x kezdopizicio
    "y":3.2, #y kezdopozicio
    "z" :5.5, #z kezdopizicio
    "rot_z" : 0, #elforgatas
    'model': None, # az a modell ami akkor van felhasznalva, ha nincs animacio
    "walk_models" : [], #seta animacio modelljei
    "jump_models" : [], #ugras animacio modelljei
    "grab_models" : [], #a tolas animacio modelljei
    "axis" : "y", # a tengely amin epp mozog
    "dist" : 0, #a tavolsag amit megtesz egy animacio soran
    "const_dist" :0, # a tavolsag ugyszinten, de mivel a dist folyamatosan csökken ez a visszaallitasban segit
    "anim" : "", #melyik animacio zajlik eppen
    "block" : False, #van-e akadaly
    "color" : [0,0.8,1], #szin
    "length":0, #az animacio hossza
    "box" :-1, #melyik dobozt tollja
    "box_axis" : "" #milyen iranyba tollja a dobozt
}

box_data={
"model" : [], #a modellek tombje
"color" : [], #a modellek szine
"x" : [-14,-10,-6,-2,2,6,10,14,-14,-10,-6,-2,2,6,10,14], # x kezdopizicioi a dobozoknak
"y" : [13,-2,13,-2,13,-2,13,-2,-2,13,-2,13,-2,13,-2,13], # y kezdopizicioi a dobozoknak
"z" : [30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30], # z kezdopizicioi a dobozoknak
"removed": [], # az eltuntetett dobozok id-ja
"left": True, # azt jelzi aktiv e a bal kut
"right":False, # azt jelzi aktiv e a jobb kut
"is_over": False # akkor lesz igaz, ha az összes doboz eltunik
}
