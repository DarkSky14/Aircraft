import logging
from os import makedirs
from time import strftime

path_log = 'library/Logs'

makedirs(path_log, exist_ok=True)
log = logging
log.basicConfig(
    filename = (path_log + "/" + "logs {}.log").format(strftime("%Y-%m-%d %H-%M-%S")),
    format = u'%(levelname)-8s [%(asctime)s.%(msecs)03d] %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    level = logging.DEBUG
)



    
