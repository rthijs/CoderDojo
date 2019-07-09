# Gamedevelopment met Python en PyGame

## 0. Introductie

### Wat gaan we maken?

Een eenvoudig spelletje waarbij je een blokje bestuurt en andere blokken moet ontwijken.

### Wat gaan we leren?

 - Python natuurlijk!
 - We maken gebruik van de pygame bibliotheek
 - Werken met classes en functies
 - Object-georiënteerd programmeren

### Hoe gaan we te werk?

We gaan even nadenken over wat we willen maken, dat splitsen we dan in verschillende kleine taken die we makkelijk één voor één kunnen oplossen. 

We starten altijd met zo min mogelijk code om iets werkende krijgen en daar bouwen we telkens op verder.

Tussen de verschillende stappen door herschrijven we onze code, "*refactoren*" in het jargon, om ze proper en leesbaar te houden. Niet alleen de computer moet onze code kunnen lezen, ook onze vrienden en je toekomstige zelf ;)

### Vereisten

Je moet de pygame-bibliotheek installeren, als je [Thonny](https://thonny.org/) gebruikt kan je dat via *Tools* - *Manage Plug-ins...*, daar zoeken naar *pygame* en op *Install* klikken. Als je Idle of Visual Studio Code, of nog iets anders, gebruikt dan typ je in de console `pip install pygame`.

![Thonny PyGame](.README/thonnyPygame.png)

Test of het gelukt is door een script met enkel deze regel uit te voeren:

```python
import pygame
```

Als alles in orde is zie je in je console deze melding:

![Hello PyGame](.README/helloPygame.png)

Nu kunnen we er invliegen!

## 1. Veel kleintjes maken een groot

Eerst gaan we ons "probleem" opsplitsen in kleine stapjes. We willen en spel maken en dat is wat veel om zomaar ineens te doen. Daarom splitsen we het op in zo klein mogelijk stapjes. Elk stapje moet iets opleveren dat werkt en waarop we kunnen verder bouwen. Bijvoorbeeld:

    1. Een PyGame venster tonen
    2. Iets tekenen in het venster
    3. Iets laten bewegen in het venster
    4. Meerdere dingen tekenen en laten bewegen
    5. Iets laten bewegen met toetsenbordcommando's
    6. ...

Als we op dit punt gekomen zijn verzinnen we dan wel weer iets, de bedoeling nu is kunnen starten en iets hebben om naar toe te werken.

## 2. Een PyGame venster tonen

Wat is het kleinste dat we kunnen maken dat werkt? Een leeg venster! Niet zo erg spannend maar dat is wel de basis waarop we gaan bouwen. 

We hebben PyGame al geïmporteerd:

```python
import pygame
```

Voor we met de functies van PyGame kunnen werken moeten we PyGame initialiseren. Voorlopig gaan we hier niet dieper op in maar deze stap is belangrijk. Niet vergeten dus!

```python
import pygame

pygame.init()
```

Nu kunnen we een venster maken, we moeten zeggen hoe groot we het willen. De afmetingen zijn in pixels.

```python
import pygame

pygame.init()

spel_venster = pygame.display.set_mode((640, 480))
```

Dit zal wel werken maar iemand die onze code ziet zal zich terecht afvragen wat 640 en 480 zijn. Om de code leesbaarder te maken gaan we variabelen maken met een duidelijk naam en die gebruiken. Dit is beter:

```python
import pygame

pygame.init()

VENSTER_BREEDTE = 640
VENSTER_HOOGTE = 480

spel_venster = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))
```

Het resultaat is niet echt spannend:

![leeg venster](.README/pygameLeeg.png)

Maar ik heb geen errors dus alles gaat goed! 

Het venster sluiten gaat niet zoals je merkt, gebruik de rode stopknop van Thonny. Dat moeten we nog fiksen. Met een extra statement `pygame.quit()` sluiten we het PyGame-venster.

Als je het programma uitvoert merk je dat er even een zwart venster getoont wordt dat dan meteen afsluit. We moeten dus alles wat willen doen uitvoeren na het initialiseren, dat is al het voorbereidende werk zoals nuttige variabelen definiëren, en het `pygame.quit()` statement, dat heel de boel afsluit.

```python
import pygame

pygame.init()

VENSTER_BREEDTE = 640
VENSTER_HOOGTE = 480

spel_venster = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))

# Hier dingen doen!

pygame.quit()
```

## De game-lus

De game-lus is een simpele herhaling die al onze logica voor het spel bevat. Deze gaat steeds opnieuw uitgevoerd worden om meerdere keren per seconde onze game te verversen, net zoals een film bestaat uit meerdere beelden per seconde. Om deze te bouwen hebben we eerst nog wat andere zaken nodig:

 - een klok, elke tik van de klok verversen we het scherm
 - de spelstatus, om te weten of we nog aan het spelen zijn
 - een game-lus, die al het bovenstaande bevat en elke kloktik uitgevoerd wordt.
 - events, gebeurtenissen die acties in gang zetten

### De klok

We gaan een aantal keren per seconde het venster vernieuwen, dit drukken we uit in "Frames Per Second" of FPS. Laten we dit in een variabele steken, we gaan 60 keer per seconde tekenen.

```python
FPS = 60
```

PyGame voorziet een klasse "*Clock*", laten we daar een klok van instantiëren om te gebruiken in onze game.

```python
klok = pygame.time.Clock()
```

### De spelstatus

Zolang we het spel aan het spelen zijn moet het venster verversen, als we echter het venster sluiten moeten we uit de lus breken en alles aflsuiten. We gebruiken een variabele die moet bijhouden of we nog aan het spelen zijn.

```python
aan_het_spelen = True
```

We maken de variabele aan met de waarde `True`, de lus test elke keer of deze nog steeds `True` is en zo ja loopt hij nog een keer. Als we er tijdens de lus echter `False` van maken stopt de uitvoering en gaan we verder in de code na de lus.

### De game-lus

Als we aan het spelen zijn moet de lus steeds opnieuw uitgevoerd worden om alles op ons scherm te tekenen en te luisteren naar events. De frequentie waarmee dat gebeurt hebben we gedefinieerd in de variabele `FPS`

```python
while aan_het_spelen:

    # Hier onze voorwerpen tekenen
    # Testen of er events zijn
    # Eventueel de variabele aan_het_spelen False maken om te stoppen met spelen

    # Het frame genereren en tonen op het scherm
    pygame.display.update()

    # de game-klok een tik verder zetten met de snelheid die we gekozen hebben
    klok.tick(FPS)

```
Voor we naar events gaan even samenvatten wat we al hebben:

```python
import pygame

pygame.init()

VENSTER_BREEDTE = 640
VENSTER_HOOGTE = 480
FPS = 60

spel_venster = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))
klok = pygame.time.Clock()

aan_het_spelen = True

while aan_het_spelen:

    # Hier onze voorwerpen tekenen
    # Testen of er events zijn
    # Eventueel de variabele aan_het_spelen False maken om te stoppen met spelen

    # Het frame genereren en tonen op het scherm
    pygame.display.update()

    # de game-klok een tik verder zetten met de snelheid die we gekozen hebben
    klok.tick(FPS)

pygame.quit()
```

Als we dit uitvoeren zien we nog steeds een zwart venster dat we niet kunnen sluiten, behalve door op de rode stopknop van Thonny te drukken. Zo veel meer code en we zien geen verschil? Er is wel degelijk iets veranderd, in plaats van één leeg zwart venster tekenen we nu 60 lege vensters per seconde!

Nog even doorbijten, het wordt nog even moeilijk voor het leuke deel komt.

### Events

Een event is een gebeurtenis waarna we een actie kunnen doen. Dit kan een beweging van de muis zijn, een toets die ingedrukt wordt, ... of een klik op de sluitknop van het venster. Daar gaan we eerst op testen.

PyGame houdt de events die gebeuren bij en we kunnen die opvragen met `pygame.event.get()`. Omdat het er meerdere kunnen zijn zitten deze in een lijst. We gaan de events in de lijst één voor één af met een for-lus:

```python
for event in pygame.event.get():
```

Het sluit-het-venster-event is gekend in PyGame en is `pygame.QUIT`, als we dit event herkennen willen we niet meer verder spelen. We zetten dan de variabele `aan_het_spelen` op `False` zodat de lus niet meer herstart als deze iteratie voorbij is.

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        aan_het_spelen = False
```

Dit geeft dan deze code:

```python
import pygame

VENSTER_BREEDTE = 640
VENSTER_HOOGTE = 480
FPS = 60

pygame.init()
spel_venster = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))
klok = pygame.time.Clock()

