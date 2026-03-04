if __name__ == "__main__":
    import _lib_ as my_json
    from logged import log
else:
    import clients.Backend._lib_ as my_json
    from clients.Backend.logged import log

English = {
    0:'Start',
    1:'Options', 
    2:'Language', 
    3:'Level 1', 
    4:'Level 2', 
    5:'Level 3',
    6:'Exit',
    7:'Main Menu',
    8:'On', 
    9:'Off', 
    10:'Music:', 
    11:'Level', 
    12:'Effect:'
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
    "12": "Ефекти:"
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
    "12": "Еффекты:"
    }


class LanguageCreater:
    def __init__(self, name: str, url: str, file: str = "None"):  
        self._name = name
        self._url = url
        self._lang = {}
        self._file = file
    
    def get_lang(self):
        return self._lang if self._lang != {} else print("Null dict")
    
    def set_lang(self, reader) -> dict[int, str]:
        work = reader(self._name, self._url, self._lang, self._file) 
        self._lang = work.read()

        return self._lang 
    
    def get_name(self):
        return self._name


class LanguageSetter(LanguageCreater):
    def __init__(self, config):
        self.config = config
        self._basic = English

    def language_set(self, *args) -> dict[int, str]:
        language = self._basic
    
        for arg in args:
            check = {"language": arg.get_name()}
            if self.config.check(check) == True: 
                self._lang = arg.get_lang()
                return self._lang  
            else:
                continue
                
        self._lang = language
        return language  


ENG = LanguageCreater("EN", "library/lang", "english.json")
ENG.set_lang(my_json.JsonReader)
ENGLISH = ENG.get_lang()
log.debug({"INITIALIAZE_LANGUAGE": ENG.get_name()})

UKR = LanguageCreater("UA", "library/lang", "ukrainian.json")
UKR.set_lang(my_json.JsonReader)
UKRAINIAN = UKR.get_lang()
log.debug({"INITIALIAZE_LANGUAGE": UKR.get_name()})

language = LanguageSetter(my_json.config).language_set(ENG, UKR)

log.info("LANGUAGE LOADED...")