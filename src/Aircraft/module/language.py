from Aircraft.module.FileWorker import Lib, reader
from Aircraft.module.logger import log


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


class LanguageCreated(Lib):
    def __init__(self, name: str, url: str, file: str):
        self._lang = {}
        super().__init__(name, url, self._lang, file)
        try:
            self.data = reader(self.path)
        except FileNotFoundError:
            self.data = {}
            log.warning(f"Language %s not found.", self.name)

    @property
    def language(self) -> dict:
        return self.data


class LanguageSetter:
    def __init__(self, config):
        self.config = config
        self._basic = English

    def set_language(self, obj: dict):
        self._basic = obj

    def get_language(self):
        return self._basic

    def checking_typical_language(self, *args) -> dict[str, str]:
        for arg in args:
            check = {"language": arg.name}
            if self.config.check(check):
                self._basic = arg.language
                return arg.language
        return self._basic
