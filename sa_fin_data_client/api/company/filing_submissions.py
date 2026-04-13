from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.sub import Sub
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    period: str,
    name: None | str | Unset = UNSET,
    symbol: None | str | Unset = UNSET,
    cik: int | None | Unset = UNSET,
    figi: None | str | Unset = UNSET,
    org_permid: None | str | Unset = UNSET,
    isin: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["period"] = period

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
        "url": "/company/fs/filing_submissions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[Sub] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Sub.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[Sub]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    period: str,
    name: None | str | Unset = UNSET,
    symbol: None | str | Unset = UNSET,
    cik: int | None | Unset = UNSET,
    figi: None | str | Unset = UNSET,
    org_permid: None | str | Unset = UNSET,
    isin: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[Sub]]:
    """Filing Submissions

     Get the Annual or Quarterly financial report filing (Sub)missions for a company.

    period: The period for which to get financial report filings (all, annual, quarterly)

    Returns:
        A list of Sub(missions) that include the accession number (ADSH) to access the filing and data
    related to the submission.

    Args:
        period (str): The period for which to get filings (all, annual, quarterly)
        name (None | str | Unset):
        symbol (None | str | Unset):
        cik (int | None | Unset):
        figi (None | str | Unset):
        org_permid (None | str | Unset):
        isin (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[Sub]]
    """

    kwargs = _get_kwargs(
        period=period,
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
    period: str,
    name: None | str | Unset = UNSET,
    symbol: None | str | Unset = UNSET,
    cik: int | None | Unset = UNSET,
    figi: None | str | Unset = UNSET,
    org_permid: None | str | Unset = UNSET,
    isin: None | str | Unset = UNSET,
) -> HTTPValidationError | list[Sub] | None:
    """Filing Submissions

     Get the Annual or Quarterly financial report filing (Sub)missions for a company.

    period: The period for which to get financial report filings (all, annual, quarterly)

    Returns:
        A list of Sub(missions) that include the accession number (ADSH) to access the filing and data
    related to the submission.

    Args:
        period (str): The period for which to get filings (all, annual, quarterly)
        name (None | str | Unset):
        symbol (None | str | Unset):
        cik (int | None | Unset):
        figi (None | str | Unset):
        org_permid (None | str | Unset):
        isin (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[Sub]
    """

    return sync_detailed(
        client=client,
        period=period,
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
    period: str,
    name: None | str | Unset = UNSET,
    symbol: None | str | Unset = UNSET,
    cik: int | None | Unset = UNSET,
    figi: None | str | Unset = UNSET,
    org_permid: None | str | Unset = UNSET,
    isin: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[Sub]]:
    """Filing Submissions

     Get the Annual or Quarterly financial report filing (Sub)missions for a company.

    period: The period for which to get financial report filings (all, annual, quarterly)

    Returns:
        A list of Sub(missions) that include the accession number (ADSH) to access the filing and data
    related to the submission.

    Args:
        period (str): The period for which to get filings (all, annual, quarterly)
        name (None | str | Unset):
        symbol (None | str | Unset):
        cik (int | None | Unset):
        figi (None | str | Unset):
        org_permid (None | str | Unset):
        isin (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[Sub]]
    """

    kwargs = _get_kwargs(
        period=period,
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
    period: str,
    name: None | str | Unset = UNSET,
    symbol: None | str | Unset = UNSET,
    cik: int | None | Unset = UNSET,
    figi: None | str | Unset = UNSET,
    org_permid: None | str | Unset = UNSET,
    isin: None | str | Unset = UNSET,
) -> HTTPValidationError | list[Sub] | None:
    """Filing Submissions

     Get the Annual or Quarterly financial report filing (Sub)missions for a company.

    period: The period for which to get financial report filings (all, annual, quarterly)

    Returns:
        A list of Sub(missions) that include the accession number (ADSH) to access the filing and data
    related to the submission.

    Args:
        period (str): The period for which to get filings (all, annual, quarterly)
        name (None | str | Unset):
        symbol (None | str | Unset):
        cik (int | None | Unset):
        figi (None | str | Unset):
        org_permid (None | str | Unset):
        isin (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[Sub]
    """

    return (
        await asyncio_detailed(
            client=client,
            period=period,
            name=name,
            symbol=symbol,
            cik=cik,
            figi=figi,
            org_permid=org_permid,
            isin=isin,
        )
    ).parsed
