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
from taikunpycore.models.partner_details_for_subscription import PartnerDetailsForSubscription
from typing import Optional, Set
from typing_extensions import Self

class ListForPartnersDto(BaseModel):
    """
    ListForPartnersDto
    """ # noqa: E501
    id: Optional[StrictInt]
    name: Optional[StrictStr]
    project_limit: Optional[StrictInt] = Field(alias="projectLimit")
    server_limit: Optional[StrictInt] = Field(alias="serverLimit")
    user_limit: Optional[StrictInt] = Field(alias="userLimit")
    cloud_credential_limit: Optional[StrictInt] = Field(alias="cloudCredentialLimit")
    monthly_price: Union[StrictFloat, StrictInt] = Field(alias="monthlyPrice")
    yearly_price: Union[StrictFloat, StrictInt] = Field(alias="yearlyPrice")
    tcu_price: Union[StrictFloat, StrictInt] = Field(alias="tcuPrice")
    is_deprecated: Optional[StrictBool] = Field(alias="isDeprecated")
    currency: Optional[StrictStr]
    is_enterprise: Optional[StrictBool] = Field(alias="isEnterprise")
    partner: PartnerDetailsForSubscription
    exceeded_user: Optional[StrictBool] = Field(alias="exceededUser")
    exceeded_project: Optional[StrictBool] = Field(alias="exceededProject")
    exceeded_cloud_credential: Optional[StrictBool] = Field(alias="exceededCloudCredential")
    exceeded_servers: Optional[StrictBool] = Field(alias="exceededServers")
    is_active: Optional[StrictBool] = Field(alias="isActive")
    is_yearly: Optional[StrictBool] = Field(alias="isYearly")
    trial_days: Optional[StrictInt] = Field(alias="trialDays")
    description: Optional[StrictStr]
    is_demo: Optional[StrictBool] = Field(alias="isDemo")
    __properties: ClassVar[List[str]] = ["id", "name", "projectLimit", "serverLimit", "userLimit", "cloudCredentialLimit", "monthlyPrice", "yearlyPrice", "tcuPrice", "isDeprecated", "currency", "isEnterprise", "partner", "exceededUser", "exceededProject", "exceededCloudCredential", "exceededServers", "isActive", "isYearly", "trialDays", "description", "isDemo"]

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
        """Create an instance of ListForPartnersDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of partner
        if self.partner:
            _dict['partner'] = self.partner.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListForPartnersDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "projectLimit": obj.get("projectLimit"),
            "serverLimit": obj.get("serverLimit"),
            "userLimit": obj.get("userLimit"),
            "cloudCredentialLimit": obj.get("cloudCredentialLimit"),
            "monthlyPrice": obj.get("monthlyPrice"),
            "yearlyPrice": obj.get("yearlyPrice"),
            "tcuPrice": obj.get("tcuPrice"),
            "isDeprecated": obj.get("isDeprecated"),
            "currency": obj.get("currency"),
            "isEnterprise": obj.get("isEnterprise"),
            "partner": PartnerDetailsForSubscription.from_dict(obj["partner"]) if obj.get("partner") is not None else None,
            "exceededUser": obj.get("exceededUser"),
            "exceededProject": obj.get("exceededProject"),
            "exceededCloudCredential": obj.get("exceededCloudCredential"),
            "exceededServers": obj.get("exceededServers"),
            "isActive": obj.get("isActive"),
            "isYearly": obj.get("isYearly"),
            "trialDays": obj.get("trialDays"),
            "description": obj.get("description"),
            "isDemo": obj.get("isDemo")
        })
        return _obj


