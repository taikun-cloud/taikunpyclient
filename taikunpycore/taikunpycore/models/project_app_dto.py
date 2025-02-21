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
from taikunpycore.models.e_instance_status import EInstanceStatus
from typing import Optional, Set
from typing_extensions import Self

class ProjectAppDto(BaseModel):
    """
    ProjectAppDto
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    namespace: Optional[StrictStr] = None
    project_name: Optional[StrictStr] = Field(default=None, alias="projectName")
    project_id: Optional[StrictInt] = Field(default=None, alias="projectId")
    version: Optional[StrictStr] = None
    is_locked: Optional[StrictBool] = Field(default=None, alias="isLocked")
    status: Optional[EInstanceStatus] = None
    auto_sync: Optional[StrictBool] = Field(default=None, alias="autoSync")
    __properties: ClassVar[List[str]] = ["id", "name", "namespace", "projectName", "projectId", "version", "isLocked", "status", "autoSync"]

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
        """Create an instance of ProjectAppDto from a JSON string"""
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

        # set to None if namespace (nullable) is None
        # and model_fields_set contains the field
        if self.namespace is None and "namespace" in self.model_fields_set:
            _dict['namespace'] = None

        # set to None if project_name (nullable) is None
        # and model_fields_set contains the field
        if self.project_name is None and "project_name" in self.model_fields_set:
            _dict['projectName'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectAppDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "namespace": obj.get("namespace"),
            "projectName": obj.get("projectName"),
            "projectId": obj.get("projectId"),
            "version": obj.get("version"),
            "isLocked": obj.get("isLocked"),
            "status": obj.get("status"),
            "autoSync": obj.get("autoSync")
        })
        return _obj


