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

Українська = {
    "0": "Розпочати",
    "1": "Налаштування",
    "2": "Мова",
    "3": "Рівень 1",
    "4": "Рівень 2",
    "5": "Рівень 3",
    "6": "Вихід",
    "7": "Головне Меню",
    "8": "Ввімкнуто",
    "9": "Вимкнуто",
    "10": "Музикy:",
    "11": "Рівні",
    "12": "Ефекти:",
}

Русский = {
    "0": "Начать",
    "1": "Настройки",
    "2": "Язык",
    "3": "Уровень 1",
    "4": "Уровень 2",
    "5": "Уровень 3",
    "6": "Выход",
    "7": "Главное Меню",
    "8": "Включить",
    "9": "Выключить",
    "10": "Музыка:",
    "11": "Уровни",
    "12": "Еффекты:",
}


class LanguageCreater:
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


class LanguageSetter(LanguageCreater):
    def __init__(self, config):
        self.config = config
        self._basic = English

    def language_set(self, *args) -> dict[str, str]:
        language = self._basic

        for arg in args:
            check = {"language": arg.get_name()}
            if self.config.check(check):
                self._lang = arg.get_lang()
                return self._lang
            else:
                continue

        self._lang = language
        return language
