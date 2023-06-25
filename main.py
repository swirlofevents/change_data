import uvicorn


from app import MAIN_APP, APP_SETTINGS


if __name__ == "__main__":
    uvicorn.run(MAIN_APP, port=APP_SETTINGS["port"], host=APP_SETTINGS["host"])
