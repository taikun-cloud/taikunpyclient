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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class KubernetesResourcesDto(BaseModel):
    """
    KubernetesResourcesDto
    """ # noqa: E501
    pods: Optional[StrictInt]
    crds: Optional[StrictInt]
    helmreleases: Optional[StrictInt]
    daemon_sets: Optional[StrictInt] = Field(alias="daemonSets")
    deployments: Optional[StrictInt]
    stateful_sets: Optional[StrictInt] = Field(alias="statefulSets")
    jobs: Optional[StrictInt]
    cron_jobs: Optional[StrictInt] = Field(alias="cronJobs")
    config_maps: Optional[StrictInt] = Field(alias="configMaps")
    namespaces: Optional[StrictInt]
    nodes: Optional[StrictInt]
    pvcs: Optional[StrictInt]
    secrets: Optional[StrictInt]
    services: Optional[StrictInt]
    ingresses: Optional[StrictInt]
    network_policies: Optional[StrictInt] = Field(alias="networkPolicies")
    pdbs: Optional[StrictInt]
    storage_classes: Optional[StrictInt] = Field(alias="storageClasses")
    __properties: ClassVar[List[str]] = ["pods", "crds", "helmreleases", "daemonSets", "deployments", "statefulSets", "jobs", "cronJobs", "configMaps", "namespaces", "nodes", "pvcs", "secrets", "services", "ingresses", "networkPolicies", "pdbs", "storageClasses"]

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
        """Create an instance of KubernetesResourcesDto from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KubernetesResourcesDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pods": obj.get("pods"),
            "crds": obj.get("crds"),
            "helmreleases": obj.get("helmreleases"),
            "daemonSets": obj.get("daemonSets"),
            "deployments": obj.get("deployments"),
            "statefulSets": obj.get("statefulSets"),
            "jobs": obj.get("jobs"),
            "cronJobs": obj.get("cronJobs"),
            "configMaps": obj.get("configMaps"),
            "namespaces": obj.get("namespaces"),
            "nodes": obj.get("nodes"),
            "pvcs": obj.get("pvcs"),
            "secrets": obj.get("secrets"),
            "services": obj.get("services"),
            "ingresses": obj.get("ingresses"),
            "networkPolicies": obj.get("networkPolicies"),
            "pdbs": obj.get("pdbs"),
            "storageClasses": obj.get("storageClasses")
        })
        return _obj


