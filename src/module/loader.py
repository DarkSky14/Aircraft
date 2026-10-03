from . import url_fixer
from . import py, log

class ImageLoader:
    def __init__(self, url:str, size:tuple[int, int]):
        log.info(f"Loading image from {url}")
        try:
            self.obj = py.image.load(url_fixer(url))
            self.image = py.transform.scale(self.obj, size)
            self.size = size
            log.info(f"{url} successfully loaded")
        except FileNotFoundError:
            log.error(f"Image not found from {url}")
            self.image = None
        except Exception as e:
            log.error(f"Image load error from {url}", e, exc_info=True, stack_info=True)
            self.image = None

    def show(self):
        return self.image

    def get_obj(self):
        return self.obj

    def get_size(self):
        return self.size