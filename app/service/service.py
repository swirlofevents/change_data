from typing import Union


from httpx import AsyncClient
from fastapi.responses import StreamingResponse, HTMLResponse


from app.settings import AppSettings
from app.utils import custom_replace
from app.test import test_page_html_data


class APIService:
    def __init__(self):
        self.settings = AppSettings()

    async def get_test_page(
        self, media_type: Union[str, None] = "text/plain", replace_content: Union[str, None] = ""
    ):
        content = test_page_html_data
        if replace_content:
            content = custom_replace(content, self.settings.strings_data)
        return HTMLResponse(content=content, media_type=media_type)
