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
from taikunpycore.models.button_status_dto import ButtonStatusDto
from taikunpycore.models.cloud_type import CloudType
from taikunpycore.models.e_import_cluster_type import EImportClusterType
from taikunpycore.models.import_cluster_type import ImportClusterType
from taikunpycore.models.project_health import ProjectHealth
from taikunpycore.models.project_status import ProjectStatus
from taikunpycore.models.user_dto import UserDto
from typing import Optional, Set
from typing_extensions import Self

class ProjectListDetailDto(BaseModel):
    """
    ProjectListDetailDto
    """ # noqa: E501
    id: Optional[StrictInt]
    name: Optional[StrictStr]
    is_kubernetes: Optional[StrictBool] = Field(alias="isKubernetes")
    is_locked: Optional[StrictBool] = Field(alias="isLocked")
    is_virtual_cluster: Optional[StrictBool] = Field(alias="isVirtualCluster")
    is_monitoring_enabled: Optional[StrictBool] = Field(alias="isMonitoringEnabled")
    has_kube_config_file: Optional[StrictBool] = Field(alias="hasKubeConfigFile")
    is_maintenance_mode_enabled: Optional[StrictBool] = Field(alias="isMaintenanceModeEnabled")
    cloud_credential_name: Optional[StrictStr] = Field(default=None, alias="cloudCredentialName")
    organization_name: Optional[StrictStr] = Field(alias="organizationName")
    organization_id: Optional[StrictInt] = Field(alias="organizationId")
    status: ProjectStatus
    health: ProjectHealth
    cloud_type: Optional[CloudType] = Field(default=None, alias="cloudType")
    kubespray_current_version: Optional[StrictStr] = Field(alias="kubesprayCurrentVersion")
    kubespray_target_version: Optional[StrictStr] = Field(alias="kubesprayTargetVersion")
    kubernetes_current_version: Optional[StrictStr] = Field(alias="kubernetesCurrentVersion")
    kubernetes_target_version: Optional[StrictStr] = Field(alias="kubernetesTargetVersion")
    created_at: Optional[StrictStr] = Field(alias="createdAt")
    alerts_count: Optional[StrictInt] = Field(alias="alertsCount")
    total_servers_count: Optional[StrictInt] = Field(alias="totalServersCount")
    total_standalone_vms_count: Optional[StrictInt] = Field(alias="totalStandaloneVmsCount")
    bound_users: List[UserDto] = Field(alias="boundUsers")
    created_by: Optional[StrictStr] = Field(alias="createdBy")
    last_modified: Optional[StrictStr] = Field(alias="lastModified")
    expired_at: Optional[StrictStr] = Field(alias="expiredAt")
    delete_on_expiration: Optional[StrictBool] = Field(alias="deleteOnExpiration")
    certificate_expired_at: Optional[StrictStr] = Field(alias="certificateExpiredAt")
    last_modified_by: Optional[StrictStr] = Field(alias="lastModifiedBy")
    quota_id: Optional[StrictInt] = Field(alias="quotaId")
    allow_full_spot_kubernetes: Optional[StrictBool] = Field(alias="allowFullSpotKubernetes")
    allow_spot_workers: Optional[StrictBool] = Field(alias="allowSpotWorkers")
    allow_spot_vms: Optional[StrictBool] = Field(alias="allowSpotVMs")
    max_spot_price: Optional[Union[StrictFloat, StrictInt]] = Field(alias="maxSpotPrice")
    project_action: Optional[StrictBool] = Field(alias="projectAction")
    has_expiration_warning: Optional[StrictBool] = Field(alias="hasExpirationWarning")
    total_hourly_cost: Union[StrictFloat, StrictInt] = Field(alias="totalHourlyCost")
    is_autoscaling_enabled: Optional[StrictBool] = Field(alias="isAutoscalingEnabled")
    is_autoscaling_spot_enabled: Optional[StrictBool] = Field(alias="isAutoscalingSpotEnabled")
    ai_enabled: Optional[StrictBool] = Field(alias="aiEnabled")
    any_server: Optional[StrictBool] = Field(alias="anyServer")
    any_vm: Optional[StrictBool] = Field(alias="anyVm")
    is_backup_enabled: Optional[StrictBool] = Field(alias="isBackupEnabled")
    is_project_maintenance_mode_enabled: Optional[StrictBool] = Field(alias="isProjectMaintenanceModeEnabled")
    all_users: List[StrictStr] = Field(alias="allUsers")
    parent_project_id: Optional[StrictInt] = Field(alias="parentProjectId")
    alerting_profile_id: Optional[StrictInt] = Field(alias="alertingProfileId")
    opa_profile_id: Optional[StrictInt] = Field(alias="opaProfileId")
    lock_button: Optional[ButtonStatusDto] = Field(default=None, alias="lockButton")
    unlock_button: Optional[ButtonStatusDto] = Field(default=None, alias="unlockButton")
    delete_button: Optional[ButtonStatusDto] = Field(default=None, alias="deleteButton")
    kube_info_button: Optional[ButtonStatusDto] = Field(default=None, alias="kubeInfoButton")
    set_expiration_date_button: Optional[ButtonStatusDto] = Field(default=None, alias="setExpirationDateButton")
    reset_status_button: Optional[ButtonStatusDto] = Field(default=None, alias="resetStatusButton")
    import_cluster_type: ImportClusterType = Field(alias="importClusterType")
    e_import_cluster_type: Optional[EImportClusterType] = Field(default=None, alias="eImportClusterType")
    __properties: ClassVar[List[str]] = ["id", "name", "isKubernetes", "isLocked", "isVirtualCluster", "isMonitoringEnabled", "hasKubeConfigFile", "isMaintenanceModeEnabled", "cloudCredentialName", "organizationName", "organizationId", "status", "health", "cloudType", "kubesprayCurrentVersion", "kubesprayTargetVersion", "kubernetesCurrentVersion", "kubernetesTargetVersion", "createdAt", "alertsCount", "totalServersCount", "totalStandaloneVmsCount", "boundUsers", "createdBy", "lastModified", "expiredAt", "deleteOnExpiration", "certificateExpiredAt", "lastModifiedBy", "quotaId", "allowFullSpotKubernetes", "allowSpotWorkers", "allowSpotVMs", "maxSpotPrice", "projectAction", "hasExpirationWarning", "totalHourlyCost", "isAutoscalingEnabled", "isAutoscalingSpotEnabled", "aiEnabled", "anyServer", "anyVm", "isBackupEnabled", "isProjectMaintenanceModeEnabled", "allUsers", "parentProjectId", "alertingProfileId", "opaProfileId", "lockButton", "unlockButton", "deleteButton", "kubeInfoButton", "setExpirationDateButton", "resetStatusButton", "importClusterType", "eImportClusterType"]

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
        """Create an instance of ProjectListDetailDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in bound_users (list)
        _items = []
        if self.bound_users:
            for _item_bound_users in self.bound_users:
                if _item_bound_users:
                    _items.append(_item_bound_users.to_dict())
            _dict['boundUsers'] = _items
        # override the default output from pydantic by calling `to_dict()` of lock_button
        if self.lock_button:
            _dict['lockButton'] = self.lock_button.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unlock_button
        if self.unlock_button:
            _dict['unlockButton'] = self.unlock_button.to_dict()
        # override the default output from pydantic by calling `to_dict()` of delete_button
        if self.delete_button:
            _dict['deleteButton'] = self.delete_button.to_dict()
        # override the default output from pydantic by calling `to_dict()` of kube_info_button
        if self.kube_info_button:
            _dict['kubeInfoButton'] = self.kube_info_button.to_dict()
        # override the default output from pydantic by calling `to_dict()` of set_expiration_date_button
        if self.set_expiration_date_button:
            _dict['setExpirationDateButton'] = self.set_expiration_date_button.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reset_status_button
        if self.reset_status_button:
            _dict['resetStatusButton'] = self.reset_status_button.to_dict()
        # set to None if cloud_credential_name (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_credential_name is None and "cloud_credential_name" in self.model_fields_set:
            _dict['cloudCredentialName'] = None

        # set to None if kubespray_target_version (nullable) is None
        # and model_fields_set contains the field
        if self.kubespray_target_version is None and "kubespray_target_version" in self.model_fields_set:
            _dict['kubesprayTargetVersion'] = None

        # set to None if kubernetes_target_version (nullable) is None
        # and model_fields_set contains the field
        if self.kubernetes_target_version is None and "kubernetes_target_version" in self.model_fields_set:
            _dict['kubernetesTargetVersion'] = None

        # set to None if last_modified (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified is None and "last_modified" in self.model_fields_set:
            _dict['lastModified'] = None

        # set to None if expired_at (nullable) is None
        # and model_fields_set contains the field
        if self.expired_at is None and "expired_at" in self.model_fields_set:
            _dict['expiredAt'] = None

        # set to None if certificate_expired_at (nullable) is None
        # and model_fields_set contains the field
        if self.certificate_expired_at is None and "certificate_expired_at" in self.model_fields_set:
            _dict['certificateExpiredAt'] = None

        # set to None if last_modified_by (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified_by is None and "last_modified_by" in self.model_fields_set:
            _dict['lastModifiedBy'] = None

        # set to None if max_spot_price (nullable) is None
        # and model_fields_set contains the field
        if self.max_spot_price is None and "max_spot_price" in self.model_fields_set:
            _dict['maxSpotPrice'] = None

        # set to None if parent_project_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_project_id is None and "parent_project_id" in self.model_fields_set:
            _dict['parentProjectId'] = None

        # set to None if alerting_profile_id (nullable) is None
        # and model_fields_set contains the field
        if self.alerting_profile_id is None and "alerting_profile_id" in self.model_fields_set:
            _dict['alertingProfileId'] = None

        # set to None if opa_profile_id (nullable) is None
        # and model_fields_set contains the field
        if self.opa_profile_id is None and "opa_profile_id" in self.model_fields_set:
            _dict['opaProfileId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectListDetailDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "isKubernetes": obj.get("isKubernetes"),
            "isLocked": obj.get("isLocked"),
            "isVirtualCluster": obj.get("isVirtualCluster"),
            "isMonitoringEnabled": obj.get("isMonitoringEnabled"),
            "hasKubeConfigFile": obj.get("hasKubeConfigFile"),
            "isMaintenanceModeEnabled": obj.get("isMaintenanceModeEnabled"),
            "cloudCredentialName": obj.get("cloudCredentialName"),
            "organizationName": obj.get("organizationName"),
            "organizationId": obj.get("organizationId"),
            "status": obj.get("status"),
            "health": obj.get("health"),
            "cloudType": obj.get("cloudType"),
            "kubesprayCurrentVersion": obj.get("kubesprayCurrentVersion"),
            "kubesprayTargetVersion": obj.get("kubesprayTargetVersion"),
            "kubernetesCurrentVersion": obj.get("kubernetesCurrentVersion"),
            "kubernetesTargetVersion": obj.get("kubernetesTargetVersion"),
            "createdAt": obj.get("createdAt"),
            "alertsCount": obj.get("alertsCount"),
            "totalServersCount": obj.get("totalServersCount"),
            "totalStandaloneVmsCount": obj.get("totalStandaloneVmsCount"),
            "boundUsers": [UserDto.from_dict(_item) for _item in obj["boundUsers"]] if obj.get("boundUsers") is not None else None,
            "createdBy": obj.get("createdBy"),
            "lastModified": obj.get("lastModified"),
            "expiredAt": obj.get("expiredAt"),
            "deleteOnExpiration": obj.get("deleteOnExpiration"),
            "certificateExpiredAt": obj.get("certificateExpiredAt"),
            "lastModifiedBy": obj.get("lastModifiedBy"),
            "quotaId": obj.get("quotaId"),
            "allowFullSpotKubernetes": obj.get("allowFullSpotKubernetes"),
            "allowSpotWorkers": obj.get("allowSpotWorkers"),
            "allowSpotVMs": obj.get("allowSpotVMs"),
            "maxSpotPrice": obj.get("maxSpotPrice"),
            "projectAction": obj.get("projectAction"),
            "hasExpirationWarning": obj.get("hasExpirationWarning"),
            "totalHourlyCost": obj.get("totalHourlyCost"),
            "isAutoscalingEnabled": obj.get("isAutoscalingEnabled"),
            "isAutoscalingSpotEnabled": obj.get("isAutoscalingSpotEnabled"),
            "aiEnabled": obj.get("aiEnabled"),
            "anyServer": obj.get("anyServer"),
            "anyVm": obj.get("anyVm"),
            "isBackupEnabled": obj.get("isBackupEnabled"),
            "isProjectMaintenanceModeEnabled": obj.get("isProjectMaintenanceModeEnabled"),
            "allUsers": obj.get("allUsers"),
            "parentProjectId": obj.get("parentProjectId"),
            "alertingProfileId": obj.get("alertingProfileId"),
            "opaProfileId": obj.get("opaProfileId"),
            "lockButton": ButtonStatusDto.from_dict(obj["lockButton"]) if obj.get("lockButton") is not None else None,
            "unlockButton": ButtonStatusDto.from_dict(obj["unlockButton"]) if obj.get("unlockButton") is not None else None,
            "deleteButton": ButtonStatusDto.from_dict(obj["deleteButton"]) if obj.get("deleteButton") is not None else None,
            "kubeInfoButton": ButtonStatusDto.from_dict(obj["kubeInfoButton"]) if obj.get("kubeInfoButton") is not None else None,
            "setExpirationDateButton": ButtonStatusDto.from_dict(obj["setExpirationDateButton"]) if obj.get("setExpirationDateButton") is not None else None,
            "resetStatusButton": ButtonStatusDto.from_dict(obj["resetStatusButton"]) if obj.get("resetStatusButton") is not None else None,
            "importClusterType": obj.get("importClusterType"),
            "eImportClusterType": obj.get("eImportClusterType")
        })
        return _obj


