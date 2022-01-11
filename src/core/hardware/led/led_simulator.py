from core.hardware.led.led import Led

class LedSimulator(Led):
    def on(self):
        self.logger.debug("Led Simulator ON")

    def off(self):
        self.logger.debug("Led Simulator OFF")