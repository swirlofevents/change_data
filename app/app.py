from fastapi import FastAPI


from .settings import AppSettings
from .service import service_router

APP_SETTINGS = AppSettings()

MAIN_APP = FastAPI(title=APP_SETTINGS.APP_NAME)

MAIN_APP.include_router(service_router)
