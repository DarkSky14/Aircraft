from module.FileWorker import JsonWorker


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


class LanguageCreated(JsonWorker):
    def __init__(self, name: str, url: str, file: str):
        self._lang = {}
        super().__init__(name, url, self._lang, file)

    @property
    def language(self):
        return self.data if self.data != {} else {}

    def set_language(self, obj_class):
        self.data = obj_class.reader(self)


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
        return language
