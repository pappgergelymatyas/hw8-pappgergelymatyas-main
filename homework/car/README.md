# Class házi

Ebben a háziban az lesz a feladat, hogy csináljatok egy olyan class-t, ami egy **autót** fog reprezentálni és képes bizonyos utasítások mentén közlekedni. Alaposan olvassátok el leírást, mivel jó megoldás csak az lesz, melyben a *class*, az *attribútumok* és a *metódusok* neve is a feladatban leírtaknak megfelel! Dolgozni a **car.py** fájlban tudtok majd.

## Leírás

Az autó osztály neve legyen `Car`.

### Attribútumok 

A kocsi osztálynak három attribútuma lesz:
- `x` és `y`: Ezek lesznek az autó koordinátái, amelyek bármilyen `float` értéket felvehetnek, akár negatívat is!
- `direction`: Ez lesz az autó iránya fokban megadva, ami értelem szerűen a [0, 360] tartományon belül lesz. Figyeljetek oda, hogy 0 fokban az autó jobbra néz, ha azt egy koordináta-rendszerben képzelitek el. 

Mindegyik attribútum eleinte, tehát egy *instance* létrehozásakor, a 0 értéket vegye fel.

### Metódusok

A kocsink 3 dolgot tud majd csinálni, ezek lesznek a metódusok:
- `rotate`: Ez a method fogja forgatni a kocsi objektumot. Egy `int` paramétere lesz (az instance-en kívül), ami pedig azt fogja megadni, hogy hány fokkal forogjon el a kocsi. Ez lehet akár negatív is.
- `move`: Ez lesz majd a mozgás. Az egyetlen paramétere azt jelenti, hogy a kocsi a jelenlegi irányában pontosan hány egységnyit menjen előre. Vigyázzatok ez trükkös! Segítségetekre lehet a [trigonometria](https://en.wikipedia.org/wiki/Trigonometry) és a [`numpy`](https://numpy.org/doc/stable/reference/routines.math.html) package, de ha nagyon elakadtok vele, azt jelezzétek/kérjetek segítséget.
- `process`: Ez egy olyan függvény lesz, ami egy `str` paramétert fogad. Ez a paraméter egy jelet fog leírni, amit végre kell hajtania a kocsinak. A jel első karaktere egy betű, ami ha `M`-et vesz fel, akkor mozgást, ha pedig `R`-t akkor forgást kell végrehajtania a kocsinak. A jel ezt követő karakterei pedig egy szám (`int`), ami megmondja, hogy az adott utasítást milyen mértékben kell végrehajtani (mennyit kell mozogni vagy forogni). Tehát a jel például lehet `M42` vagy `R-221`.

### Egyéb segítség

A megoldás során érdemes tesztelni, hogy pontosan az történik-e amit szeretnétek hogy történjen. Ehhez segítségetekre lehet ha használjátok a `__repr__` metódust, hogy tudjátok pontosan hol tart a kocsi.

Emellett érdemes lehet akár ábrázolni is egy koordináta-rendszerben, amit a [`matplotlib`](https://matplotlib.org/stable/plot_types/index.html) package segítségével könnyen meg tudtok tenni.
