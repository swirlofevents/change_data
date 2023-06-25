import uvicorn


from app import MAIN_APP, APP_SETTINGS

app_config = APP_SETTINGS.app_config

if __name__ == "__main__":
    uvicorn.run(MAIN_APP, port=app_config["port"], host=app_config["host"])
