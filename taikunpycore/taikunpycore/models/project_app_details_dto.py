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
from taikunpycore.models.project_app_param_dto import ProjectAppParamDto
from typing import Optional, Set
from typing_extensions import Self

class ProjectAppDetailsDto(BaseModel):
    """
    ProjectAppDetailsDto
    """ # noqa: E501
    id: Optional[StrictInt]
    name: Optional[StrictStr]
    namespace: Optional[StrictStr]
    status: EInstanceStatus
    version: Optional[StrictStr]
    catalog_id: Optional[StrictInt] = Field(alias="catalogId")
    catalog_name: Optional[StrictStr] = Field(alias="catalogName")
    catalog_app_name: Optional[StrictStr] = Field(alias="catalogAppName")
    app_repo_name: Optional[StrictStr] = Field(alias="appRepoName")
    logo: Optional[StrictStr]
    values: Optional[StrictStr]
    auto_sync: Optional[StrictBool] = Field(alias="autoSync")
    release_notes: Optional[StrictStr] = Field(alias="releaseNotes")
    project_name: Optional[StrictStr] = Field(alias="projectName")
    helm_result: Optional[StrictStr] = Field(alias="helmResult")
    project_id: Optional[StrictInt] = Field(alias="projectId")
    has_json_schema: Optional[StrictBool] = Field(alias="hasJsonSchema")
    catalog_app_id: Optional[StrictInt] = Field(alias="catalogAppId")
    package_id: Optional[StrictStr] = Field(alias="packageId")
    logs: Optional[StrictStr]
    project_app_params: Optional[List[ProjectAppParamDto]] = Field(alias="projectAppParams")
    __properties: ClassVar[List[str]] = ["id", "name", "namespace", "status", "version", "catalogId", "catalogName", "catalogAppName", "appRepoName", "logo", "values", "autoSync", "releaseNotes", "projectName", "helmResult", "projectId", "hasJsonSchema", "catalogAppId", "packageId", "logs", "projectAppParams"]

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
        """Create an instance of ProjectAppDetailsDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in project_app_params (list)
        _items = []
        if self.project_app_params:
            for _item_project_app_params in self.project_app_params:
                if _item_project_app_params:
                    _items.append(_item_project_app_params.to_dict())
            _dict['projectAppParams'] = _items
        # set to None if logo (nullable) is None
        # and model_fields_set contains the field
        if self.logo is None and "logo" in self.model_fields_set:
            _dict['logo'] = None

        # set to None if release_notes (nullable) is None
        # and model_fields_set contains the field
        if self.release_notes is None and "release_notes" in self.model_fields_set:
            _dict['releaseNotes'] = None

        # set to None if logs (nullable) is None
        # and model_fields_set contains the field
        if self.logs is None and "logs" in self.model_fields_set:
            _dict['logs'] = None

        # set to None if project_app_params (nullable) is None
        # and model_fields_set contains the field
        if self.project_app_params is None and "project_app_params" in self.model_fields_set:
            _dict['projectAppParams'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectAppDetailsDto from a dict"""
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
            "appRepoName": obj.get("appRepoName"),
            "logo": obj.get("logo"),
            "values": obj.get("values"),
            "autoSync": obj.get("autoSync"),
            "releaseNotes": obj.get("releaseNotes"),
            "projectName": obj.get("projectName"),
            "helmResult": obj.get("helmResult"),
            "projectId": obj.get("projectId"),
            "hasJsonSchema": obj.get("hasJsonSchema"),
            "catalogAppId": obj.get("catalogAppId"),
            "packageId": obj.get("packageId"),
            "logs": obj.get("logs"),
            "projectAppParams": [ProjectAppParamDto.from_dict(_item) for _item in obj["projectAppParams"]] if obj.get("projectAppParams") is not None else None
        })
        return _obj


