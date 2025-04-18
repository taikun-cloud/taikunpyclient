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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class BackupStorageLocationDto(BaseModel):
    """
    BackupStorageLocationDto
    """ # noqa: E501
    metadata_name: Optional[StrictStr] = Field(alias="metadataName")
    provider: Optional[StrictStr]
    namespace: Optional[StrictStr]
    last_validated: Optional[datetime] = Field(alias="lastValidated")
    created_at: Optional[datetime] = Field(alias="createdAt")
    access_mode: Optional[StrictStr] = Field(alias="accessMode")
    phase: Optional[StrictStr]
    backup_credential_id: Optional[StrictInt] = Field(alias="backupCredentialId")
    __properties: ClassVar[List[str]] = ["metadataName", "provider", "namespace", "lastValidated", "createdAt", "accessMode", "phase", "backupCredentialId"]

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
        """Create an instance of BackupStorageLocationDto from a JSON string"""
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
        # set to None if last_validated (nullable) is None
        # and model_fields_set contains the field
        if self.last_validated is None and "last_validated" in self.model_fields_set:
            _dict['lastValidated'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['createdAt'] = None

        # set to None if phase (nullable) is None
        # and model_fields_set contains the field
        if self.phase is None and "phase" in self.model_fields_set:
            _dict['phase'] = None

        # set to None if backup_credential_id (nullable) is None
        # and model_fields_set contains the field
        if self.backup_credential_id is None and "backup_credential_id" in self.model_fields_set:
            _dict['backupCredentialId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BackupStorageLocationDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "metadataName": obj.get("metadataName"),
            "provider": obj.get("provider"),
            "namespace": obj.get("namespace"),
            "lastValidated": obj.get("lastValidated"),
            "createdAt": obj.get("createdAt"),
            "accessMode": obj.get("accessMode"),
            "phase": obj.get("phase"),
            "backupCredentialId": obj.get("backupCredentialId")
        })
        return _obj


