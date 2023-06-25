from typing import Union


from fastapi import APIRouter, Request


from .service import APIService

service_router = APIRouter()


@service_router.get("/test")
async def get_test(media_type: Union[str, None] = "text/plain", replace_content: Union[str, None] = ""):
    service = APIService()
    return await service.get_test_page(media_type=media_type, replace_content=replace_content)
