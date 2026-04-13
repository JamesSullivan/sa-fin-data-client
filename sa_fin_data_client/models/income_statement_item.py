from enum import Enum


class IncomeStatementItem(str, Enum):
    BOTTOM_LINE_NET_INCOME = "Bottom_Line_Net_Income"
    COST_AND_EXPENSES = "Cost_And_Expenses"
    COST_OF_REVENUE = "Cost_Of_Revenue"
    DEPRECIATION_AND_AMORTIZATION = "Depreciation_And_Amortization"
    EBIT = "EBIT"
    EBITDA = "EBITDA"
    EPS = "EPS"
    EPS_DILUTED = "EPS_Diluted"
    GENERAL_AND_ADMINISTRATIVE_EXPENSES = "General_And_Administrative_Expenses"
    GROSS_PROFIT = "Gross_Profit"
    INCOME_BEFORE_TAX = "Income_Before_Tax"
    INCOME_TAX_EXPENSE = "Income_Tax_Expense"
    INTEREST_EXPENSE = "Interest_Expense"
    INTEREST_INCOME = "Interest_Income"
    NET_INCOME = "Net_Income"
    NET_INCOME_DEDUCTIONS = "Net_Income_Deductions"
    NET_INCOME_FROM_CONTINUING_OPERATIONS = "Net_Income_From_Continuing_Operations"
    NET_INCOME_FROM_DISCONTINUED_OPERATIONS = "Net_Income_From_Discontinued_Operations"
    NET_INTEREST_INCOME = "Net_Interest_Income"
    NON_OPERATING_INCOME_EXCLUDING_INTEREST = "Non_Operating_Income_Excluding_Interest"
    OPERATING_EXPENSES = "Operating_Expenses"
    OPERATING_INCOME = "Operating_Income"
    OTHER_ADJUSTMENTS_TO_NET_INCOME = "Other_Adjustments_To_Net_Income"
    OTHER_EXPENSES = "Other_Expenses"
    RESEARCH_AND_DEVELOPMENT_EXPENSES = "Research_And_Development_Expenses"
    REVENUE = "Revenue"
    SELLING_AND_MARKETING_EXPENSES = "Selling_And_Marketing_Expenses"
    SELLING_GENERAL_AND_ADMINISTRATIVE_EXPENSES = "Selling_General_And_Administrative_Expenses"
    TOTAL_OTHER_INCOME_EXPENSES_NET = "Total_Other_Income_Expenses_Net"
    WEIGHTED_AVERAGE_SHS_OUT = "Weighted_Average_Shs_Out"
    WEIGHTED_AVERAGE_SHS_OUT_DIL = "Weighted_Average_Shs_Out_Dil"

    def __str__(self) -> str:
        return str(self.value)
