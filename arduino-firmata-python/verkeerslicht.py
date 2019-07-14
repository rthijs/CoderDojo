import pyfirmata
import time

arduino = pyfirmata.Arduino('/dev/ttyACM0')

ROOD = 8
ORANJE = 9
GROEN = 10

AAN = 1
UIT = 0

def alles_uit():
    arduino.digital[ROOD].write(UIT)
    arduino.digital[ORANJE].write(UIT)
    arduino.digital[GROEN].write(UIT)
    
def maak_rood(tijd):
    alles_uit()
    arduino.digital[ROOD].write(AAN)
    time.sleep(tijd)
    
def maak_oranje(tijd):
    alles_uit()
    arduino.digital[ORANJE].write(AAN)
    time.sleep(tijd)
    
def maak_groen(tijd):
    alles_uit()
    arduino.digital[GROEN].write(AAN)
    time.sleep(tijd)
    

while True:
    maak_groen(3)
    maak_oranje(1)
    maak_rood(3)