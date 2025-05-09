# coding: utf-8

"""
    Taikun - WebApi

    This Api will be responsible for overall data distribution and authorization.

    The version of the OpenAPI document: v1
    Contact: noreply@taikun.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CreateOpenstackCloudCommand(BaseModel):
    """
    CreateOpenstackCloudCommand
    """ # noqa: E501
    name: Optional[StrictStr] = None
    open_stack_user: Optional[StrictStr] = Field(default=None, alias="openStackUser")
    open_stack_password: Optional[StrictStr] = Field(default=None, alias="openStackPassword")
    open_stack_url: Optional[StrictStr] = Field(default=None, alias="openStackUrl")
    open_stack_project: Optional[StrictStr] = Field(default=None, alias="openStackProject")
    open_stack_public_network: Optional[StrictStr] = Field(default=None, alias="openStackPublicNetwork")
    open_stack_availability_zone: Optional[StrictStr] = Field(default=None, alias="openStackAvailabilityZone")
    open_stack_domain: Optional[StrictStr] = Field(default=None, alias="openStackDomain")
    open_stack_region: Optional[StrictStr] = Field(default=None, alias="openStackRegion")
    open_stack_continent: Optional[StrictStr] = Field(default=None, alias="openStackContinent")
    open_stack_volume_type: Optional[StrictStr] = Field(default=None, alias="openStackVolumeType")
    open_stack_import_network: Optional[StrictBool] = Field(default=None, alias="openStackImportNetwork")
    open_stack_internal_subnet_id: Optional[StrictStr] = Field(default=None, alias="openStackInternalSubnetId")
    organization_id: Optional[StrictInt] = Field(default=None, alias="organizationId")
    application_cred_enabled: Optional[StrictBool] = Field(default=None, alias="applicationCredEnabled")
    is_admin: Optional[StrictBool] = Field(default=None, alias="isAdmin")
    skip_tls_flag: Optional[StrictBool] = Field(default=None, alias="skipTlsFlag")
    __properties: ClassVar[List[str]] = ["name", "openStackUser", "openStackPassword", "openStackUrl", "openStackProject", "openStackPublicNetwork", "openStackAvailabilityZone", "openStackDomain", "openStackRegion", "openStackContinent", "openStackVolumeType", "openStackImportNetwork", "openStackInternalSubnetId", "organizationId", "applicationCredEnabled", "isAdmin", "skipTlsFlag"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateOpenstackCloudCommand from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if open_stack_user (nullable) is None
        # and model_fields_set contains the field
        if self.open_stack_user is None and "open_stack_user" in self.model_fields_set:
            _dict['openStackUser'] = None

        # set to None if open_stack_password (nullable) is None
        # and model_fields_set contains the field
        if self.open_stack_password is None and "open_stack_password" in self.model_fields_set:
            _dict['openStackPassword'] = None

        # set to None if open_stack_url (nullable) is None
        # and model_fields_set contains the field
        if self.open_stack_url is None and "open_stack_url" in self.model_fields_set:
            _dict['openStackUrl'] = None

        # set to None if open_stack_project (nullable) is None
        # and model_fields_set contains the field
        if self.open_stack_project is None and "open_stack_project" in self.model_fields_set:
            _dict['openStackProject'] = None

        # set to None if open_stack_public_network (nullable) is None
        # and model_fields_set contains the field
        if self.open_stack_public_network is None and "open_stack_public_network" in self.model_fields_set:
            _dict['openStackPublicNetwork'] = None

        # set to None if open_stack_availability_zone (nullable) is None
        # and model_fields_set contains the field
        if self.open_stack_availability_zone is None and "open_stack_availability_zone" in self.model_fields_set:
            _dict['openStackAvailabilityZone'] = None

        # set to None if open_stack_domain (nullable) is None
        # and model_fields_set contains the field
        if self.open_stack_domain is None and "open_stack_domain" in self.model_fields_set:
            _dict['openStackDomain'] = None

        # set to None if open_stack_region (nullable) is None
        # and model_fields_set contains the field
        if self.open_stack_region is None and "open_stack_region" in self.model_fields_set:
            _dict['openStackRegion'] = None

        # set to None if open_stack_continent (nullable) is None
        # and model_fields_set contains the field
        if self.open_stack_continent is None and "open_stack_continent" in self.model_fields_set:
            _dict['openStackContinent'] = None

        # set to None if open_stack_volume_type (nullable) is None
        # and model_fields_set contains the field
        if self.open_stack_volume_type is None and "open_stack_volume_type" in self.model_fields_set:
            _dict['openStackVolumeType'] = None

        # set to None if open_stack_internal_subnet_id (nullable) is None
        # and model_fields_set contains the field
        if self.open_stack_internal_subnet_id is None and "open_stack_internal_subnet_id" in self.model_fields_set:
            _dict['openStackInternalSubnetId'] = None

        # set to None if organization_id (nullable) is None
        # and model_fields_set contains the field
        if self.organization_id is None and "organization_id" in self.model_fields_set:
            _dict['organizationId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateOpenstackCloudCommand from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "openStackUser": obj.get("openStackUser"),
            "openStackPassword": obj.get("openStackPassword"),
            "openStackUrl": obj.get("openStackUrl"),
            "openStackProject": obj.get("openStackProject"),
            "openStackPublicNetwork": obj.get("openStackPublicNetwork"),
            "openStackAvailabilityZone": obj.get("openStackAvailabilityZone"),
            "openStackDomain": obj.get("openStackDomain"),
            "openStackRegion": obj.get("openStackRegion"),
            "openStackContinent": obj.get("openStackContinent"),
            "openStackVolumeType": obj.get("openStackVolumeType"),
            "openStackImportNetwork": obj.get("openStackImportNetwork"),
            "openStackInternalSubnetId": obj.get("openStackInternalSubnetId"),
            "organizationId": obj.get("organizationId"),
            "applicationCredEnabled": obj.get("applicationCredEnabled"),
            "isAdmin": obj.get("isAdmin"),
            "skipTlsFlag": obj.get("skipTlsFlag")
        })
        return _obj


