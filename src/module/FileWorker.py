import json
from os import makedirs

try:
    from module.logged import log
except ImportError:
    from logged import log


class Lib:
    def __init__(self, name: str, url: str, data, file: str = "None"):
        self._name = name
        self._url = url
        self._data = data
        self._file = file

    def get_name(self):
        return self._name

    def get_url(self):
        return self._url

    def get_data(self):
        return self._data

    def get_file(self):
        return self._file

    def get_value(self, arg_id: str):
        return dict.get(self._data, arg_id)

    def update_name(self, new_name: str):
        self._name = new_name

    def update_url(self, new_url: str):
        self._url = new_url

    def update_dict(self, new_data):
        self._data = new_data

    def update_file(self, new_file: str):
        self._file = new_file


class _DLib(Lib):
    def __init__(self, name: str, url: str, data: dict, file: str = "None"):
        Lib.__init__(self, name, url, data, file)
        self._name = name
        self._url = url
        self._dict = data
        self._file = file

    def get_value(self, arg_id: str):
        return dict.get(self._dict, arg_id, 0)

    def update_dict(self, new_dict: dict):
        self._dict.update(new_dict)

    def clear_dict(self):
        self._dict.clear()


class CheckedDict:
    @staticmethod
    def check(data: dict, args: dict):
        key = list(args.keys()).pop()
        return args == {key: f"{data.get(key)}"}

    # @staticmethod
    # def return_value(data: dict, value: str, default = 0):
    #    return dict.get(data, value, default)

    # @staticmethod
    # def return_key(args: dict):
    #    return list(args.keys()).pop()


class JsonReader(_DLib):
    def __init__(self, name: str, url: str, data: dict, file: str = "None"):
        _DLib.__init__(self, name, url, data, file)

    def read(self, encoding="utf-8"):
        with open(self._url + "/" + self._file, "r", encoding=encoding) as file:
            data = json.load(file)
            self.update_dict(data)
            return data


class JsonWriter(_DLib):
    def __init__(self, name: str, url: str, data: dict, file: str = "None"):
        _DLib.__init__(self, name, url, data, file)

    def write(self, args: dict, encoding=None):
        data = self._dict.copy()
        data.update(args)

        self._dict.update(data)
        makedirs(self._url, exist_ok=True)

        with open((self._url + "/" + self._file), "w", encoding=encoding) as file:
            json.dump(data, file, indent=4)


class JsonWorker(JsonReader, JsonWriter, _DLib):
    def __init__(self, name: str, url: str, data: dict, file: str = "None"):
        _DLib.__init__(self, name, url, data, file)

    def check(self, args: dict, script=None):
        checker = CheckedDict.check(self.get_data(), args)
        if checker:
            if script is not None:
                script()  # type: ignore
            return True

        elif not checker:
            return False
        else:
            log.error("Undefined error...", {self.get_data(): args}, stack_info=True)
            return None

    def reader(self, encoding="utf-8"):
        try:
            self.read(encoding)
            log.info({f"Load {self.get_name()}": self.get_data()})

        except FileNotFoundError:
            log.exception(
                f"File {self.get_file()} not found, creating new file...",
                stack_info=True,
            )
            self.writer(self._dict)

        except json.decoder.JSONDecodeError as jde:
            log.exception(
                {f"File {self.get_file()} void or crash, recording...": jde},
                stack_info=True,
            )
            self.writer(self._dict)

    def writer(self, args: dict, encoding="utf-8"):
        self.write(args, encoding)
