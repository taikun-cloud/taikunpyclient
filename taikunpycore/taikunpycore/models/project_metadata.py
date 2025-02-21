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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from taikunpycore.models.provider import Provider
from typing import Optional, Set
from typing_extensions import Self

class ProjectMetadata(BaseModel):
    """
    ProjectMetadata
    """ # noqa: E501
    path: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    vcs_sub_path: Optional[StrictStr] = Field(default=None, alias="vcsSubPath")
    providers: Optional[List[Provider]] = None
    __properties: ClassVar[List[str]] = ["path", "type", "vcsSubPath", "providers"]

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
        """Create an instance of ProjectMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in providers (list)
        _items = []
        if self.providers:
            for _item_providers in self.providers:
                if _item_providers:
                    _items.append(_item_providers.to_dict())
            _dict['providers'] = _items
        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if vcs_sub_path (nullable) is None
        # and model_fields_set contains the field
        if self.vcs_sub_path is None and "vcs_sub_path" in self.model_fields_set:
            _dict['vcsSubPath'] = None

        # set to None if providers (nullable) is None
        # and model_fields_set contains the field
        if self.providers is None and "providers" in self.model_fields_set:
            _dict['providers'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "path": obj.get("path"),
            "type": obj.get("type"),
            "vcsSubPath": obj.get("vcsSubPath"),
            "providers": [Provider.from_dict(_item) for _item in obj["providers"]] if obj.get("providers") is not None else None
        })
        return _obj


