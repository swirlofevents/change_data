from typing import Union


from httpx import AsyncClient
from fastapi import Request
from fastapi.responses import StreamingResponse, HTMLResponse


from app.settings import AppSettings
from app.utils import custom_replace
from app.test import test_page_html_data
from .headers_cache import HeadersCache


class APIService:
    def __init__(self):
        self.settings = AppSettings()
        self.headers_cache = HeadersCache()

    async def get_test_page(
        self, media_type: Union[str, None] = "text/plain", replace_content: Union[str, None] = ""
    ):
        content = test_page_html_data
        if replace_content:
            content = custom_replace(content, self.settings.strings_data)
        return HTMLResponse(content=content, media_type=media_type)

    async def get_rec_stream(self, request: Request):
        headers = self.headers_cache.get_headers(request)

        async def inner_generator(inner_request: Request):
            async with AsyncClient(base_url=self.settings.base_url, headers=headers) as httpx_client:
                async with httpx_client.stream("GET", url=inner_request.url.path) as req_response:
                    async for bytes_chunk in req_response.aiter_bytes():
                        replaced_chunk = custom_replace(bytes_chunk, self.settings.strings_data)
                        yield replaced_chunk

        return StreamingResponse(inner_generator(request))
