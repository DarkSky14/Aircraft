import logging
import os
from time import strftime
from module import url_fixer


class Logger:
    def __init__(self):
        path_log = url_fixer("Logs")
        os.makedirs(path_log, exist_ok=True)
        self.file = os.path.join(path_log, "logs {}.log").format(strftime("%Y-%m-%d %H-%M-%S"))

        self.logging = logging
        self.logging.basicConfig(
            filename=self.file,
            format="[%(asctime)s.%(msecs)03d] %(levelname)-8s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.DEBUG,
        )

        self.danger = False

    def delete_log(self):
        self.logging.shutdown()
        if not self.danger:
            os.remove(self.file)

    def log(self, level: int,
        msg: object,
        *args: object,
        exc_info: None | bool | tuple[type[BaseException], BaseException, None] | tuple[None, None, None] | BaseException = None,
        stack_info: bool = False,
        stack_level: int = 1,
        extra = None
        ):
        self.logging.log(level, msg, *args, exc_info=exc_info, stack_info=stack_info, stacklevel=stack_level, extra=extra)

    def info(self,
        msg: object,
        *args: object,
        exc_info: None | bool | tuple[type[BaseException], BaseException, None] | tuple[None, None, None] | BaseException = None,
        stack_info: bool = False,
        stack_level: int = 1,
        extra = None
        ):
        self.logging.info(msg, *args, exc_info=exc_info, stack_info=stack_info, stacklevel=stack_level, extra=extra)

    def debug(self,
        msg: object,
        *args: object,
        exc_info: None | bool | tuple[type[BaseException], BaseException, None] | tuple[None, None, None] | BaseException = None,
        stack_info: bool = False,
        stack_level: int = 1,
        extra = None
        ):
        self.logging.debug(msg, *args, exc_info=exc_info, stack_info=stack_info, stacklevel=stack_level, extra=extra)

    def exception(self,
             msg: object,
             *args: object,
             exc_info: None | bool | tuple[type[BaseException], BaseException, None] | tuple[
                 None, None, None] | BaseException = None,
             stack_info: bool = False,
             stack_level: int = 1,
             extra=None
             ):
        self.danger = True
        self.logging.exception(msg, *args, exc_info=exc_info, stack_info=stack_info, stacklevel=stack_level, extra=extra)

    def error(self,
        msg: object,
        *args: object,
        exc_info: None | bool | tuple[type[BaseException], BaseException, None] | tuple[None, None, None] | BaseException = None,
        stack_info: bool = False,
        stack_level: int = 1,
        extra = None
        ):
        self.danger = True
        self.logging.error(msg, *args, exc_info=exc_info, stack_info=stack_info, stacklevel=stack_level, extra=extra)

    def critical(self,
        msg: object,
        *args: object,
        exc_info: None | bool | tuple[type[BaseException], BaseException, None] | tuple[None, None, None] | BaseException = None,
        stack_info: bool = False,
        stack_level: int = 1,
        extra = None
        ):
        self.danger = True
        self.logging.critical(msg, *args, exc_info=exc_info, stack_info=stack_info, stacklevel=stack_level, extra=extra)

    def warning(self,
        msg: object,
        *args: object,
        exc_info: None | bool | tuple[type[BaseException], BaseException, None] | tuple[None, None, None] | BaseException = None,
        stack_info: bool = False,
        stack_level: int = 1,
        extra = None
        ):
        self.danger = True
        self.logging.warning(msg, *args, exc_info=exc_info, stack_info=stack_info, stacklevel=stack_level, extra=extra)


log = Logger()
