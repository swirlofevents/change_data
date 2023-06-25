from fastapi import FastAPI


from settings import AppSettings

APP_SETTINGS = AppSettings()

MAIN_APP = FastAPI(title=APP_SETTINGS.APP_NAME)
