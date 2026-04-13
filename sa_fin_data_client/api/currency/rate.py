from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.currency_rate import CurrencyRate
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    from_currency: str,
    to_currency: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/currency/rate/{from_currency}/{to_currency}".format(
            from_currency=quote(str(from_currency), safe=""),
            to_currency=quote(str(to_currency), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[CurrencyRate] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CurrencyRate.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[CurrencyRate]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    from_currency: str,
    to_currency: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | list[CurrencyRate]]:
    """Rate

     Calculate the exchange rate between any two currencies - AUD, BRL, CAD, CNY, EUR, GBP, HKD, INR,
    IDR, JPY, MXN, NZD, NOK, PEN, RUB, SAR, SGD, ZAR, KRW, SEK, CHF, TWD, TRY, USD

    Returns:
        A list of CurrencyRates

    Args:
        from_currency (str): The original currency
        to_currency (str): The currency of the rate to be converted to

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[CurrencyRate]]
    """

    kwargs = _get_kwargs(
        from_currency=from_currency,
        to_currency=to_currency,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    from_currency: str,
    to_currency: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | list[CurrencyRate] | None:
    """Rate

     Calculate the exchange rate between any two currencies - AUD, BRL, CAD, CNY, EUR, GBP, HKD, INR,
    IDR, JPY, MXN, NZD, NOK, PEN, RUB, SAR, SGD, ZAR, KRW, SEK, CHF, TWD, TRY, USD

    Returns:
        A list of CurrencyRates

    Args:
        from_currency (str): The original currency
        to_currency (str): The currency of the rate to be converted to

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[CurrencyRate]
    """

    return sync_detailed(
        from_currency=from_currency,
        to_currency=to_currency,
        client=client,
    ).parsed


async def asyncio_detailed(
    from_currency: str,
    to_currency: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | list[CurrencyRate]]:
    """Rate

     Calculate the exchange rate between any two currencies - AUD, BRL, CAD, CNY, EUR, GBP, HKD, INR,
    IDR, JPY, MXN, NZD, NOK, PEN, RUB, SAR, SGD, ZAR, KRW, SEK, CHF, TWD, TRY, USD

    Returns:
        A list of CurrencyRates

    Args:
        from_currency (str): The original currency
        to_currency (str): The currency of the rate to be converted to

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[CurrencyRate]]
    """

    kwargs = _get_kwargs(
        from_currency=from_currency,
        to_currency=to_currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    from_currency: str,
    to_currency: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | list[CurrencyRate] | None:
    """Rate

     Calculate the exchange rate between any two currencies - AUD, BRL, CAD, CNY, EUR, GBP, HKD, INR,
    IDR, JPY, MXN, NZD, NOK, PEN, RUB, SAR, SGD, ZAR, KRW, SEK, CHF, TWD, TRY, USD

    Returns:
        A list of CurrencyRates

    Args:
        from_currency (str): The original currency
        to_currency (str): The currency of the rate to be converted to

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[CurrencyRate]
    """

    return (
        await asyncio_detailed(
            from_currency=from_currency,
            to_currency=to_currency,
            client=client,
        )
    ).parsed
