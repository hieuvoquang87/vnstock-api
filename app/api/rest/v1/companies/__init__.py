from fastapi import APIRouter

from app.api.rest.v1.companies.routes import router as companies_router

router = APIRouter()
router.include_router(companies_router) 