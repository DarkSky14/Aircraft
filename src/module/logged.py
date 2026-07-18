import logging
import os
from time import strftime
from module import absolute_import

path_log = absolute_import("Logs")

os.makedirs(path_log, exist_ok=True)
log = logging
log.basicConfig(
    filename=(os.path.join(path_log, "logs {}.log").format(strftime("%Y-%m-%d %H-%M-%S"))),
    format="%(levelname)-8s [%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
)
