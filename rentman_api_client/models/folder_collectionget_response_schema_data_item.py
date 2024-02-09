import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.folder_collectionget_response_schema_data_item_itemtype import (
    FolderCollectiongetResponseSchemaDataItemItemtype,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FolderCollectiongetResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class FolderCollectiongetResponseSchemaDataItem:
    """ """

    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    itemtype: Union[Unset, FolderCollectiongetResponseSchemaDataItemItemtype] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    parent: Union[Unset, None, str] = UNSET
    path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        displayname = self.displayname
        id = self.id
        itemtype: Union[Unset, str] = UNSET
        if not isinstance(self.itemtype, Unset):
            itemtype = self.itemtype.value

        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        name = self.name
        order = self.order
        parent = self.parent
        path = self.path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if id is not UNSET:
            field_dict["id"] = id
        if itemtype is not UNSET:
            field_dict["itemtype"] = itemtype
        if modified is not UNSET:
            field_dict["modified"] = modified
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if parent is not UNSET:
            field_dict["parent"] = parent
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        displayname = d.pop("displayname", UNSET)

        id = d.pop("id", UNSET)

        itemtype: Union[Unset, FolderCollectiongetResponseSchemaDataItemItemtype] = UNSET
        _itemtype = d.pop("itemtype", UNSET)
        if not isinstance(_itemtype, Unset):
            itemtype = FolderCollectiongetResponseSchemaDataItemItemtype(_itemtype)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        parent = d.pop("parent", UNSET)

        path = d.pop("path", UNSET)

        folder_collectionget_response_schema_data_item = cls(
            created=created,
            creator=creator,
            displayname=displayname,
            id=id,
            itemtype=itemtype,
            modified=modified,
            name=name,
            order=order,
            parent=parent,
            path=path,
        )

        folder_collectionget_response_schema_data_item.additional_properties = d
        return folder_collectionget_response_schema_data_item

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
