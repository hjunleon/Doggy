import spidev
import time

spi = spidev.SpiDev()
spi.open(0,1)

def BytesToHex(Bytes):
    return ''.join(["0x%02X " % x for x in Bytes]).strip()



try:
    while True:
        resp = spi.xfer2([0x01, 0x02])
        print(BytesToHex(resp))
        time.sleep(1)

except KeyboardInterrupt:
    spi.close()
