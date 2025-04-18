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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class UpdateSubscriptionCommand(BaseModel):
    """
    UpdateSubscriptionCommand
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    project_limit: Optional[StrictInt] = Field(default=None, alias="projectLimit")
    server_limit: Optional[StrictInt] = Field(default=None, alias="serverLimit")
    user_limit: Optional[StrictInt] = Field(default=None, alias="userLimit")
    cloud_credential_limit: Optional[StrictInt] = Field(default=None, alias="cloudCredentialLimit")
    monthly_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="monthlyPrice")
    yearly_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="yearlyPrice")
    tcu_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="tcuPrice")
    trial_days: Optional[StrictInt] = Field(default=None, alias="trialDays")
    __properties: ClassVar[List[str]] = ["id", "name", "projectLimit", "serverLimit", "userLimit", "cloudCredentialLimit", "monthlyPrice", "yearlyPrice", "tcuPrice", "trialDays"]

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
        """Create an instance of UpdateSubscriptionCommand from a JSON string"""
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

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateSubscriptionCommand from a dict"""
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
            "trialDays": obj.get("trialDays")
        })
        return _obj


