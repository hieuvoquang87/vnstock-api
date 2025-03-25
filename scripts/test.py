import json
from vnstock.common.data.data_explorer import Company

def main():
    company = Company(symbol="VNM", source="tcbs")
    company_overview = company.overview().to_dict(orient='records'),
    print(company_overview)

if __name__ == "__main__":
    main()
