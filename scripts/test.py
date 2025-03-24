import json
from vnstock.common.data.data_explorer import Company

def main():
    company = Company(symbol="VNM", source="tcbs")
    company_overview = company.overview()
    company_overview_json = json.dumps(
        company_overview.to_json(orient='records'),
        ensure_ascii=False,  # This is the key setting for Vietnamese characters
        indent=2,
        default=str  # Handles datetime objects by converting to string
    )
    print(company_overview_json)

if __name__ == "__main__":
    main()
