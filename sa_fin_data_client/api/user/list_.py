from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_org_list import UserOrgList
from ...types import UNSET, Response


def _get_kwargs(
    *,
    list_name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["list_name"] = list_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/user/list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UserOrgList | None:
    if response.status_code == 200:
        response_200 = UserOrgList.from_dict(response.json())

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
) -> Response[HTTPValidationError | UserOrgList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    list_name: str,
) -> Response[HTTPValidationError | UserOrgList]:
    """List

     Args:
        list_name: The name of the list to get

    Returns:
        A UserOrgList

    Args:
        list_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserOrgList]
    """

    kwargs = _get_kwargs(
        list_name=list_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    list_name: str,
) -> HTTPValidationError | UserOrgList | None:
    """List

     Args:
        list_name: The name of the list to get

    Returns:
        A UserOrgList

    Args:
        list_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserOrgList
    """

    return sync_detailed(
        client=client,
        list_name=list_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    list_name: str,
) -> Response[HTTPValidationError | UserOrgList]:
    """List

     Args:
        list_name: The name of the list to get

    Returns:
        A UserOrgList

    Args:
        list_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserOrgList]
    """

    kwargs = _get_kwargs(
        list_name=list_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    list_name: str,
) -> HTTPValidationError | UserOrgList | None:
    """List

     Args:
        list_name: The name of the list to get

    Returns:
        A UserOrgList

    Args:
        list_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserOrgList
    """

    return (
        await asyncio_detailed(
            client=client,
            list_name=list_name,
        )
    ).parsed
