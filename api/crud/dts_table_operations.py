from api.database import SessionLocal
from api.models.dts_table_models import (Operating_Cash_Balance,
                                         Deposits_Withdrawals_Operating_Cash,
                                         Public_Debt_Transactions,
                                         Adjustment_Public_Debt_Transactions_Cash_Basis,
                                         Debt_Subject_To_Limit,
                                         Inter_Agency_Tax_Transfers,
                                         Income_Tax_Refunds_Issued,
                                         Federal_Tax_Deposits,
                                         Short_Term_Cash_Investments)
from api.schemas import dts_table_schemas


class DTSTableOperations:
    def __init__(self, db: SessionLocal):
        self.dts_tables = {
            "Operating Cash Balance": Operating_Cash_Balance,
            "Deposits and Withdrawals of Operating Cash": Deposits_Withdrawals_Operating_Cash,
            "Public Debt Transactions": Public_Debt_Transactions,
            "Adjustment of Public Debt Transactions to Cash Basis": Adjustment_Public_Debt_Transactions_Cash_Basis,
            "Debt Subject to Limit": Debt_Subject_To_Limit,
            "Inter-agency Tax Transfers": Inter_Agency_Tax_Transfers,
            "Income Tax Refunds Issued": Income_Tax_Refunds_Issued,
            "Federal Tax Deposits": Federal_Tax_Deposits,
            "Short-Term Cash Investments": Short_Term_Cash_Investments,
        }
        self.db = db

    def get_all_data(self, table_name: str):
        """Get all data from a specific table in dts tables"""
        for table_obj in self.dts_tables.values():
            if table_obj.__name__.lower() == table_name.lower():
                table_name = table_obj.__name__
                return self.db.query(table_obj).all()
        return None

    def get_data_using_fyear(self, table_name: str, fyear: int):
        """Filter data using fiscal year"""
        for table_obj in self.dts_tables.values():
            if table_obj.__name__.lower() == table_name.lower():
                table_name = table_obj.__name__
                return self.db.query(table_obj).filter(table_obj.record_fiscal_year == fyear).all()
        return None

    # def get_data_using_cyear(self, table_name: str, cyear: int):
    #     data = self.db.query(table_name).where(cyear).all()
    #     if not data:
    #         return None
    #     return data

    # def get_data_cyear_fyear(self, table_name: str, fyear: int, cyear: int):
    #     data = self.db.query