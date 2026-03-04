import logging
import os


path_log = 'library/log'

os.makedirs(path_log, exist_ok=True)
log = logging
log.basicConfig(
    filename = (path_log + "/" + "logs.log"),
    format = u'%(levelname)-8s [%(asctime)s] %(message)s', 
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
    

log.addLevelName(50, "SPACE")
log.log(50, "---------------------------------------")
log.log(50, "---------------------------------------")
log.log(50, "---------------------------------------")
log.log(50, "---------------------------------------")
log.log(50, "---------------------------------------")
