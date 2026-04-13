from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FSStandardized")


@_attrs_define
class FSStandardized:
    """
    Attributes:
        cik (int):
        stmt (str):
        item (str):
        ddate (datetime.date):
        value (float):
        uom (str):
        tags (str):
        version (str):
        form (str):
        fy (int):
        fp (str):
        filed (datetime.date):
        qtrs (int):
        adsh (str):
        stmtsrc (str):
        valid (bool | Unset):  Default: True.
        missed_no (int | Unset):  Default: 0.
        footnote (None | str | Unset):
    """

    cik: int
    stmt: str
    item: str
    ddate: datetime.date
    value: float
    uom: str
    tags: str
    version: str
    form: str
    fy: int
    fp: str
    filed: datetime.date
    qtrs: int
    adsh: str
    stmtsrc: str
    valid: bool | Unset = True
    missed_no: int | Unset = 0
    footnote: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cik = self.cik

        stmt = self.stmt

        item = self.item

        ddate = self.ddate.isoformat()

        value = self.value

        uom = self.uom

        tags = self.tags

        version = self.version

        form = self.form

        fy = self.fy

        fp = self.fp

        filed = self.filed.isoformat()

        qtrs = self.qtrs

        adsh = self.adsh

        stmtsrc = self.stmtsrc

        valid = self.valid

        missed_no = self.missed_no

        footnote: None | str | Unset
        if isinstance(self.footnote, Unset):
            footnote = UNSET
        else:
            footnote = self.footnote

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cik": cik,
                "stmt": stmt,
                "item": item,
                "ddate": ddate,
                "value": value,
                "uom": uom,
                "tags": tags,
                "version": version,
                "form": form,
                "fy": fy,
                "fp": fp,
                "filed": filed,
                "qtrs": qtrs,
                "adsh": adsh,
                "stmtsrc": stmtsrc,
            }
        )
        if valid is not UNSET:
            field_dict["valid"] = valid
        if missed_no is not UNSET:
            field_dict["missed_no"] = missed_no
        if footnote is not UNSET:
            field_dict["footnote"] = footnote

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cik = d.pop("cik")

        stmt = d.pop("stmt")

        item = d.pop("item")

        ddate = isoparse(d.pop("ddate")).date()

        value = d.pop("value")

        uom = d.pop("uom")

        tags = d.pop("tags")

        version = d.pop("version")

        form = d.pop("form")

        fy = d.pop("fy")

        fp = d.pop("fp")

        filed = isoparse(d.pop("filed")).date()

        qtrs = d.pop("qtrs")

        adsh = d.pop("adsh")

        stmtsrc = d.pop("stmtsrc")

        valid = d.pop("valid", UNSET)

        missed_no = d.pop("missed_no", UNSET)

        def _parse_footnote(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        footnote = _parse_footnote(d.pop("footnote", UNSET))

        fs_standardized = cls(
            cik=cik,
            stmt=stmt,
            item=item,
            ddate=ddate,
            value=value,
            uom=uom,
            tags=tags,
            version=version,
            form=form,
            fy=fy,
            fp=fp,
            filed=filed,
            qtrs=qtrs,
            adsh=adsh,
            stmtsrc=stmtsrc,
            valid=valid,
            missed_no=missed_no,
            footnote=footnote,
        )

        fs_standardized.additional_properties = d
        return fs_standardized

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
