from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.field_info import FieldInfo
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    tableid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/list/field_info/{tableid}".format(
            tableid=quote(str(tableid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[FieldInfo] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FieldInfo.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[FieldInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tableid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | list[FieldInfo]]:
    """Field Info

    Args:
        tableid (str): The table name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[FieldInfo]]
    """

    kwargs = _get_kwargs(
        tableid=tableid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tableid: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | list[FieldInfo] | None:
    """Field Info

    Args:
        tableid (str): The table name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[FieldInfo]
    """

    return sync_detailed(
        tableid=tableid,
        client=client,
    ).parsed


async def asyncio_detailed(
    tableid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | list[FieldInfo]]:
    """Field Info

    Args:
        tableid (str): The table name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[FieldInfo]]
    """

    kwargs = _get_kwargs(
        tableid=tableid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tableid: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | list[FieldInfo] | None:
    """Field Info

    Args:
        tableid (str): The table name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[FieldInfo]
    """

    return (
        await asyncio_detailed(
            tableid=tableid,
            client=client,
        )
    ).parsed
