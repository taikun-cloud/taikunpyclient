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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CBackupDto(BaseModel):
    """
    CBackupDto
    """ # noqa: E501
    metadata_name: Optional[StrictStr] = Field(alias="metadataName")
    created_at: Optional[datetime] = Field(alias="createdAt")
    expiration: Optional[datetime]
    schedule_name: Optional[StrictStr] = Field(alias="scheduleName")
    namespace: Optional[StrictStr]
    location: Optional[StrictStr]
    phase: Optional[StrictStr]
    __properties: ClassVar[List[str]] = ["metadataName", "createdAt", "expiration", "scheduleName", "namespace", "location", "phase"]

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
        """Create an instance of CBackupDto from a JSON string"""
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
        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['createdAt'] = None

        # set to None if expiration (nullable) is None
        # and model_fields_set contains the field
        if self.expiration is None and "expiration" in self.model_fields_set:
            _dict['expiration'] = None

        # set to None if schedule_name (nullable) is None
        # and model_fields_set contains the field
        if self.schedule_name is None and "schedule_name" in self.model_fields_set:
            _dict['scheduleName'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if phase (nullable) is None
        # and model_fields_set contains the field
        if self.phase is None and "phase" in self.model_fields_set:
            _dict['phase'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CBackupDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "metadataName": obj.get("metadataName"),
            "createdAt": obj.get("createdAt"),
            "expiration": obj.get("expiration"),
            "scheduleName": obj.get("scheduleName"),
            "namespace": obj.get("namespace"),
            "location": obj.get("location"),
            "phase": obj.get("phase")
        })
        return _obj


