from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.balance_sheet_item import BalanceSheetItem
from ...models.cash_flow_item import CashFlowItem
from ...models.fs_code import FSCode
from ...models.fs_standardized import FSStandardized
from ...models.http_validation_error import HTTPValidationError
from ...models.income_statement_item import IncomeStatementItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cik: int,
    stmt: FSCode,
    *,
    items: list[BalanceSheetItem | CashFlowItem | IncomeStatementItem],
    fiscal_period: str | Unset = "annual",
    reporting_basis: str | Unset = "latest",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_items = []
    for items_item_data in items:
        items_item: str
        if isinstance(items_item_data, BalanceSheetItem):
            items_item = items_item_data.value
        elif isinstance(items_item_data, CashFlowItem):
            items_item = items_item_data.value
        else:
            items_item = items_item_data.value

        json_items.append(items_item)

    params["items"] = json_items

    params["fiscal_period"] = fiscal_period

    params["reporting_basis"] = reporting_basis

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/company/fs/standardized/{cik}/{stmt}".format(
            cik=quote(str(cik), safe=""),
            stmt=quote(str(stmt), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[FSStandardized] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FSStandardized.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | list[FSStandardized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cik: int,
    stmt: FSCode,
    *,
    client: AuthenticatedClient | Client,
    items: list[BalanceSheetItem | CashFlowItem | IncomeStatementItem],
    fiscal_period: str | Unset = "annual",
    reporting_basis: str | Unset = "latest",
) -> Response[HTTPValidationError | list[FSStandardized]]:
    """Standardized

     Fetch financial stmt item time series data.

    Args:
        cik: Company central index key
        stmt: Statement type (e.g., 'BS' for Balance Sheet, 'IS' for Income Statement, 'CF' for Cash
    Flow)
        item: Item name such as 'revenue', 'costOfRevenue'
        FiscalPeriod: Reporting period ('annual' or 'quarterly')
        original: Boolean to indicate whether to return original values or latest values

    Returns:
        List of FSStandardized (cik, stmt, item, date, value, uom, tag, version, form, fy, pf filed,
    qtrs, adsh)

    Args:
        cik (int):
        stmt (FSCode):
        items (list[BalanceSheetItem | CashFlowItem | IncomeStatementItem]):
            **List of specific financial line items to retrieve.** The required items depend on the
            `stmt` parameter:

            * **For stmt=`BS` (Balance Sheet) valid items are:**
                `Cash_And_Cash_Equivalents`, `Short_Term_Investments`,
            `Cash_And_Short_Term_Investments`, `Net_Receivables`, `Accounts_Receivables`,
            `Other_Receivables`, `Inventory`, `Prepaids`, `Other_Current_Assets`,
            `Total_Current_Assets`, `Property_Plant_Equipment_Net`, `Goodwill`, `Intangible_Assets`,
            `Goodwill_And_Intangible_Assets`, `Long_Term_Investments`, `Tax_Assets`,
            `Other_Non_Current_Assets`, `Total_Non_Current_Assets`, `Other_Assets`, `Total_Assets`,
            `Total_Payables`, `Accounts_Payables`, `Other_Payables`, `Accrued_Expenses`,
            `Short_Term_Debt`, `Capital_Lease_Obligations_Current`, `Tax_Payables`,
            `Deferred_Revenue`, `Other_Current_Liabilities`, `Total_Current_Liabilities`,
            `Long_Term_Debt`, `Capital_Lease_Obligations_Non_Current`, `Deferred_Revenue_Non_Current`,
            `Deferred_Tax_Liabilities_Non_Current`, `Other_Non_Current_Liabilities`,
            `Total_Non_Current_Liabilities`, `Other_Liabilities`, `Capital_Lease_Obligations`,
            `Total_Liabilities`, `Treasury_Stock`, `Preferred_Stock`, `Common_Stock`,
            `Retained_Earnings`, `Additional_Paid_In_Capital`,
            `Accumulated_Other_Comprehensive_Income_Loss`, `Other_Total_Stockholders_Equity`,
            `Total_Stockholders_Equity`, `Total_Equity`, `Minority_Interest`,
            `Total_Liabilities_And_Total_Equity`, `Total_Investments`, `Total_Debt`, `Net_Debt`
            * **For stmt=`CF` (Cash Flow) valid items are:**
                `Net_Income`, `Depreciation_And_Amortization`, `Deferred_Income_Tax`,
            `Stock_Based_Compensation`, `Change_In_Working_Capital`, `Accounts_Receivables`,
            `Inventory`, `Accounts_Payables`, `Other_Working_Capital`, `Other_Non_Cash_Items`,
            `Net_Cash_Provided_By_Operating_Activities`,
            `Investments_In_Property_Plant_And_Equipment`, `Acquisitions_Net`,
            `Purchases_Of_Investments`, `Sales_Maturities_Of_Investments`,
            `Other_Investing_Activities`, `Net_Cash_Provided_By_Investing_Activities`,
            `Net_Debt_Issuance`, `Long_Term_Net_Debt_Issuance`, `Short_Term_Net_Debt_Issuance`,
            `Net_Stock_Issuance`, `Net_Common_Stock_Issuance`, `Common_Stock_Issuance`,
            `Common_Stock_Repurchased`, `Net_Preferred_Stock_Issuance`, `Net_Dividends_Paid`,
            `Common_Dividends_Paid`, `Preferred_Dividends_Paid`, `Other_Financing_Activities`,
            `Net_Cash_Provided_By_Financing_Activities`, `Effect_Of_Forex_Changes_On_Cash`,
            `Net_Change_In_Cash`, `Cash_At_End_Of_Period`, `Cash_At_Beginning_Of_Period`,
            `Operating_Cash_Flow`, `Capital_Expenditure`, `Free_Cash_Flow`, `Income_Taxes_Paid`,
            `Interest_Paid`
            * **For stmt=`IS` (Income Statement):**
                `Revenue`, `Cost_Of_Revenue`, `Gross_Profit`, `Research_And_Development_Expenses`,
            `General_And_Administrative_Expenses`, `Selling_And_Marketing_Expenses`,
            `Selling_General_And_Administrative_Expenses`, `Other_Expenses`, `Operating_Expenses`,
            `Cost_And_Expenses`, `Net_Interest_Income`, `Interest_Income`, `Interest_Expense`,
            `Depreciation_And_Amortization`, `EBITDA`, `EBIT`,
            `Non_Operating_Income_Excluding_Interest`, `Operating_Income`,
            `Total_Other_Income_Expenses_Net`, `Income_Before_Tax`, `Income_Tax_Expense`,
            `Net_Income_From_Continuing_Operations`, `Net_Income_From_Discontinued_Operations`,
            `Other_Adjustments_To_Net_Income`, `Net_Income`, `Net_Income_Deductions`,
            `Bottom_Line_Net_Income`, `EPS`, `EPS_Diluted`, `Weighted_Average_Shs_Out`,
            `Weighted_Average_Shs_Out_Dil`

            *Note: Requesting an item that does not belong to the selected stmt will result in a 400
            error.*
        fiscal_period (str | Unset): Fiscal period (e.g., 'annual' or 'quarterly') Default:
            'annual'.
        reporting_basis (str | Unset): Reporting basis (e.g., 'original' or 'latest' or 'all')
            Default: 'latest'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[FSStandardized]]
    """

    kwargs = _get_kwargs(
        cik=cik,
        stmt=stmt,
        items=items,
        fiscal_period=fiscal_period,
        reporting_basis=reporting_basis,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cik: int,
    stmt: FSCode,
    *,
    client: AuthenticatedClient | Client,
    items: list[BalanceSheetItem | CashFlowItem | IncomeStatementItem],
    fiscal_period: str | Unset = "annual",
    reporting_basis: str | Unset = "latest",
) -> HTTPValidationError | list[FSStandardized] | None:
    """Standardized

     Fetch financial stmt item time series data.

    Args:
        cik: Company central index key
        stmt: Statement type (e.g., 'BS' for Balance Sheet, 'IS' for Income Statement, 'CF' for Cash
    Flow)
        item: Item name such as 'revenue', 'costOfRevenue'
        FiscalPeriod: Reporting period ('annual' or 'quarterly')
        original: Boolean to indicate whether to return original values or latest values

    Returns:
        List of FSStandardized (cik, stmt, item, date, value, uom, tag, version, form, fy, pf filed,
    qtrs, adsh)

    Args:
        cik (int):
        stmt (FSCode):
        items (list[BalanceSheetItem | CashFlowItem | IncomeStatementItem]):
            **List of specific financial line items to retrieve.** The required items depend on the
            `stmt` parameter:

            * **For stmt=`BS` (Balance Sheet) valid items are:**
                `Cash_And_Cash_Equivalents`, `Short_Term_Investments`,
            `Cash_And_Short_Term_Investments`, `Net_Receivables`, `Accounts_Receivables`,
            `Other_Receivables`, `Inventory`, `Prepaids`, `Other_Current_Assets`,
            `Total_Current_Assets`, `Property_Plant_Equipment_Net`, `Goodwill`, `Intangible_Assets`,
            `Goodwill_And_Intangible_Assets`, `Long_Term_Investments`, `Tax_Assets`,
            `Other_Non_Current_Assets`, `Total_Non_Current_Assets`, `Other_Assets`, `Total_Assets`,
            `Total_Payables`, `Accounts_Payables`, `Other_Payables`, `Accrued_Expenses`,
            `Short_Term_Debt`, `Capital_Lease_Obligations_Current`, `Tax_Payables`,
            `Deferred_Revenue`, `Other_Current_Liabilities`, `Total_Current_Liabilities`,
            `Long_Term_Debt`, `Capital_Lease_Obligations_Non_Current`, `Deferred_Revenue_Non_Current`,
            `Deferred_Tax_Liabilities_Non_Current`, `Other_Non_Current_Liabilities`,
            `Total_Non_Current_Liabilities`, `Other_Liabilities`, `Capital_Lease_Obligations`,
            `Total_Liabilities`, `Treasury_Stock`, `Preferred_Stock`, `Common_Stock`,
            `Retained_Earnings`, `Additional_Paid_In_Capital`,
            `Accumulated_Other_Comprehensive_Income_Loss`, `Other_Total_Stockholders_Equity`,
            `Total_Stockholders_Equity`, `Total_Equity`, `Minority_Interest`,
            `Total_Liabilities_And_Total_Equity`, `Total_Investments`, `Total_Debt`, `Net_Debt`
            * **For stmt=`CF` (Cash Flow) valid items are:**
                `Net_Income`, `Depreciation_And_Amortization`, `Deferred_Income_Tax`,
            `Stock_Based_Compensation`, `Change_In_Working_Capital`, `Accounts_Receivables`,
            `Inventory`, `Accounts_Payables`, `Other_Working_Capital`, `Other_Non_Cash_Items`,
            `Net_Cash_Provided_By_Operating_Activities`,
            `Investments_In_Property_Plant_And_Equipment`, `Acquisitions_Net`,
            `Purchases_Of_Investments`, `Sales_Maturities_Of_Investments`,
            `Other_Investing_Activities`, `Net_Cash_Provided_By_Investing_Activities`,
            `Net_Debt_Issuance`, `Long_Term_Net_Debt_Issuance`, `Short_Term_Net_Debt_Issuance`,
            `Net_Stock_Issuance`, `Net_Common_Stock_Issuance`, `Common_Stock_Issuance`,
            `Common_Stock_Repurchased`, `Net_Preferred_Stock_Issuance`, `Net_Dividends_Paid`,
            `Common_Dividends_Paid`, `Preferred_Dividends_Paid`, `Other_Financing_Activities`,
            `Net_Cash_Provided_By_Financing_Activities`, `Effect_Of_Forex_Changes_On_Cash`,
            `Net_Change_In_Cash`, `Cash_At_End_Of_Period`, `Cash_At_Beginning_Of_Period`,
            `Operating_Cash_Flow`, `Capital_Expenditure`, `Free_Cash_Flow`, `Income_Taxes_Paid`,
            `Interest_Paid`
            * **For stmt=`IS` (Income Statement):**
                `Revenue`, `Cost_Of_Revenue`, `Gross_Profit`, `Research_And_Development_Expenses`,
            `General_And_Administrative_Expenses`, `Selling_And_Marketing_Expenses`,
            `Selling_General_And_Administrative_Expenses`, `Other_Expenses`, `Operating_Expenses`,
            `Cost_And_Expenses`, `Net_Interest_Income`, `Interest_Income`, `Interest_Expense`,
            `Depreciation_And_Amortization`, `EBITDA`, `EBIT`,
            `Non_Operating_Income_Excluding_Interest`, `Operating_Income`,
            `Total_Other_Income_Expenses_Net`, `Income_Before_Tax`, `Income_Tax_Expense`,
            `Net_Income_From_Continuing_Operations`, `Net_Income_From_Discontinued_Operations`,
            `Other_Adjustments_To_Net_Income`, `Net_Income`, `Net_Income_Deductions`,
            `Bottom_Line_Net_Income`, `EPS`, `EPS_Diluted`, `Weighted_Average_Shs_Out`,
            `Weighted_Average_Shs_Out_Dil`

            *Note: Requesting an item that does not belong to the selected stmt will result in a 400
            error.*
        fiscal_period (str | Unset): Fiscal period (e.g., 'annual' or 'quarterly') Default:
            'annual'.
        reporting_basis (str | Unset): Reporting basis (e.g., 'original' or 'latest' or 'all')
            Default: 'latest'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[FSStandardized]
    """

    return sync_detailed(
        cik=cik,
        stmt=stmt,
        client=client,
        items=items,
        fiscal_period=fiscal_period,
        reporting_basis=reporting_basis,
    ).parsed


async def asyncio_detailed(
    cik: int,
    stmt: FSCode,
    *,
    client: AuthenticatedClient | Client,
    items: list[BalanceSheetItem | CashFlowItem | IncomeStatementItem],
    fiscal_period: str | Unset = "annual",
    reporting_basis: str | Unset = "latest",
) -> Response[HTTPValidationError | list[FSStandardized]]:
    """Standardized

     Fetch financial stmt item time series data.

    Args:
        cik: Company central index key
        stmt: Statement type (e.g., 'BS' for Balance Sheet, 'IS' for Income Statement, 'CF' for Cash
    Flow)
        item: Item name such as 'revenue', 'costOfRevenue'
        FiscalPeriod: Reporting period ('annual' or 'quarterly')
        original: Boolean to indicate whether to return original values or latest values

    Returns:
        List of FSStandardized (cik, stmt, item, date, value, uom, tag, version, form, fy, pf filed,
    qtrs, adsh)

    Args:
        cik (int):
        stmt (FSCode):
        items (list[BalanceSheetItem | CashFlowItem | IncomeStatementItem]):
            **List of specific financial line items to retrieve.** The required items depend on the
            `stmt` parameter:

            * **For stmt=`BS` (Balance Sheet) valid items are:**
                `Cash_And_Cash_Equivalents`, `Short_Term_Investments`,
            `Cash_And_Short_Term_Investments`, `Net_Receivables`, `Accounts_Receivables`,
            `Other_Receivables`, `Inventory`, `Prepaids`, `Other_Current_Assets`,
            `Total_Current_Assets`, `Property_Plant_Equipment_Net`, `Goodwill`, `Intangible_Assets`,
            `Goodwill_And_Intangible_Assets`, `Long_Term_Investments`, `Tax_Assets`,
            `Other_Non_Current_Assets`, `Total_Non_Current_Assets`, `Other_Assets`, `Total_Assets`,
            `Total_Payables`, `Accounts_Payables`, `Other_Payables`, `Accrued_Expenses`,
            `Short_Term_Debt`, `Capital_Lease_Obligations_Current`, `Tax_Payables`,
            `Deferred_Revenue`, `Other_Current_Liabilities`, `Total_Current_Liabilities`,
            `Long_Term_Debt`, `Capital_Lease_Obligations_Non_Current`, `Deferred_Revenue_Non_Current`,
            `Deferred_Tax_Liabilities_Non_Current`, `Other_Non_Current_Liabilities`,
            `Total_Non_Current_Liabilities`, `Other_Liabilities`, `Capital_Lease_Obligations`,
            `Total_Liabilities`, `Treasury_Stock`, `Preferred_Stock`, `Common_Stock`,
            `Retained_Earnings`, `Additional_Paid_In_Capital`,
            `Accumulated_Other_Comprehensive_Income_Loss`, `Other_Total_Stockholders_Equity`,
            `Total_Stockholders_Equity`, `Total_Equity`, `Minority_Interest`,
            `Total_Liabilities_And_Total_Equity`, `Total_Investments`, `Total_Debt`, `Net_Debt`
            * **For stmt=`CF` (Cash Flow) valid items are:**
                `Net_Income`, `Depreciation_And_Amortization`, `Deferred_Income_Tax`,
            `Stock_Based_Compensation`, `Change_In_Working_Capital`, `Accounts_Receivables`,
            `Inventory`, `Accounts_Payables`, `Other_Working_Capital`, `Other_Non_Cash_Items`,
            `Net_Cash_Provided_By_Operating_Activities`,
            `Investments_In_Property_Plant_And_Equipment`, `Acquisitions_Net`,
            `Purchases_Of_Investments`, `Sales_Maturities_Of_Investments`,
            `Other_Investing_Activities`, `Net_Cash_Provided_By_Investing_Activities`,
            `Net_Debt_Issuance`, `Long_Term_Net_Debt_Issuance`, `Short_Term_Net_Debt_Issuance`,
            `Net_Stock_Issuance`, `Net_Common_Stock_Issuance`, `Common_Stock_Issuance`,
            `Common_Stock_Repurchased`, `Net_Preferred_Stock_Issuance`, `Net_Dividends_Paid`,
            `Common_Dividends_Paid`, `Preferred_Dividends_Paid`, `Other_Financing_Activities`,
            `Net_Cash_Provided_By_Financing_Activities`, `Effect_Of_Forex_Changes_On_Cash`,
            `Net_Change_In_Cash`, `Cash_At_End_Of_Period`, `Cash_At_Beginning_Of_Period`,
            `Operating_Cash_Flow`, `Capital_Expenditure`, `Free_Cash_Flow`, `Income_Taxes_Paid`,
            `Interest_Paid`
            * **For stmt=`IS` (Income Statement):**
                `Revenue`, `Cost_Of_Revenue`, `Gross_Profit`, `Research_And_Development_Expenses`,
            `General_And_Administrative_Expenses`, `Selling_And_Marketing_Expenses`,
            `Selling_General_And_Administrative_Expenses`, `Other_Expenses`, `Operating_Expenses`,
            `Cost_And_Expenses`, `Net_Interest_Income`, `Interest_Income`, `Interest_Expense`,
            `Depreciation_And_Amortization`, `EBITDA`, `EBIT`,
            `Non_Operating_Income_Excluding_Interest`, `Operating_Income`,
            `Total_Other_Income_Expenses_Net`, `Income_Before_Tax`, `Income_Tax_Expense`,
            `Net_Income_From_Continuing_Operations`, `Net_Income_From_Discontinued_Operations`,
            `Other_Adjustments_To_Net_Income`, `Net_Income`, `Net_Income_Deductions`,
            `Bottom_Line_Net_Income`, `EPS`, `EPS_Diluted`, `Weighted_Average_Shs_Out`,
            `Weighted_Average_Shs_Out_Dil`

            *Note: Requesting an item that does not belong to the selected stmt will result in a 400
            error.*
        fiscal_period (str | Unset): Fiscal period (e.g., 'annual' or 'quarterly') Default:
            'annual'.
        reporting_basis (str | Unset): Reporting basis (e.g., 'original' or 'latest' or 'all')
            Default: 'latest'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[FSStandardized]]
    """

    kwargs = _get_kwargs(
        cik=cik,
        stmt=stmt,
        items=items,
        fiscal_period=fiscal_period,
        reporting_basis=reporting_basis,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cik: int,
    stmt: FSCode,
    *,
    client: AuthenticatedClient | Client,
    items: list[BalanceSheetItem | CashFlowItem | IncomeStatementItem],
    fiscal_period: str | Unset = "annual",
    reporting_basis: str | Unset = "latest",
) -> HTTPValidationError | list[FSStandardized] | None:
    """Standardized

     Fetch financial stmt item time series data.

    Args:
        cik: Company central index key
        stmt: Statement type (e.g., 'BS' for Balance Sheet, 'IS' for Income Statement, 'CF' for Cash
    Flow)
        item: Item name such as 'revenue', 'costOfRevenue'
        FiscalPeriod: Reporting period ('annual' or 'quarterly')
        original: Boolean to indicate whether to return original values or latest values

    Returns:
        List of FSStandardized (cik, stmt, item, date, value, uom, tag, version, form, fy, pf filed,
    qtrs, adsh)

    Args:
        cik (int):
        stmt (FSCode):
        items (list[BalanceSheetItem | CashFlowItem | IncomeStatementItem]):
            **List of specific financial line items to retrieve.** The required items depend on the
            `stmt` parameter:

            * **For stmt=`BS` (Balance Sheet) valid items are:**
                `Cash_And_Cash_Equivalents`, `Short_Term_Investments`,
            `Cash_And_Short_Term_Investments`, `Net_Receivables`, `Accounts_Receivables`,
            `Other_Receivables`, `Inventory`, `Prepaids`, `Other_Current_Assets`,
            `Total_Current_Assets`, `Property_Plant_Equipment_Net`, `Goodwill`, `Intangible_Assets`,
            `Goodwill_And_Intangible_Assets`, `Long_Term_Investments`, `Tax_Assets`,
            `Other_Non_Current_Assets`, `Total_Non_Current_Assets`, `Other_Assets`, `Total_Assets`,
            `Total_Payables`, `Accounts_Payables`, `Other_Payables`, `Accrued_Expenses`,
            `Short_Term_Debt`, `Capital_Lease_Obligations_Current`, `Tax_Payables`,
            `Deferred_Revenue`, `Other_Current_Liabilities`, `Total_Current_Liabilities`,
            `Long_Term_Debt`, `Capital_Lease_Obligations_Non_Current`, `Deferred_Revenue_Non_Current`,
            `Deferred_Tax_Liabilities_Non_Current`, `Other_Non_Current_Liabilities`,
            `Total_Non_Current_Liabilities`, `Other_Liabilities`, `Capital_Lease_Obligations`,
            `Total_Liabilities`, `Treasury_Stock`, `Preferred_Stock`, `Common_Stock`,
            `Retained_Earnings`, `Additional_Paid_In_Capital`,
            `Accumulated_Other_Comprehensive_Income_Loss`, `Other_Total_Stockholders_Equity`,
            `Total_Stockholders_Equity`, `Total_Equity`, `Minority_Interest`,
            `Total_Liabilities_And_Total_Equity`, `Total_Investments`, `Total_Debt`, `Net_Debt`
            * **For stmt=`CF` (Cash Flow) valid items are:**
                `Net_Income`, `Depreciation_And_Amortization`, `Deferred_Income_Tax`,
            `Stock_Based_Compensation`, `Change_In_Working_Capital`, `Accounts_Receivables`,
            `Inventory`, `Accounts_Payables`, `Other_Working_Capital`, `Other_Non_Cash_Items`,
            `Net_Cash_Provided_By_Operating_Activities`,
            `Investments_In_Property_Plant_And_Equipment`, `Acquisitions_Net`,
            `Purchases_Of_Investments`, `Sales_Maturities_Of_Investments`,
            `Other_Investing_Activities`, `Net_Cash_Provided_By_Investing_Activities`,
            `Net_Debt_Issuance`, `Long_Term_Net_Debt_Issuance`, `Short_Term_Net_Debt_Issuance`,
            `Net_Stock_Issuance`, `Net_Common_Stock_Issuance`, `Common_Stock_Issuance`,
            `Common_Stock_Repurchased`, `Net_Preferred_Stock_Issuance`, `Net_Dividends_Paid`,
            `Common_Dividends_Paid`, `Preferred_Dividends_Paid`, `Other_Financing_Activities`,
            `Net_Cash_Provided_By_Financing_Activities`, `Effect_Of_Forex_Changes_On_Cash`,
            `Net_Change_In_Cash`, `Cash_At_End_Of_Period`, `Cash_At_Beginning_Of_Period`,
            `Operating_Cash_Flow`, `Capital_Expenditure`, `Free_Cash_Flow`, `Income_Taxes_Paid`,
            `Interest_Paid`
            * **For stmt=`IS` (Income Statement):**
                `Revenue`, `Cost_Of_Revenue`, `Gross_Profit`, `Research_And_Development_Expenses`,
            `General_And_Administrative_Expenses`, `Selling_And_Marketing_Expenses`,
            `Selling_General_And_Administrative_Expenses`, `Other_Expenses`, `Operating_Expenses`,
            `Cost_And_Expenses`, `Net_Interest_Income`, `Interest_Income`, `Interest_Expense`,
            `Depreciation_And_Amortization`, `EBITDA`, `EBIT`,
            `Non_Operating_Income_Excluding_Interest`, `Operating_Income`,
            `Total_Other_Income_Expenses_Net`, `Income_Before_Tax`, `Income_Tax_Expense`,
            `Net_Income_From_Continuing_Operations`, `Net_Income_From_Discontinued_Operations`,
            `Other_Adjustments_To_Net_Income`, `Net_Income`, `Net_Income_Deductions`,
            `Bottom_Line_Net_Income`, `EPS`, `EPS_Diluted`, `Weighted_Average_Shs_Out`,
            `Weighted_Average_Shs_Out_Dil`

            *Note: Requesting an item that does not belong to the selected stmt will result in a 400
            error.*
        fiscal_period (str | Unset): Fiscal period (e.g., 'annual' or 'quarterly') Default:
            'annual'.
        reporting_basis (str | Unset): Reporting basis (e.g., 'original' or 'latest' or 'all')
            Default: 'latest'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[FSStandardized]
    """

    return (
        await asyncio_detailed(
            cik=cik,
            stmt=stmt,
            client=client,
            items=items,
            fiscal_period=fiscal_period,
            reporting_basis=reporting_basis,
        )
    ).parsed
