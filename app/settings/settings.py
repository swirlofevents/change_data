from __future__ import annotations
from typing import Optional
from threading import Lock
from os.path import dirname, realpath
from yaml import safe_load


class SingletonMeta(type):
    _instance: Optional[AppSettings] = None

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

    def reset(cls):
        cls._instance = None


class AppSettings(metaclass=SingletonMeta):
    SETTINGS_FILENAME = "settings.yaml"
    APP_NAME = "Test APP"

    def __init__(self, settings_path=None) -> None:
        if not settings_path:
            path = dirname(realpath(__file__))
            settings_path = "{}/{}".format(path, AppSettings.SETTINGS_FILENAME)

        with open(settings_path, "r", encoding="utf-8") as settings_file:
            self._config = safe_load(settings_file)

    @property
    def app_settings(self):
        return self._config["app"]
