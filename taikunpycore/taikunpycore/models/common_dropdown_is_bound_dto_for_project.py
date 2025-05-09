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
from taikunpycore.models.cloud_type import CloudType
from taikunpycore.models.import_cluster_type import ImportClusterType
from taikunpycore.models.project_health import ProjectHealth
from taikunpycore.models.project_status import ProjectStatus
from typing import Optional, Set
from typing_extensions import Self

class CommonDropdownIsBoundDtoForProject(BaseModel):
    """
    CommonDropdownIsBoundDtoForProject
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    is_bound: Optional[StrictBool] = Field(default=None, alias="isBound")
    has_kube_config_file: Optional[StrictBool] = Field(default=None, alias="hasKubeConfigFile")
    kubernetes_version: Optional[StrictStr] = Field(default=None, alias="kubernetesVersion")
    is_locked: Optional[StrictBool] = Field(default=None, alias="isLocked")
    maintenance_mode_enabled: Optional[StrictBool] = Field(default=None, alias="maintenanceModeEnabled")
    is_virtual_cluster: Optional[StrictBool] = Field(default=None, alias="isVirtualCluster")
    alerting_profile_id: Optional[StrictInt] = Field(default=None, alias="alertingProfileId")
    cloud_type: Optional[CloudType] = Field(default=None, alias="cloudType")
    status: Optional[ProjectStatus] = None
    health: Optional[ProjectHealth] = None
    import_cluster_type: Optional[ImportClusterType] = Field(default=None, alias="importClusterType")
    __properties: ClassVar[List[str]] = ["id", "name", "isBound", "hasKubeConfigFile", "kubernetesVersion", "isLocked", "maintenanceModeEnabled", "isVirtualCluster", "alertingProfileId", "cloudType", "status", "health", "importClusterType"]

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
        """Create an instance of CommonDropdownIsBoundDtoForProject from a JSON string"""
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

        # set to None if kubernetes_version (nullable) is None
        # and model_fields_set contains the field
        if self.kubernetes_version is None and "kubernetes_version" in self.model_fields_set:
            _dict['kubernetesVersion'] = None

        # set to None if alerting_profile_id (nullable) is None
        # and model_fields_set contains the field
        if self.alerting_profile_id is None and "alerting_profile_id" in self.model_fields_set:
            _dict['alertingProfileId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonDropdownIsBoundDtoForProject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "isBound": obj.get("isBound"),
            "hasKubeConfigFile": obj.get("hasKubeConfigFile"),
            "kubernetesVersion": obj.get("kubernetesVersion"),
            "isLocked": obj.get("isLocked"),
            "maintenanceModeEnabled": obj.get("maintenanceModeEnabled"),
            "isVirtualCluster": obj.get("isVirtualCluster"),
            "alertingProfileId": obj.get("alertingProfileId"),
            "cloudType": obj.get("cloudType"),
            "status": obj.get("status"),
            "health": obj.get("health"),
            "importClusterType": obj.get("importClusterType")
        })
        return _obj


