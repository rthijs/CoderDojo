# Arduino en Python
Het is mogelijk om een Arduino aan te sturen en uit te lezen met Python. Hiervoor moeten beiden wel dezelfde "taal" spreken, tussen twee computers noemen we dat een *protocol*.

## Firmata
[Firmata](https://github.com/firmata/protocol) is een *protocol* om een computer (of tablet, gsm, ...) te laten communiceren met een *microcontroller*, zoals een [**Arduino**](https://nl.wikipedia.org/wiki/Arduino_(computerplatform)). Wat gaan we doen?

1. Op de Arduino laden we de Firmata firmware, dit is een *besturingssysteem* voor de Arduino. Als dit gebeurt is "spreekt" de Arduino de Firmata-taal.

2. Op onze computer schrijven we code die firmata spreekt met de Arduino. Hiervoor gebruiken we een *bibliotheek*, "library" in het Engels, zodat we niet alle details van deze taal zelf moeten programmeren. In principe kan je elke programmeertaal gebruiken die een library heeft voor Firmata, in deze oefening gaan we Python gebruiken.

## Wat hebben we nodig?

- Hardware
    - Een laptop of Raspberry Pi
    - Een Arduino, verbonden met de laptop of Pi via usb
    - Breadbord
    - Jumperkabels
    - Wat LED-jes en weerstanden

- Software
    - De Arduino IDE
    - Python geïnstalleerd op laptop of Pi
    - Een IDE voor Python, zoals Idle, Thonny of VSCode
