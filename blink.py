import machine
import time
from picozero import pico_led

while True:
  pico_led.on()
  time.sleep(1)
  pico_led.off()
  time.sleep(1)