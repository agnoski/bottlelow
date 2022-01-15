from gpiozero import LED
from core.hardware.led.led import Led

class LedRBP(Led):
    def __init__(self, led_id = 19):
        self.led = LED(led_id)

    def on(self):
        self.led.on()

    def off(self):
        self.led.off()