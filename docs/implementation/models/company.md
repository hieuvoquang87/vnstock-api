# Company Models

## Overview

This module defines the Pydantic models used for representing company-related data in the API. These models are used for request/response validation, documentation, and data transformation throughout the application. The models are structured to match the data returned by the VNStock library and TCBS data format.

## Models

### CompanyProfile

**Description:**
Represents the profile information of a company.

**Fields:**

- `symbol` (str): Stock symbol/ticker.
- `company_name` (str): Name of the company.
- `exchange` (str): The exchange where the stock is listed (e.g., HOSE, HNX).
- `industry` (str): The industry in which the company operates.
- `established_year` (Optional[int]): Year when the company was established.
- `listing_date` (Optional[date]): Date when the company was listed on the exchange.
- `charter_capital` (Optional[float]): Charter capital in billions of VND.
- `number_of_employees` (Optional[int]): Number of employees.
- `website` (Optional[str]): Company website URL.
- `description` (Optional[str]): Brief description of the company.
- `company_profile` (Optional[str]): Detailed company profile.
- `history_dev` (Optional[str]): Company development history.
- `business_risk` (Optional[str]): Business risks disclosure.
- `key_developments` (Optional[str]): Key company developments.
- `business_strategies` (Optional[str]): Company business strategies.

### CompanyOfficer

**Description:**
Represents an officer or executive of a company.

**Fields:**

- `no` (Optional[int]): Sequential number.
- `symbol` (str): Stock symbol/ticker.
- `name` (str): Name of the officer.
- `position` (str): Position held in the company.
- `ownership_percent` (Optional[float]): Percentage of shares owned.
- `appointed_date` (Optional[date]): Date when the officer was appointed.
- `education` (Optional[str]): Educational background.
- `experience` (Optional[str]): Professional experience.

### Shareholder

**Description:**
Represents a major shareholder of a company.

**Fields:**

- `no` (Optional[int]): Sequential number.
- `symbol` (str): Stock symbol/ticker.
- `name` (str): Name of the shareholder.
- `ownership_percent` (Optional[float]): Percentage of shares owned.
- `shares_held` (Optional[int]): Number of shares held.
- `shareholder_type` (Optional[str]): Type of shareholder (e.g., individual, institutional).

### InsiderTransaction

**Description:**
Represents an insider trading transaction.

**Fields:**

- `no` (Optional[int]): Sequential number.
- `symbol` (str): Stock symbol/ticker.
- `transaction_date` (Optional[date]): Date of the transaction.
- `person` (Optional[str]): Person or entity involved.
- `relation` (Optional[str]): Relationship to the company.
- `dealing_method` (Optional[str]): Method of dealing (e.g., buy, sell).
- `quantity` (Optional[int]): Number of shares involved.
- `price` (Optional[float]): Price per share.
- `ownership_before` (Optional[float]): Ownership percentage before transaction.
- `ownership_after` (Optional[float]): Ownership percentage after transaction.
- `registered_date` (Optional[date]): Date when transaction was registered.
- `status` (Optional[str]): Status of the transaction.

### Subsidiary

**Description:**
Represents a subsidiary of a company.

**Fields:**

- `no` (Optional[int]): Sequential number.
- `symbol` (str): Stock symbol/ticker of the parent company.
- `name` (str): Name of the subsidiary.
- `ownership_percent` (Optional[float]): Percentage of ownership by the parent company.
- `business` (Optional[str]): Business area of the subsidiary.
- `charter_capital` (Optional[float]): Charter capital in billions of VND.
- `address` (Optional[str]): Address of the subsidiary.

### CompanyEvent

**Description:**
Represents a corporate event.

**Fields:**

- `id` (Optional[int]): Event ID.
- `symbol` (str): Stock symbol/ticker.
- `event_name` (str): Name of the event.
- `event_code` (Optional[str]): Code of the event.
- `notify_date` (Optional[date]): Date of notification.
- `ex_date` (Optional[date]): Ex-date of the event.
- `record_date` (Optional[date]): Record date.
- `value` (Optional[float]): Event value (e.g., dividend amount).
- `description` (Optional[str]): Detailed description of the event.
- `status` (Optional[str]): Status of the event.
- `is_confirmed` (Optional[bool]): Whether the event is confirmed.

### NewsItem

**Description:**
Represents a news article related to a company.

**Fields:**

- `id` (Optional[int]): News item ID.
- `symbol` (str): Stock symbol/ticker.
- `title` (str): Title of the news article.
- `published_date` (Optional[datetime]): Publication date and time.
- `source` (Optional[str]): Source of the news.
- `url` (Optional[str]): URL of the news article.
- `content` (Optional[str]): Content of the news article.
- `summary` (Optional[str]): Summary of the news article.
- `change_percent` (Optional[float]): Stock price change percentage related to the news.

### Dividend

**Description:**
Represents a dividend payment.

**Fields:**

- `no` (Optional[int]): Sequential number.
- `symbol` (str): Stock symbol/ticker.
- `ex_date` (Optional[date]): Ex-dividend date.
- `record_date` (Optional[date]): Record date.
- `payment_date` (Optional[date]): Payment date.
- `dividend_type` (Optional[str]): Type of dividend (e.g., cash, stock).
- `amount` (Optional[float]): Dividend amount per share.
- `currency` (Optional[str]): Currency of the dividend.
- `year` (Optional[int]): Fiscal year of the dividend.
- `status` (Optional[str]): Status of the dividend payment.

### CompanyInfo

**Description:**
A composite model that includes all information about a company.

**Fields:**

- `profile` (CompanyProfile): Company profile information.
- `officers` (Optional[List[CompanyOfficer]]): List of company officers.
- `shareholders` (Optional[List[Shareholder]]): List of major shareholders.
- `insider_transactions` (Optional[List[InsiderTransaction]]): List of insider transactions.
- `subsidiaries` (Optional[List[Subsidiary]]): List of subsidiaries.
- `events` (Optional[List[CompanyEvent]]): List of company events.
- `news` (Optional[List[NewsItem]]): List of news articles.
- `dividends` (Optional[List[Dividend]]): List of dividend payments.

## Usage

These models are used in several ways throughout the application:

1. **Request/Response Validation**: FastAPI uses these models to validate incoming requests and format outgoing responses.

2. **Data Transformation**: The service layer uses these models to transform data from the data sources into a standardized format.

3. **Documentation**: The models are used to generate the API documentation automatically.

4. **Type Hinting**: The models provide type hinting for better IDE support and code quality.

## Example

```python
from app.models.schemas.company import CompanyProfile

# Create a company profile instance
profile = CompanyProfile(
    symbol="VNM",
    company_name="Vietnam Dairy Products Joint Stock Company",
    exchange="HOSE",
    industry="Food & Beverages",
    established_year=1976,
    website="https://www.vinamilk.com.vn"
)

# Convert to dictionary
profile_dict = profile.dict()

# Convert to JSON
profile_json = profile.json()
```

## Extending the Models

To add new fields to the models:

1. Update the relevant Pydantic model in `app/models/schemas/company.py`
2. Ensure that any new fields have appropriate type annotations
3. Add appropriate aliases if the field names in the data source differ from the API naming conventions
4. Update the documentation to reflect the new fields
