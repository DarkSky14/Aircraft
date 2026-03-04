import logging
import os
import time


path_log = 'library/Logs'

os.makedirs(path_log, exist_ok=True)
log = logging
log.basicConfig(
    filename = (path_log + "/" + "logs {}.log").format(time.strftime("%Y-%m-%d %H-%M-%S")),
    format = u'%(levelname)-8s [%(asctime)s.%(msecs)03d] %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    level = logging.DEBUG
)


class LoggingError(BaseException):
    pass

class Logger:
    def __init__(self):
        pass

    def log(self, text):
        return print("LOG: {}".format(text))
    
    def log_error(self, text, error):
        return print("LOG_ERROR: {} / {}".format(error, text))
    
    def critical_error(self, text):
        raise LoggingError("CRITICAL: {}".format(text))
    
