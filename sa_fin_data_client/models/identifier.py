from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Identifier")


@_attrs_define
class Identifier:
    """
    Attributes:
        name (str):
        primary_exchange (None | str):
        primary_exchange_symbol (None | str):
        cik (int):
        figi (None | str):
        org_permid (None | str):
        isin (None | str):
        cusip (None | str):
    """

    name: str
    primary_exchange: None | str
    primary_exchange_symbol: None | str
    cik: int
    figi: None | str
    org_permid: None | str
    isin: None | str
    cusip: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        primary_exchange: None | str
        primary_exchange = self.primary_exchange

        primary_exchange_symbol: None | str
        primary_exchange_symbol = self.primary_exchange_symbol

        cik = self.cik

        figi: None | str
        figi = self.figi

        org_permid: None | str
        org_permid = self.org_permid

        isin: None | str
        isin = self.isin

        cusip: None | str
        cusip = self.cusip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "primary_exchange": primary_exchange,
                "primary_exchange_symbol": primary_exchange_symbol,
                "cik": cik,
                "figi": figi,
                "org_permid": org_permid,
                "isin": isin,
                "cusip": cusip,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_primary_exchange(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        primary_exchange = _parse_primary_exchange(d.pop("primary_exchange"))

        def _parse_primary_exchange_symbol(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        primary_exchange_symbol = _parse_primary_exchange_symbol(d.pop("primary_exchange_symbol"))

        cik = d.pop("cik")

        def _parse_figi(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        figi = _parse_figi(d.pop("figi"))

        def _parse_org_permid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        org_permid = _parse_org_permid(d.pop("org_permid"))

        def _parse_isin(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        isin = _parse_isin(d.pop("isin"))

        def _parse_cusip(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cusip = _parse_cusip(d.pop("cusip"))

        identifier = cls(
            name=name,
            primary_exchange=primary_exchange,
            primary_exchange_symbol=primary_exchange_symbol,
            cik=cik,
            figi=figi,
            org_permid=org_permid,
            isin=isin,
            cusip=cusip,
        )

        identifier.additional_properties = d
        return identifier

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
