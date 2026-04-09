try:
    from logged import log
except ImportError:
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

    def get_lang(self):
        return self._lang if self._lang != {} else {0: ""}

    def set_lang(self, reader):
        work = reader(self._name, self._url, self._lang, self._file)
        try:
            self._lang = work.read()
            log.debug({"LANGUAGE LOADED:": self._name})
        except FileNotFoundError:
            log.error({"LANGUAGE_LOAD_ERROR": self._file})

    def get_name(self):
        return self._name


class LanguageSetter:
    def __init__(self, config):
        self.config = config
        self._basic = English

    def language_set(self, *args) -> dict[str, str]:
        language = self._basic

        for arg in args:
            check = {"language": arg.get_name()}
            if self.config.check(check):
                return arg.get_lang()
            else:
                continue

        return language
