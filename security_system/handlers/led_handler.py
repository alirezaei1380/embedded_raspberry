import RPi.GPIO as GPIO

LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)


LED_LOCK_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_LOCK_PIN, GPIO.OUT)


def turn_led_on():
    GPIO.output(LED_PIN, GPIO.HIGH)


def turn_led_off():
    GPIO.output(LED_PIN, GPIO.LOW)


def turn_lock_led_on():
    GPIO.output(LED_LOCK_PIN, GPIO.HIGH)


def turn_lock_led_off():
    GPIO.output(LED_LOCK_PIN, GPIO.LOW)
