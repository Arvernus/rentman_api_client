import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.rate_itemget_response_schema_data_subtype import RateItemgetResponseSchemaDataSubtype
from ..models.rate_itemget_response_schema_data_type import RateItemgetResponseSchemaDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RateItemgetResponseSchemaData")


@attr.s(auto_attribs=True)
class RateItemgetResponseSchemaData:
    """All the data about the requested items"""

    archived: Union[Unset, bool] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    subtype: Union[Unset, RateItemgetResponseSchemaDataSubtype] = UNSET
    type: Union[Unset, RateItemgetResponseSchemaDataType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        archived = self.archived
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        displayname = self.displayname
        id = self.id
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        name = self.name
        subtype: Union[Unset, str] = UNSET
        if not isinstance(self.subtype, Unset):
            subtype = self.subtype.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived is not UNSET:
            field_dict["archived"] = archived
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if id is not UNSET:
            field_dict["id"] = id
        if modified is not UNSET:
            field_dict["modified"] = modified
        if name is not UNSET:
            field_dict["name"] = name
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        archived = d.pop("archived", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        displayname = d.pop("displayname", UNSET)

        id = d.pop("id", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        name = d.pop("name", UNSET)

        subtype: Union[Unset, RateItemgetResponseSchemaDataSubtype] = UNSET
        _subtype = d.pop("subtype", UNSET)
        if not isinstance(_subtype, Unset):
            subtype = RateItemgetResponseSchemaDataSubtype(_subtype)

        type: Union[Unset, RateItemgetResponseSchemaDataType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = RateItemgetResponseSchemaDataType(_type)

        rate_itemget_response_schema_data = cls(
            archived=archived,
            created=created,
            creator=creator,
            displayname=displayname,
            id=id,
            modified=modified,
            name=name,
            subtype=subtype,
            type=type,
        )

        rate_itemget_response_schema_data.additional_properties = d
        return rate_itemget_response_schema_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
