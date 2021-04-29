import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
TRIG = 18
ECHO = 24

print("in progress")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    GPIO.output(TRIG, False)
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        print "input = 0"

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        print "input = 1"

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print("Distance:", distance)
except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()
