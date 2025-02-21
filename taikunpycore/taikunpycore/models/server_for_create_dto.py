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
from taikunpycore.models.cloud_role import CloudRole
from taikunpycore.models.kubernetes_node_labels_dto import KubernetesNodeLabelsDto
from taikunpycore.models.proxmox_role import ProxmoxRole
from typing import Optional, Set
from typing_extensions import Self

class ServerForCreateDto(BaseModel):
    """
    ServerForCreateDto
    """ # noqa: E501
    name: Optional[StrictStr] = None
    role: Optional[CloudRole] = None
    project_id: Optional[StrictInt] = Field(default=None, alias="projectId")
    disk_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="diskSize")
    flavor: Optional[StrictStr] = None
    count: Optional[StrictInt] = None
    spot_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="spotPrice")
    spot_instance: Optional[StrictBool] = Field(default=None, alias="spotInstance")
    wasm_enabled: Optional[StrictBool] = Field(default=None, alias="wasmEnabled")
    autoscaling_group: Optional[StrictStr] = Field(default=None, alias="autoscalingGroup")
    availability_zone: Optional[StrictStr] = Field(default=None, alias="availabilityZone")
    proxmox_extra_disk_size: Optional[StrictInt] = Field(default=None, alias="proxmoxExtraDiskSize")
    proxmox_role: Optional[ProxmoxRole] = Field(default=None, alias="proxmoxRole")
    hypervisor: Optional[StrictStr] = None
    kubernetes_node_labels: Optional[List[KubernetesNodeLabelsDto]] = Field(default=None, alias="kubernetesNodeLabels")
    replica_count: Optional[StrictInt] = Field(default=None, alias="replicaCount")
    __properties: ClassVar[List[str]] = ["name", "role", "projectId", "diskSize", "flavor", "count", "spotPrice", "spotInstance", "wasmEnabled", "autoscalingGroup", "availabilityZone", "proxmoxExtraDiskSize", "proxmoxRole", "hypervisor", "kubernetesNodeLabels", "replicaCount"]

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
        """Create an instance of ServerForCreateDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in kubernetes_node_labels (list)
        _items = []
        if self.kubernetes_node_labels:
            for _item_kubernetes_node_labels in self.kubernetes_node_labels:
                if _item_kubernetes_node_labels:
                    _items.append(_item_kubernetes_node_labels.to_dict())
            _dict['kubernetesNodeLabels'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if flavor (nullable) is None
        # and model_fields_set contains the field
        if self.flavor is None and "flavor" in self.model_fields_set:
            _dict['flavor'] = None

        # set to None if spot_price (nullable) is None
        # and model_fields_set contains the field
        if self.spot_price is None and "spot_price" in self.model_fields_set:
            _dict['spotPrice'] = None

        # set to None if autoscaling_group (nullable) is None
        # and model_fields_set contains the field
        if self.autoscaling_group is None and "autoscaling_group" in self.model_fields_set:
            _dict['autoscalingGroup'] = None

        # set to None if availability_zone (nullable) is None
        # and model_fields_set contains the field
        if self.availability_zone is None and "availability_zone" in self.model_fields_set:
            _dict['availabilityZone'] = None

        # set to None if hypervisor (nullable) is None
        # and model_fields_set contains the field
        if self.hypervisor is None and "hypervisor" in self.model_fields_set:
            _dict['hypervisor'] = None

        # set to None if kubernetes_node_labels (nullable) is None
        # and model_fields_set contains the field
        if self.kubernetes_node_labels is None and "kubernetes_node_labels" in self.model_fields_set:
            _dict['kubernetesNodeLabels'] = None

        # set to None if replica_count (nullable) is None
        # and model_fields_set contains the field
        if self.replica_count is None and "replica_count" in self.model_fields_set:
            _dict['replicaCount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServerForCreateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "role": obj.get("role"),
            "projectId": obj.get("projectId"),
            "diskSize": obj.get("diskSize"),
            "flavor": obj.get("flavor"),
            "count": obj.get("count"),
            "spotPrice": obj.get("spotPrice"),
            "spotInstance": obj.get("spotInstance"),
            "wasmEnabled": obj.get("wasmEnabled"),
            "autoscalingGroup": obj.get("autoscalingGroup"),
            "availabilityZone": obj.get("availabilityZone"),
            "proxmoxExtraDiskSize": obj.get("proxmoxExtraDiskSize"),
            "proxmoxRole": obj.get("proxmoxRole"),
            "hypervisor": obj.get("hypervisor"),
            "kubernetesNodeLabels": [KubernetesNodeLabelsDto.from_dict(_item) for _item in obj["kubernetesNodeLabels"]] if obj.get("kubernetesNodeLabels") is not None else None,
            "replicaCount": obj.get("replicaCount")
        })
        return _obj


