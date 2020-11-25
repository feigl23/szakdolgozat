# PINGVINES Játék

A játék célja a dobozok eltüntetése, a szökőkutakba kell bele tolni őket.
Minden pingvin csak a saját színével megegyező dobozt tolhatja, egyszerre csak egy kút aktív és
pontosan annyi doboz kell bele amennyi játékos van.
Ha minden doboz eltűnik, akkor ér véget a játék,nyernek a
játékosok.  
Minden játékoshoz 4 doboz tartozik, maximum négy fő vehet részt a játékban.

#### A felhasznált modellek:
https://free3d.com/3d-model/emperor-penguin-601811.html
https://free3d.com/3d-model/fantasy-castle-40715.html
https://free3d.com/3d-model/crate-86737.html


#### A felhasznált képek:
https://miro.medium.com/max/500/1*KOj47lkJHi9w8bxAvFAvEg.jpeg


### Tesztelni a következőképpen lehet:

  El kell indítani a server.py-t, aztán pedig a game.py-t, ez egyetlen kliens-t szimulál.
  Ha nem állítódik le a server.py, de a game.py újraindítódik, akkor az már a következő
  kliensek számít.

  A modell betöltések miatt időbe telik, míg elindul a game.py.

  A teszteléshez szükséges egy kamera, egy marker (egy olyan, ami a megfelelő könyvtárba tartozik, mint images/marker.svg),
  OpenCV, PyOpenGL,aruco, python3, falcon, waitress, requests és egyéb csomagok, amiket hiányolhat a futtatás közben.

  A karaktert a w,s,a,d billentyűkkel lehet irányítani, a space-szel ugrani és az e billentyűvel tolni a dobozt.

  A program két játékosra lett tervezve ( ezt lehet bővíteni a megfelelő kezdőadatok felvételével a data.py-ban és a game.py-ban a maximum érétket)
