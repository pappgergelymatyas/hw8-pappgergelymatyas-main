---
title: Objektum Orientált Programozás
marp: true
math: mathjax
class: lead
paginate: false
footer: Prog1 - Prelogika
size: 16:9
theme: uncover
author: Bence Kovács
---

# OOP, class, package

---

## Object-Oriented Programming

Magyarul:
Objektum Orientált Programozás

---

### Mi az az OOP?

Az objektumorientált programozás egy olyan programozási paradigma, amelyben a program adatokat és az azokhoz kapcsolódó logikát, műveleteket objektumokba csomagolja.

---

### Imperatív Programozás

Az OOP az imperatív programozási paradigma része, amely lépésről lépésre halad a program célja felé. Az imperatív programozás során nem csak a tevékenységet vagy logikát adjuk meg, hanem az objektumokat is, amelyek köré építjük a programot.

---

#### Jelenleg használt imperatív paradigma:

- **Procedurális programozás**: Eljárások (függvények) segítségével utasításokat adunk a számítógépnek.

---

#### Jelenlegi kódírás:

- Vannak adataink
  - Szöveg
  - Szám
  - Logikai
  - Stb
- Vannak utasításaink
  - Állítások (if, else stb)
  - Ciklusok (for, while)
  - Függvények

---

### Spagetti Kód

A „spagetti kód” kifejezés olyan programkódot jelöl, amely rendezetlen, nehezen olvasható és követhetetlen logikai struktúrájú. Ez a kódolási stílus káoszt eredményezhet, különösen akkor, ha a program növekszik vagy bonyolultabbá válik.

---

#### Jellemzői:

- **Összevissza logikai szerkezet**: Nehezen követhető vezérlési folyamatok (pl. túl sok elágazás, összekuszált ciklusok).
- **Elérhetetlen vagy ismétlődő kódrészletek**: Az újrahasznosíthatóság és modularitás hiánya miatt sok ismétlődő kódblokk.
- **Kevés vagy semmi komment**: Megfelelő dokumentáció hiányában nehéz megérteni a kód célját és működését.
- **Globális változók túlzott használata**: Az adatok átláthatatlanná válnak, különösen ha több helyről módosítják őket.

---

#### Miért probléma a Spagetti Kód?

- **Karbantarthatóság**: Nehéz megérteni, tesztelni és javítani.
- **Olvashatóság**: Még a tapasztalt fejlesztők számára is időigényes és zavaros lehet értelmezni.
- **Hibák**: Gyakran vezet logikai hibákhoz és nehezen javítható problémákhoz.

---

#### Hogyan Kerülhető El?

- **Modularitás**: A kódot logikai részekre bontva könnyebben kezelhető, mint a nagy, összefüggő blokkok.
- **Függvények és osztályok használata**: A funkciók elválasztása és újrafelhasználhatóságuk növelése érdekében érdemes külön függvényeket vagy osztályokat használni.
- **Kommentek és dokumentáció**: Rövid leírások és dokumentációk segítenek másoknak (és magunknak) is megérteni a kódot.
- **Jól átgondolt struktúra**: Logikus kódszerkezet kialakítása a későbbi fejlesztés megkönnyítése érdekében.

---

#### Példa Spagetti Kódra:

```python
if condition1:
    for i in range(10):
        if condition2:
            do_something()
        else:
            for j in range(5):
                if condition3:
                    do_something_else()
else:
    do_another_thing()
```

---

#### Példa feladat

Írjunk egy kódot, amely megállapítja egy kutyáról, hogy jó-e

- Legyen neve a macskának
- Legyen életkora
- Legyen színe a bundájának
- Tudjuk róla, hogy él-e még

---

```python
name = "Dogy McDoogle"
color = "black"
age = 4
alive = True

if color == "black" and name == "Dogy McDoogle":
    print(name + " egy jó kutya!")
else:
    print("Oké minden kutya jó kutya")

```

---

### Hogy nézne ez ki OOP-ben?

![kutya](./img/dog.jpg)

---

### Hogyan működik az OOP?

Az OOP lényege, hogy az adatokat és az azokhoz kapcsolódó műveleteket (függvények) objektumokba csomagoljuk. Ezzel együtt a program struktúráját az objektumok köré építjük fel, nem pedig különálló eljárások köré. Ennek egyik legfontosabb eleme az **osztály**, amely az objektum alapját képezi.

---

### Osztályok és Objektumok

