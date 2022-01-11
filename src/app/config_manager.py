import logging
import yaml

class ConfigManager:
    def __init__(self, path):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.path = path
        with open(self.path, "r") as file:
            try:
                self.config = yaml.safe_load(file)
            except yaml.YAMLError as exception:
                self.logger.error(exception)

    def save(self):
        with open(self.path, "w") as file:
            self.logger.info("Saving config...")
            yaml.dump(self.config, file)