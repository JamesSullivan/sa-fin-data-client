from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StatementRow")


@_attrs_define
class StatementRow:
    """
    Attributes:
        report (int):
        line (int):
        tag (str):
        plabel (str):
        ddate (None | str):
        value (None | str):
        footnote (None | str):
    """

    report: int
    line: int
    tag: str
    plabel: str
    ddate: None | str
    value: None | str
    footnote: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        report = self.report

        line = self.line

        tag = self.tag

        plabel = self.plabel

        ddate: None | str
        ddate = self.ddate

        value: None | str
        value = self.value

        footnote: None | str
        footnote = self.footnote

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "report": report,
                "line": line,
                "tag": tag,
                "plabel": plabel,
                "ddate": ddate,
                "value": value,
                "footnote": footnote,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        report = d.pop("report")

        line = d.pop("line")

        tag = d.pop("tag")

        plabel = d.pop("plabel")

        def _parse_ddate(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ddate = _parse_ddate(d.pop("ddate"))

        def _parse_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value = _parse_value(d.pop("value"))

        def _parse_footnote(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        footnote = _parse_footnote(d.pop("footnote"))

        statement_row = cls(
            report=report,
            line=line,
            tag=tag,
            plabel=plabel,
            ddate=ddate,
            value=value,
            footnote=footnote,
        )

        statement_row.additional_properties = d
        return statement_row

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
