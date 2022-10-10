#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import subprocess
 
SENSOR_PIN = 3
 
GPIO.setmode(GPIO.BCM)

GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.wait_for_edge(SENSOR_PIN, GPIO.FALLING)

flag = 0

f = open("/home/christopher/Shutdown-LOG.txt", "a")
f.write("\nBoot-time: "+ time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))
f.close()
 
def mein_callback(channel):
    # Hier kann alternativ eine Anwendung/Befehl etc. gestartet werden.
    print('Es gab eine Bewegung!')
    global flag
    flag = 0
 
GPIO.add_event_detect(SENSOR_PIN , GPIO.FALLING, callback=mein_callback)
while True:
     time.sleep(6) #alle 6 Sekunden aufgerufen
     flag = flag + 1
     print(flag)
     if flag >= 150: #In 10/Minuten wartezeit
        print("ABSCHALTEN")
        f = open("/home/christopher/Shutdown-LOG.txt", "a")
        f.write("\nShutdown: "+ time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))
        f.close()
         
        GPIO.cleanup() 
        subprocess.call(['shutdown', '-h', 'now'], shell=False)
        break

