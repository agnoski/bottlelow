from led.led import Led
from gpiozero import LED

class LedRBP(Led.Led):
    def __init__(self, led_id = 19):
        self.led = LED(led_id)

    def on(self):
        self.led.on()

    def off(self):
        self.led.off()