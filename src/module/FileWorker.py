import json
import os
from os import makedirs
from typing import Any, Optional
from module.logged import log



class Lib:
    def __init__(self, name: str, url: str, data, file: Optional[str] = None):
        self._name = name
        self._url = url
        self._data = data
        self._file = file

    @property
    def path(self) -> str|bytes:
        return os.path.join(self._url, self._file)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, new_url: str) -> None:
        self._url = new_url

    @property
    def data(self) -> Any:
        return self._data

    @data.setter
    def data(self, new_data: Any) -> None:
        self._data = new_data

    @property
    def file(self) -> Optional[str]:
        return self._file

    @file.setter
    def file(self, new_file: Optional[str]) -> None:
        self._file = new_file

    def get_value(self, arg_id: str, default: Any = None) -> Any:
        return self._data.get(arg_id, default)


class _DLib(Lib):
    def __init__(self, name: str, url: str, data: dict, file: Optional[str] = None):
        Lib.__init__(self, name, url, data, file)

    def update_dict(self, new_dict: dict):
        self._data.update(new_dict)

    def clear_dict(self):
        self._data.clear()


class CheckedDict:
    @staticmethod
    def check(data: dict, arg: dict):
        key, value = next(iter(arg.items()))
        return data.get(key) == value


class JsonReader:
    @staticmethod
    def read(path, encoding="utf-8"):
        with open(path, "r", encoding=encoding) as file:
            return json.load(file)


class JsonWriter:
    @staticmethod
    def write(url, path, data,  args: dict, encoding="utf-8"):
        data.update(args)
        makedirs(url, exist_ok=True)

        with open(path, "w", encoding=encoding) as file:
           json.dump(data, file, indent=4)
        return data


class JsonWorker(JsonReader, JsonWriter, _DLib):
    def __init__(self, name: str, url: str, data: dict, file: str = "None"):
        _DLib.__init__(self, name, url, data, file)

    def check(self, args: dict, script=None):
        checker = CheckedDict.check(self.data, args)
        if checker and script is not None:
            script()  # type: ignore
        return checker

    def reader(self, encoding="utf-8"):
        try:
            data = self.read(self.path, encoding)
            log.info("Loaded %s: %s", self.name, self.data)
        except FileNotFoundError:
            log.warning("File %s not found, creating new one...", self.file)
            self.writer(self.data)
        except json.JSONDecodeError as jde:
            log.exception("File %s is empty or corrupted: %s", self.file, jde)
            self.writer(self.data)
        else:
            self.data = data

    def writer(self, args: dict, encoding="utf-8"):
        self.write(self.url, self.path, self.data, args, encoding)
