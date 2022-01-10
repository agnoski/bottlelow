import yaml
import logging

class ConfigManager:
    def __init__(self, path):
        logging.getLogger(self.__class__.__name__)
        self.path = path
        with open(self.path, "r") as file:
            try:
                self.config = yaml.safe_load(file)
            except yaml.YAMLError as exception:
                logging.error(exception)

    def save(self):
        with open(self.path, "w") as file:
            yaml.dump(self.config, file)