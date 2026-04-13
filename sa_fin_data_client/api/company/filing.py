from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fs_code_extended import FSCodeExtended
from ...models.http_validation_error import HTTPValidationError
from ...models.statement_row import StatementRow
from ...types import UNSET, Response, Unset


def _get_kwargs(
    adsh: str,
    *,
    stmt: FSCodeExtended | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_stmt: None | str | Unset
    if isinstance(stmt, Unset):
        json_stmt = UNSET
    elif isinstance(stmt, FSCodeExtended):
        json_stmt = stmt.value
    else:
        json_stmt = stmt
    params["stmt"] = json_stmt

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/company/fs/filing/{adsh}".format(
            adsh=quote(str(adsh), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[StatementRow] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = StatementRow.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[StatementRow]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    adsh: str,
    *,
    client: AuthenticatedClient | Client,
    stmt: FSCodeExtended | None | Unset = UNSET,
) -> Response[HTTPValidationError | list[StatementRow]]:
    """Filing

     Fetch financial statement data for a given ADSH and statement type. ADSHs for a company can be found
    using company/get_filings.

    Returns:
        List of statement rows with tag, label, date, and values

    Args:
        adsh (str): The accession number (ADSH) of the filing.
        stmt (FSCodeExtended | None | Unset): The statement type for which to get financial data,
            e.g. CP-Cover Page, IS-Income Statement, CI-Comprehensive Income,BS-Balance Sheet, CF-Cash
            Flow,  EQ-Equity, OT-Other (NULL or UN), UN-Unclassifiable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[StatementRow]]
    """

    kwargs = _get_kwargs(
        adsh=adsh,
        stmt=stmt,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    adsh: str,
    *,
    client: AuthenticatedClient | Client,
    stmt: FSCodeExtended | None | Unset = UNSET,
) -> HTTPValidationError | list[StatementRow] | None:
    """Filing

     Fetch financial statement data for a given ADSH and statement type. ADSHs for a company can be found
    using company/get_filings.

    Returns:
        List of statement rows with tag, label, date, and values

    Args:
        adsh (str): The accession number (ADSH) of the filing.
        stmt (FSCodeExtended | None | Unset): The statement type for which to get financial data,
            e.g. CP-Cover Page, IS-Income Statement, CI-Comprehensive Income,BS-Balance Sheet, CF-Cash
            Flow,  EQ-Equity, OT-Other (NULL or UN), UN-Unclassifiable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[StatementRow]
    """

    return sync_detailed(
        adsh=adsh,
        client=client,
        stmt=stmt,
    ).parsed


async def asyncio_detailed(
    adsh: str,
    *,
    client: AuthenticatedClient | Client,
    stmt: FSCodeExtended | None | Unset = UNSET,
) -> Response[HTTPValidationError | list[StatementRow]]:
    """Filing

     Fetch financial statement data for a given ADSH and statement type. ADSHs for a company can be found
    using company/get_filings.

    Returns:
        List of statement rows with tag, label, date, and values

    Args:
        adsh (str): The accession number (ADSH) of the filing.
        stmt (FSCodeExtended | None | Unset): The statement type for which to get financial data,
            e.g. CP-Cover Page, IS-Income Statement, CI-Comprehensive Income,BS-Balance Sheet, CF-Cash
            Flow,  EQ-Equity, OT-Other (NULL or UN), UN-Unclassifiable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[StatementRow]]
    """

    kwargs = _get_kwargs(
        adsh=adsh,
        stmt=stmt,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    adsh: str,
    *,
    client: AuthenticatedClient | Client,
    stmt: FSCodeExtended | None | Unset = UNSET,
) -> HTTPValidationError | list[StatementRow] | None:
    """Filing

     Fetch financial statement data for a given ADSH and statement type. ADSHs for a company can be found
    using company/get_filings.

    Returns:
        List of statement rows with tag, label, date, and values

    Args:
        adsh (str): The accession number (ADSH) of the filing.
        stmt (FSCodeExtended | None | Unset): The statement type for which to get financial data,
            e.g. CP-Cover Page, IS-Income Statement, CI-Comprehensive Income,BS-Balance Sheet, CF-Cash
            Flow,  EQ-Equity, OT-Other (NULL or UN), UN-Unclassifiable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[StatementRow]
    """

    return (
        await asyncio_detailed(
            adsh=adsh,
            client=client,
            stmt=stmt,
        )
    ).parsed
