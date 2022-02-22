import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED_PIN = 13

GPIO.setup(LED_PIN,GPIO.OUT)



while True:
    GPIO.output(LED_PIN,1)
    time.sleep(1)

    GPIO.output(LED_PIN, 0)
    time.sleep(1)













