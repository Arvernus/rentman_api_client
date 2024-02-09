import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuoteItempostResponseSchemaData")


@attr.s(auto_attribs=True)
class QuoteItempostResponseSchemaData:
    """All the data about the requested items"""

    contact: Union[Unset, None, str] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    customer: Union[Unset, None, str] = UNSET
    date: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    expiration_date: Union[Unset, None, str] = UNSET
    filename: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    number: Union[Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    price_invat: Union[Unset, float] = UNSET
    project: Union[Unset, str] = UNSET
    project_crew_price: Union[Unset, float] = UNSET
    project_insurance_price: Union[Unset, float] = UNSET
    project_other_price: Union[Unset, float] = UNSET
    project_rental_price: Union[Unset, float] = UNSET
    project_sale_price: Union[Unset, float] = UNSET
    project_total_price: Union[Unset, float] = UNSET
    project_transport_price: Union[Unset, float] = UNSET
    show_tax: Union[Unset, bool] = UNSET
    subject: Union[Unset, str] = UNSET
    vat_amount: Union[Unset, float] = UNSET
    version: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact = self.contact
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        customer = self.customer
        date = self.date
        displayname = self.displayname
        expiration_date = self.expiration_date
        filename = self.filename
        id = self.id
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        number = self.number
        price = self.price
        price_invat = self.price_invat
        project = self.project
        project_crew_price = self.project_crew_price
        project_insurance_price = self.project_insurance_price
        project_other_price = self.project_other_price
        project_rental_price = self.project_rental_price
        project_sale_price = self.project_sale_price
        project_total_price = self.project_total_price
        project_transport_price = self.project_transport_price
        show_tax = self.show_tax
        subject = self.subject
        vat_amount = self.vat_amount
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact is not UNSET:
            field_dict["contact"] = contact
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if customer is not UNSET:
            field_dict["customer"] = customer
        if date is not UNSET:
            field_dict["date"] = date
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date
        if filename is not UNSET:
            field_dict["filename"] = filename
        if id is not UNSET:
            field_dict["id"] = id
        if modified is not UNSET:
            field_dict["modified"] = modified
        if number is not UNSET:
            field_dict["number"] = number
        if price is not UNSET:
            field_dict["price"] = price
        if price_invat is not UNSET:
            field_dict["price_invat"] = price_invat
        if project is not UNSET:
            field_dict["project"] = project
        if project_crew_price is not UNSET:
            field_dict["project_crew_price"] = project_crew_price
        if project_insurance_price is not UNSET:
            field_dict["project_insurance_price"] = project_insurance_price
        if project_other_price is not UNSET:
            field_dict["project_other_price"] = project_other_price
        if project_rental_price is not UNSET:
            field_dict["project_rental_price"] = project_rental_price
        if project_sale_price is not UNSET:
            field_dict["project_sale_price"] = project_sale_price
        if project_total_price is not UNSET:
            field_dict["project_total_price"] = project_total_price
        if project_transport_price is not UNSET:
            field_dict["project_transport_price"] = project_transport_price
        if show_tax is not UNSET:
            field_dict["show_tax"] = show_tax
        if subject is not UNSET:
            field_dict["subject"] = subject
        if vat_amount is not UNSET:
            field_dict["vat_amount"] = vat_amount
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contact = d.pop("contact", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        customer = d.pop("customer", UNSET)

        date = d.pop("date", UNSET)

        displayname = d.pop("displayname", UNSET)

        expiration_date = d.pop("expiration_date", UNSET)

        filename = d.pop("filename", UNSET)

        id = d.pop("id", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        number = d.pop("number", UNSET)

        price = d.pop("price", UNSET)

        price_invat = d.pop("price_invat", UNSET)

        project = d.pop("project", UNSET)

        project_crew_price = d.pop("project_crew_price", UNSET)

        project_insurance_price = d.pop("project_insurance_price", UNSET)

        project_other_price = d.pop("project_other_price", UNSET)

        project_rental_price = d.pop("project_rental_price", UNSET)

        project_sale_price = d.pop("project_sale_price", UNSET)

        project_total_price = d.pop("project_total_price", UNSET)

        project_transport_price = d.pop("project_transport_price", UNSET)

        show_tax = d.pop("show_tax", UNSET)

        subject = d.pop("subject", UNSET)

        vat_amount = d.pop("vat_amount", UNSET)

        version = d.pop("version", UNSET)

        quote_itempost_response_schema_data = cls(
            contact=contact,
            created=created,
            creator=creator,
            customer=customer,
            date=date,
            displayname=displayname,
            expiration_date=expiration_date,
            filename=filename,
            id=id,
            modified=modified,
            number=number,
            price=price,
            price_invat=price_invat,
            project=project,
            project_crew_price=project_crew_price,
            project_insurance_price=project_insurance_price,
            project_other_price=project_other_price,
            project_rental_price=project_rental_price,
            project_sale_price=project_sale_price,
            project_total_price=project_total_price,
            project_transport_price=project_transport_price,
            show_tax=show_tax,
            subject=subject,
            vat_amount=vat_amount,
            version=version,
        )

        quote_itempost_response_schema_data.additional_properties = d
        return quote_itempost_response_schema_data

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
