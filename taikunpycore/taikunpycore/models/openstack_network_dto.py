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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OpenstackNetworkDto(BaseModel):
    """
    OpenstackNetworkDto
    """ # noqa: E501
    network_limit: Optional[StrictInt] = Field(default=None, alias="networkLimit")
    subnet_limit: Optional[StrictInt] = Field(default=None, alias="subnetLimit")
    floating_ip_limit: Optional[StrictInt] = Field(default=None, alias="floatingIpLimit")
    router_limit: Optional[StrictInt] = Field(default=None, alias="routerLimit")
    security_group_limit: Optional[StrictInt] = Field(default=None, alias="securityGroupLimit")
    security_group_rule_limit: Optional[StrictInt] = Field(default=None, alias="securityGroupRuleLimit")
    port_limit: Optional[StrictInt] = Field(default=None, alias="portLimit")
    network_used: Optional[StrictInt] = Field(default=None, alias="networkUsed")
    subnet_used: Optional[StrictInt] = Field(default=None, alias="subnetUsed")
    floating_ip_used: Optional[StrictInt] = Field(default=None, alias="floatingIpUsed")
    router_used: Optional[StrictInt] = Field(default=None, alias="routerUsed")
    security_group_used: Optional[StrictInt] = Field(default=None, alias="securityGroupUsed")
    port_used: Optional[StrictInt] = Field(default=None, alias="portUsed")
    security_group_rule_used: Optional[StrictInt] = Field(default=None, alias="securityGroupRuleUsed")
    __properties: ClassVar[List[str]] = ["networkLimit", "subnetLimit", "floatingIpLimit", "routerLimit", "securityGroupLimit", "securityGroupRuleLimit", "portLimit", "networkUsed", "subnetUsed", "floatingIpUsed", "routerUsed", "securityGroupUsed", "portUsed", "securityGroupRuleUsed"]

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
        """Create an instance of OpenstackNetworkDto from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OpenstackNetworkDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "networkLimit": obj.get("networkLimit"),
            "subnetLimit": obj.get("subnetLimit"),
            "floatingIpLimit": obj.get("floatingIpLimit"),
            "routerLimit": obj.get("routerLimit"),
            "securityGroupLimit": obj.get("securityGroupLimit"),
            "securityGroupRuleLimit": obj.get("securityGroupRuleLimit"),
            "portLimit": obj.get("portLimit"),
            "networkUsed": obj.get("networkUsed"),
            "subnetUsed": obj.get("subnetUsed"),
            "floatingIpUsed": obj.get("floatingIpUsed"),
            "routerUsed": obj.get("routerUsed"),
            "securityGroupUsed": obj.get("securityGroupUsed"),
            "portUsed": obj.get("portUsed"),
            "securityGroupRuleUsed": obj.get("securityGroupRuleUsed")
        })
        return _obj


