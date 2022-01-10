from led.led import Led

class LedSimulator(Led):
    def on(self):
        self.logger.info("Led Simulator ON")

    def off(self):
        self.logger.info("Led Simulator OFF")