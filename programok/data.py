p_model_data={ # ezek az adatok a kek pingvin kezdoadatai voltak a demoban
    "position":(0,3.2,5.5),
    "rot_z" : 0, #elforgatas
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
"color" : [], #a modell szine
"position" : (-14,13,30), # a modell pozicioja
"removed": [], # az eltuntetett dobozok id-ja ez lehet igazábol egy olyan valtozo is gondolom, hogy el van vagy nincs eltuntetve
"left": True, # azt jelzi aktiv e a bal kut
"right":False, # azt jelzi aktiv e a jobb kut
"is_over": False # akkor lesz igaz, ha az összes doboz eltunik
}
