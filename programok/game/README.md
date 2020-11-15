# PINGVINES Játék

A játék célja a dobozok eltüntetése, a szökőkutakba kell bele tolni őket.
Minden pingvin csak a saját színével megegyező dobozt tolhatja, különben
véget ér a játék, a játékosok veszettek.
Ha minden doboz eltűnik, akkor ér véget a játék, ebben az esetben nyertek a
játékosok.  

### animation.py:

    Az animációk megjelenítésére használható osztály. Minden karakter meghívja.
    Függvényei a walk, jump és grab.
    A walk a séta animációt valósítja meg a megfelelő irányba a kapott
    paraméterek alapján.
    A walk a séta animációt valósítja meg.
    A grab függvényben két lehetőség van: amikor van mit tolni, tehát van doboz
    a közelben és mikor nem. Ha nincs simán lepörög az animáció, ha van, akkor
    a karakter halad a megfelelő irányba és tolja maga előtt a dobozt. (a doboz
    mozgását a Box osztály valósítja meg)

### blue.py és lilac.py:

    A karakterek modelljeinek betöltése és animáció nélküli kirajzolása történik
    itt. Továbbá egy olyan függvény is van az osztályban, ami az animáció meghatározását
    végzi.

### castle.py:

    Betölti és rendereli a kastélyt.

### collision.py:

    Az ütközésvizsgálatot végző osztály. Egyetlen függvénnyel rendelkezik, ami
    minden karakter pozíció váltásakor meghívódik.
    Nem a teljes távot vizsgálja, hanem az adott i-dik modellhez tartozó új pozíciót.
    Megnézi a modellek egymáshoz való helyzetét, a modell dobozokhoz való helyzetét,
    valamint azt, hogy a játéktérben maradt-e.

### direct_animation.py:

    Az animáció irányító osztály. Meghatározza, hogy a pozícióváltás melyik
    modellere vonatkozik, meghívja az animációt meghatározó függvényt,
    meghívja az ütközésvizsgálatot végző függvényt, majd az utolsó mozdulatkor
    vissza állítja és hamissá teszi a megfelelő változókat a következő animációhoz.

### game.py:

    A játék fő eleme, innen hívódik meg minden más, ami a játékhoz szükséges.

### keyboard.py:

    Az inputokat kezeli és minden szükséges változónak megadja a megfelelő értéket.
    A kék pingvin a w,s,a,d,space,e a lila a i,j,k,o,p billentyűket használja.
