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

class CreateOpaProfileCommand(BaseModel):
    """
    CreateOpaProfileCommand
    """ # noqa: E501
    name: Optional[StrictStr] = None
    forbid_node_port: Optional[StrictBool] = Field(default=None, alias="forbidNodePort")
    forbid_http_ingress: Optional[StrictBool] = Field(default=None, alias="forbidHttpIngress")
    require_probe: Optional[StrictBool] = Field(default=None, alias="requireProbe")
    unique_ingresses: Optional[StrictBool] = Field(default=None, alias="uniqueIngresses")
    unique_service_selector: Optional[StrictBool] = Field(default=None, alias="uniqueServiceSelector")
    force_pod_resource: Optional[StrictBool] = Field(default=None, alias="forcePodResource")
    is_node_name_forbidden_in_vc: Optional[StrictBool] = Field(default=None, alias="isNodeNameForbiddenInVC")
    is_master_taint_enforced: Optional[StrictBool] = Field(default=None, alias="isMasterTaintEnforced")
    allowed_repo: Optional[List[StrictStr]] = Field(default=None, alias="allowedRepo")
    forbid_specific_tags: Optional[List[StrictStr]] = Field(default=None, alias="forbidSpecificTags")
    ingress_whitelist: Optional[List[StrictStr]] = Field(default=None, alias="ingressWhitelist")
    whitelist_master_taint_namespaces: Optional[List[StrictStr]] = Field(default=None, alias="whitelistMasterTaintNamespaces")
    organization_id: Optional[StrictInt] = Field(default=None, alias="organizationId")
    __properties: ClassVar[List[str]] = ["name", "forbidNodePort", "forbidHttpIngress", "requireProbe", "uniqueIngresses", "uniqueServiceSelector", "forcePodResource", "isNodeNameForbiddenInVC", "isMasterTaintEnforced", "allowedRepo", "forbidSpecificTags", "ingressWhitelist", "whitelistMasterTaintNamespaces", "organizationId"]

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
        """Create an instance of CreateOpaProfileCommand from a JSON string"""
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

        # set to None if allowed_repo (nullable) is None
        # and model_fields_set contains the field
        if self.allowed_repo is None and "allowed_repo" in self.model_fields_set:
            _dict['allowedRepo'] = None

        # set to None if forbid_specific_tags (nullable) is None
        # and model_fields_set contains the field
        if self.forbid_specific_tags is None and "forbid_specific_tags" in self.model_fields_set:
            _dict['forbidSpecificTags'] = None

        # set to None if ingress_whitelist (nullable) is None
        # and model_fields_set contains the field
        if self.ingress_whitelist is None and "ingress_whitelist" in self.model_fields_set:
            _dict['ingressWhitelist'] = None

        # set to None if whitelist_master_taint_namespaces (nullable) is None
        # and model_fields_set contains the field
        if self.whitelist_master_taint_namespaces is None and "whitelist_master_taint_namespaces" in self.model_fields_set:
            _dict['whitelistMasterTaintNamespaces'] = None

        # set to None if organization_id (nullable) is None
        # and model_fields_set contains the field
        if self.organization_id is None and "organization_id" in self.model_fields_set:
            _dict['organizationId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateOpaProfileCommand from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "forbidNodePort": obj.get("forbidNodePort"),
            "forbidHttpIngress": obj.get("forbidHttpIngress"),
            "requireProbe": obj.get("requireProbe"),
            "uniqueIngresses": obj.get("uniqueIngresses"),
            "uniqueServiceSelector": obj.get("uniqueServiceSelector"),
            "forcePodResource": obj.get("forcePodResource"),
            "isNodeNameForbiddenInVC": obj.get("isNodeNameForbiddenInVC"),
            "isMasterTaintEnforced": obj.get("isMasterTaintEnforced"),
            "allowedRepo": obj.get("allowedRepo"),
            "forbidSpecificTags": obj.get("forbidSpecificTags"),
            "ingressWhitelist": obj.get("ingressWhitelist"),
            "whitelistMasterTaintNamespaces": obj.get("whitelistMasterTaintNamespaces"),
            "organizationId": obj.get("organizationId")
        })
        return _obj


