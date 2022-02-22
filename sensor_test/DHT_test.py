import time
import RPi.GPIO as GPIO
from datetime import datetime
#import Adafruit_DHT as DHT
import adafruit_dht as DHT
import board
import sqlite3
import sys

conn = sqlite3.connect('../db/sensorsData.db')
curs=conn.cursor()

def add_data(temp, hum):
    curs.execute("INSERT INTO DHT_data values(datetime('now'),(?), (?))", (temp, hum))
    conn.commit()


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print(GPIO.getmode()==GPIO.BCM)


DHT_SENSOR = DHT.DHT22(board.D4)


while True:
    try:
        c_temp = DHT_SENSOR.temperature
        #f_temp = c_temp * (9/5) + 32
        humidity = DHT_SENSOR.humidity
        print("Temp {:.2f}C    Humidity {}%".format(c_temp, humidity))
        add_data(c_temp, humidity)


    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue

    except KeyboardInterrupt as error:
        DHT_SENSOR.exit()
        conn.close()
        print('Keyboard interrupt')
        sys.exit(0)

    except Exception as error:
        DHT_SENSOR.exit()
        conn.close()
        raise error

    time.sleep(1.0)
        
#DHT_PIN = 1111




