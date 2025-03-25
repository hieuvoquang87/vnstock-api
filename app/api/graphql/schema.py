import strawberry
from typing import List, Optional
import logging
from datetime import datetime
from .types import (
    CompanyProfile,
    CompanyOfficer,
    Shareholder,
    InsiderTrading,
    Subsidiary,
    CompanyEvent,
    CompanyNews,
    Dividend
)

logger = logging.getLogger(__name__)

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    @strawberry.field
    def company_profile(self, symbol: str) -> CompanyProfile:
        """Return mock company profile data for development"""
        # Return mock data for FPT
        if symbol.upper() == "FPT":
            return CompanyProfile(
                symbol="FPT",
                company_name="FPT Corporation",
                exchange="HOSE",
                industry="Technology",
                established_year="2002",
                no_employees=48878,
                website="https://www.fpt.com.vn",
                business_summary="Leading technology company in Vietnam",
                short_name="FPT Corp"
            )
        # Default mock data for other symbols
        return CompanyProfile(
            symbol=symbol.upper(),
            company_name=f"{symbol.upper()} Corporation",
            exchange="HOSE",
            industry="Unknown",
            established_year="2000",
            website=f"https://www.{symbol.lower()}.com",
            business_summary=f"Mock data for {symbol.upper()}"
        )

    @strawberry.field
    def company_officers(self, symbol: str) -> List[CompanyOfficer]:
        """Return mock company officers data for development"""
        return [
            CompanyOfficer(
                name="John Doe",
                position="CEO",
                age=45,
                nationality="Vietnamese",
                shares=100000
            ),
            CompanyOfficer(
                name="Jane Smith",
                position="CTO",
                age=40,
                nationality="Vietnamese",
                shares=80000
            )
        ]

    @strawberry.field
    def shareholders(self, symbol: str) -> List[Shareholder]:
        """Return mock shareholders data for development"""
        return [
            Shareholder(
                name="Investment Group A",
                shares=1000000,
                percentage=30.5,
                type="Organization"
            ),
            Shareholder(
                name="Investment Group B",
                shares=800000,
                percentage=24.2,
                type="Organization"
            )
        ]

    @strawberry.field
    def insider_trading(self, symbol: str) -> List[InsiderTrading]:
        """Return mock insider trading data for development"""
        return [
            InsiderTrading(
                date=datetime.now(),
                type="Buy",
                shares=10000,
                price=85.2,
                value=852000.0
            ),
            InsiderTrading(
                date=datetime.now(),
                type="Sell",
                shares=5000,
                price=86.4,
                value=432000.0
            )
        ]

schema = strawberry.Schema(query=Query) 