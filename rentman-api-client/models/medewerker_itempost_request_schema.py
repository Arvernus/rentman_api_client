from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.medewerker_itempost_request_schema_country import MedewerkerItempostRequestSchemaCountry
from ..models.medewerker_itempost_request_schema_custom import MedewerkerItempostRequestSchemaCustom
from ..types import UNSET, Unset

T = TypeVar("T", bound="MedewerkerItempostRequestSchema")


@attr.s(auto_attribs=True)
class MedewerkerItempostRequestSchema:
    """ """

    folder: Union[Unset, None, str] = UNSET
    street: Union[Unset, str] = UNSET
    housenumber: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    addressline_2: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    country: Union[Unset, MedewerkerItempostRequestSchemaCountry] = UNSET
    birthdate: Union[Unset, None, str] = UNSET
    passport_number: Union[Unset, str] = UNSET
    emergency_contact: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    driving_license: Union[Unset, str] = UNSET
    contract: Union[Unset, str] = UNSET
    bank: Union[Unset, str] = UNSET
    contract_date: Union[Unset, None, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    vat_code: Union[Unset, str] = UNSET
    coc_code: Union[Unset, str] = UNSET
    firstname: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    lastname: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    avatar: Union[Unset, None, str] = UNSET
    vt_fullname: Union[Unset, str] = UNSET
    custom: Union[Unset, MedewerkerItempostRequestSchemaCustom] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        folder = self.folder
        street = self.street
        housenumber = self.housenumber
        city = self.city
        postal_code = self.postal_code
        addressline_2 = self.addressline_2
        state = self.state
        country: Union[Unset, str] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.value

        birthdate = self.birthdate
        passport_number = self.passport_number
        emergency_contact = self.emergency_contact
        remark = self.remark
        driving_license = self.driving_license
        contract = self.contract
        bank = self.bank
        contract_date = self.contract_date
        company_name = self.company_name
        vat_code = self.vat_code
        coc_code = self.coc_code
        firstname = self.firstname
        middle_name = self.middle_name
        lastname = self.lastname
        email = self.email
        phone = self.phone
        active = self.active
        avatar = self.avatar
        vt_fullname = self.vt_fullname
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if folder is not UNSET:
            field_dict["folder"] = folder
        if street is not UNSET:
            field_dict["street"] = street
        if housenumber is not UNSET:
            field_dict["housenumber"] = housenumber
        if city is not UNSET:
            field_dict["city"] = city
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if addressline_2 is not UNSET:
            field_dict["addressline2"] = addressline_2
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country
        if birthdate is not UNSET:
            field_dict["birthdate"] = birthdate
        if passport_number is not UNSET:
            field_dict["passport_number"] = passport_number
        if emergency_contact is not UNSET:
            field_dict["emergency_contact"] = emergency_contact
        if remark is not UNSET:
            field_dict["remark"] = remark
        if driving_license is not UNSET:
            field_dict["driving_license"] = driving_license
        if contract is not UNSET:
            field_dict["contract"] = contract
        if bank is not UNSET:
            field_dict["bank"] = bank
        if contract_date is not UNSET:
            field_dict["contract_date"] = contract_date
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if vat_code is not UNSET:
            field_dict["vat_code"] = vat_code
        if coc_code is not UNSET:
            field_dict["coc_code"] = coc_code
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if active is not UNSET:
            field_dict["active"] = active
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if vt_fullname is not UNSET:
            field_dict["vt_fullname"] = vt_fullname
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        folder = d.pop("folder", UNSET)

        street = d.pop("street", UNSET)

        housenumber = d.pop("housenumber", UNSET)

        city = d.pop("city", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        addressline_2 = d.pop("addressline2", UNSET)

        state = d.pop("state", UNSET)

        country: Union[Unset, MedewerkerItempostRequestSchemaCountry] = UNSET
        _country = d.pop("country", UNSET)
        if not isinstance(_country, Unset):
            country = MedewerkerItempostRequestSchemaCountry(_country)

        birthdate = d.pop("birthdate", UNSET)

        passport_number = d.pop("passport_number", UNSET)

        emergency_contact = d.pop("emergency_contact", UNSET)

        remark = d.pop("remark", UNSET)

        driving_license = d.pop("driving_license", UNSET)

        contract = d.pop("contract", UNSET)

        bank = d.pop("bank", UNSET)

        contract_date = d.pop("contract_date", UNSET)

        company_name = d.pop("company_name", UNSET)

        vat_code = d.pop("vat_code", UNSET)

        coc_code = d.pop("coc_code", UNSET)

        firstname = d.pop("firstname", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        lastname = d.pop("lastname", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        active = d.pop("active", UNSET)

        avatar = d.pop("avatar", UNSET)

        vt_fullname = d.pop("vt_fullname", UNSET)

        custom: Union[Unset, MedewerkerItempostRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = MedewerkerItempostRequestSchemaCustom.from_dict(_custom)

        medewerker_itempost_request_schema = cls(
            folder=folder,
            street=street,
            housenumber=housenumber,
            city=city,
            postal_code=postal_code,
            addressline_2=addressline_2,
            state=state,
            country=country,
            birthdate=birthdate,
            passport_number=passport_number,
            emergency_contact=emergency_contact,
            remark=remark,
            driving_license=driving_license,
            contract=contract,
            bank=bank,
            contract_date=contract_date,
            company_name=company_name,
            vat_code=vat_code,
            coc_code=coc_code,
            firstname=firstname,
            middle_name=middle_name,
            lastname=lastname,
            email=email,
            phone=phone,
            active=active,
            avatar=avatar,
            vt_fullname=vt_fullname,
            custom=custom,
        )

        medewerker_itempost_request_schema.additional_properties = d
        return medewerker_itempost_request_schema

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
