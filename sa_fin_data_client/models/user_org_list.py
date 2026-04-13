from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_org_list_organizations_item import UserOrgListOrganizationsItem


T = TypeVar("T", bound="UserOrgList")


@_attrs_define
class UserOrgList:
    """
    Attributes:
        list_name (str):
        user_id (int):
        id (int | None | Unset):
        organizations (list[UserOrgListOrganizationsItem] | Unset):
        description (None | str | Unset):
        is_public (bool | Unset):  Default: False.
        is_active (bool | Unset):  Default: True.
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
        group_id (int | None | Unset):
    """

    list_name: str
    user_id: int
    id: int | None | Unset = UNSET
    organizations: list[UserOrgListOrganizationsItem] | Unset = UNSET
    description: None | str | Unset = UNSET
    is_public: bool | Unset = False
    is_active: bool | Unset = True
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    group_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_name = self.list_name

        user_id = self.user_id

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        organizations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()
                organizations.append(organizations_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_public = self.is_public

        is_active = self.is_active

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        group_id: int | None | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        else:
            group_id = self.group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "list_name": list_name,
                "user_id": user_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if description is not UNSET:
            field_dict["description"] = description
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if group_id is not UNSET:
            field_dict["group_id"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_org_list_organizations_item import UserOrgListOrganizationsItem

        d = dict(src_dict)
        list_name = d.pop("list_name")

        user_id = d.pop("user_id")

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        _organizations = d.pop("organizations", UNSET)
        organizations: list[UserOrgListOrganizationsItem] | Unset = UNSET
        if _organizations is not UNSET:
            organizations = []
            for organizations_item_data in _organizations:
                organizations_item = UserOrgListOrganizationsItem.from_dict(organizations_item_data)

                organizations.append(organizations_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        is_public = d.pop("is_public", UNSET)

        is_active = d.pop("is_active", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        def _parse_group_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        group_id = _parse_group_id(d.pop("group_id", UNSET))

        user_org_list = cls(
            list_name=list_name,
            user_id=user_id,
            id=id,
            organizations=organizations,
            description=description,
            is_public=is_public,
            is_active=is_active,
            created_at=created_at,
            updated_at=updated_at,
            group_id=group_id,
        )

        user_org_list.additional_properties = d
        return user_org_list

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
