from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Sub")


@_attrs_define
class Sub:
    """
    Attributes:
        adsh (str):
        form (str):
        filed (datetime.date):
        accepted (str):
        cik (int | None | Unset):
        name (None | str | Unset):
        sic (float | None | Unset):
        countryba (None | str | Unset):
        stprba (None | str | Unset):
        cityba (None | str | Unset):
        zipba (None | str | Unset):
        bas1 (None | str | Unset):
        bas2 (None | str | Unset):
        baph (None | str | Unset):
        countryma (None | str | Unset):
        stprma (None | str | Unset):
        cityma (None | str | Unset):
        zipma (None | str | Unset):
        mas1 (None | str | Unset):
        mas2 (None | str | Unset):
        countryinc (None | str | Unset):
        stprinc (None | str | Unset):
        ein (int | None | Unset):
        former (None | str | Unset):
        changed (datetime.date | None | Unset):
        afs (None | str | Unset):
        wksi (bool | None | Unset):
        fye (int | None | Unset):
        period (datetime.date | None | Unset):
        fy (float | None | Unset):
        fp (None | str | Unset):
        prevrpt (bool | None | Unset):
        detail (bool | None | Unset):
        instance (None | str | Unset):
        nciks (int | None | Unset):
        aciks (None | str | Unset):
        pubfloatusd (float | None | Unset):
        floatdate (datetime.date | None | Unset):
        floataxis (None | str | Unset):
        floatmems (float | None | Unset):
    """

    adsh: str
    form: str
    filed: datetime.date
    accepted: str
    cik: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    sic: float | None | Unset = UNSET
    countryba: None | str | Unset = UNSET
    stprba: None | str | Unset = UNSET
    cityba: None | str | Unset = UNSET
    zipba: None | str | Unset = UNSET
    bas1: None | str | Unset = UNSET
    bas2: None | str | Unset = UNSET
    baph: None | str | Unset = UNSET
    countryma: None | str | Unset = UNSET
    stprma: None | str | Unset = UNSET
    cityma: None | str | Unset = UNSET
    zipma: None | str | Unset = UNSET
    mas1: None | str | Unset = UNSET
    mas2: None | str | Unset = UNSET
    countryinc: None | str | Unset = UNSET
    stprinc: None | str | Unset = UNSET
    ein: int | None | Unset = UNSET
    former: None | str | Unset = UNSET
    changed: datetime.date | None | Unset = UNSET
    afs: None | str | Unset = UNSET
    wksi: bool | None | Unset = UNSET
    fye: int | None | Unset = UNSET
    period: datetime.date | None | Unset = UNSET
    fy: float | None | Unset = UNSET
    fp: None | str | Unset = UNSET
    prevrpt: bool | None | Unset = UNSET
    detail: bool | None | Unset = UNSET
    instance: None | str | Unset = UNSET
    nciks: int | None | Unset = UNSET
    aciks: None | str | Unset = UNSET
    pubfloatusd: float | None | Unset = UNSET
    floatdate: datetime.date | None | Unset = UNSET
    floataxis: None | str | Unset = UNSET
    floatmems: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adsh = self.adsh

        form = self.form

        filed = self.filed.isoformat()

        accepted = self.accepted

        cik: int | None | Unset
        if isinstance(self.cik, Unset):
            cik = UNSET
        else:
            cik = self.cik

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        sic: float | None | Unset
        if isinstance(self.sic, Unset):
            sic = UNSET
        else:
            sic = self.sic

        countryba: None | str | Unset
        if isinstance(self.countryba, Unset):
            countryba = UNSET
        else:
            countryba = self.countryba

        stprba: None | str | Unset
        if isinstance(self.stprba, Unset):
            stprba = UNSET
        else:
            stprba = self.stprba

        cityba: None | str | Unset
        if isinstance(self.cityba, Unset):
            cityba = UNSET
        else:
            cityba = self.cityba

        zipba: None | str | Unset
        if isinstance(self.zipba, Unset):
            zipba = UNSET
        else:
            zipba = self.zipba

        bas1: None | str | Unset
        if isinstance(self.bas1, Unset):
            bas1 = UNSET
        else:
            bas1 = self.bas1

        bas2: None | str | Unset
        if isinstance(self.bas2, Unset):
            bas2 = UNSET
        else:
            bas2 = self.bas2

        baph: None | str | Unset
        if isinstance(self.baph, Unset):
            baph = UNSET
        else:
            baph = self.baph

        countryma: None | str | Unset
        if isinstance(self.countryma, Unset):
            countryma = UNSET
        else:
            countryma = self.countryma

        stprma: None | str | Unset
        if isinstance(self.stprma, Unset):
            stprma = UNSET
        else:
            stprma = self.stprma

        cityma: None | str | Unset
        if isinstance(self.cityma, Unset):
            cityma = UNSET
        else:
            cityma = self.cityma

        zipma: None | str | Unset
        if isinstance(self.zipma, Unset):
            zipma = UNSET
        else:
            zipma = self.zipma

        mas1: None | str | Unset
        if isinstance(self.mas1, Unset):
            mas1 = UNSET
        else:
            mas1 = self.mas1

        mas2: None | str | Unset
        if isinstance(self.mas2, Unset):
            mas2 = UNSET
        else:
            mas2 = self.mas2

        countryinc: None | str | Unset
        if isinstance(self.countryinc, Unset):
            countryinc = UNSET
        else:
            countryinc = self.countryinc

        stprinc: None | str | Unset
        if isinstance(self.stprinc, Unset):
            stprinc = UNSET
        else:
            stprinc = self.stprinc

        ein: int | None | Unset
        if isinstance(self.ein, Unset):
            ein = UNSET
        else:
            ein = self.ein

        former: None | str | Unset
        if isinstance(self.former, Unset):
            former = UNSET
        else:
            former = self.former

        changed: None | str | Unset
        if isinstance(self.changed, Unset):
            changed = UNSET
        elif isinstance(self.changed, datetime.date):
            changed = self.changed.isoformat()
        else:
            changed = self.changed

        afs: None | str | Unset
        if isinstance(self.afs, Unset):
            afs = UNSET
        else:
            afs = self.afs

        wksi: bool | None | Unset
        if isinstance(self.wksi, Unset):
            wksi = UNSET
        else:
            wksi = self.wksi

        fye: int | None | Unset
        if isinstance(self.fye, Unset):
            fye = UNSET
        else:
            fye = self.fye

        period: None | str | Unset
        if isinstance(self.period, Unset):
            period = UNSET
        elif isinstance(self.period, datetime.date):
            period = self.period.isoformat()
        else:
            period = self.period

        fy: float | None | Unset
        if isinstance(self.fy, Unset):
            fy = UNSET
        else:
            fy = self.fy

        fp: None | str | Unset
        if isinstance(self.fp, Unset):
            fp = UNSET
        else:
            fp = self.fp

        prevrpt: bool | None | Unset
        if isinstance(self.prevrpt, Unset):
            prevrpt = UNSET
        else:
            prevrpt = self.prevrpt

        detail: bool | None | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        instance: None | str | Unset
        if isinstance(self.instance, Unset):
            instance = UNSET
        else:
            instance = self.instance

        nciks: int | None | Unset
        if isinstance(self.nciks, Unset):
            nciks = UNSET
        else:
            nciks = self.nciks

        aciks: None | str | Unset
        if isinstance(self.aciks, Unset):
            aciks = UNSET
        else:
            aciks = self.aciks

        pubfloatusd: float | None | Unset
        if isinstance(self.pubfloatusd, Unset):
            pubfloatusd = UNSET
        else:
            pubfloatusd = self.pubfloatusd

        floatdate: None | str | Unset
        if isinstance(self.floatdate, Unset):
            floatdate = UNSET
        elif isinstance(self.floatdate, datetime.date):
            floatdate = self.floatdate.isoformat()
        else:
            floatdate = self.floatdate

        floataxis: None | str | Unset
        if isinstance(self.floataxis, Unset):
            floataxis = UNSET
        else:
            floataxis = self.floataxis

        floatmems: float | None | Unset
        if isinstance(self.floatmems, Unset):
            floatmems = UNSET
        else:
            floatmems = self.floatmems

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "adsh": adsh,
                "form": form,
                "filed": filed,
                "accepted": accepted,
            }
        )
        if cik is not UNSET:
            field_dict["cik"] = cik
        if name is not UNSET:
            field_dict["name"] = name
        if sic is not UNSET:
            field_dict["sic"] = sic
        if countryba is not UNSET:
            field_dict["countryba"] = countryba
        if stprba is not UNSET:
            field_dict["stprba"] = stprba
        if cityba is not UNSET:
            field_dict["cityba"] = cityba
        if zipba is not UNSET:
            field_dict["zipba"] = zipba
        if bas1 is not UNSET:
            field_dict["bas1"] = bas1
        if bas2 is not UNSET:
            field_dict["bas2"] = bas2
        if baph is not UNSET:
            field_dict["baph"] = baph
        if countryma is not UNSET:
            field_dict["countryma"] = countryma
        if stprma is not UNSET:
            field_dict["stprma"] = stprma
        if cityma is not UNSET:
            field_dict["cityma"] = cityma
        if zipma is not UNSET:
            field_dict["zipma"] = zipma
        if mas1 is not UNSET:
            field_dict["mas1"] = mas1
        if mas2 is not UNSET:
            field_dict["mas2"] = mas2
        if countryinc is not UNSET:
            field_dict["countryinc"] = countryinc
        if stprinc is not UNSET:
            field_dict["stprinc"] = stprinc
        if ein is not UNSET:
            field_dict["ein"] = ein
        if former is not UNSET:
            field_dict["former"] = former
        if changed is not UNSET:
            field_dict["changed"] = changed
        if afs is not UNSET:
            field_dict["afs"] = afs
        if wksi is not UNSET:
            field_dict["wksi"] = wksi
        if fye is not UNSET:
            field_dict["fye"] = fye
        if period is not UNSET:
            field_dict["period"] = period
        if fy is not UNSET:
            field_dict["fy"] = fy
        if fp is not UNSET:
            field_dict["fp"] = fp
        if prevrpt is not UNSET:
            field_dict["prevrpt"] = prevrpt
        if detail is not UNSET:
            field_dict["detail"] = detail
        if instance is not UNSET:
            field_dict["instance"] = instance
        if nciks is not UNSET:
            field_dict["nciks"] = nciks
        if aciks is not UNSET:
            field_dict["aciks"] = aciks
        if pubfloatusd is not UNSET:
            field_dict["pubfloatusd"] = pubfloatusd
        if floatdate is not UNSET:
            field_dict["floatdate"] = floatdate
        if floataxis is not UNSET:
            field_dict["floataxis"] = floataxis
        if floatmems is not UNSET:
            field_dict["floatmems"] = floatmems

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        adsh = d.pop("adsh")

        form = d.pop("form")

        filed = isoparse(d.pop("filed")).date()

        accepted = d.pop("accepted")

        def _parse_cik(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cik = _parse_cik(d.pop("cik", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_sic(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sic = _parse_sic(d.pop("sic", UNSET))

        def _parse_countryba(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        countryba = _parse_countryba(d.pop("countryba", UNSET))

        def _parse_stprba(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stprba = _parse_stprba(d.pop("stprba", UNSET))

        def _parse_cityba(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cityba = _parse_cityba(d.pop("cityba", UNSET))

        def _parse_zipba(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zipba = _parse_zipba(d.pop("zipba", UNSET))

        def _parse_bas1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bas1 = _parse_bas1(d.pop("bas1", UNSET))

        def _parse_bas2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bas2 = _parse_bas2(d.pop("bas2", UNSET))

        def _parse_baph(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        baph = _parse_baph(d.pop("baph", UNSET))

        def _parse_countryma(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        countryma = _parse_countryma(d.pop("countryma", UNSET))

        def _parse_stprma(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stprma = _parse_stprma(d.pop("stprma", UNSET))

        def _parse_cityma(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cityma = _parse_cityma(d.pop("cityma", UNSET))

        def _parse_zipma(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zipma = _parse_zipma(d.pop("zipma", UNSET))

        def _parse_mas1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mas1 = _parse_mas1(d.pop("mas1", UNSET))

        def _parse_mas2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mas2 = _parse_mas2(d.pop("mas2", UNSET))

        def _parse_countryinc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        countryinc = _parse_countryinc(d.pop("countryinc", UNSET))

        def _parse_stprinc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stprinc = _parse_stprinc(d.pop("stprinc", UNSET))

        def _parse_ein(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ein = _parse_ein(d.pop("ein", UNSET))

        def _parse_former(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        former = _parse_former(d.pop("former", UNSET))

        def _parse_changed(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changed_type_0 = isoparse(data).date()

                return changed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        changed = _parse_changed(d.pop("changed", UNSET))

        def _parse_afs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        afs = _parse_afs(d.pop("afs", UNSET))

        def _parse_wksi(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        wksi = _parse_wksi(d.pop("wksi", UNSET))

        def _parse_fye(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fye = _parse_fye(d.pop("fye", UNSET))

        def _parse_period(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_type_0 = isoparse(data).date()

                return period_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        period = _parse_period(d.pop("period", UNSET))

        def _parse_fy(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fy = _parse_fy(d.pop("fy", UNSET))

        def _parse_fp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fp = _parse_fp(d.pop("fp", UNSET))

        def _parse_prevrpt(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        prevrpt = _parse_prevrpt(d.pop("prevrpt", UNSET))

        def _parse_detail(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))

        def _parse_instance(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instance = _parse_instance(d.pop("instance", UNSET))

        def _parse_nciks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        nciks = _parse_nciks(d.pop("nciks", UNSET))

        def _parse_aciks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aciks = _parse_aciks(d.pop("aciks", UNSET))

        def _parse_pubfloatusd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pubfloatusd = _parse_pubfloatusd(d.pop("pubfloatusd", UNSET))

        def _parse_floatdate(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                floatdate_type_0 = isoparse(data).date()

                return floatdate_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        floatdate = _parse_floatdate(d.pop("floatdate", UNSET))

        def _parse_floataxis(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        floataxis = _parse_floataxis(d.pop("floataxis", UNSET))

        def _parse_floatmems(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        floatmems = _parse_floatmems(d.pop("floatmems", UNSET))

        sub = cls(
            adsh=adsh,
            form=form,
            filed=filed,
            accepted=accepted,
            cik=cik,
            name=name,
            sic=sic,
            countryba=countryba,
            stprba=stprba,
            cityba=cityba,
            zipba=zipba,
            bas1=bas1,
            bas2=bas2,
            baph=baph,
            countryma=countryma,
            stprma=stprma,
            cityma=cityma,
            zipma=zipma,
            mas1=mas1,
            mas2=mas2,
            countryinc=countryinc,
            stprinc=stprinc,
            ein=ein,
            former=former,
            changed=changed,
            afs=afs,
            wksi=wksi,
            fye=fye,
            period=period,
            fy=fy,
            fp=fp,
            prevrpt=prevrpt,
            detail=detail,
            instance=instance,
            nciks=nciks,
            aciks=aciks,
            pubfloatusd=pubfloatusd,
            floatdate=floatdate,
            floataxis=floataxis,
            floatmems=floatmems,
        )

        sub.additional_properties = d
        return sub

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