- **Osztályok**: Az objektumok sablonjai, amelyek attribútumokat (változókat) és metódusokat (függvényeket) tartalmaznak.
- **Objektumok**: Az osztályok példányai, amelyek saját adatokat tárolnak.

---

```python
class Kutya:
    def __init__(self, nev, szin, eletkor, el_e):
        self.nev = nev
        self.szin = szin
        self.eletkor = eletkor
        self.el_e = el_e

    def jo_kutya(self):
        if self.szin == "black" and self.nev == "Dogy McDoogle":
            print(self.nev + " egy jó kutya!")
        else:
            print("Oké minden kutya jó kutya")

# Példányosítás és használat
kutya1 = Kutya("Dogy McDoogle", "black", 4, True)
kutya1.jo_kutya()
```

---

#### Magyarázat

- `__init__`: Ez a konstruktor metódus, amely a kutya attribútumait inicializálja, amikor a Kutya osztályból példányt hozunk létre.
- `jo_kutya metódus`: Ez a metódus ellenőrzi, hogy a kutya neve és színe megegyezik-e a feltételekkel, és ennek alapján kiírja az üzenetet.

---

### Gyakori OOP Fogalmak

1. Konstruktor (Constructor)

A konstruktor egy speciális metódus, amelyet az objektum létrehozásakor hívunk meg. Pythonban a konstruktort az `__init__` metódus reprezentálja.

---

### Gyakori OOP Fogalmak

2. Getterek és Setterek

Ezekkel a metódusokkal férünk hozzá az objektum attribútumaihoz és módosíthatjuk azokat.

```python
class Ember:
    def __init__(self, nev):
        self.__nev = nev

    def get_nev(self):
        return self.__nev

    def set_nev(self, uj_nev):
        self.__nev = uj_nev
```

---

### Kiegészítő rész

Python konvenciók: Az `__name__`, `_name` ...

Pythonban az aláhúzás karakterekkel jelölhetjük a változók és metódusok speciális jelentését. Ezek a konvenciók segítenek tiszta, olvasható és karbantartható kódot írni.

---

#### `_name`

- Cél: Jelzi, hogy egy változó vagy metódus belső használatra (védett) készült.
- Viselkedés: Ez egy konvenció; a változó elérhető kívülről is, de jelzi a fejlesztőknek, hogy nem ajánlott közvetlenül elérni.

---

#### `name_`

- Cél: Elkerüli a Python beépített neveivel vagy kulcsszavaival való ütközést.
- Használat: Olyankor, amikor olyan nevet szeretnénk használni, amely Python kulcsszó vagy beépített függvény.

---

#### `__name`

- Cél: Nevek elrejtése (névösszefűzés) a névütközések elkerülésére, különösen alosztályokban.
- Viselkedés: A Python belsőleg átalakítja a változó nevét, hogy tartalmazza az osztály nevét is.

---

```python
class Osztaly:
    def __init__(self):
        self.__privat_valtozo = 42  # Névösszefűzésre kerül: _Osztaly__privat_valtozo

    def get_privat_valtozo(self):
        return self.__privat_valtozo

obj = Osztaly()
# print(obj.__privat_valtozo)  # AttributeError
print(obj._Osztaly__privat_valtozo)  # Elérhető a névösszefűzéssel
```

---

#### `__name__`

- Cél: Fenntartott különleges metódusok és változók (úgynevezett dunder vagy mágikus metódusok).
- Használat: Python speciális funkcióira és operátor túlterhelésére használja ezeket.

---

##### Gyakori Példák:

`__init__`: Objektum konstruktor.
`__str__`: Az objektum szöveges reprezentációját definiálja.
`__len__`: Az objektum hosszát adja meg a len() függvényhez.
`__name__`: A modul nevét adja meg.

---

### Öröklés (Inheritance)

- Az öröklés lehetővé teszi, hogy egy új osztály (alosztály) átvegye egy másik osztály (ősosztály) tulajdonságait és metódusait.
- Az alosztály továbbfejlesztheti vagy kiegészítheti az ősosztály működését.

---

#### Példa:

```python
class Allat:
    def mozog(self):
        print("Az állat mozog")

class Kutya(Allat):
    def ugat(self):
        print("Vau!")

kutya = Kutya()
kutya.mozog()  # Kimenet: Az állat mozog
kutya.ugat()   # Kimenet: Vau!
```

---

### Inkapszuláció (Encapsulation)

