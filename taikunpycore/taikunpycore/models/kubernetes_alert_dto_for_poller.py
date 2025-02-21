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

class KubernetesAlertDtoForPoller(BaseModel):
    """
    KubernetesAlertDtoForPoller
    """ # noqa: E501
    id: Optional[StrictInt]
    labels: Optional[Any]
    description: Optional[StrictStr]
    title: Optional[StrictStr]
    severity: Optional[StrictStr]
    fingerprint: Optional[StrictStr]
    status: Optional[StrictStr]
    starts_at: Optional[StrictStr] = Field(alias="startsAt")
    end_at: Optional[StrictStr] = Field(alias="endAt")
    is_solved: Optional[StrictBool] = Field(alias="isSolved")
    project_id: Optional[StrictInt] = Field(alias="projectId")
    project_name: Optional[StrictStr] = Field(alias="projectName")
    is_silenced: Optional[StrictBool] = Field(alias="isSilenced")
    silence_reason: Optional[StrictStr] = Field(alias="silenceReason")
    last_modified_by: Optional[StrictStr] = Field(alias="lastModifiedBy")
    __properties: ClassVar[List[str]] = ["id", "labels", "description", "title", "severity", "fingerprint", "status", "startsAt", "endAt", "isSolved", "projectId", "projectName", "isSilenced", "silenceReason", "lastModifiedBy"]

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
        """Create an instance of KubernetesAlertDtoForPoller from a JSON string"""
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
        # set to None if labels (nullable) is None
        # and model_fields_set contains the field
        if self.labels is None and "labels" in self.model_fields_set:
            _dict['labels'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if severity (nullable) is None
        # and model_fields_set contains the field
        if self.severity is None and "severity" in self.model_fields_set:
            _dict['severity'] = None

        # set to None if fingerprint (nullable) is None
        # and model_fields_set contains the field
        if self.fingerprint is None and "fingerprint" in self.model_fields_set:
            _dict['fingerprint'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if starts_at (nullable) is None
        # and model_fields_set contains the field
        if self.starts_at is None and "starts_at" in self.model_fields_set:
            _dict['startsAt'] = None

        # set to None if end_at (nullable) is None
        # and model_fields_set contains the field
        if self.end_at is None and "end_at" in self.model_fields_set:
            _dict['endAt'] = None

        # set to None if project_name (nullable) is None
        # and model_fields_set contains the field
        if self.project_name is None and "project_name" in self.model_fields_set:
            _dict['projectName'] = None

        # set to None if silence_reason (nullable) is None
        # and model_fields_set contains the field
        if self.silence_reason is None and "silence_reason" in self.model_fields_set:
            _dict['silenceReason'] = None

        # set to None if last_modified_by (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified_by is None and "last_modified_by" in self.model_fields_set:
            _dict['lastModifiedBy'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KubernetesAlertDtoForPoller from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "labels": obj.get("labels"),
            "description": obj.get("description"),
            "title": obj.get("title"),
            "severity": obj.get("severity"),
            "fingerprint": obj.get("fingerprint"),
            "status": obj.get("status"),
            "startsAt": obj.get("startsAt"),
            "endAt": obj.get("endAt"),
            "isSolved": obj.get("isSolved"),
            "projectId": obj.get("projectId"),
            "projectName": obj.get("projectName"),
            "isSilenced": obj.get("isSilenced"),
            "silenceReason": obj.get("silenceReason"),
            "lastModifiedBy": obj.get("lastModifiedBy")
        })
        return _obj


