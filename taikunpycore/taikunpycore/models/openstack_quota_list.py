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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from taikunpycore.models.openstack_compute_quota_dto import OpenstackComputeQuotaDto
from taikunpycore.models.openstack_network_dto import OpenstackNetworkDto
from taikunpycore.models.openstack_volume_quota_dto import OpenstackVolumeQuotaDto
from typing import Optional, Set
from typing_extensions import Self

class OpenstackQuotaList(BaseModel):
    """
    OpenstackQuotaList
    """ # noqa: E501
    compute: Optional[OpenstackComputeQuotaDto] = None
    volume: Optional[OpenstackVolumeQuotaDto] = None
    network: Optional[OpenstackNetworkDto] = None
    is_infra: Optional[StrictBool] = Field(default=None, alias="isInfra")
    __properties: ClassVar[List[str]] = ["compute", "volume", "network", "isInfra"]

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
        """Create an instance of OpenstackQuotaList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of compute
        if self.compute:
            _dict['compute'] = self.compute.to_dict()
        # override the default output from pydantic by calling `to_dict()` of volume
        if self.volume:
            _dict['volume'] = self.volume.to_dict()
        # override the default output from pydantic by calling `to_dict()` of network
        if self.network:
            _dict['network'] = self.network.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OpenstackQuotaList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "compute": OpenstackComputeQuotaDto.from_dict(obj["compute"]) if obj.get("compute") is not None else None,
            "volume": OpenstackVolumeQuotaDto.from_dict(obj["volume"]) if obj.get("volume") is not None else None,
            "network": OpenstackNetworkDto.from_dict(obj["network"]) if obj.get("network") is not None else None,
            "isInfra": obj.get("isInfra")
        })
        return _obj


