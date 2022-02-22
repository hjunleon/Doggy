import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED_PIN = 13
IR_PIN = 11

GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(IR_PIN, GPIO.IN)



while True:
    out = GPIO.input(IR_PIN)
    if out == 1:
        print("DETECTED")
        GPIO.output(LED_PIN,1)
    else:
        8#print("NOPE")
        GPIO.output(LED_PIN, 0)
    time.sleep(0.1)













