
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


log = Logger()