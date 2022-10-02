import RPi.GP10 as GP10
import dht11
from time import sleep
from datetime import date, datetime

GP10.setwarnings(False)
GP10.setmode(GP10.BCM)
GP10.cleanup()

f=open("data.txt","a")

while True:
    now=datetime.utcnow()
    now_str=now.strftime('%Y.%m.%d %H:%M:%S')
    instance=dht11,DHT11(pin=23)
    result=instance.read()
    if result.is_valid():
        payload={"timestemp":"'=now_str='","temperature"'+str(result.temperature)='",humidity":'+str(result.humidity)+'}
        print(payload)
        f.writelines(payload+'/n')
        f.close()
        f.open('data.txt',"a")
        sleep(4)
