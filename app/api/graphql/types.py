from typing import Optional, List
import strawberry
from enum import Enum
from datetime import datetime
from app.datasources.base import SOURCE_TCBS, SOURCE_VCI, SOURCE_UNIFIED

@strawberry.enum
class DataSource(Enum):
    TCBS = SOURCE_TCBS
    VCI = SOURCE_VCI
    ALL = SOURCE_UNIFIED

@strawberry.type
class CompanyProfile:
    symbol: str
    exchange: Optional[str] = None
    industry: Optional[str] = None
    company_type: Optional[str] = None
    no_shareholders: Optional[int] = None
    foreign_percent: Optional[float] = None
    outstanding_share: Optional[float] = None
    issue_share: Optional[float] = None
    established_year: Optional[str] = None
    no_employees: Optional[int] = None
    stock_rating: Optional[float] = None
    delta_in_week: Optional[float] = None
    delta_in_month: Optional[float] = None
    delta_in_year: Optional[float] = None
    short_name: Optional[str] = None
    website: Optional[str] = None
    industry_id: Optional[int] = None
    industry_id_v2: Optional[str] = None
    # Additional fields that might come from other sources
    company_name: Optional[str] = None
    listing_date: Optional[datetime] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    business_summary: Optional[str] = None
    history: Optional[str] = None
    business_strategies: Optional[str] = None
    business_risks: Optional[str] = None
    key_developments: Optional[str] = None
    promise: Optional[str] = None
    employees: Optional[int] = None

@strawberry.type
class CompanyOfficer:
    name: str
    position: str
    age: Optional[int] = None
    nationality: Optional[str] = None
    shares: Optional[int] = None

@strawberry.type
class Shareholder:
    name: str
    shares: int
    percentage: float
    type: Optional[str] = None

@strawberry.type
class InsiderTrading:
    date: datetime
    type: str
    shares: int
    price: float
    value: float

@strawberry.type
class Subsidiary:
    name: str
    symbol: Optional[str] = None
    ownership_percentage: float
    business_type: Optional[str] = None

@strawberry.type
class CompanyEvent:
    date: datetime
    type: str
    description: str
    impact: Optional[str] = None

@strawberry.type
class CompanyNews:
    date: datetime
    title: str
    content: str
    source: str
    url: Optional[str] = None

@strawberry.type
class Dividend:
    date: datetime
    type: str
    amount: float
    payment_date: Optional[datetime] = None
    ex_date: Optional[datetime] = None 