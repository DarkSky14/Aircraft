import json
import os

if __name__ == "__main__":
    from logged import log
else: 
    try:
        from clients.module.logged import log
    except ImportError:
        from logged import log


class _DLib: #Correct
    def __init__(self, name: str, url: str, dict: dict, file: str = "None"):
        self._name = name
        self._url = url
        self._dict = dict
        self._file = file

    def get_name(self):
        return self._name

    def get_url(self):
        return self._url

    def get_dict(self):
        return self._dict

    def get_file(self):
        return self._file
    
    def get_value(self, argID: str):
        return dict.get(self._dict, argID)

    def update_name(self, new_name: str):
        self._name = new_name

    def update_url(self, new_url: str):
        self._url = new_url

    def update_dict(self, new_dict: dict):
        self._dict.update(new_dict)

    def update_file(self, new_file: str):
        self._file = new_file

    def clear_dict(self):
        self._dict.clear()


class CheckedDict(_DLib):
    def __init__(self):
        pass

    def check(self, args: dict, script = None):
        key = args.keys().__str__().lstrip("dict_keys").strip("([''])")

        if args != {key: self.get_value(key)}:
            return False
            
        else: 
            try:
                script() #type: ignore
            except TypeError:
                script  #type: ignore
            return True       


class JsonReader(_DLib):
    def __init__(self, name: str, url: str, data: dict, file: str = "None"):
        _DLib.__init__(self, name, url, data, file)
    
    def read(self, encoding = "utf-8"):
        with open(self._url + "/" + self._file, "r", encoding = encoding) as file:
            data = json.load(file)
            self.update_dict(data)
            return data


class JsonWriter(_DLib):
    def __init__(self, name: str, url: str, data: dict, file: str = "None"):
        _DLib.__init__(self, name, url, data, file)

    def write(self, args: dict, encoding = None):
        data = self._dict.copy()
        data.update(args)

        self._dict.update(data)
        os.makedirs(self._url, exist_ok=True)

        with open((self._url + "/" + self._file), "w", encoding=encoding) as file:
            json.dump(data, file, indent = 4) 


class JsonWorker(JsonReader, JsonWriter, CheckedDict, _DLib):
    def __init__(self, name: str, url: str, data: dict, file: str = "None"):
        _DLib.__init__(self, name, url, data, file)
        JsonWriter.__init__(self, name, url, data, file)
        JsonReader.__init__(self, name, url, data, file)

    def reader(self, encoding = "utf-8"):
        try: 
            with open(self._url + "/" + self._file, "r", encoding = encoding) as file:
                data = json.load(file)
                self.update_dict(data)
                log.info({f"Load {self.get_name()}": self.get_dict()})
                return data
            
        except FileNotFoundError as fnfe: 
            log.exception({"File not found, creating new file...": fnfe})
            self.writer(self._dict)

        except json.decoder.JSONDecodeError as jde:
            log.exception({"File void or crash, recording...": jde})
            self.writer(self._dict)
        except:
            log.critical("Undefined error...", stack_info=True)

    def writer(self, args: dict, encoding = "utf-8"):
        data = self._dict.copy()
        data.update(args)

        self._dict.update(data)
        os.makedirs(self._url, exist_ok=True)

        with open((self._url + "/" + self._file), "w", encoding = encoding) as file:
            json.dump(data, file, indent = 4) 
         

config = JsonWorker(
    "config",
    "library/data",
    {
        "level": 1, 
        "effect": "True", 
        "music": "True", 
        "language": "EN"
    },
    "config.json"
)
config.reader()

temp = JsonWorker(
    "temp",
    "none",
    {"musicID": "None"}
)
log.debug({"INITIALIAZE_TEMP": temp.get_dict()})