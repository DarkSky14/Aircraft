import logging
import os
from time import strftime
from module import base_absolute_import


class Logger:
    def __init__(self):
        path_log = base_absolute_import("Logs")
        os.makedirs(path_log, exist_ok=True)
        self.file = os.path.join(path_log, "logs {}.log").format(strftime("%Y-%m-%d %H-%M-%S"))

        self.logging = logging
        self.logging.basicConfig(
            filename=self.file,
            format="[%(asctime)s.%(msecs)03d] %(levelname)-8s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.DEBUG,
        )

    def delete_log(self):
        self.logging.shutdown()
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
        self.logging.exception(msg, *args, exc_info=exc_info, stack_info=stack_info, stacklevel=stack_level, extra=extra)

    def error(self,
        msg: object,
        *args: object,
        exc_info: None | bool | tuple[type[BaseException], BaseException, None] | tuple[None, None, None] | BaseException = None,
        stack_info: bool = False,
        stack_level: int = 1,
        extra = None
        ):
        self.logging.error(msg, *args, exc_info=exc_info, stack_info=stack_info, stacklevel=stack_level, extra=extra)

    def critical(self,
        msg: object,
        *args: object,
        exc_info: None | bool | tuple[type[BaseException], BaseException, None] | tuple[None, None, None] | BaseException = None,
        stack_info: bool = False,
        stack_level: int = 1,
        extra = None
        ):
        self.logging.critical(msg, *args, exc_info=exc_info, stack_info=stack_info, stacklevel=stack_level, extra=extra)


log = Logger()
