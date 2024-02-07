from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.setinhoud_collectionget_response_schema_data_item import SetinhoudCollectiongetResponseSchemaDataItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="SetinhoudCollectiongetResponseSchema")


@attr.s(auto_attribs=True)
class SetinhoudCollectiongetResponseSchema:
    """ """

    data: Union[Unset, List[SetinhoudCollectiongetResponseSchemaDataItem]] = UNSET
    item_count: Union[Unset, float] = UNSET
    limit: Union[Unset, float] = UNSET
    offset: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

        item_count = self.item_count
        limit = self.limit
        offset = self.offset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if item_count is not UNSET:
            field_dict["itemCount"] = item_count
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = SetinhoudCollectiongetResponseSchemaDataItem.from_dict(data_item_data)

            data.append(data_item)

        item_count = d.pop("itemCount", UNSET)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        setinhoud_collectionget_response_schema = cls(
            data=data,
            item_count=item_count,
            limit=limit,
            offset=offset,
        )

        setinhoud_collectionget_response_schema.additional_properties = d
        return setinhoud_collectionget_response_schema

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
