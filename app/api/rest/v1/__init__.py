from fastapi import APIRouter

# from app.api.rest.v1.stocks.routes import router as stocks_router
# from app.api.rest.v1.market.routes import router as market_router
from app.api.rest.v1.companies.routes import router as companies_router
from app.api.rest.v1.financial.routes import router as financial_router
from app.api.rest.v1.listing import router as listing_router

# Create v1 router
v1_router = APIRouter(prefix="/v1")

# Include routers
v1_router.include_router(companies_router, prefix="/companies", tags=["Companies"])
v1_router.include_router(financial_router, prefix="/financial", tags=["Financial"])
v1_router.include_router(listing_router)

__all__ = ["v1_router"]