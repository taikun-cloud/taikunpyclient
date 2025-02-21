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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CostComponent(BaseModel):
    """
    CostComponent
    """ # noqa: E501
    name: Optional[StrictStr] = None
    unit: Optional[StrictStr] = None
    hourly_quantity: Optional[StrictStr] = Field(default=None, alias="hourlyQuantity")
    monthly_quantity: Optional[StrictStr] = Field(default=None, alias="monthlyQuantity")
    price: Optional[StrictStr] = None
    hourly_cost: Optional[StrictStr] = Field(default=None, alias="hourlyCost")
    monthly_cost: Optional[StrictStr] = Field(default=None, alias="monthlyCost")
    price_not_found: Optional[StrictBool] = Field(default=None, alias="priceNotFound")
    usage_based: Optional[StrictBool] = Field(default=None, alias="usageBased")
    __properties: ClassVar[List[str]] = ["name", "unit", "hourlyQuantity", "monthlyQuantity", "price", "hourlyCost", "monthlyCost", "priceNotFound", "usageBased"]

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
        """Create an instance of CostComponent from a JSON string"""
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

        # set to None if unit (nullable) is None
        # and model_fields_set contains the field
        if self.unit is None and "unit" in self.model_fields_set:
            _dict['unit'] = None

        # set to None if hourly_quantity (nullable) is None
        # and model_fields_set contains the field
        if self.hourly_quantity is None and "hourly_quantity" in self.model_fields_set:
            _dict['hourlyQuantity'] = None

        # set to None if monthly_quantity (nullable) is None
        # and model_fields_set contains the field
        if self.monthly_quantity is None and "monthly_quantity" in self.model_fields_set:
            _dict['monthlyQuantity'] = None

        # set to None if price (nullable) is None
        # and model_fields_set contains the field
        if self.price is None and "price" in self.model_fields_set:
            _dict['price'] = None

        # set to None if hourly_cost (nullable) is None
        # and model_fields_set contains the field
        if self.hourly_cost is None and "hourly_cost" in self.model_fields_set:
            _dict['hourlyCost'] = None

        # set to None if monthly_cost (nullable) is None
        # and model_fields_set contains the field
        if self.monthly_cost is None and "monthly_cost" in self.model_fields_set:
            _dict['monthlyCost'] = None

        # set to None if usage_based (nullable) is None
        # and model_fields_set contains the field
        if self.usage_based is None and "usage_based" in self.model_fields_set:
            _dict['usageBased'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CostComponent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "unit": obj.get("unit"),
            "hourlyQuantity": obj.get("hourlyQuantity"),
            "monthlyQuantity": obj.get("monthlyQuantity"),
            "price": obj.get("price"),
            "hourlyCost": obj.get("hourlyCost"),
            "monthlyCost": obj.get("monthlyCost"),
            "priceNotFound": obj.get("priceNotFound"),
            "usageBased": obj.get("usageBased")
        })
        return _obj


