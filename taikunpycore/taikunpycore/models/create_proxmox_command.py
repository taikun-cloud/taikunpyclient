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
from taikunpycore.models.create_proxmox_network_dto import CreateProxmoxNetworkDto
from typing import Optional, Set
from typing_extensions import Self

class CreateProxmoxCommand(BaseModel):
    """
    CreateProxmoxCommand
    """ # noqa: E501
    name: Optional[StrictStr] = None
    token_id: Optional[StrictStr] = Field(default=None, alias="tokenId")
    url: Optional[StrictStr] = None
    token_secret: Optional[StrictStr] = Field(default=None, alias="tokenSecret")
    storage: Optional[StrictStr] = None
    vm_template_name: Optional[StrictStr] = Field(default=None, alias="vmTemplateName")
    continent: Optional[StrictStr] = None
    organization_id: Optional[StrictInt] = Field(default=None, alias="organizationId")
    hypervisors: Optional[List[StrictStr]] = None
    public_network: Optional[CreateProxmoxNetworkDto] = Field(default=None, alias="publicNetwork")
    private_network: Optional[CreateProxmoxNetworkDto] = Field(default=None, alias="privateNetwork")
    skip_tls_flag: Optional[StrictBool] = Field(default=None, alias="skipTlsFlag")
    __properties: ClassVar[List[str]] = ["name", "tokenId", "url", "tokenSecret", "storage", "vmTemplateName", "continent", "organizationId", "hypervisors", "publicNetwork", "privateNetwork", "skipTlsFlag"]

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
        """Create an instance of CreateProxmoxCommand from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of public_network
        if self.public_network:
            _dict['publicNetwork'] = self.public_network.to_dict()
        # override the default output from pydantic by calling `to_dict()` of private_network
        if self.private_network:
            _dict['privateNetwork'] = self.private_network.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if token_id (nullable) is None
        # and model_fields_set contains the field
        if self.token_id is None and "token_id" in self.model_fields_set:
            _dict['tokenId'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if token_secret (nullable) is None
        # and model_fields_set contains the field
        if self.token_secret is None and "token_secret" in self.model_fields_set:
            _dict['tokenSecret'] = None

        # set to None if storage (nullable) is None
        # and model_fields_set contains the field
        if self.storage is None and "storage" in self.model_fields_set:
            _dict['storage'] = None

        # set to None if vm_template_name (nullable) is None
        # and model_fields_set contains the field
        if self.vm_template_name is None and "vm_template_name" in self.model_fields_set:
            _dict['vmTemplateName'] = None

        # set to None if continent (nullable) is None
        # and model_fields_set contains the field
        if self.continent is None and "continent" in self.model_fields_set:
            _dict['continent'] = None

        # set to None if organization_id (nullable) is None
        # and model_fields_set contains the field
        if self.organization_id is None and "organization_id" in self.model_fields_set:
            _dict['organizationId'] = None

        # set to None if hypervisors (nullable) is None
        # and model_fields_set contains the field
        if self.hypervisors is None and "hypervisors" in self.model_fields_set:
            _dict['hypervisors'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateProxmoxCommand from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "tokenId": obj.get("tokenId"),
            "url": obj.get("url"),
            "tokenSecret": obj.get("tokenSecret"),
            "storage": obj.get("storage"),
            "vmTemplateName": obj.get("vmTemplateName"),
            "continent": obj.get("continent"),
            "organizationId": obj.get("organizationId"),
            "hypervisors": obj.get("hypervisors"),
            "publicNetwork": CreateProxmoxNetworkDto.from_dict(obj["publicNetwork"]) if obj.get("publicNetwork") is not None else None,
            "privateNetwork": CreateProxmoxNetworkDto.from_dict(obj["privateNetwork"]) if obj.get("privateNetwork") is not None else None,
            "skipTlsFlag": obj.get("skipTlsFlag")
        })
        return _obj


