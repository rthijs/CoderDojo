import pyfirmata

arduino = pyfirmata.Arduino('/dev/ttyACM0')

arduino.digital[13].write(1)