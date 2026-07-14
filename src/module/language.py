import os

from module.logged import log


English = {
    "0": "Start",
    "1": "Options",
    "2": "Language",
    "3": "Level 1",
    "4": "Level 2",
    "5": "Level 3",
    "6": "Exit",
    "7": "Main Menu",
    "8": "On",
    "9": "Off",
    "10": "Music:",
    "11": "Level",
    "12": "Effect:",
}

class LanguageCreated:
    def __init__(self, name: str, url: str, file: str = "None"):
        self._name = name
        self._url = url
        self._lang = {}
        self._file = file

    @property
    def path(self) -> str | bytes:
        return os.path.join(self._url, self._file)

    @property
    def name(self):
        return self._name

    @property
    def language(self):
        return self._lang if self._lang != {} else {0: ""}

    def set_language(self, obj_class):
        try:
            self._lang = obj_class.read(self.path)
            log.debug("LANGUAGE LOADED: %s", self._name)
        except FileNotFoundError:
            log.error("LANGUAGE_LOAD_ERROR: %s", self._file)


class LanguageSetter:
    def __init__(self, config):
        self.config = config
        self._basic = English

    def language_set(self, *args) -> dict[str, str]:
        language = self._basic

        for arg in args:
            check = {"language": arg.name}
            if self.config.check(check):
                return arg.language
            else:
                continue

        return language
