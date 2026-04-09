import logging
from os import makedirs
from time import strftime
from module import fix_import

path_log = fix_import + "library/Logs"

makedirs(path_log, exist_ok=True)
log = logging
log.basicConfig(
    filename=(path_log + "/" + "logs {}.log").format(strftime("%Y-%m-%d %H-%M-%S")),
    format="%(levelname)-8s [%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
)
