from fastapi import APIRouter

from workshop.api.operations import router as operations_router


router = APIRouter()

router.include_router(router)
