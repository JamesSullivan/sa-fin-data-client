from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="CurrencyRate")


@_attrs_define
class CurrencyRate:
    """
    Attributes:
        date (datetime.date):
        rate (float | None):
    """

    date: datetime.date
    rate: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        rate: float | None
        rate = self.rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "rate": rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = isoparse(d.pop("date")).date()

        def _parse_rate(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        rate = _parse_rate(d.pop("rate"))

        currency_rate = cls(
            date=date,
            rate=rate,
        )

        currency_rate.additional_properties = d
        return currency_rate

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
