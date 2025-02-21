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

class CatalogAppParamsDetailsDto(BaseModel):
    """
    CatalogAppParamsDetailsDto
    """ # noqa: E501
    id: Optional[StrictInt] = None
    catalog_app_name: Optional[StrictStr] = Field(default=None, alias="catalogAppName")
    key: Optional[StrictStr] = None
    value: Optional[StrictStr] = None
    is_editable_when_installing: Optional[StrictBool] = Field(default=None, alias="isEditableWhenInstalling")
    is_editable_after_installation: Optional[StrictBool] = Field(default=None, alias="isEditableAfterInstallation")
    is_mandatory: Optional[StrictBool] = Field(default=None, alias="isMandatory")
    has_json_schema: Optional[StrictBool] = Field(default=None, alias="hasJsonSchema")
    __properties: ClassVar[List[str]] = ["id", "catalogAppName", "key", "value", "isEditableWhenInstalling", "isEditableAfterInstallation", "isMandatory", "hasJsonSchema"]

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
        """Create an instance of CatalogAppParamsDetailsDto from a JSON string"""
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
        # set to None if catalog_app_name (nullable) is None
        # and model_fields_set contains the field
        if self.catalog_app_name is None and "catalog_app_name" in self.model_fields_set:
            _dict['catalogAppName'] = None

        # set to None if key (nullable) is None
        # and model_fields_set contains the field
        if self.key is None and "key" in self.model_fields_set:
            _dict['key'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CatalogAppParamsDetailsDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "catalogAppName": obj.get("catalogAppName"),
            "key": obj.get("key"),
            "value": obj.get("value"),
            "isEditableWhenInstalling": obj.get("isEditableWhenInstalling"),
            "isEditableAfterInstallation": obj.get("isEditableAfterInstallation"),
            "isMandatory": obj.get("isMandatory"),
            "hasJsonSchema": obj.get("hasJsonSchema")
        })
        return _obj


