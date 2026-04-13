from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company import Company
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: None | str | Unset = UNSET,
    symbol: None | str | Unset = UNSET,
    cik: int | None | Unset = UNSET,
    figi: None | str | Unset = UNSET,
    org_permid: None | str | Unset = UNSET,
    isin: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_name: None | str | Unset
    if isinstance(name, Unset):
        json_name = UNSET
    else:
        json_name = name
    params["name"] = json_name

    json_symbol: None | str | Unset
    if isinstance(symbol, Unset):
        json_symbol = UNSET
    else:
        json_symbol = symbol
    params["symbol"] = json_symbol

    json_cik: int | None | Unset
    if isinstance(cik, Unset):
        json_cik = UNSET
    else:
        json_cik = cik
    params["cik"] = json_cik

    json_figi: None | str | Unset
    if isinstance(figi, Unset):
        json_figi = UNSET
    else:
        json_figi = figi
    params["figi"] = json_figi

    json_org_permid: None | str | Unset
    if isinstance(org_permid, Unset):
        json_org_permid = UNSET
    else:
        json_org_permid = org_permid
    params["org_permid"] = json_org_permid

    json_isin: None | str | Unset
    if isinstance(isin, Unset):
        json_isin = UNSET
    else:
        json_isin = isin
    params["isin"] = json_isin

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/company/overview",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Company | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = Company.from_dict(response.json())

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
) -> Response[Company | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: None | str | Unset = UNSET,
    symbol: None | str | Unset = UNSET,
    cik: int | None | Unset = UNSET,
    figi: None | str | Unset = UNSET,
    org_permid: None | str | Unset = UNSET,
    isin: None | str | Unset = UNSET,
) -> Response[Company | HTTPValidationError]:
    """Overview

     Fetch Company overview data for a given company identifier.

    Returns:
        Company data such as name, description, industry, identifiers, exchanges, etc.

    Args:
        name (None | str | Unset): Full legal name of the entity - Supports fuzzy matching for
            partial or similar names
        symbol (None | str | Unset): Stock ticker symbol - The exchange-listed trading symbol for
            the company
        cik (int | None | Unset): Central Index Key (CIK). SEC assigned ten digit number (with
            leading zeros) to each registrant that submits filings.
        figi (None | str | Unset): Financial Instrument Global Identifier - A 12-character
            identifier for financial instruments
        org_permid (None | str | Unset): A globally unique, persistent identifier assigned by LSEG
            to companies and organizations.
        isin (None | str | Unset): International Securities Identification Number - A 12-character
            code identifying a security instrument

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Company | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        name=name,
        symbol=symbol,
        cik=cik,
        figi=figi,
        org_permid=org_permid,
        isin=isin,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    name: None | str | Unset = UNSET,
    symbol: None | str | Unset = UNSET,
    cik: int | None | Unset = UNSET,
    figi: None | str | Unset = UNSET,
    org_permid: None | str | Unset = UNSET,
    isin: None | str | Unset = UNSET,
) -> Company | HTTPValidationError | None:
    """Overview

     Fetch Company overview data for a given company identifier.

    Returns:
        Company data such as name, description, industry, identifiers, exchanges, etc.

    Args:
        name (None | str | Unset): Full legal name of the entity - Supports fuzzy matching for
            partial or similar names
        symbol (None | str | Unset): Stock ticker symbol - The exchange-listed trading symbol for
            the company
        cik (int | None | Unset): Central Index Key (CIK). SEC assigned ten digit number (with
            leading zeros) to each registrant that submits filings.
        figi (None | str | Unset): Financial Instrument Global Identifier - A 12-character
            identifier for financial instruments
        org_permid (None | str | Unset): A globally unique, persistent identifier assigned by LSEG
            to companies and organizations.
        isin (None | str | Unset): International Securities Identification Number - A 12-character
            code identifying a security instrument

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Company | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        name=name,
        symbol=symbol,
        cik=cik,
        figi=figi,
        org_permid=org_permid,
        isin=isin,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: None | str | Unset = UNSET,
    symbol: None | str | Unset = UNSET,
    cik: int | None | Unset = UNSET,
    figi: None | str | Unset = UNSET,
    org_permid: None | str | Unset = UNSET,
    isin: None | str | Unset = UNSET,
) -> Response[Company | HTTPValidationError]:
    """Overview

     Fetch Company overview data for a given company identifier.

    Returns:
        Company data such as name, description, industry, identifiers, exchanges, etc.

    Args:
        name (None | str | Unset): Full legal name of the entity - Supports fuzzy matching for
            partial or similar names
        symbol (None | str | Unset): Stock ticker symbol - The exchange-listed trading symbol for
            the company
        cik (int | None | Unset): Central Index Key (CIK). SEC assigned ten digit number (with
            leading zeros) to each registrant that submits filings.
        figi (None | str | Unset): Financial Instrument Global Identifier - A 12-character
            identifier for financial instruments
        org_permid (None | str | Unset): A globally unique, persistent identifier assigned by LSEG
            to companies and organizations.
        isin (None | str | Unset): International Securities Identification Number - A 12-character
            code identifying a security instrument

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Company | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        name=name,
        symbol=symbol,
        cik=cik,
        figi=figi,
        org_permid=org_permid,
        isin=isin,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: None | str | Unset = UNSET,
    symbol: None | str | Unset = UNSET,
    cik: int | None | Unset = UNSET,
    figi: None | str | Unset = UNSET,
    org_permid: None | str | Unset = UNSET,
    isin: None | str | Unset = UNSET,
) -> Company | HTTPValidationError | None:
    """Overview

     Fetch Company overview data for a given company identifier.

    Returns:
        Company data such as name, description, industry, identifiers, exchanges, etc.

    Args:
        name (None | str | Unset): Full legal name of the entity - Supports fuzzy matching for
            partial or similar names
        symbol (None | str | Unset): Stock ticker symbol - The exchange-listed trading symbol for
            the company
        cik (int | None | Unset): Central Index Key (CIK). SEC assigned ten digit number (with
            leading zeros) to each registrant that submits filings.
        figi (None | str | Unset): Financial Instrument Global Identifier - A 12-character
            identifier for financial instruments
        org_permid (None | str | Unset): A globally unique, persistent identifier assigned by LSEG
            to companies and organizations.
        isin (None | str | Unset): International Securities Identification Number - A 12-character
            code identifying a security instrument

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Company | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            symbol=symbol,
            cik=cik,
            figi=figi,
            org_permid=org_permid,
            isin=isin,
        )
    ).parsed
