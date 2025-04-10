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

class InstanceAppListDto(BaseModel):
    """
    InstanceAppListDto
    """ # noqa: E501
    id: Optional[StrictInt]
    name: Optional[StrictStr]
    namespace: Optional[StrictStr]
    status: EInstanceStatus
    version: Optional[StrictStr]
    catalog_id: Optional[StrictInt] = Field(alias="catalogId")
    catalog_name: Optional[StrictStr] = Field(alias="catalogName")
    catalog_app_name: Optional[StrictStr] = Field(alias="catalogAppName")
    catalog_app_id: Optional[StrictInt] = Field(alias="catalogAppId")
    app_repo_name: Optional[StrictStr] = Field(alias="appRepoName")
    logo: Optional[StrictStr]
    auto_sync: Optional[StrictBool] = Field(alias="autoSync")
    created: Optional[StrictStr]
    created_by: Optional[StrictStr] = Field(alias="createdBy")
    last_modified: Optional[StrictStr] = Field(alias="lastModified")
    last_modified_by: Optional[StrictStr] = Field(alias="lastModifiedBy")
    project_id: Optional[StrictInt] = Field(alias="projectId")
    project_name: Optional[StrictStr] = Field(alias="projectName")
    logs: Optional[StrictStr]
    __properties: ClassVar[List[str]] = ["id", "name", "namespace", "status", "version", "catalogId", "catalogName", "catalogAppName", "catalogAppId", "appRepoName", "logo", "autoSync", "created", "createdBy", "lastModified", "lastModifiedBy", "projectId", "projectName", "logs"]

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
        """Create an instance of InstanceAppListDto from a JSON string"""
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

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        # set to None if catalog_name (nullable) is None
        # and model_fields_set contains the field
        if self.catalog_name is None and "catalog_name" in self.model_fields_set:
            _dict['catalogName'] = None

        # set to None if catalog_app_name (nullable) is None
        # and model_fields_set contains the field
        if self.catalog_app_name is None and "catalog_app_name" in self.model_fields_set:
            _dict['catalogAppName'] = None

        # set to None if app_repo_name (nullable) is None
        # and model_fields_set contains the field
        if self.app_repo_name is None and "app_repo_name" in self.model_fields_set:
            _dict['appRepoName'] = None

        # set to None if logo (nullable) is None
        # and model_fields_set contains the field
        if self.logo is None and "logo" in self.model_fields_set:
            _dict['logo'] = None

        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and "created" in self.model_fields_set:
            _dict['created'] = None

        # set to None if created_by (nullable) is None
        # and model_fields_set contains the field
        if self.created_by is None and "created_by" in self.model_fields_set:
            _dict['createdBy'] = None

        # set to None if last_modified (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified is None and "last_modified" in self.model_fields_set:
            _dict['lastModified'] = None

        # set to None if last_modified_by (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified_by is None and "last_modified_by" in self.model_fields_set:
            _dict['lastModifiedBy'] = None

        # set to None if project_name (nullable) is None
        # and model_fields_set contains the field
        if self.project_name is None and "project_name" in self.model_fields_set:
            _dict['projectName'] = None

        # set to None if logs (nullable) is None
        # and model_fields_set contains the field
        if self.logs is None and "logs" in self.model_fields_set:
            _dict['logs'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InstanceAppListDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "namespace": obj.get("namespace"),
            "status": obj.get("status"),
            "version": obj.get("version"),
            "catalogId": obj.get("catalogId"),
            "catalogName": obj.get("catalogName"),
            "catalogAppName": obj.get("catalogAppName"),
            "catalogAppId": obj.get("catalogAppId"),
            "appRepoName": obj.get("appRepoName"),
            "logo": obj.get("logo"),
            "autoSync": obj.get("autoSync"),
            "created": obj.get("created"),
            "createdBy": obj.get("createdBy"),
            "lastModified": obj.get("lastModified"),
            "lastModifiedBy": obj.get("lastModifiedBy"),
            "projectId": obj.get("projectId"),
            "projectName": obj.get("projectName"),
            "logs": obj.get("logs")
        })
        return _obj


