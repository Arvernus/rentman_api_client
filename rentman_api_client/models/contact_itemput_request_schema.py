from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.contact_itemput_request_schema_country import ContactItemputRequestSchemaCountry
from ..models.contact_itemput_request_schema_custom import ContactItemputRequestSchemaCustom
from ..models.contact_itemput_request_schema_invoice_country import ContactItemputRequestSchemaInvoiceCountry
from ..models.contact_itemput_request_schema_mailing_country import ContactItemputRequestSchemaMailingCountry
from ..models.contact_itemput_request_schema_type import ContactItemputRequestSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactItemputRequestSchema")


@attr.s(auto_attribs=True)
class ContactItemputRequestSchema:
    """ """

    accounting_code: Union[Unset, str] = UNSET
    admin_contactperson: Union[Unset, None, str] = UNSET
    bank_account: Union[Unset, str] = UNSET
    bic: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    commerce_code: Union[Unset, str] = UNSET
    contact_warning: Union[Unset, str] = UNSET
    country: Union[Unset, ContactItemputRequestSchemaCountry] = UNSET
    custom: Union[Unset, ContactItemputRequestSchemaCustom] = UNSET
    default_person: Union[Unset, None, str] = UNSET
    discount_crew: Union[Unset, float] = UNSET
    discount_rental: Union[Unset, float] = UNSET
    discount_sale: Union[Unset, float] = UNSET
    discount_subrent: Union[Unset, float] = UNSET
    discount_total: Union[Unset, float] = UNSET
    discount_transport: Union[Unset, float] = UNSET
    distance: Union[Unset, float] = UNSET
    email_1: Union[Unset, str] = UNSET
    email_2: Union[Unset, str] = UNSET
    ext_name_line: Union[Unset, str] = UNSET
    firstname: Union[Unset, str] = UNSET
    fiscal_code: Union[Unset, str] = UNSET
    folder: Union[Unset, None, str] = UNSET
    gender: Union[Unset, str] = UNSET
    invoice_city: Union[Unset, str] = UNSET
    invoice_country: Union[Unset, ContactItemputRequestSchemaInvoiceCountry] = UNSET
    invoice_number: Union[Unset, str] = UNSET
    invoice_postalcode: Union[Unset, str] = UNSET
    invoice_state: Union[Unset, str] = UNSET
    invoice_street: Union[Unset, str] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    mailing_city: Union[Unset, str] = UNSET
    mailing_country: Union[Unset, ContactItemputRequestSchemaMailingCountry] = UNSET
    mailing_number: Union[Unset, str] = UNSET
    mailing_postalcode: Union[Unset, str] = UNSET
    mailing_state: Union[Unset, str] = UNSET
    mailing_street: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    phone_1: Union[Unset, str] = UNSET
    phone_2: Union[Unset, str] = UNSET
    projectnote: Union[Unset, str] = UNSET
    projectnote_title: Union[Unset, str] = UNSET
    purchase_number: Union[Unset, str] = UNSET
    surfix: Union[Unset, str] = UNSET
    surname: Union[Unset, str] = UNSET
    travel_time: Union[Unset, None, float] = UNSET
    type: Union[Unset, ContactItemputRequestSchemaType] = UNSET
    vat_code: Union[Unset, str] = UNSET
    visit_city: Union[Unset, str] = UNSET
    visit_number: Union[Unset, str] = UNSET
    visit_postalcode: Union[Unset, str] = UNSET
    visit_state: Union[Unset, str] = UNSET
    visit_street: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accounting_code = self.accounting_code
        admin_contactperson = self.admin_contactperson
        bank_account = self.bank_account
        bic = self.bic
        code = self.code
        commerce_code = self.commerce_code
        contact_warning = self.contact_warning
        country: Union[Unset, str] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.value

        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        default_person = self.default_person
        discount_crew = self.discount_crew
        discount_rental = self.discount_rental
        discount_sale = self.discount_sale
        discount_subrent = self.discount_subrent
        discount_total = self.discount_total
        discount_transport = self.discount_transport
        distance = self.distance
        email_1 = self.email_1
        email_2 = self.email_2
        ext_name_line = self.ext_name_line
        firstname = self.firstname
        fiscal_code = self.fiscal_code
        folder = self.folder
        gender = self.gender
        invoice_city = self.invoice_city
        invoice_country: Union[Unset, str] = UNSET
        if not isinstance(self.invoice_country, Unset):
            invoice_country = self.invoice_country.value

        invoice_number = self.invoice_number
        invoice_postalcode = self.invoice_postalcode
        invoice_state = self.invoice_state
        invoice_street = self.invoice_street
        latitude = self.latitude
        longitude = self.longitude
        mailing_city = self.mailing_city
        mailing_country: Union[Unset, str] = UNSET
        if not isinstance(self.mailing_country, Unset):
            mailing_country = self.mailing_country.value

        mailing_number = self.mailing_number
        mailing_postalcode = self.mailing_postalcode
        mailing_state = self.mailing_state
        mailing_street = self.mailing_street
        name = self.name
        phone_1 = self.phone_1
        phone_2 = self.phone_2
        projectnote = self.projectnote
        projectnote_title = self.projectnote_title
        purchase_number = self.purchase_number
        surfix = self.surfix
        surname = self.surname
        travel_time = self.travel_time
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        vat_code = self.vat_code
        visit_city = self.visit_city
        visit_number = self.visit_number
        visit_postalcode = self.visit_postalcode
        visit_state = self.visit_state
        visit_street = self.visit_street
        website = self.website

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accounting_code is not UNSET:
            field_dict["accounting_code"] = accounting_code
        if admin_contactperson is not UNSET:
            field_dict["admin_contactperson"] = admin_contactperson
        if bank_account is not UNSET:
            field_dict["bank_account"] = bank_account
        if bic is not UNSET:
            field_dict["bic"] = bic
        if code is not UNSET:
            field_dict["code"] = code
        if commerce_code is not UNSET:
            field_dict["commerce_code"] = commerce_code
        if contact_warning is not UNSET:
            field_dict["contact_warning"] = contact_warning
        if country is not UNSET:
            field_dict["country"] = country
        if custom is not UNSET:
            field_dict["custom"] = custom
        if default_person is not UNSET:
            field_dict["default_person"] = default_person
        if discount_crew is not UNSET:
            field_dict["discount_crew"] = discount_crew
        if discount_rental is not UNSET:
            field_dict["discount_rental"] = discount_rental
        if discount_sale is not UNSET:
            field_dict["discount_sale"] = discount_sale
        if discount_subrent is not UNSET:
            field_dict["discount_subrent"] = discount_subrent
        if discount_total is not UNSET:
            field_dict["discount_total"] = discount_total
        if discount_transport is not UNSET:
            field_dict["discount_transport"] = discount_transport
        if distance is not UNSET:
            field_dict["distance"] = distance
        if email_1 is not UNSET:
            field_dict["email_1"] = email_1
        if email_2 is not UNSET:
            field_dict["email_2"] = email_2
        if ext_name_line is not UNSET:
            field_dict["ext_name_line"] = ext_name_line
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if fiscal_code is not UNSET:
            field_dict["fiscal_code"] = fiscal_code
        if folder is not UNSET:
            field_dict["folder"] = folder
        if gender is not UNSET:
            field_dict["gender"] = gender
        if invoice_city is not UNSET:
            field_dict["invoice_city"] = invoice_city
        if invoice_country is not UNSET:
            field_dict["invoice_country"] = invoice_country
        if invoice_number is not UNSET:
            field_dict["invoice_number"] = invoice_number
        if invoice_postalcode is not UNSET:
            field_dict["invoice_postalcode"] = invoice_postalcode
        if invoice_state is not UNSET:
            field_dict["invoice_state"] = invoice_state
        if invoice_street is not UNSET:
            field_dict["invoice_street"] = invoice_street
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if mailing_city is not UNSET:
            field_dict["mailing_city"] = mailing_city
        if mailing_country is not UNSET:
            field_dict["mailing_country"] = mailing_country
        if mailing_number is not UNSET:
            field_dict["mailing_number"] = mailing_number
        if mailing_postalcode is not UNSET:
            field_dict["mailing_postalcode"] = mailing_postalcode
        if mailing_state is not UNSET:
            field_dict["mailing_state"] = mailing_state
        if mailing_street is not UNSET:
            field_dict["mailing_street"] = mailing_street
        if name is not UNSET:
            field_dict["name"] = name
        if phone_1 is not UNSET:
            field_dict["phone_1"] = phone_1
        if phone_2 is not UNSET:
            field_dict["phone_2"] = phone_2
        if projectnote is not UNSET:
            field_dict["projectnote"] = projectnote
        if projectnote_title is not UNSET:
            field_dict["projectnote_title"] = projectnote_title
        if purchase_number is not UNSET:
            field_dict["purchase_number"] = purchase_number
        if surfix is not UNSET:
            field_dict["surfix"] = surfix
        if surname is not UNSET:
            field_dict["surname"] = surname
        if travel_time is not UNSET:
            field_dict["travel_time"] = travel_time
        if type is not UNSET:
            field_dict["type"] = type
        if vat_code is not UNSET:
            field_dict["VAT_code"] = vat_code
        if visit_city is not UNSET:
            field_dict["visit_city"] = visit_city
        if visit_number is not UNSET:
            field_dict["visit_number"] = visit_number
        if visit_postalcode is not UNSET:
            field_dict["visit_postalcode"] = visit_postalcode
        if visit_state is not UNSET:
            field_dict["visit_state"] = visit_state
        if visit_street is not UNSET:
            field_dict["visit_street"] = visit_street
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        accounting_code = d.pop("accounting_code", UNSET)

        admin_contactperson = d.pop("admin_contactperson", UNSET)

        bank_account = d.pop("bank_account", UNSET)

        bic = d.pop("bic", UNSET)

        code = d.pop("code", UNSET)

        commerce_code = d.pop("commerce_code", UNSET)

        contact_warning = d.pop("contact_warning", UNSET)

        country: Union[Unset, ContactItemputRequestSchemaCountry] = UNSET
        _country = d.pop("country", UNSET)
        if not isinstance(_country, Unset):
            country = ContactItemputRequestSchemaCountry(_country)

        custom: Union[Unset, ContactItemputRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ContactItemputRequestSchemaCustom.from_dict(_custom)

        default_person = d.pop("default_person", UNSET)

        discount_crew = d.pop("discount_crew", UNSET)

        discount_rental = d.pop("discount_rental", UNSET)

        discount_sale = d.pop("discount_sale", UNSET)

        discount_subrent = d.pop("discount_subrent", UNSET)

        discount_total = d.pop("discount_total", UNSET)

        discount_transport = d.pop("discount_transport", UNSET)

        distance = d.pop("distance", UNSET)

        email_1 = d.pop("email_1", UNSET)

        email_2 = d.pop("email_2", UNSET)

        ext_name_line = d.pop("ext_name_line", UNSET)

        firstname = d.pop("firstname", UNSET)

        fiscal_code = d.pop("fiscal_code", UNSET)

        folder = d.pop("folder", UNSET)

        gender = d.pop("gender", UNSET)

        invoice_city = d.pop("invoice_city", UNSET)

        invoice_country: Union[Unset, ContactItemputRequestSchemaInvoiceCountry] = UNSET
        _invoice_country = d.pop("invoice_country", UNSET)
        if not isinstance(_invoice_country, Unset):
            invoice_country = ContactItemputRequestSchemaInvoiceCountry(_invoice_country)

        invoice_number = d.pop("invoice_number", UNSET)

        invoice_postalcode = d.pop("invoice_postalcode", UNSET)

        invoice_state = d.pop("invoice_state", UNSET)

        invoice_street = d.pop("invoice_street", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        mailing_city = d.pop("mailing_city", UNSET)

        mailing_country: Union[Unset, ContactItemputRequestSchemaMailingCountry] = UNSET
        _mailing_country = d.pop("mailing_country", UNSET)
        if not isinstance(_mailing_country, Unset):
            mailing_country = ContactItemputRequestSchemaMailingCountry(_mailing_country)

        mailing_number = d.pop("mailing_number", UNSET)

        mailing_postalcode = d.pop("mailing_postalcode", UNSET)

        mailing_state = d.pop("mailing_state", UNSET)

        mailing_street = d.pop("mailing_street", UNSET)

        name = d.pop("name", UNSET)

        phone_1 = d.pop("phone_1", UNSET)

        phone_2 = d.pop("phone_2", UNSET)

        projectnote = d.pop("projectnote", UNSET)

        projectnote_title = d.pop("projectnote_title", UNSET)

        purchase_number = d.pop("purchase_number", UNSET)

        surfix = d.pop("surfix", UNSET)

        surname = d.pop("surname", UNSET)

        travel_time = d.pop("travel_time", UNSET)

        type: Union[Unset, ContactItemputRequestSchemaType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = ContactItemputRequestSchemaType(_type)

        vat_code = d.pop("VAT_code", UNSET)

        visit_city = d.pop("visit_city", UNSET)

        visit_number = d.pop("visit_number", UNSET)

        visit_postalcode = d.pop("visit_postalcode", UNSET)

        visit_state = d.pop("visit_state", UNSET)

        visit_street = d.pop("visit_street", UNSET)

        website = d.pop("website", UNSET)

        contact_itemput_request_schema = cls(
            accounting_code=accounting_code,
            admin_contactperson=admin_contactperson,
            bank_account=bank_account,
            bic=bic,
            code=code,
            commerce_code=commerce_code,
            contact_warning=contact_warning,
            country=country,
            custom=custom,
            default_person=default_person,
            discount_crew=discount_crew,
            discount_rental=discount_rental,
            discount_sale=discount_sale,
            discount_subrent=discount_subrent,
            discount_total=discount_total,
            discount_transport=discount_transport,
            distance=distance,
            email_1=email_1,
            email_2=email_2,
            ext_name_line=ext_name_line,
            firstname=firstname,
            fiscal_code=fiscal_code,
            folder=folder,
            gender=gender,
            invoice_city=invoice_city,
            invoice_country=invoice_country,
            invoice_number=invoice_number,
            invoice_postalcode=invoice_postalcode,
            invoice_state=invoice_state,
            invoice_street=invoice_street,
            latitude=latitude,
            longitude=longitude,
            mailing_city=mailing_city,
            mailing_country=mailing_country,
            mailing_number=mailing_number,
            mailing_postalcode=mailing_postalcode,
            mailing_state=mailing_state,
            mailing_street=mailing_street,
            name=name,
            phone_1=phone_1,
            phone_2=phone_2,
            projectnote=projectnote,
            projectnote_title=projectnote_title,
            purchase_number=purchase_number,
            surfix=surfix,
            surname=surname,
            travel_time=travel_time,
            type=type,
            vat_code=vat_code,
            visit_city=visit_city,
            visit_number=visit_number,
            visit_postalcode=visit_postalcode,
            visit_state=visit_state,
            visit_street=visit_street,
            website=website,
        )

        contact_itemput_request_schema.additional_properties = d
        return contact_itemput_request_schema

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
