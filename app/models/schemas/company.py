from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime


class CompanyProfile(BaseModel):
    """Company profile information"""
    symbol: str = Field(..., description="Company stock symbol", alias="ticker")
    company_name: str = Field(..., description="Full company name", alias="companyName")
    exchange: Optional[str] = Field(None, description="Stock exchange")
    industry: Optional[str] = Field(None, description="Industry sector")
    established_year: Optional[int] = Field(None, description="Year the company was established")
    listing_date: Optional[datetime] = Field(None, description="Date listed on the exchange")
    website: Optional[str] = Field(None, description="Company website URL")
    address: Optional[str] = Field(None, description="Company address")
    phone: Optional[str] = Field(None, description="Contact phone number")
    business_summary: Optional[str] = Field(None, description="Summary of the company's business", alias="companyProfile")
    history: Optional[str] = Field(None, description="Company history", alias="historyDev")
    business_strategies: Optional[str] = Field(None, description="Company business strategies", alias="businessStrategies")
    business_risks: Optional[str] = Field(None, description="Company business risks", alias="businessRisk")
    key_developments: Optional[str] = Field(None, description="Key developments", alias="keyDevelopments")
    promise: Optional[str] = Field(None, description="Company promise", alias="companyPromise")
    employees: Optional[int] = Field(None, description="Number of employees")

    class Config:
        populate_by_name = True


class CompanyOfficer(BaseModel):
    """Company officer/executive information"""
    no: Optional[int] = Field(None, description="Sequential number")
    symbol: str = Field(..., description="Company stock symbol", alias="ticker")
    name: str = Field(..., description="Officer name")
    position: Optional[str] = Field(None, description="Officer's position")
    ownership_percent: Optional[float] = Field(None, description="Percentage of ownership", alias="ownPercent")
    appointment_date: Optional[datetime] = Field(None, description="Date appointed to position")
    profile: Optional[str] = Field(None, description="Officer's profile")

    class Config:
        populate_by_name = True


class Shareholder(BaseModel):
    """Major shareholder information"""
    no: Optional[int] = Field(None, description="Sequential number")
    symbol: str = Field(..., description="Shareholder's ticker if applicable", alias="ticker")
    name: str = Field(..., description="Shareholder name")
    ownership_percent: float = Field(..., description="Percentage of ownership", alias="ownPercent")
    shares_held: Optional[int] = Field(None, description="Number of shares held")
    last_changed: Optional[datetime] = Field(None, description="Last date of change in ownership")

    class Config:
        populate_by_name = True


class InsiderTransaction(BaseModel):
    """Insider trading transaction"""
    no: Optional[int] = Field(None, description="Sequential number")
    symbol: str = Field(..., description="Company stock symbol", alias="ticker")
    transaction_date: datetime = Field(..., description="Date of transaction", alias="anDate")
    dealing_method: Optional[int] = Field(None, description="Dealing method code", alias="dealingMethod")
    dealing_action: Optional[str] = Field(None, description="Dealing action code", alias="dealingAction")
    quantity: Optional[int] = Field(None, description="Number of shares", alias="quantity")
    price: Optional[float] = Field(None, description="Price per share")
    ratio: Optional[float] = Field(None, description="Change ratio")
    insider_name: Optional[str] = Field(None, description="Name of the insider")
    position: Optional[str] = Field(None, description="Position in the company")
    shares_after: Optional[int] = Field(None, description="Shares owned after transaction")

    class Config:
        populate_by_name = True


class Subsidiary(BaseModel):
    """Company subsidiary information"""
    no: Optional[int] = Field(None, description="Sequential number")
    symbol: str = Field(..., description="Company stock symbol", alias="ticker")
    name: str = Field(..., description="Subsidiary name", alias="companyName")
    ownership_percent: float = Field(..., description="Percentage of ownership", alias="ownPercent")
    business: Optional[str] = Field(None, description="Business description")
    country: Optional[str] = Field(None, description="Country of incorporation")

    class Config:
        populate_by_name = True