aan_het_spelen = True

while aan_het_spelen:

    # Testen op events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # de speler wil het venster sluiten dus: stoppen met spelen
            aan_het_spelen = False

    # Dingen tekenen
    # TODO

    # Het frame genereren en tonen op het scherm
    pygame.display.update()

    # de game-klok een tik verder zetten met de snelheid die we gekozen hebben
    klok.tick(FPS)

pygame.quit()
```

Als we deze uitvoeren kan je het venster sluiten met de sluitknop.

Je hebt misschien gemerkt dat de code een beetje herschikt is en de commentaar aangepast. Dat heb ik gedaan omdat ik tijdens het code schrijven dacht dat het zo ordelijker en beter leesbaar zou zijn. Je moet nooit aarzelen om verbeteringen aan te brengen, dat zorgt er op iets langere termijn voor dat je sneller en met minder bugs kan programmeren.

Ik schik de code als volgt, maar je mag natuurlijk je eigen systeem gebruiken als je dat duidelijker vindt:

    - imports
    - variabelen die niet veranderen gedurende de uitvoering van het programma, geschreven met HOOFDLETTERS. In het jargon zijn dit de "statische variabelen".
    - initialiseren van objecten, zoals het spelvenster en de klok
    - andere variabelen
    - de game loop, met daarin:
        - afhandelen van events
        - tekenen, dit moeten we nog doen, vandaar de commentaar "TODO"
        - het venster verversen
        - de klok een tik vooruitzetten
    - alles opkuisen, in dit geval is `pygame.quit()` alles wat er nodig is.