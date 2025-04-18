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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from taikunpycore.models.cloud_type import CloudType
from taikunpycore.models.project_status import ProjectStatus
from typing import Optional, Set
from typing_extensions import Self

class ProjectDetailsForVmsDto(BaseModel):
    """
    ProjectDetailsForVmsDto
    """ # noqa: E501
    status: ProjectStatus
    name: Optional[StrictStr]
    id: Optional[StrictInt]
    cloud_type: CloudType = Field(alias="cloudType")
    cloud_name: Optional[StrictStr] = Field(alias="cloudName")
    cloud_id: Optional[StrictInt] = Field(alias="cloudId")
    organization_name: Optional[StrictStr] = Field(alias="organizationName")
    organization_id: Optional[StrictInt] = Field(alias="organizationId")
    is_locked: Optional[StrictBool] = Field(alias="isLocked")
    is_project_maintenance_mode_enabled: Optional[StrictBool] = Field(alias="isProjectMaintenanceModeEnabled")
    has_selected_flavors: Optional[StrictBool] = Field(alias="hasSelectedFlavors")
    is_maintenance_mode_enabled: Optional[StrictBool] = Field(alias="isMaintenanceModeEnabled")
    is_drs_enabled: Optional[StrictBool] = Field(alias="isDrsEnabled")
    project_cloud_revision: Optional[StrictInt] = Field(alias="projectCloudRevision")
    cloud_credential_revision: Optional[StrictInt] = Field(alias="cloudCredentialRevision")
    allow_full_spot_kubernetes: Optional[StrictBool] = Field(alias="allowFullSpotKubernetes")
    allow_spot_workers: Optional[StrictBool] = Field(alias="allowSpotWorkers")
    allow_spot_vms: Optional[StrictBool] = Field(alias="allowSpotVMs")
    max_spot_price: Optional[Union[StrictFloat, StrictInt]] = Field(alias="maxSpotPrice")
    total_hourly_cost: Union[StrictFloat, StrictInt] = Field(alias="totalHourlyCost")
    availability_zones: Optional[List[StrictStr]] = Field(alias="availabilityZones")
    hypervisors: Optional[List[StrictStr]]
    expired_at: Optional[StrictStr] = Field(alias="expiredAt")
    __properties: ClassVar[List[str]] = ["status", "name", "id", "cloudType", "cloudName", "cloudId", "organizationName", "organizationId", "isLocked", "isProjectMaintenanceModeEnabled", "hasSelectedFlavors", "isMaintenanceModeEnabled", "isDrsEnabled", "projectCloudRevision", "cloudCredentialRevision", "allowFullSpotKubernetes", "allowSpotWorkers", "allowSpotVMs", "maxSpotPrice", "totalHourlyCost", "availabilityZones", "hypervisors", "expiredAt"]

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
        """Create an instance of ProjectDetailsForVmsDto from a JSON string"""
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
        # set to None if cloud_id (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_id is None and "cloud_id" in self.model_fields_set:
            _dict['cloudId'] = None

        # set to None if has_selected_flavors (nullable) is None
        # and model_fields_set contains the field
        if self.has_selected_flavors is None and "has_selected_flavors" in self.model_fields_set:
            _dict['hasSelectedFlavors'] = None

        # set to None if project_cloud_revision (nullable) is None
        # and model_fields_set contains the field
        if self.project_cloud_revision is None and "project_cloud_revision" in self.model_fields_set:
            _dict['projectCloudRevision'] = None

        # set to None if cloud_credential_revision (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_credential_revision is None and "cloud_credential_revision" in self.model_fields_set:
            _dict['cloudCredentialRevision'] = None

        # set to None if max_spot_price (nullable) is None
        # and model_fields_set contains the field
        if self.max_spot_price is None and "max_spot_price" in self.model_fields_set:
            _dict['maxSpotPrice'] = None

        # set to None if availability_zones (nullable) is None
        # and model_fields_set contains the field
        if self.availability_zones is None and "availability_zones" in self.model_fields_set:
            _dict['availabilityZones'] = None

        # set to None if hypervisors (nullable) is None
        # and model_fields_set contains the field
        if self.hypervisors is None and "hypervisors" in self.model_fields_set:
            _dict['hypervisors'] = None

        # set to None if expired_at (nullable) is None
        # and model_fields_set contains the field
        if self.expired_at is None and "expired_at" in self.model_fields_set:
            _dict['expiredAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectDetailsForVmsDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "name": obj.get("name"),
            "id": obj.get("id"),
            "cloudType": obj.get("cloudType"),
            "cloudName": obj.get("cloudName"),
            "cloudId": obj.get("cloudId"),
            "organizationName": obj.get("organizationName"),
            "organizationId": obj.get("organizationId"),
            "isLocked": obj.get("isLocked"),
            "isProjectMaintenanceModeEnabled": obj.get("isProjectMaintenanceModeEnabled"),
            "hasSelectedFlavors": obj.get("hasSelectedFlavors"),
            "isMaintenanceModeEnabled": obj.get("isMaintenanceModeEnabled"),
            "isDrsEnabled": obj.get("isDrsEnabled"),
            "projectCloudRevision": obj.get("projectCloudRevision"),
            "cloudCredentialRevision": obj.get("cloudCredentialRevision"),
            "allowFullSpotKubernetes": obj.get("allowFullSpotKubernetes"),
            "allowSpotWorkers": obj.get("allowSpotWorkers"),
            "allowSpotVMs": obj.get("allowSpotVMs"),
            "maxSpotPrice": obj.get("maxSpotPrice"),
            "totalHourlyCost": obj.get("totalHourlyCost"),
            "availabilityZones": obj.get("availabilityZones"),
            "hypervisors": obj.get("hypervisors"),
            "expiredAt": obj.get("expiredAt")
        })
        return _obj


