from fastapi import APIRouter

# from app.api.rest.v1.stocks.routes import router as stocks_router
# from app.api.rest.v1.market.routes import router as market_router
from app.api.rest.v1.companies.routes import router as companies_router

router = APIRouter()
# router.include_router(stocks_router, prefix="/stocks", tags=["Stocks"])
# router.include_router(market_router, prefix="/market", tags=["Market"])
router.include_router(companies_router, prefix="/companies", tags=["Companies"])
