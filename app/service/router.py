from fastapi import APIRouter


from .service import APIService

service_router = APIRouter()


@service_router.get("/test")
async def get_test():
    service = APIService()
    return await service.get_test_page()
