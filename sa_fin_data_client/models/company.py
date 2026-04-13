from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Company")


@_attrs_define
class Company:
    """
    Attributes:
        name (str):
        cik (int):
        url (None | str | Unset):
        overview (None | str | Unset):
        naics (int | None | Unset):
        sic (int | None | Unset):
        key_focus (None | str | Unset):
        primary_regions (None | str | Unset):
        exchanges (list[str] | None | Unset):
        primary_exchange (None | str | Unset):
        primary_exchange_symbol (None | str | Unset):
        otc (None | str | Unset):
        figi (None | str | Unset):
        org_permid (None | str | Unset):
        isin (None | str | Unset):
        cusip (None | str | Unset):
        nyse_symbol (None | str | Unset):
        tsx_symbol (None | str | Unset):
        tsx_listing_type (None | str | Unset):
        tsx_listing_date (datetime.date | None | Unset):
        index_component (None | str | Unset):
        market_cap_cad (float | None | Unset):
        os_shares (int | None | Unset):
    """

    name: str
    cik: int
    url: None | str | Unset = UNSET
    overview: None | str | Unset = UNSET
    naics: int | None | Unset = UNSET
    sic: int | None | Unset = UNSET
    key_focus: None | str | Unset = UNSET
    primary_regions: None | str | Unset = UNSET
    exchanges: list[str] | None | Unset = UNSET
    primary_exchange: None | str | Unset = UNSET
    primary_exchange_symbol: None | str | Unset = UNSET
    otc: None | str | Unset = UNSET
    figi: None | str | Unset = UNSET
    org_permid: None | str | Unset = UNSET
    isin: None | str | Unset = UNSET
    cusip: None | str | Unset = UNSET
    nyse_symbol: None | str | Unset = UNSET
    tsx_symbol: None | str | Unset = UNSET
    tsx_listing_type: None | str | Unset = UNSET
    tsx_listing_date: datetime.date | None | Unset = UNSET
    index_component: None | str | Unset = UNSET
    market_cap_cad: float | None | Unset = UNSET
    os_shares: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        cik = self.cik

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        overview: None | str | Unset
        if isinstance(self.overview, Unset):
            overview = UNSET
        else:
            overview = self.overview

        naics: int | None | Unset
        if isinstance(self.naics, Unset):
            naics = UNSET
        else:
            naics = self.naics

        sic: int | None | Unset
        if isinstance(self.sic, Unset):
            sic = UNSET
        else:
            sic = self.sic

        key_focus: None | str | Unset
        if isinstance(self.key_focus, Unset):
            key_focus = UNSET
        else:
            key_focus = self.key_focus

        primary_regions: None | str | Unset
        if isinstance(self.primary_regions, Unset):
            primary_regions = UNSET
        else:
            primary_regions = self.primary_regions

        exchanges: list[str] | None | Unset
        if isinstance(self.exchanges, Unset):
            exchanges = UNSET
        elif isinstance(self.exchanges, list):
            exchanges = self.exchanges

        else:
            exchanges = self.exchanges

        primary_exchange: None | str | Unset
        if isinstance(self.primary_exchange, Unset):
            primary_exchange = UNSET
        else:
            primary_exchange = self.primary_exchange

        primary_exchange_symbol: None | str | Unset
        if isinstance(self.primary_exchange_symbol, Unset):
            primary_exchange_symbol = UNSET
        else:
            primary_exchange_symbol = self.primary_exchange_symbol

        otc: None | str | Unset
        if isinstance(self.otc, Unset):
            otc = UNSET
        else:
            otc = self.otc

        figi: None | str | Unset
        if isinstance(self.figi, Unset):
            figi = UNSET
        else:
            figi = self.figi

        org_permid: None | str | Unset
        if isinstance(self.org_permid, Unset):
            org_permid = UNSET
        else:
            org_permid = self.org_permid

        isin: None | str | Unset
        if isinstance(self.isin, Unset):
            isin = UNSET
        else:
            isin = self.isin

        cusip: None | str | Unset
        if isinstance(self.cusip, Unset):
            cusip = UNSET
        else:
            cusip = self.cusip

        nyse_symbol: None | str | Unset
        if isinstance(self.nyse_symbol, Unset):
            nyse_symbol = UNSET
        else:
            nyse_symbol = self.nyse_symbol

        tsx_symbol: None | str | Unset
        if isinstance(self.tsx_symbol, Unset):
            tsx_symbol = UNSET
        else:
            tsx_symbol = self.tsx_symbol

        tsx_listing_type: None | str | Unset
        if isinstance(self.tsx_listing_type, Unset):
            tsx_listing_type = UNSET
        else:
            tsx_listing_type = self.tsx_listing_type

        tsx_listing_date: None | str | Unset
        if isinstance(self.tsx_listing_date, Unset):
            tsx_listing_date = UNSET
        elif isinstance(self.tsx_listing_date, datetime.date):
            tsx_listing_date = self.tsx_listing_date.isoformat()
        else:
            tsx_listing_date = self.tsx_listing_date

        index_component: None | str | Unset
        if isinstance(self.index_component, Unset):
            index_component = UNSET
        else:
            index_component = self.index_component

        market_cap_cad: float | None | Unset
        if isinstance(self.market_cap_cad, Unset):
            market_cap_cad = UNSET
        else:
            market_cap_cad = self.market_cap_cad

        os_shares: int | None | Unset
        if isinstance(self.os_shares, Unset):
            os_shares = UNSET
        else:
            os_shares = self.os_shares

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "cik": cik,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if overview is not UNSET:
            field_dict["overview"] = overview
        if naics is not UNSET:
            field_dict["naics"] = naics
        if sic is not UNSET:
            field_dict["sic"] = sic
        if key_focus is not UNSET:
            field_dict["key_focus"] = key_focus
        if primary_regions is not UNSET:
            field_dict["primary_regions"] = primary_regions
        if exchanges is not UNSET:
            field_dict["exchanges"] = exchanges
        if primary_exchange is not UNSET:
            field_dict["primary_exchange"] = primary_exchange
        if primary_exchange_symbol is not UNSET:
            field_dict["primary_exchange_symbol"] = primary_exchange_symbol
        if otc is not UNSET:
            field_dict["otc"] = otc
        if figi is not UNSET:
            field_dict["figi"] = figi
        if org_permid is not UNSET:
            field_dict["org_permid"] = org_permid
        if isin is not UNSET:
            field_dict["isin"] = isin
        if cusip is not UNSET:
            field_dict["cusip"] = cusip
        if nyse_symbol is not UNSET:
            field_dict["nyse_symbol"] = nyse_symbol
        if tsx_symbol is not UNSET:
            field_dict["tsx_symbol"] = tsx_symbol
        if tsx_listing_type is not UNSET:
            field_dict["tsx_listing_type"] = tsx_listing_type
        if tsx_listing_date is not UNSET:
            field_dict["tsx_listing_date"] = tsx_listing_date
        if index_component is not UNSET:
            field_dict["index_component"] = index_component
        if market_cap_cad is not UNSET:
            field_dict["market_cap_cad"] = market_cap_cad
        if os_shares is not UNSET:
            field_dict["os_shares"] = os_shares

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        cik = d.pop("cik")

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_overview(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overview = _parse_overview(d.pop("overview", UNSET))

        def _parse_naics(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        naics = _parse_naics(d.pop("naics", UNSET))

        def _parse_sic(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sic = _parse_sic(d.pop("sic", UNSET))

        def _parse_key_focus(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_focus = _parse_key_focus(d.pop("key_focus", UNSET))

        def _parse_primary_regions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_regions = _parse_primary_regions(d.pop("primary_regions", UNSET))

        def _parse_exchanges(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exchanges_type_0 = cast(list[str], data)

                return exchanges_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exchanges = _parse_exchanges(d.pop("exchanges", UNSET))

        def _parse_primary_exchange(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_exchange = _parse_primary_exchange(d.pop("primary_exchange", UNSET))

        def _parse_primary_exchange_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_exchange_symbol = _parse_primary_exchange_symbol(d.pop("primary_exchange_symbol", UNSET))

        def _parse_otc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        otc = _parse_otc(d.pop("otc", UNSET))

        def _parse_figi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        figi = _parse_figi(d.pop("figi", UNSET))

        def _parse_org_permid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_permid = _parse_org_permid(d.pop("org_permid", UNSET))

        def _parse_isin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        isin = _parse_isin(d.pop("isin", UNSET))

        def _parse_cusip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cusip = _parse_cusip(d.pop("cusip", UNSET))

        def _parse_nyse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nyse_symbol = _parse_nyse_symbol(d.pop("nyse_symbol", UNSET))

        def _parse_tsx_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tsx_symbol = _parse_tsx_symbol(d.pop("tsx_symbol", UNSET))

        def _parse_tsx_listing_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tsx_listing_type = _parse_tsx_listing_type(d.pop("tsx_listing_type", UNSET))

        def _parse_tsx_listing_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tsx_listing_date_type_0 = isoparse(data).date()

                return tsx_listing_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        tsx_listing_date = _parse_tsx_listing_date(d.pop("tsx_listing_date", UNSET))

        def _parse_index_component(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        index_component = _parse_index_component(d.pop("index_component", UNSET))

        def _parse_market_cap_cad(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        market_cap_cad = _parse_market_cap_cad(d.pop("market_cap_cad", UNSET))

        def _parse_os_shares(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        os_shares = _parse_os_shares(d.pop("os_shares", UNSET))

        company = cls(
            name=name,
            cik=cik,
            url=url,
            overview=overview,
            naics=naics,
            sic=sic,
            key_focus=key_focus,
            primary_regions=primary_regions,
            exchanges=exchanges,
            primary_exchange=primary_exchange,
            primary_exchange_symbol=primary_exchange_symbol,
            otc=otc,
            figi=figi,
            org_permid=org_permid,
            isin=isin,
            cusip=cusip,
            nyse_symbol=nyse_symbol,
            tsx_symbol=tsx_symbol,
            tsx_listing_type=tsx_listing_type,
            tsx_listing_date=tsx_listing_date,
            index_component=index_component,
            market_cap_cad=market_cap_cad,
            os_shares=os_shares,
        )

        company.additional_properties = d
        return company

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
