import logging
from logging import config
from ..config.config import settings


class MyFileLogger():
    # The config file for logging formatter.
    config.fileConfig(settings.log_config, defaults={"logfile": settings.log_file_path}, disable_existing_loggers=True)

    def __init__(self, name):
        self.logger=logging.getLogger(name)

    def log_debug(self, message):
        self.logger.debug(message)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_critical(self, message):
        self.logger.critical(message)