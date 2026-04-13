from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FieldInfo")


@_attrs_define
class FieldInfo:
    """
    Attributes:
        tableid (str):
        fieldid (str):
        description (str):
        source (str):
        format_ (str):
        max_ (int):
        nullid (bool):
        keyid (bool):
        human_readable (str):
    """

    tableid: str
    fieldid: str
    description: str
    source: str
    format_: str
    max_: int
    nullid: bool
    keyid: bool
    human_readable: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tableid = self.tableid

        fieldid = self.fieldid

        description = self.description

        source = self.source

        format_ = self.format_

        max_ = self.max_

        nullid = self.nullid

        keyid = self.keyid

        human_readable = self.human_readable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tableid": tableid,
                "fieldid": fieldid,
                "description": description,
                "source": source,
                "format": format_,
                "max": max_,
                "nullid": nullid,
                "keyid": keyid,
                "human_readable": human_readable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tableid = d.pop("tableid")

        fieldid = d.pop("fieldid")

        description = d.pop("description")

        source = d.pop("source")

        format_ = d.pop("format")

        max_ = d.pop("max")

        nullid = d.pop("nullid")

        keyid = d.pop("keyid")

        human_readable = d.pop("human_readable")

        field_info = cls(
            tableid=tableid,
            fieldid=fieldid,
            description=description,
            source=source,
            format_=format_,
            max_=max_,
            nullid=nullid,
            keyid=keyid,
            human_readable=human_readable,
        )

        field_info.additional_properties = d
        return field_info

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
