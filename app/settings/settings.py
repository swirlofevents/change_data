from typing import Optional, Dict
from threading import Lock
from os.path import dirname, realpath
from yaml import safe_load
from json import load


class SingletonMeta(type):
    _instance: Optional["AppSettings"] = None

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

    def reset(cls):
        cls._instance = None


class AppSettings(metaclass=SingletonMeta):
    STRINGS_DATA_FILENAME = "strings_data.json"
    SETTINGS_FILENAME = "settings.yaml"
    APP_NAME = "Test APP"

    def __init__(self, settings_path=None, strings_data=None) -> None:
        if not settings_path:
            path = dirname(realpath(__file__))
            settings_path = "{}/{}".format(path, AppSettings.SETTINGS_FILENAME)

        if not strings_data:
            path = dirname(realpath(__file__))
            strings_data_filename = "{}/{}".format(path, AppSettings.STRINGS_DATA_FILENAME)

        with open(settings_path, "r", encoding="utf-8") as settings_file:
            self._config = safe_load(settings_file)

        with open(strings_data_filename, "r", encoding="utf-8") as strings_file:
            self._strings_data = load(strings_file)

        # TODO: убрать костыль, чтоб не перекидывало с приложения
        self._strings_data[
            self._config["app"]["base_url"] + ":433"
        ] = f"http://{self._config['app']['host']}:{self._config['app']['port']}"

    @property
    def app_config(self) -> Dict:
        return self._config["app"]

    @property
    def strings_data(self) -> Dict:
        return self._strings_data

    @property
    def base_url(self) -> str:
        return self._config["app"]["base_url"]
