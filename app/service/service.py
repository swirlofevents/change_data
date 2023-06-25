from app.settings import AppSettings


class APIService:
    def __init__(self):
        self.settings = AppSettings()

    async def get_test_page(self):
        return {"test": "page"}
