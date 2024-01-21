from pydantic import BaseModel


class Operating_Cash_Balance(BaseModel):
    record_date: str
    account_type: str
    close_today_bal: str
    open_today_bal: str
    open_month_bal: str
    open_fiscal_year_bal: str
    table_nbr: str
    table_nm: str
    sub_table_name: str
    src_line_nbr: str
    record_fiscal_year: str
    record_fiscal_quarter: str
    record_calendar_year: str
    record_calendar_quarter: str
    record_calendar_month: str
    record_calendar_day: str


class Deposits_Withdrawals_Operating_Cash(BaseModel):
    record_date: str
    account_type: str
    transaction_type: str
    transaction_catg: str
    transaction_catg_desc: str
    transaction_today_amt: str
    transaction_mtd_amt: str
    transaction_fytd_amt: str
    table_nbr: str
    table_nm: str
    src_line_nbr: str
    record_fiscal_year: str
    record_fiscal_quarter: str
    record_calendar_year: str
    record_calendar_quarter: str
    record_calendar_month: str
    record_calendar_day: str


class Public_Debt_Transactions(BaseModel):
    record_date: str
    transaction_type: str
    security_market: str
    security_type: str
    security_type_desc: str
    transaction_today_amt: str
    transaction_mtd_amt: str
    transaction_fytd_amt: str
    table_nbr: str
    table_nm: str
    src_line_nbr: str
    record_fiscal_year: str
    record_fiscal_quarter: str
    record_calendar_year: str
    record_calendar_quarter: str
    record_calendar_month: str
    record_calendar_day: str


class Adjustment_Public_Debt_Transactions_Cash_Basis(BaseModel):
    record_date: str
    transaction_type: str
    adj_type: str
    adj_type_desc: str
    adj_today_amt: str
    adj_mtd_amt: str
    adj_fytd_amt: str
    table_nbr: str
    table_nm: str
    sub_table_name: str
    src_line_nbr: str
    record_fiscal_year: str
    record_fiscal_quarter: str
    record_calendar_year: str
    record_calendar_quarter: str
    record_calendar_month: str
    record_calendar_day: str


class Debt_Subject_To_Limit(BaseModel):
    record_date: str
    debt_catg: str
    debt_catg_desc: str
    close_today_bal: str
    open_today_bal: str
    open_month_bal: str
    open_fiscal_year_bal: str
    table_nbr: str
    table_nm: str
    sub_table_name: str
    src_line_nbr: str
    record_fiscal_year: str
    record_fiscal_quarter: str
    record_calendar_year: str
    record_calendar_quarter: str
    record_calendar_month: str
    record_calendar_day: str


class Inter_Agency_Tax_Transfers(BaseModel):
    record_date: str
    classification: str
    today_amt: str
    mtd_amt: str
    fytd_amt: str
    table_nbr: str
    table_nm: str
    sub_table_name: str
    src_line_nbr: str
    record_fiscal_year: str
    record_fiscal_quarter: str
    record_calendar_year: str
    record_calendar_quarter: str
    record_calendar_month: str
    record_calendar_day: str


class Income_Tax_Refunds_Issued(BaseModel):
    record_date: str
    tax_refund_type: str
    tax_refund_type_desc: str
    tax_refund_today_amt: str
    tax_refund_mtd_amt: str
    tax_refund_fytd_amt: str
    table_nbr: str
    table_nm: str
    sub_table_name: str
    src_line_nbr: str
    record_fiscal_year: str
    record_fiscal_quarter: str
    record_calendar_year: str
    record_calendar_quarter: str
    record_calendar_month: str
    record_calendar_day: str


class Federal_Tax_Deposits(BaseModel):
    record_date: str
    tax_deposit_type: str
    tax_deposit_type_desc: str
    tax_deposit_today_amt: str
    tax_deposit_mtd_amt: str
    tax_deposit_fytd_amt: str
    table_nbr: str
    table_nm: str
    sub_table_name: str
    src_line_nbr: str
    record_fiscal_year: str
    record_fiscal_quarter: str
    record_calendar_year: str
    record_calendar_quarter: str
    record_calendar_month: str
    record_calendar_day: str


class Short_Term_Cash_Investments(BaseModel):
    record_date: str
    transaction_type: str
    transaction_type_desc: str
    depositary_type_a_amt: str
    depositary_type_b_amt: str
    depositary_type_c_amt: str
    total_amt: str
    table_nbr: str
    table_nm: str
    sub_table_name: str
    src_line_nbr: str
    record_fiscal_year: str
    record_fiscal_quarter: str
    record_calendar_year: str
    record_calendar_quarter: str
    record_calendar_month: str
    record_calendar_day: str