- Az inkapszuláció egy programozási technika, amellyel az osztályok belső adatai és metódusai el vannak rejtve a külvilág elől.
- Segít megvédeni a kódot, hogy kívülről ne lehessen közvetlenül elérni vagy módosítani a belső adatokat.

---

#### Példa:

```python
class BankSzamla:
    def __init__(self, egyenleg):
        self.__egyenleg = egyenleg

    def megjelenit_egyenleg(self):
        return self.__egyenleg

szamla = BankSzamla(1000)
print(szamla.megjelenit_egyenleg())  # Kimenet: 1000
```

---

### Absztrakció (Abstraction)

- Az absztrakció segítségével elrejthetjük a részleteket, és csak a lényeges információkat mutatjuk meg.
- Az absztrakció lehetővé teszi, hogy csak a legfontosabb metódusokat definiáljuk, amelyeket minden alosztálynak meg kell valósítania.

---

#### Példa:

```python
class Allat:
    def hang(self):
        raise NotImplementedError("A metódust az alosztályoknak kell megvalósítaniuk")

class Kutya(Allat):
    def hang(self):
        print("Vau!")

kutya = Kutya()
kutya.hang()  # Kimenet: Vau!
```

---

### Polimorfizmus (Polymorphism)

- A polimorfizmus lehetővé teszi, hogy ugyanaz a metódus különböző osztályokban máshogyan működjön.
- Ugyanaz a metódusnév különböző típusú objektumok esetében más-más eredményt adhat.

---

#### Példa:

```python
class Kutya:
    def hang(self):
        print("Vau!")

class Macska:
    def hang(self):
        print("Miau!")

def hangot_ad(allat):
    allat.hang()

hangot_ad(Kutya())  # Kimenet: Vau!
hangot_ad(Macska()) # Kimenet: Miau!
```

---

### Metódus Felülírás (Overriding) és Túlterhelés (Overloading)

- Felülírás (Overriding): Az alosztályban felülírhatjuk az ősosztály metódusait, hogy azok máshogyan működjenek.
- Túlterhelés (Overloading): Pythonban nincs hagyományos túlterhelés, de az alapértelmezett paraméterértékek segítségével hasonló eredmény érhető el.

---

#### Példa Felülírásra:

```python
class Kutya:
    def hang(self):
        print("Vau!")

class NagyKutya(Kutya):
    def hang(self):
        print("Mélységes ugatás!")

kutya = Kutya()
nagy_kutya = NagyKutya()

kutya.hang()      # Kimenet: Vau!
nagy_kutya.hang() # Kimenet: Mélységes ugatás!
```

---

#### Példa Túlterhelés Szimulálására:

```python
class Szamitas:
    def osszeg(self, a, b, c=0):
        return a + b + c

szamitas = Szamitas()
print(szamitas.osszeg(2, 3))       # Kimenet: 5
print(szamitas.osszeg(2, 3, 4))    # Kimenet: 9
```

---

## Python Csomagok

---

## Mi az a Python Csomag?

- Egy Python csomag egy olyan gyűjtemény, amely modulfájlokat (`.py` fájlokat) tartalmaz mappákba szervezve.
- Célja: Segít a kód újrahasznosíthatóságában, modularitásában és a kód logikus szervezésében.

---

### Python Csomagok Struktúrája

```plaintext
my_package/
│
├── __init__.py          # A csomag inicializáló fájlja
├── modul1.py            # Egy modul a csomagon belül
├── modul2.py            # Egy másik modul
│
└── subpackage/          # Alkategória (alcsomag)
    ├── __init__.py
    └── modul3.py
```

- `__init__`.py fájl: Ezzel jelöljük, hogy a mappa csomagként kezelendő. Lehet üres, de tartalmazhat importokat is.
- Modulok: Egyéni .py fájlok, amelyek függvényeket, osztályokat vagy változókat tartalmaznak.

---

### Csomagok Telepítése és Használata

- Python Csomag Index (PyPI) segítségével telepíthetünk csomagokat.
- Parancs a telepítéshez:

```plaintext
pip install <csomagnev>
```

---

### Csomagok Importálása

- Egy csomag vagy modul használatához importáljuk azt a fájlba:

```python
import my_package.modul1
from my_package.subpackage import modul3
```

---

### Python Csomagok Előnyei

- Modularitás: A kód logikusan különálló modulokba szervezhető.
- Újrafelhasználhatóság: Könnyebb a kód újrahasznosítása és megosztása más projektekkel.
- Telepítési Könnyedség: A csomagok könnyen megoszthatók és telepíthetők a pip használatával.
