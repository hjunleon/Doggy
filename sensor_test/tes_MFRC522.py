import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED_PIN = 13


GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN,GPIO.OUT)

reader = SimpleMFRC522()


while True:

    try: 
        text = input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("WRITTEN")

        GPIO.output(LED_PIN,1)
        time.sleep(1)

        GPIO.output(LED_PIN, 0)
        time.sleep(1)

    finally:
        GPIO.cleanup()