class CompanyEvent(BaseModel):
    """Company corporate event"""
    id: Optional[int] = Field(None, description="Event ID")
    symbol: str = Field(..., description="Company stock symbol", alias="ticker")
    event_name: str = Field(..., description="Event name", alias="eventName")
    event_code: str = Field(..., description="Event code", alias="eventCode")
    notify_date: datetime = Field(..., description="Notification date", alias="notifyDate")
    execution_date: datetime = Field(..., description="Execution date", alias="exerDate")
    registration_date: Optional[datetime] = Field(None, description="Registration date", alias="regFinalDate")
    ex_right_date: Optional[datetime] = Field(None, description="Ex-right date", alias="exRigthDate")
    description: Optional[str] = Field(None, description="Event description", alias="eventDesc")
    price: Optional[float] = Field(None, description="Stock price at event time")
    price_change: Optional[float] = Field(None, description="Price change", alias="priceChange")
    price_change_ratio: Optional[float] = Field(None, description="Price change ratio", alias="priceChangeRatio")

    class Config:
        populate_by_name = True


class NewsItem(BaseModel):
    """Company news item"""
    id: Optional[int] = Field(None, description="News ID")
    symbol: str = Field(..., description="Company stock symbol", alias="ticker")
    title: str = Field(..., description="News title")
    published_date: datetime = Field(..., description="Publication date", alias="publishDate")
    source: str = Field(..., description="News source")
    url: Optional[str] = Field(None, description="News URL")
    summary: Optional[str] = Field(None, description="News summary")
    price: Optional[float] = Field(None, description="Stock price at news time")
    price_change: Optional[float] = Field(None, description="Price change", alias="priceChange")
    price_change_ratio: Optional[float] = Field(None, description="Price change ratio", alias="priceChangeRatio")

    class Config:
        populate_by_name = True


class Dividend(BaseModel):
    """Dividend payment record"""
    no: Optional[int] = Field(None, description="Sequential number")
    symbol: str = Field(..., description="Company stock symbol", alias="ticker")
    ex_date: datetime = Field(..., description="Ex-dividend date", alias="exerciseDate")
    cash_year: Optional[int] = Field(None, description="Year of cash dividend", alias="cashYear")
    dividend_type: str = Field(..., description="Cash or stock", alias="issueMethod")
    amount: float = Field(..., description="Dividend amount", alias="cashDividendPercentage")
    record_date: Optional[datetime] = Field(None, description="Record date")
    payment_date: Optional[datetime] = Field(None, description="Payment date")
    yield_percent: Optional[float] = Field(None, description="Dividend yield percentage")

    class Config:
        populate_by_name = True


class CompanyInfo(BaseModel):
    """Full company information"""
    profile: CompanyProfile = Field(..., description="Company profile")
    officers: Optional[List[CompanyOfficer]] = Field(None, description="Company officers", alias="listKeyOfficer")
    major_shareholders: Optional[List[Shareholder]] = Field(None, description="Major shareholders", alias="listShareHolder")
    insider_transactions: Optional[List[InsiderTransaction]] = Field(None, description="Insider transactions", alias="listInsiderDealing")
    subsidiaries: Optional[List[Subsidiary]] = Field(None, description="Subsidiaries", alias="listSubCompany")
    events: Optional[List[CompanyEvent]] = Field(None, description="Company events", alias="listEventNews")
    news: Optional[List[NewsItem]] = Field(None, description="Company news", alias="listActivityNews")
    dividends: Optional[List[Dividend]] = Field(None, description="Dividend payments", alias="listDividendPaymentHis")

    class Config:
        populate_by_name = True


# Response models for individual endpoints
class CompanyProfileResponse(BaseModel):
    data: CompanyProfile


class CompanyOfficersResponse(BaseModel):
    data: List[CompanyOfficer]


class ShareholdersResponse(BaseModel):
    data: List[Shareholder]


class InsiderTransactionsResponse(BaseModel):
    data: List[InsiderTransaction]


class SubsidiariesResponse(BaseModel):
    data: List[Subsidiary]


class CompanyEventsResponse(BaseModel):
    data: List[CompanyEvent]


class CompanyNewsResponse(BaseModel):
    data: List[NewsItem]


class DividendsResponse(BaseModel):
    data: List[Dividend]


class CompanyInfoResponse(BaseModel):
    data: CompanyInfo 